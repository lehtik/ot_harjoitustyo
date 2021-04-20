import unittest
import os
from datetime import datetime
from saver import Saver

class TestSaver(unittest.TestCase):
    def test_saving_and_writing_succesful(self):
        if os.path.exists("kinkeri.jsonlines"):
            os.remove("kinkeri.jsonlines")
        self.saving = Saver("kinkeri.jsonlines")
        self.saving.save_measurement(69.69, 96, 13, datetime(1952, 12, 24, 16, 12, 59, 13))
        self.saving.save_measurement(15, 50, 16, datetime(1992, 11, 17, 15, 00, 59, 12))
        self.saving.save_measurement(27, 65, 14, datetime(1994, 1, 27, 11, 00, 45, 59))
        self.saving.stop_recording()
        with open('kinkeri.jsonlines') as testfile:
            # avattu testataan
            rivit = testfile.read().split("\n")
            self.assertEqual(len(rivit), 4)
        open('kinkeri.jsonlines', 'w').close()

    def test_text_is_the_same_as_input(self):
        if os.path.exists("kinkeri.jsonlines"):
            os.remove("kinkeri.jsonlines")
        self.saving = Saver("kinkeri.jsonlines")
        self.saving.save_measurement(69.69, 96, 13, datetime(1952, 12, 24, 16, 12, 59, 13))
        self.saving.save_measurement(15, 50, 16, datetime(1992, 11, 17, 15, 00, 59, 12))
        self.saving.save_measurement(27, 65, 14, datetime(1994, 1, 27, 11, 00, 45, 59))
        self.saving.stop_recording()
        rivino = 0
        with open('kinkeri.jsonlines') as testfile:
            # avattu testataan
            rivit = testfile.read().split("\n")
            #self.assertEqual(rivit, '')
            for rivi in rivit:
                if rivino == 0:
                    self.assertEqual(rivi, '{"datetime": "24.12.1952 16.12.59", "temperature": 69.69, "moisture": 96, "height": 13}')
                if rivino == 1:
                    self.assertEqual(rivi, '{"datetime": "17.11.1992 15.00.59", "temperature": 15, "moisture": 50, "height": 16}')
                if rivino == 2:
                    self.assertEqual(rivi, '{"datetime": "27.01.1994 11.00.45", "temperature": 27, "moisture": 65, "height": 14}')
                rivino += 1
        open('kinkeri.jsonlines', 'w').close()

    def test_no_extra_rows_after_saving(self):
        if os.path.exists("kinkeri.jsonlines"):
            os.remove("kinkeri.jsonlines")
        self.saving = Saver("kinkeri.jsonlines")
        self.saving.save_measurement(69.69, 96, 13, datetime(1952, 12, 24, 16, 12, 59, 13))
        self.saving.save_measurement(15, 50, 16, datetime(1992, 11, 17, 15, 00, 59, 12))
        self.saving.stop_recording()
        self.saving.save_measurement(27, 65, 14, datetime(1994, 1, 27, 11, 00, 45, 59))
        with open('kinkeri.jsonlines') as testfile:
            rivit = testfile.read().split("\n")
            self.assertEqual(len(rivit), 3)
        open('kinkeri.jsonlines', 'w').close()

    def test_data_persistence(self):
        if os.path.exists("persistence.jsonlines"):
            os.remove("persistence.jsonlines")
        new_measurement = Saver("persistence.jsonlines") #luo uusi mittaussessio saveri
        new_measurement.save_measurement(69.69, 96, 13, datetime(1952, 12, 24, 16, 12, 59, 13))
        new_measurement.save_measurement(15, 50, 16, datetime(1992, 11, 17, 15, 00, 59, 12)) #kaksi mittaustulosta lisätään
        #lue heti ennen kuin pysäyttämistä onko ne kaksi mittaustulosta siellä vai ei
        meas = new_measurement.read_measurements()
        self.assertEqual(len(meas), 2)
        self.assertEqual(meas[0]["temperature"], 69.69)
        self.assertEqual(meas[1]["moisture"], 50)
        new_measurement.stop_recording() #pysäytä
        new_measurement2 = Saver("persistence.jsonlines") #luo uusi mittaussessio samalla nimellä kuin edellinen
        meas2 = new_measurement2.read_measurements()
        self.assertEqual(len(meas2), 2)
        self.assertEqual(meas2[0]["temperature"], 69.69)
        self.assertEqual(meas2[1]["moisture"], 50)       #mitä tapahtuuu lue heti mittaustulokset read mEASUrements --> onko samat kun aiemmat..?

    def test_data_read(self):
        if os.path.exists("dataread.jsonlines"):
            os.remove("dataread.jsonlines")
        new_measurement = Saver("dataread.jsonlines") #luo uusi mittaussessio saveri
        new_measurement.save_measurement(69.69, 96, 13, datetime(1952, 12, 24, 16, 12, 59, 13))
        new_measurement.save_measurement(15, 50, 16, datetime(1992, 11, 17, 15, 00, 59, 12)) #kaksi mittaustulosta lisätään
        meas = new_measurement.read_measurements()
        self.assertEqual(len(meas), 2)
        self.assertEqual(meas[0]["temperature"], 69.69)
        self.assertEqual(meas[1]["moisture"], 50)