'''
Created on Dec 16, 2013
@author: ank
A class specifically designed for communication with the 
'''

from __future__ import print_function
import ConfigParser
import os
from pprint import PrettyPrinter
from itertools import compress
# import string

rootdir=os.path.abspath(os.path.join(os.path.dirname(__file__),'../schemes/'))
shortnames=['MainScheme','NoteScheme']
schemefiles=[rootdir+'/'+name+'.ini' for name in shortnames ]
ErrorString="<broken inheritence!>"
ComputationString="<computed>"
# Additional levels of restriction, we'll leave them out for now
allowed_container_types=["_String","_Float","_Int"]
allowed_class_types=["_Index","_Node","_Relation"]


def generate_scheme():
    '''
    '''
    scheme = ConfigParser.SafeConfigParser()
    scheme.set('DEFAULT', "*_class_type", ComputationString)            #Can be ommited in the classes as long is inheritence is specified
    scheme.set('DEFAULT', "*_inherits_from", ErrorString)       # Is used to infer type. In case of classType is default, inferred classtype is used, otherwise a warning is issued
    scheme.set('DEFAULT', "Instance_Display_Name_!", "@self.class_name+@self._instance_ID")
    scheme.set('DEFAULT', "*_instance_ID_!", "*_String")
    scheme.add_section('NODE')
    scheme.set('NODE', "*_class_type", 'Node')
    scheme.set('NODE', "*_inherits_from", '@BaseClass')  
    scheme.add_section('RELATION')
    scheme.set('RELATION', "*_class_type", 'Relation')
    scheme.set('RELATION', "*_inherits_from", '@BaseClass')      # Is used to infer type. In case of classType is default, inferred classtype is used, otherwise a warning is issued    
    scheme.add_section('ADJACENCY')                              #Will only be used for the strict schemes; RESPECTS INHERITENCE MODELS
    scheme.set('ADJACENCY', "*_class_type", 'Adjacency')
    scheme.set('ADJACENCY', "*_inherits_from", '@BaseClass')
    scheme.set('ADJACENCY', "*_permitted_connects", '@node, @relation')
    with open(schemefiles[0],'w') as configfile:
        scheme.write(configfile)

