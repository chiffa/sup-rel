'''
Created on Dec 15, 2013

@author: ank

performs config-dependent IO
'''

import configparser
import os

configsfiles=['../configs/servers.ini','../configs/options.ini']
   
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
    cfg1=configparser.ConfigParser()
    cfg1.read(configsfiles[0])
    cfg2=configparser.ConfigParser()
    cfg2.read(configsfiles[1])
    return cfg1, cfg2


if __name__ == "__main__":
    if not os.path.exists('../configs'):
        os.makedirs('../configs')
    generate_configs()