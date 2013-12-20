'''
Created on Dec 16, 2013
@author: ank
A class specifically designed for communication with the 
'''

from __future__ import print_function
import ConfigParser
import os
from pprint import PrettyPrinter

rootdir=os.path.abspath(os.path.join(os.path.dirname(__file__),'../schemes/'))
shortnames=['MainScheme']
configsfiles=[rootdir+'/'+name+'.ini' for name in shortnames ]
ErrorString="<To Be Filled>"
allowed_container_types=["_String","_Float","_Int"]
allowed_class_types=["_Index","_Node","_Relation"]


def generate_scheme():
    '''
    '''
    scheme = ConfigParser.SafeConfigParser()
    scheme.set('DEFAULT', "*_class_type", ErrorString)
    scheme.set('DEFAULT', "*_class_name", ErrorString)
    scheme.set('DEFAULT', "*_inherits_from", ErrorString)       # Is used to infer type. In case of classType is default, inferred classtype is used, otherwise a warning is issued
    scheme.set('DEFAULT', "Instance_Display_Name_!", "@self.type+@self._instance_ID")
    scheme.set('DEFAULT', "*_instance_ID_!", "*_String")       # Is used to infer type. In case of classType is default, inferred classtype is used, otherwise a warning is issued
    scheme.add_section('NODE')
    scheme.set('NODE', "*_class_type", 'Node')  #Can be ommited in the classes as long is inheritence is specified
    scheme.set('NODE', "*_class_name", 'node')
    scheme.set('NODE', "*_inherits_from", '@BaseClass')       # Is used to infer type. In case of classType is default, inferred classtype is used, otherwise a warning is issued    
    scheme.add_section('RELATION')
    scheme.set('RELATION', "*_class_type", 'Relation')  #Can be ommited in the classes as long is inheritence is specified
    scheme.set('RELATION', "*_class_name", 'relation')
    scheme.set('RELATION', "*_inherits_from", '@BaseClass')       # Is used to infer type. In case of classType is default, inferred classtype is used, otherwise a warning is issued    
    with open(configsfiles[0],'w') as configfile:
        scheme.write(configfile)

def parse_scheme(schemeStorageObject=""):
    ''' '''

    def improved_read(path):
        '''
        Will throw an IOError in case it can't read a file
        '''
        cfg=ConfigParser.SafeConfigParser()
        rfs=cfg.read(path)
        if rfs==[]:
            raise IOError('cannot load '+path)
        print(cfg.sections())
        return cfg
    
    def process():
        scheme_ini=improved_read(configsfiles[0])
        MainDict={}
        for section in scheme_ini.sections():
            section_name="_".join([elt.capitalize() for elt in section.split('_')])
            MainDict[section_name]={}
            for option in scheme_ini.options(section):
                MainDict[section_name][option]=scheme_ini.get(section, option)
        return MainDict
    
    return process()


if __name__ == "__main__":
    if not os.path.exists(rootdir):
        os.makedirs(rootdir)
    generate_scheme()
    pp=PrettyPrinter(indent=4)
    pp.pprint(parse_scheme())