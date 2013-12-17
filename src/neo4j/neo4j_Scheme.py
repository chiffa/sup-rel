'''
Created on Dec 16, 2013
@author: ank
Contains the Scheme and StrictScheme classes that is used to build neo4j database scheme and 
'''

class SchemeGenerator(object):
    '''
    Used to build a neo4j object
    '''

    def __init__(self, params=[]):
        '''
        Constructor
        '''
        self.contents="pretty please"
    
    def execute(self):    
        print("Scheme says: "+self.contents)
        
        
class StrictSchemeGenerator(SchemeGenerator):
    '''
    In addition to implementing the normal interface of a string, also 
    controls that the realtions fit well one another.
    '''
    
    
    def __intit__(self, params=[]):
        '''
        Constructor
        '''
        super(SchemeGenerator,self).__init__(params)
    
    def execute(self):
        print("StrictScheme says: "+self.contents)
        
        

if __name__ == "__main__":
    StS=StrictSchemeGenerator()
    StS.execute()