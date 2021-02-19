import unittest
import pm_telemetry as pmt
import pandas as pd
import numpy as np

class TestPmTelemetry(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.tele = pmt.PmTelemetry()
    
    def setUp(self):
        self.tele_count = len(self.tele.data)
        print(f"telemetry.csv has {self.tele_count} records")
        
    def test_merge_maint(self):
        print(f"Data count should maintain at {len(self.tele.data)} after merging maint.csv")
        self.tele.merge_maint()
        self.assertEqual(self.tele_count, len(self.tele.data))
    
    def test_merge_errors(self):
        print(f"Data count should maintain at {len(self.tele.data)} after merging errors.csv")
        self.tele.merge_errors()
        self.assertEqual(self.tele_count, len(self.tele.data))
        
    def test_merge_failures(self):
        print(f"Data count should maintain at {len(self.tele.data)} after merging failures.csv")
        self.tele.merge_failures()
        self.assertEqual(self.tele_count, len(self.tele.data))
        
    def test_merge_machines(self):
        print(f"Data count should maintain at {len(self.tele.data)} after merging machines.csv")
        self.tele.merge_machines()
        self.assertEqual(self.tele_count, len(self.tele.data))
    
    def test_gen_past_hr_rolling_telemetry(self):
        print("Check that the mean of machine 1 volt data on 2nd Jan 2015 is 165.35")
        test_date = pd.Timestamp(2015, 1, 2, 0)
        test_date_records = self.tele.data[(self.tele.data.datetime.dt.date == test_date) & (self.tele.data.machineID == 1)]
        manual_calc_answer = 165.35
        self.assertEqual(manual_calc_answer, np.round(test_date_records["volt"].mean(), 2))
    
    @classmethod
    def tearDownClass(cls):
        del cls.tele

if __name__ == '__main__':
    unittest.main()