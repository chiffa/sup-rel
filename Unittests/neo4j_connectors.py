'''
Created on Dec 8, 2013
@author: ank
Tests the ability to connect locally and through a server to a neo4j database and measures the IO speed the local/server
database connectors
'''
import unittest
import src.config as cfg
from src.neo4j import local_IO

#TODO: create a new neo4j database for the IO testing purposes?
# => Yes, so we don't pollute the main database


class Test_neo4j_connection(unittest.TestCase):

    def setUp(self):
        pass    

    def test_neo4j_path_existance(self):
        neo4j_readme=cfg.local_neo4j+'/README.txt'
        print('Expecting neo4j README @ '+neo4j_readme,end='')
        try:
            open(neo4j_readme,'r')
        except:
            self.fail("config specifies a non-exisitng file")
        print(' - Succes!')
        
    def test_neo4j_local_IO(self):
        
        print(' - Succes!')
        
    
    def TearDown(self):
        pass 


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()