import unittest
import os
from datetime import datetime, timedelta
from analyzer import MovingAverage, SmoothedIncrease, StateMachine, WindowedStd
from saver import Saver
import time # so we can override time.time
import time_machine


class TestAnalyzer(unittest.TestCase):
    def test_buffer_pop_functional(self):
        m = MovingAverage(5)
        m.evaluate(1)
        m.evaluate(2)
        m.evaluate(3)
        m.evaluate(4)
        m.evaluate(5)
        m.evaluate(6)
        self.assertEqual(len(m.buffer), 5)

    def test_buffer_pops_first_value(self):
        m = MovingAverage(5)
        m.evaluate(1)
        m.evaluate(2)
        m.evaluate(3)
        m.evaluate(4)
        m.evaluate(5)
        m.evaluate(6)
        self.assertEqual(m.buffer, [2,3,4,5,6])

    def test_mean_value_ok(self):
        m = MovingAverage(5)
        m.evaluate(1)
        m.evaluate(2)
        m.evaluate(3)
        m.evaluate(4)
        self.assertEqual(m.evaluate(5), 3)

    def test_mean_value_plus_1_ok(self):
        m = MovingAverage(5)
        m.evaluate(1)
        m.evaluate(2)
        m.evaluate(3)
        m.evaluate(4)
        m.evaluate(5)
        self.assertEqual(m.evaluate(6), 4)

    def test_least_squares_positive(self):
        m = SmoothedIncrease(5)
        m.evaluate(1)
        m.evaluate(2)
        m.evaluate(3)
        m.evaluate(4)
        m.evaluate(5)
        self.assertEqual(m.evaluate(6), 1)

    def test_least_squares_negative(self):
        m = SmoothedIncrease(5)
        m.evaluate(6)
        m.evaluate(5)
        m.evaluate(4)
        m.evaluate(3)
        m.evaluate(2)
        self.assertEqual(m.evaluate(1), -1)

    def test_least_squares_negative(self):
        m = SmoothedIncrease(6)
        m.evaluate(6)
        m.evaluate(5)
        m.evaluate(4)
        m.evaluate(4)
        m.evaluate(5)
        self.assertLess(m.evaluate(6), 0.01)

    def test_windowed_std(self):
        m = WindowedStd(6)
        m.evaluate(1)
        m.evaluate(2)
        m.evaluate(3)
        m.evaluate(4)
        m.evaluate(5)
        self.assertEqual(m.evaluate(6), 1.707825127659933)

    
    def test_state_calibration(self):
        m = StateMachine(calibration_time=300)
        m.set_time(0)
        # Testataan pysytäänkö kalibrointitilassa koko 5 min: (aika=0)
        self.assertEqual(m.get_time(), 0)
        self.assertEqual(m.state, "calibration")
        for l in [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]:
            m.evaluate(l)
        self.assertEqual(m.state, "calibration")
        self.assertEqual(m.get_time(), 0)
        self.assertEqual(m.calibration_start_time, 0)
        # Testataan siirrytäänkö start-tilaan heti kun kalibraatioaika on ohi (aika>300)
        
        m.set_time(601)
        self.assertEqual(m.get_time(), 601)
        self.assertEqual(m.calibration_start_time, 0)

        self.assertEqual(m.state, "calibration") # Tila ei vielä ole muuttunut ennen kuin kutsutaan evaluate
        m.evaluate(1)
        m.evaluate(1)
        self.assertEqual(m.state, "start")
        
        self.assertLessEqual(m.k_calib, 0.0001)
        self.assertEqual(m.d_calib, 0)

        m.evaluate(1)
        m.evaluate(1)
        m.evaluate(1)
        m.evaluate(1)
        self.assertEqual(m.state, "start")

        m.evaluate(3)
        m.evaluate(4)
        m.evaluate(5)
        self.assertEqual(m.state, "grow_calib")

        m.set_time(801)
        self.assertEqual(m.get_time(), 801)
        m.evaluate(6)
        m.evaluate(7)
        m.evaluate(8)
        self.assertEqual(m.state, "grow_calib")

        m.set_time(951)
        self.assertEqual(m.get_time(), 951)
        m.evaluate(9)
        self.assertEqual(m.state, "grow")

        self.assertGreaterEqual(m.k_calib, 0.5)
        self.assertGreaterEqual(m.d_calib, 0)
        self.assertLess(m.d_calib, 1)

        m.evaluate(10)
        m.evaluate(11)
        m.evaluate(12)
        self.assertEqual(m.state, "grow")

        m.evaluate(12)
        m.evaluate(12)
        m.evaluate(12)
        m.evaluate(12)
        m.evaluate(12)
        m.evaluate(12)
        m.evaluate(12)
        self.assertEqual(m.state, "end")