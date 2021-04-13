import tkinter
import requests,sys
from tkinter import Tk, StringVar

POLL_INTERVAL = 1000

def get_data(sensorname):
    r = requests.get(f'https://watchdough.apps.emblica.com/sensor/{sensorname}')
    return r.json()

class UI:
    def __init__(self, root, sensorname):
        self._root = root
        self._temperature_var = None
        self.sensorname = sensorname

    def poll_data(self):
        data = get_data(self.sensorname)
        self._temperature_var.set(f'{data["temp"]:2f} °C')
        self._moisture_var.set(f'{data["humidity"]:2f} %')
        self._height_var.set(f'{data["distance"]:2f} cm')
        self._root.after(POLL_INTERVAL, self.poll_data)

    def start(self):
        BASE_COLOR = "#fff9e8"

        self._temperature_var = StringVar()
        self._temperature_var.set("0 °C")

        self._moisture_var = StringVar()
        self._moisture_var.set("0 %")

        self._height_var = StringVar()
        self._height_var.set("0 cm")

        heading_label = tkinter.Label(master=self._root, text="WatchDough", font=("Papyrus", 36), bg=BASE_COLOR, pady=3, padx=3)

        # heading_label.config(font=("Papyrus", 36))

        lampotila_label = tkinter.Label(master=self._root, text="Lämpötila", pady=3, padx=3)
        lampotila_arvo_label = tkinter.Label(master=self._root, textvariable=self._temperature_var, pady=3, padx=3)

        kosteus_label = tkinter.Label(master=self._root, text="Kosteus", pady=3, padx=3)
        kosteus_arvo_label = tkinter.Label(master=self._root, textvariable=self._moisture_var, pady=3, padx=3)

        korkeus_label = tkinter.Label(master=self._root, text="Korkeus", pady=3, padx=3)
        korkeus_arvo_label = tkinter.Label(master=self._root, textvariable=self._height_var, pady=3, padx=3)

        heading_label.grid(row=0, column=0, columnspan=3)

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


if __name__ == "__main__":
    window = Tk()
    window.geometry("600x600")
    window.title("WatchDough")
    window.configure(bg="#fff9e8")

    sensorname ="DEV"
    if len(sys.argv) > 1:
        sensorname = sys.argv[1]
    ui = UI(window, sensorname)
    ui.start()

    window.mainloop()