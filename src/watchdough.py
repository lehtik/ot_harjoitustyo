import tkinter
from saver import Saver
import requests,sys
from tkinter import Tk, StringVar
from datetime import datetime

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

POLL_INTERVAL = 1000

def get_data(sensorname):
    r = requests.get(f'https://watchdough.apps.emblica.com/sensor/{sensorname}')
    return r.json()

class UI:
    """
    Luo käyttöliittymän.

    Args:
        root: Ikkunan muodostaminen
        sensorname: Sensorin nimi (DEV = simulointi tai R1 = oikea anturi)
    """
    def __init__(self, root: str, sensorname: str):
        """
        Luokan konstruktori, joka luo uuden istunnon

        Args:
            root: Ikkunan muodostaminen
            sensorname: Sensorin nimi (DEV = simulointi tai R1 = oikea anturi)
        """
        self._root = root
        self._temperature_var = None
        self.sensorname = sensorname
        self.saving_status = False

    def poll_data(self):
        """
        Hakee datan sensorilta
        """
        data = get_data(self.sensorname)
        self._temperature_var.set(f'{data["temp"]:2f} °C')
        self._moisture_var.set(f'{data["humidity"]:2f} %')
        self._height_var.set(f'{data["distance"]:2f} cm')
        self._root.after(POLL_INTERVAL, self.poll_data)
        if self.saving_status:
            self.saver.save_measurement(data["temp"], data["humidity"], data["distance"], datetime.now())
            self.plot_data()
        
    def start(self):
        """
        Näyttää datan käyttöliittymässä
        """
        BASE_COLOR = "#fff9e8"

        self._temperature_var = StringVar()
        self._temperature_var.set("0 °C")

        self._moisture_var = StringVar()
        self._moisture_var.set("0 %")

        self._height_var = StringVar()
        self._height_var.set("0 cm")

        heading_label = tkinter.Label(master=self._root, text="WatchDough", font=("Papyrus", 36), bg=BASE_COLOR, pady=3, padx=3)

        fig = Figure(figsize=(8, 5), dpi=100)
        self.p1 = fig.add_subplot(311)
        self.p2 = fig.add_subplot(312)
        self.p3 = fig.add_subplot(313)

        # p.ylabel('Height, cm')
        # p.xlabel('Time, min')

        self.canvas = FigureCanvasTkAgg(fig, master=self._root)  # A tk.DrawingArea.
        self.canvas.draw()

        toolbar = NavigationToolbar2Tk(self.canvas, self._root, pack_toolbar=False)
        toolbar.update()

        lampotila_label = tkinter.Label(master=self._root, text="Lämpötila", pady=3, padx=3)
        lampotila_arvo_label = tkinter.Label(master=self._root, textvariable=self._temperature_var, pady=3, padx=3)

        kosteus_label = tkinter.Label(master=self._root, text="Kosteus", pady=3, padx=3)
        kosteus_arvo_label = tkinter.Label(master=self._root, textvariable=self._moisture_var, pady=3, padx=3)

        korkeus_label = tkinter.Label(master=self._root, text="Korkeus", pady=3, padx=3)
        korkeus_arvo_label = tkinter.Label(master=self._root, textvariable=self._height_var, pady=3, padx=3)
        
        tallennus_button = tkinter.Button(
            master=self._root,
            text="Aloita tallennus",
            pady=3,
            padx=3,
            command=self._start_loging
        )

        lopetus_button = tkinter.Button(
            master=self._root,
            text="Lopeta tallennus",
            pady=3,
            padx=3,
            command=self._stop_loging
        )

        #rivi 0
        heading_label.grid(row=0, column=1)

        #rivi 1 ja 2
        lampotila_label.grid(row=1, column=0)
        lampotila_arvo_label.grid(row=2, column=0)

        kosteus_label.grid(row=1, column=1)
        kosteus_arvo_label.grid(row=2, column=1)

        korkeus_label.grid(row=1, column=2)
        korkeus_arvo_label.grid(row=2, column=2)

        self._root.grid_columnconfigure(0, weight=1)
        self._root.grid_columnconfigure(1, weight=1)
        self._root.grid_columnconfigure(2, weight=1)
        self._root.after(POLL_INTERVAL, self.poll_data)

        self.canvas.mpl_connect(
            "key_press_event", lambda event: print(f"you pressed {event.key}"))
        self.canvas.mpl_connect("key_press_event", key_press_handler)
        
        #rivi 4
        toolbar.grid(row=4, column=0, columnspan=3)
        self.canvas.get_tk_widget().grid(row=3, column=0, columnspan=3)

        #rivi 6
        tallennus_button.grid(row=6, column=0, columnspan=3)

        #rivi 7
        lopetus_button.grid(row=7, column=0, columnspan=3)
        
    def _stop_loging(self):
        """
        Pysäyttää tallennuksen, kun lopeta tallennus -painiketta painetaan.
        """
        if self.saving_status:
            self.saver.stop_recording()
            self.saving_status = False

    def _start_loging(self):
        """
        Aloittaa tallennuksen, kun aloita tallennus -painiketta painetaan.
        """
        self.saver = Saver(datetime.now().strftime("%d.%m.%Y.%H.%M.%S.jsonlines"))
        self.saving_status = True

    def plot_data(self):
        """
        Piirtää graafit
        """
        self.p1.cla()
        self.p2.cla()
        self.p3.cla()
        self.p1.plot(self.saver.read_temperature(), label='Temperature, °C', color='red')
        self.p2.plot(self.saver.read_moisture(), label='Moisture, %', color='green')
        self.p3.plot(self.saver.read_height(), label='Height, cm', color='blue')
        self.p1.legend()
        self.p2.legend()
        self.p3.legend()
        self.canvas.draw()
        
if __name__ == "__main__":
    window = Tk()
    window.geometry("800x800")
    window.title("WatchDough")
    window.configure(bg="#fff9e8")

    sensorname ="DEV"
    if len(sys.argv) > 1:
        sensorname = sys.argv[1]
    ui = UI(window, sensorname)
    ui.start()

    window.mainloop()
