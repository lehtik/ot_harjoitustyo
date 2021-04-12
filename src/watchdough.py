from tkinter import Tk, ttk

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        label = ttk.Label(master=self._root, text="WatchDough")

        label.pack()

window = Tk()
window.title("WatchDough")

ui = UI(window)
ui.start()

window.mainloop()