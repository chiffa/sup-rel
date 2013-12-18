'''
Created on Dec 17, 2013
@author: ank
I am fedup with the differences in behavior of ConfigParser between python2.7 
and python3.3 and fed up with the py3.3 bad accessibility of the parsed values
from the code (it is a dict, but it doesn't behave as a dict)

This class is implemented as a factory with costum read/write methods to make
the whole entreprise more sane
'''

from __future__ import print_function
from collections import MutableMapping

class OneLvlDict(MutableMapping):
    """A allowing no recursion at all"""

    def __init__(self, *args, **kwargs):
        self.store = dict()
        self.update(dict(*args, **kwargs))  # use the free update to set keys

    def __getitem__(self, key):
        return self.store[self.__keytransform__(key)]

    def __setitem__(self, key, value):
        self.store[self.__keytransform__(key)] = value

    def __delitem__(self, key):
        del self.store[self.__keytransform__(key)]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def __keytransform__(self, key):
        return key
    
    def __repr__(self):
        return self.store.__repr__()
    
    def __str__(self):
        return self.store.__str__()


class ConfigParser(MutableMapping):
    #We'll just use it as a parser/writer and a factory
    
    """A dictionary that applies an arbitrary key-altering
       function before accessing the keys"""

    def __init__(self, *args, **kwargs):
        self.store = dict()
        self.update(dict(*args, **kwargs))  # use the free update to set keys

    def __getitem__(self, key):
        return self.store[self.__keytransform__(key)]

    def __setitem__(self, key, value):
        self.store[self.__keytransform__(key)] = value

    def __delitem__(self, key):
        del self.store[self.__keytransform__(key)]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def __keytransform__(self, key):
        return key
    
    def __repr__(self):
        return self.store.__repr__()
    
    def __str__(self):
        return self.store.__str__()
    
    def pre_write(self):
        for elt in self.dict
    
    def write(self, fp, space_around_delimiters=True):
        """Write an .ini-format representation of the configuration state.
        If `space_around_delimiters' is True (the default), delimiters
        between keys and values are surrounded by spaces.
        """
        if space_around_delimiters:
            d = " {} ".format(self._delimiters[0])
        else:
            d = self._delimiters[0]
        if self._defaults:
            self._write_section(fp, self.default_section,
                                    self._defaults.items(), d)
        for section in self._sections:
            self._write_section(fp, section,
                                self._sections[section].items(), d)
    def read(self):
        '''
        Unlike the default parser will raise an IOError
        '''

if __name__ == "__main__":
    ND=ConfigParser({1:{1:'a',2:'b'},2:'b'})
    print(ND)
    ND.pprint()