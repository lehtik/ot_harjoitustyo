import numpy as np
import math
from saver import Saver
import statistics
from time import time
import copy

CALIBRATION_TIME = 30 # SUOSITELTU KALIBROINTIAIKA 300 s, testimielessä voi käyttää lyhyempää aikaa. 

class MovingAverage:
    """
    Luokka, joka laskee liikkuvan keskiarvon aikaikkunan sisällä.

    Args:
        windowsize: haluttu aikaikkuna, jonka sisällä tarkastellaan keskiarvoa
    """
    def __init__(self, windowsize:int):
        self.buffer = []
        self.windowsize = windowsize

    def evaluate(self, value:int):
        """
        Laskee keskiarvon

        Args:
            value: mittauspiste
        """
        self.buffer.append(value)
        if len(self.buffer) > self.windowsize:
            self.buffer.pop(0)
        return statistics.mean(self.buffer)

class SmoothedIncrease:
    """
    Luokka, joka laskee derivaatan eli kuvaajan kulmakertoimen.

    Args:
        windowsize: haluttu aikaikkuna, jonka sisällä tarkastellaan kulmakerrointa
    """
    def __init__(self, windowsize: int):
        self.buffer = []
        self.windowsize = windowsize
        self.x = np.array(range(self.windowsize))
        self.A = np.vstack([self.x, np.ones(len(self.x))]).T

    def least_squares(self):
        """
        Kulmakertoimen laskenta
        """
        y = np.array(self.buffer)
        m, c = np.linalg.lstsq(self.A[:len(y)], y, rcond=None)[0]
        return m

    def evaluate(self, value):
        """
        Muokkaa bufferia ikkunan koon mukaiseksi ja lisää mittauspisteen ikkunaan

        Args:
            value: mittauspiste
        
        Returns:
            Kulmakerroin
        """
        self.buffer.append(value)
        if len(self.buffer) > self.windowsize:
            self.buffer.pop(0)
        return self.least_squares()

class WindowedStd:
    """
    Luokka, joka laskee keskihajonnan (standard deviation).

    Args:
        windowsize: haluttu aikaikkuna, jonka sisällä tarkastellaan kulmakerrointa
    """
    def __init__(self, windowsize):
        self.buffer = []
        self.windowsize = windowsize

    def evaluate(self, value):
        """
        Muokkaa bufferia ikkunan koon mukaiseksi ja lisää mittauspisteen ikkunaan

        Args:
            value: mittauspiste
        
        Returns:
            Keskihajonta
        """
        self.buffer.append(value)
        if len(self.buffer) > self.windowsize:
            self.buffer.pop(0)
        return np.std(self.buffer)

class StateMachine:
    """
    Luokka, jossa on tilakone. Tarkastaa missä tilassa juuren kohotus on (kalibrointi, alku, kasvuvaihe vai valmis juuri)
    """
    def __init__(self, calibration_time=CALIBRATION_TIME):
        self.state = "calibration"
        self.calibration_time = calibration_time
        self.av = MovingAverage(5)
        self.k = SmoothedIncrease(5)
        self.d = WindowedStd(5)
        self.average_k = MovingAverage(5)
        self.calibration_start_time = None
        self.k_calib = None
        self.d_calib = None
        self.t = None

    def set_time(self, t):
        """
        Ajan asettaminen (lähinnä testejä varten)

        Args:
            t: aika
        """
        self.t = t

    def get_time(self):
        """
        Hakee ajan
        """
        if self.t != None:
            return copy.deepcopy(self.t)
        return time()

    def evaluate(self, datapoint):
        """
        Tarkastaa missä tilassa kohotuksessa ollaan. Hakee myös kulmakertoimen ja keskihajonnan arvot tarkastusta varten.

        Args:
            datapoint: datapiste, jossa parhaillaan ollaan
        """
        av_datapoint = self.av.evaluate(datapoint)
        k_datapoint = self.k.evaluate(av_datapoint)
        d_datapoint = self.d.evaluate(k_datapoint)
        k_average_datapoint = self.average_k.evaluate(k_datapoint)
        if self.state == "calibration":
            return self.calibration(k_datapoint, d_datapoint)
        if self.state == "start":
            return self.start(k_datapoint)
        if self.state == "grow_calib":
            return self.grow_calib(k_datapoint, d_datapoint)
        if self.state == "grow":
            return self.grow(k_datapoint)

    def calibration(self, k_datapoint, d_datapoint):
        """
        Kalibrointivaihe. Tässä asetetaan kulmakerroin ja keskihajonta alkua varten.

        Args:
            k_datapoint: keskiarvo
            d_datapoint: keskihajonta
        """
        if self.calibration_start_time == None:
            self.calibration_start_time = self.get_time()
        if self.get_time() - self.calibration_start_time > self.calibration_time:
            self.state = "start"
            self.k_calib = k_datapoint
            self.d_calib = d_datapoint
            self.calibration_start_time = None

    def start(self, k_datapoint):
        """
        Alkuvaihe. Juuri heräilee. Siirrytään kasvuvaiheeseen, kun kulmakerroin kaksinkertaistuu keskihajontaan nähden.

        Args:
            k_datapoint: keskiarvo
        """
        if abs(k_datapoint - self.k_calib) > self.d_calib * 2:
            self.state = "grow_calib"

    def grow_calib(self, k_datapoint, d_datapoint):
        """
        Kalibroidaan uudelleen kasvuvaiheessa keskihajonta ja kulmakerroin

        Args:
            k_datapoint: keskiarvo
            d_datapoint: keskihajonta
        """
        if self.calibration_start_time == None:
            self.calibration_start_time = self.get_time()
        if self.get_time() - self.calibration_start_time > self.calibration_time:
            self.state = "grow"
            self.k_calib = k_datapoint
            self.d_calib = d_datapoint

    def grow(self, k_datapoint):
        """
        Kasvuvaihe. Juuri kasvaa korkeutta, kunnes huippu saavutetaan ja leipominen voi alkaa

        Args:
            k_datapoint: keskiarvo
        """
        if abs(k_datapoint - self.k_calib) > self.d_calib * 2:
            self.state = "end"

# LASKENNAN TOIMINTA
# sisään tuleva signaali (pinnankorkeus) on L, yksittäinen mittauspiste on L ajan funktiona L(t)
# useasta mittauspisteestä lasketaan liukuvaa keskiarvoa (Av) eli syntyy uusi ajan funktiona liukuvia keskiarvopisteitä muodostava funktio Av(t)
# Liukuvista keskiarvoista lasketaan liukuvaa suoran kulmakerrointa K (jälleen K(t)))
# liukuvista suoran kulmakertoimista lasketaan liukuvaa keskihajontaa: D(t)

# eli koko putki L(t) -> Av(t) -> K(t) -> D(t)

# aloitetaan tilasta C (calibration), tilassa lasketaan 5 min ajan keskihajontaa (D(t)) sekä keskimääräistä kulmakerrointa average(K(t)) jota kutsutaan K_calib
# D(t[c:n siirtymä]) = D_calib
# average(K(t)) = K_calib

# Siirrytään tilaan S (start) KUN aikaa on kulunut 5 min
# tilassa S lasketaan mittauspisteitä K(t) kunnes abs(K(t) - K_calib) > D_calib*2 jolloin siirrytään tilaan G
# Tilassa G (Grow) 