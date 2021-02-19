import unittest
import pm_telemetry as pmt

class TestPmTelemetry(unittest.TestCase):
    
    def test_init(self):
        tele = pmt.PmTelemetry()
        self.assertIsNotNone(tele.data)

if __name__ == '__main__':
    unittest.main()