def parse_scheme(path_to_scheme,schemeStorageObject=""):
    ''' '''

    def improved_read(path):
        '''
        Will throw an IOError in case it can't read a file
        '''
        scheme_ini=ConfigParser.SafeConfigParser()
        rfs=scheme_ini.read(path)
        if rfs==[]:
            raise IOError('cannot load '+path)
        MainDict={}
        for section in scheme_ini.sections():
            section_name="_".join([elt.capitalize() for elt in section.split('_')])
            MainDict[section_name]={}
            for option in scheme_ini.options(section):
                MainDict[section_name][option]=scheme_ini.get(section, option).lower()
        return MainDict
    
    def check_config(scheme_dict):        
        
        def strict_lvl2_flatten(dico):
            '''
            Flattens dicts up to level 2 deep, assuming all the values in the global dictionary are nested dictionaries
            and all the keys and values are strings
            '''
            FlatDict={}
            for superkey in dico.keys():
                for subkey in dico[superkey].keys():
                    FlatDict[superkey.upper()+"/"+subkey.lower()]=dico[superkey][subkey]
            return FlatDict
        
        def ref_scheme_error_print(erred_Dict_List,flatenend_actual_dict):
            ''' prints beautifully the error pairs (as much as an error can be beautiful) '''
            returnString="\n\n"
            for elt in errlist:
                returnString+=elt[0]+ " = "+elt[1]+ " expected\n"
                coelt=flatenend_actual_dict.get(elt[0])
                try:
                    returnString+=elt[0]+" = "+coelt+" found\n\n"
                except TypeError:
                    returnString.append("nothing found\n")
            return returnString
        
        def inheritance_error_print(flattened_actual_dict):
            ''' prints all the nodes that are due to the inheritence'''
            returnString="\n"
            for composite_key, value in d2.iteritems():
                if value==ErrorString:
                    returnString+=composite_key+"\n"
            return returnString
        
        def build_inheritance(flattened_actual_dict):
            ''' '''
            Inheritant2Inherited={}
            for key, value in flattened_actual_dict.iteritems():
                if "*_inherits_from" in key:
                    Inheritant2Inherited[key.split('/')[0].lower()]=value.strip('@')
            return Inheritant2Inherited
        
        def check_connexity(InhDict):
            ''' in addition to checking that no loops are present, also checks that none of the classes is attached to the baseclass'''
            
            def reduce_inheritance_dictionnary(Inh_Dict):
                while True:
                    prevDict=Inh_Dict.copy()
                    leaf_classes=set(Inh_Dict.keys()).difference(set(Inh_Dict.values()))
                    for cls in leaf_classes:
                        if Inh_Dict[cls]!="baseclass":
                            del Inh_Dict[cls]
                    if prevDict==Inh_Dict:
                        break
                for cls in ['node', 'adjacency', 'relation']:
                    del Inh_Dict[cls]
                return Inh_Dict
            
            Reduced_Class_Dict=reduce_inheritance_dictionnary(InhDict)
            if len(Reduced_Class_Dict)==0:
                return
            Inerited2Inheritant={}
            for key, value in Reduced_Class_Dict.iteritems():
                if value not in Inerited2Inheritant.keys():
                    Inerited2Inheritant[value]=[]
                Inerited2Inheritant[value]=Inerited2Inheritant[value].append(key)
            if "baseclass" in Inerited2Inheritant.keys():
                errmsg="Non-base classes inherit from the baseclass: \n"+Inerited2Inheritant["baseclass"]
                raise Exception(errmsg)
            else: 
                errmsg="Circular inheritance for the following objects: \n"+Inerited2Inheritant.keys().__str__()
                raise Exception(errmsg)
            
            #TODO:feature, add verification of different inheritance loops
                
            
        
        ref_scheme=improved_read(schemefiles[0])
        d1,d2=(strict_lvl2_flatten(ref_scheme),strict_lvl2_flatten(scheme_dict))
        if not all(item in scheme_dict.items() for item in ref_scheme.items()):
            errlist=list(compress(d1.items(),[item not in d2.items() for item in d1.items()]))
            errstr="Reference classes have been altered. Please return Default, Node, Relation and Adjacency classes in their initial states:"+ref_scheme_error_print(errlist,d2)
            raise Exception(errstr)
        if ErrorString in d2.values():
            errstr="A class that inherits from no-one has been found. He feels lonely. Please correct this for: "+inheritance_error_print(d2)
            raise Exception(errstr)
        Inheritant2Inherited = build_inheritance(d2)
        check_connexity(Inheritant2Inherited)
        
        # TODO: check that the inheritence actually has a tree-structure
        # implementation: dict of dicts?, then intersection of keys and values, iterate until no nodes remain
        # Compare the both sets to check that no nodes are suspended in the void.
        # inheritant : inerited => all the keys that are not in values
        # Single inheritance Only 
        
    def complete(scheme_dict):
        pass
    
    def process():
        scheme_dict=improved_read(path_to_scheme)
        # TODO : inflate inheritant2inherited her and split min config and connexity verification in 2; then re-split the connexity verification into smaller caseclasses
        check_config(scheme_dict)
        # TODO: Inflate the class names, types and features => use the accumulation on the baseclasses method and inheritant2inherited verification
        # TODO: Set computable categories in the neo4j_Scheme instance
        

        return scheme_dict
    
    return process()


if __name__ == "__main__":
    if not os.path.exists(rootdir):
        os.makedirs(rootdir)
    generate_scheme()
    pp=PrettyPrinter(indent=4)
    pp.pprint(parse_scheme(schemefiles[1]))