from unittest import TestCase

from Classes.Time import Time


class TestTime(TestCase):
    def test_str(self):
        self.assertEqual("01:00:00", str(Time(3600)))
        self.assertEqual("00:00:00", str(Time(0)))
        self.assertEqual("03:27:15", str(Time(12435)))
        self.assertEqual("-4:32:45", str(Time(-12435)))

    def test_repr(self):
        self.assertEqual("Time(3600)", repr(Time(3600)))
        self.assertEqual("Time(0)", repr(Time(0)))
        self.assertEqual("Time(12435)", repr(Time(12435)))
        self.assertEqual("Time(-12435)", repr(Time(-12435)))

    def test_add(self):
        self.assertEqual("35:17:23", str(Time(3600) + Time(123443)))
        self.assertEqual("-3:32:45", str(Time(3600) + Time(-12435)))

    def test_int(self):
        self.assertEqual(3600, int(Time(3600)))
        self.assertEqual(-12435, int(Time(-12435)))
