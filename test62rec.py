import unittest
import lab62rec as code

class TestProgramm(unittest.TestCase):
    def test_high_and_low_number(self):
        p = code.create(10,p = [])
        p = sorted(p)
        list_a = []
        list_a.append(p[0])
        list_a.append(p[len(p) - 1])
        list_a.append(0)
        list_a.append(0)
        list_low_and_high = code.high_and_low_number(p,list_low_and_high=[])

        self.assertEqual(list_a, list_low_and_high)
