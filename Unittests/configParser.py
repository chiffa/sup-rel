'''
Created on Dec 15, 2013

@author: ank

Checks if all the relevant information is in the ConfigParser-defined files
'''
import unittest
import src.ConfigParser as cfgPrs

class ConfigsParser_TestSuite(unittest.TestCase):

    @staticmethod
    def pprint(confparserobj):
        for sec in confparserobj.sections():
            print(sec)
            for key in confparserobj[sec]:
                print('\t'+str(key)+'\t:\t'+str(confparserobj[sec][key]))

    def test_Configs_Parser(self):
        cfg1, cfg2 = cfgPrs.parse_configs()
        self.pprint(cfg1)
        print("<================>")
        self.pprint(cfg2)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()