'''
Created on Dec 7, 2013
@author: ank
Allows to configure the execution environement
'''
import logging

class Production(object):
    ''' To be used in the production environment '''
    
    servers_are_local=True #''' Are the servers are on the same machine as Python code is running ? '''
    
    local_neo4j="/usr/local/Cellar/neo4j/1.9.5/libexec/data" # ''' Where is the local copy of the neo4j database? '''
    
    server_neo4j="http://localhost:7474" #''' Where is the remote neo4j source? '''

class Test(object):
    ''' To be used for testing and development purposes'''
    
    local_neo4j="/Users/ank/Programming/DBs/neo4j"
