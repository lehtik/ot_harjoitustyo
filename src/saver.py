import json
from datetime import datetime
from os import path

class Saver:
    def __init__(self, filename):
        self.filename = filename
        self.measurements = []
        #onko vanhaa tiedostoa olemassa, jos on niin ladataan tiedoston sisältö muistiin
        if path.exists(filename):
            self.load_file()
            self.file = open(filename, "a")
        else:
            self.file = open(filename, "w")
        self.canwrite = True
        
    #stops recording and closes the file
    def stop_recording(self):
        self.canwrite = False
        self.file.close()

    # function used for inputting data to the measurement file
    def save_measurement(self, temp, moist, height, ts):
        if not self.canwrite:
            return
        data = {"datetime": ts.strftime("%d.%m.%Y %H.%M.%S"), "temperature": temp, "moisture": moist, "height": height}
        self.file.write(json.dumps(data) + "\n") #tallennetaan levylle
        self.measurements.append(data)
        self.file.flush()

    #read data from files and add them to list
    def load_file(self):
        with open(self.filename) as f:
            rivit = f.read().split("\n")
            for rivi in rivit:
                if len(rivi) > 0:
                    self.measurements.append(json.loads(rivi))

    #return the list
    def read_measurements(self):
        return self.measurements

if __name__ == "__main__":
    ohjelma = Saver("kinkeri.jsonlines")
    ohjelma.save_measurement(69.69, 96, 13, datetime(1952, 12, 24, 16, 12, 59, 13))
    print(ohjelma.read_measurements())
    print(len(ohjelma.read_measurements()))
    ohjelma.stop_recording()
