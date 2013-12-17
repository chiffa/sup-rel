'''
Created on Dec 15, 2013
@author: ank
performs configfiles reading and writing
'''

# Python 2.7 specific imports here
from __future__ import print_function
try:
    import configparser
except:
    import CostumConfigParser as configparser
import os

rootdir=os.path.abspath(os.path.join(os.path.dirname(__file__),'../configs/'))
shortnames=['servers','options']
configsfiles=[rootdir+'/'+name+'.ini' for name in shortnames ]

def generate_configs():
    '''
    Generates the configFiles. Executed only on call of module as if it was main
    '''
    
    def generate_servers_config():
        '''
        Generates configuration files for the different execution types
        '''
        config = configparser.ConfigParser()
        config["DEFAULT"] = {"servers_are_local":"True",
                              "server_neo4j":"http://localhost:7474"}  
        config["TEST"]={"local_neo4j":"/Users/ank/Programming/DBs/neo4j"}
        config["PRODUCTION"]={"local_neo4j":"/usr/local/Cellar/neo4j/1.9.5/libexec/data"}   
        with open(configsfiles[0],'w') as configfile:
            config.write(configfile)
    
    def generate_options_config():
        '''
        Generates configurations files for different runtime options
        '''
        config = configparser.ConfigParser()
        config["JVM"] = {"NEO4J_PYTHON_JVMARGS": "-Xms128M -Xmx512M" ,
                         "JAVA_HOME": "/usr/lib/jvm/java" }
        config["LOGGER"] = {"level":"DEBUG",
                            "output_file":"/Users/ank/Programming/logs/production_neo4j_logger.txt"}
        with open(configsfiles[1],'w') as configfile:
            config.write(configfile)
    
    generate_options_config()
    generate_servers_config()

def parse_configs():
    ''' parses all the relevant configs '''

    def improved_read(path):
        '''
        Parses a config file on given path, in case of failure raises an IOError, 
        '''
        cfg=configparser.ConfigParser()
        rfs=cfg.read(path)
        if rfs==[]:
            raise IOError('cannot load '+path)
        return cfg
    
    return improved_read(configsfiles[0]), improved_read(configsfiles[1])


if __name__ == "__main__":
    if not os.path.exists(rootdir):
        os.makedirs(rootdir)
    generate_configs()