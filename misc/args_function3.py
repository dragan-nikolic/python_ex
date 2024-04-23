"""
Demo how to specify argument type and default value
Created on 2024-04-01

@author: dnikolic
"""

def arg_type_and_default_value(first_name: str = 'Dragan', second_name: str = None):
    print('default_value_for_arg')
    print('first_name = {}'.format(first_name))
    print('second_name = {}'.format(second_name))
    print('-----')

arg_type_and_default_value()
arg_type_and_default_value(second_name='Nikolic')
arg_type_and_default_value('Pera')
arg_type_and_default_value('Pera', 'Zdera')
