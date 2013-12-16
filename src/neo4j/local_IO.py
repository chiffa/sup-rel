'''
Created on Dec 15, 2013
@author: ank
Deals with the local IO for the neo4j database
'''

import src.config as cfg
import logging
import os

class Connector(object):
    
    
    def __init__(self, logger_configs=cfg.Test.logger_confs, JVM_Configs=cfg.Test.jvm_confs, local_server_Configs=cfg.Test.):
        logging.basicConfig()
        for argument, value in JVM_Configs:
            logging.debug("setting "+argument+" to "+value)
            os.environ[argument]=value
            
        

import os
os.environ['NEO4J_PYTHON_JVMARGS']='-Xms128M -Xmx512M'
# os.environ['JAVA_HOME']='/usr/lib/jvm/java'
from neo4j import GraphDatabase

neo=GraphDatabase(cfg.Test.local_neo4j) 


#Containers contain indexes and objects that have been loaded from the scheme-defined objects

def create_scheme(text_file):
    '''
    creates a scheme file from a text file containing 
    '''

def load_from_scheme(neo, schemeObject, container):
    with neo.transaction:
        prot_idx=neo.node.indexes.get('proteins')
        gos_idx=neo.node.indexes.get('gos')
        for rel in neo.reference_node.GOS:
            gos = rel.end
        for rel in neo.reference_node.PROTEINS:
            proteins = rel.end

def create_from_scheme(neo, schemeObject,container):
    with neo.transaction:
        proteins=neo.node()
        gos=neo.node()
        neo.reference_node.PROTEINS(proteins)
        neo.reference_node.GOS(gos)
        prot_idx=neo.node.indexes.create('proteins')
        gos_idx=neo.node.indexes.create('gos')


class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        