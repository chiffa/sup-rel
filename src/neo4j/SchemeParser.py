'''
Created on Dec 16, 2013
@author: ank
A class specifically designed for communication with the 
'''

import configparser
import os

rootdir=os.path.abspath(os.path.join(os.path.dirname(__file__),'../configs/'))
shortnames=['servers','options']
configsfiles=[rootdir+'/'+name+'.ini' for name in shortnames ]

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        