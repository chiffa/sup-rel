'''
Created on Dec 16, 2013
@author: ank
A class specifically designed for communication with the 
'''

import configparser
import os

rootdir=os.path.abspath(os.path.join(os.path.dirname(__file__),'../schemes/'))
shortnames=['MainScheme']
configsfiles=[rootdir+'/'+name+'.ini' for name in shortnames ]
ErrorString="<To Be Filled>"
allowed_container_types=["_String","_Float","_Int"]
allowed_class_types=["_Index","_Node","_Relation"]


def generate_scheme():
    '''
    '''
    scheme = configparser.ConfigParser()
    scheme["DEFAULT"] = {"_class_type":ErrorString,
                         "_class_name":ErrorString,
                         "_inherits_from":ErrorString}      # Is used to infer type. In case of classType is default, inferred classtype is used, otherwise a warning is issued
    scheme["INDEX"]={"_class_type":"_Index",
                     "_class_name":"Index",
                     "_inherits_from":"BaseClass", 
                     }
    scheme["NODE"]={"_class_type":"_Node",
                     "_class_name":"Node",
                     "_inherits_from":"BaseClass",
                     "Instance_Display_Name":"@self.Instance_ID", # could we use some logic around here like @self.Name + @self.Pointer ?
                     "Instance_ID":"_String" 
                    }   
    scheme["RELATION"]={"class_type":"_Relation",
                     "_class_name":"Relation",
                     "_inherits_from":"BaseClass", 
                        }
    with open(configsfiles[0],'w') as configfile:
        scheme.write(configfile)

def parse_scheme(schemeStorageObject):
    ''' '''

    def improved_read(path):
        '''
        Will throw an IOError in case it can't read a file
        '''
        cfg=configparser.ConfigParser()
        rfs=cfg.read(path)
        if rfs==[]:
            raise IOError('cannot load '+path)
        return cfg
    
    def process():
    
        return improved_read(configsfiles[0]), improved_read(configsfiles[1])


if __name__ == "__main__":
    if not os.path.exists(rootdir):
        os.makedirs(rootdir)
    generate_scheme()