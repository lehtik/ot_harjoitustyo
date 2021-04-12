import tkinter
from tkinter import Tk

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        BASE_COLOR = "#fff9e8"
        heading_label = tkinter.Label(master=self._root, text="WatchDough", font=("Papyrus", 36), bg=BASE_COLOR, pady=3, padx=3)

        # heading_label.config(font=("Papyrus", 36))

        lampotila_label = tkinter.Label(master=self._root, text="Lämpötila", pady=3, padx=3)
        lampotila_arvo_label = tkinter.Label(master=self._root, text="69 °C", pady=3, padx=3)

        kosteus_label = tkinter.Label(master=self._root, text="Kosteus", pady=3, padx=3)
        kosteus_arvo_label = tkinter.Label(master=self._root, text="69 %", pady=3, padx=3)

        korkeus_label = tkinter.Label(master=self._root, text="Korkeus", pady=3, padx=3)
        korkeus_arvo_label = tkinter.Label(master=self._root, text="69 mm", pady=3, padx=3)

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



window = Tk()
window.geometry("600x600")
window.title("WatchDough")
window.configure(bg="#fff9e8")

ui = UI(window)
ui.start()

window.mainloop()