import unittest
from gp302_tax_package import gp302_tax

cal_taxPayable = gp302_tax.cal_taxPable

class TestCases(unittest.TestCase):
    def test1(self):
        income_self = 420000
        income_spouse = 540000
        TP_self = cal_taxPayable(income_self, 0)
        TP_spouse = cal_taxPayable(income_spouse, 0)
        TP_joint = cal_taxPayable(income_self, income_spouse)
        
        self.assertEqual(TP_self, 27900)
        self.assertEqual(TP_spouse, 48300)
        self.assertEqual(TP_joint, 94200)
        
    def test2(self):
        income_self = 0
        income_spouse = 5400000
        TP_self = cal_taxPayable(income_self, 0)
        TP_spouse = cal_taxPayable(income_spouse, 0)
        TP_joint = cal_taxPayable(income_self, income_spouse)
        
        self.assertEqual(TP_self, 0)
        self.assertEqual(TP_spouse, 807300)
        self.assertEqual(TP_joint, 807300)
        
    def test3(self):
        income_self = 5400
        income_spouse = 3990
        TP_self = cal_taxPayable(income_self, 0)
        TP_spouse = cal_taxPayable(income_spouse, 0)
        TP_joint = cal_taxPayable(income_self, income_spouse)
        
        self.assertEqual(TP_self, 0)
        self.assertEqual(TP_spouse, 0)
        self.assertEqual(TP_joint, 0)
if __name__ == "__main__":
    unittest.main()