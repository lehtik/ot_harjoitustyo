import json
from datetime import datetime
from os import path

class Saver:
    """
    Luokka, jonka avulla tallennetaan mittaustietoja

    Args:
        filename: haluttu tiedoston nimi
    """
    def __init__(self, filename: str):
        """
        Konstruktori, joka luo uuden tiedoston tallentamista varten tai avaa olemassa olevan

        Args:
            filename: haluttu tiedoston nimi
        """
        self.filename = filename
        self.measurements = []
        #onko vanhaa tiedostoa olemassa, jos on niin ladataan tiedoston sisältö muistiin
        if path.exists(filename):
            self.load_file()
            self.file = open(filename, "a")
        else:
            self.file = open(filename, "w")
        self.canwrite = True
        
    def stop_recording(self):
        """
        Lopettaa tallentamisen ja sulkee tiedoston.
        """
        self.canwrite = False
        self.file.close()

    # function used for inputting data to the measurement file
    def save_measurement(self, temp, moist, height, ts):
        """
        Tallentaa mittauksen levylle dictinä.

        Args:
            temp: Lämpötila dictissä
            moist: Kosteus dictissä
            height: Korkeus dictissä
            ts: datetime dictissä
        """
        if not self.canwrite:
            return
        data = {"datetime": ts.strftime("%d.%m.%Y %H.%M.%S"), "temperature": temp, "moisture": moist, "height": height}
        self.file.write(json.dumps(data) + "\n") #tallennetaan levylle
        self.measurements.append(data)
        self.file.flush()

    def load_file(self):
        """
        Ladataan data tiedostosta ja lisätään se listaan, josta voidaan lukea dataa myöhemmin
        """
        with open(self.filename) as f:
            rivit = f.read().split("\n")
            for rivi in rivit:
                if len(rivi) > 0:
                    self.measurements.append(json.loads(rivi))

    #return the list
    def read_measurements(self):
        """
        Luetaan mittaukset
        
        Return:
            Mittaukset listana
        """
        return self.measurements

    def read_temperature(self):
        """
        Luetaan vain lämpötila esimerkiksi kuvaajaa varten

        Return:
            Lämpötilat listana
        """
        temperaturet = []
        for dict_measurement_set in self.measurements:
            temperaturet.append(dict_measurement_set["temperature"])
        return temperaturet

    def read_moisture(self):
        """
        Luetaan vain kosteus esimerkiksi kuvaajaa varten

        Return:
            Kosteudet listana
        """
        moisturet = []
        for dict_measurement_set in self.measurements:
            moisturet.append(dict_measurement_set["moisture"])
        return moisturet

    def read_height(self):
        """
        Luetaan vain korkeus esimerkiksi kuvaajaa varten

        Return:
            Korkeudet listana
        """
        height = []
        for dict_measurement_set in self.measurements:
            height.append(dict_measurement_set["height"])
        return height

# if __name__ == "__main__":
#     ohjelma = Saver("kinkeri.jsonlines")
#     ohjelma.save_measurement(69.69, 96, 13, datetime(1952, 12, 24, 16, 12, 59, 13))
#     print(ohjelma.read_measurements())
#     print(len(ohjelma.read_measurements()))
#     ohjelma.stop_recording()
