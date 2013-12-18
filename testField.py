'''
Created on Dec 17, 2013

@author: ank

'''

from __future__ import print_function
import ConfigParser

config = ConfigParser.SafeConfigParser()

config.add_section('SUPERUSER')
config.set('SUPERUSER', 'supernice', 'no')
config.set('DEFAULT', 'nice', 'yes')

config.write(open('test_config.ini','w'))

config2 = ConfigParser.SafeConfigParser()
config2.read('test_config.ini')

print(config2.sections())
print(config2.get(config2.sections()[0], 'nice'))
print(config2.get(config2.sections()[0], 'supernice'))