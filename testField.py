'''
Created on Dec 17, 2013

@author: ank

'''

from __future__ import print_function, super
from neo4j import GraphDatabase


class BetterDict(dict):
    
    def __init__(self):
        super(dict,self).__init__()
    

if __name__ == "__main__":
    BD=BetterDict()