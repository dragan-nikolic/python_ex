import yaml
import pprint


data = yaml.load(open("table.yml"), Loader=yaml.Loader)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)

# {   
#     'column_names_check': False,
#     'columns': {   'column_name': {   'abs_max': 14.3,
#                                       'abs_min': 0.1,
#                                       'abs_non_zero_min': 1.5,
#                                       'distinct_values': [   'value1',
#                                                              'value2',
#                                                              'value3'],
#                                       'max': 30,
#                                       'min': -10,
#                                       'nulls': False,
#                                       'unique': True}},
#     'foreign_keys': [   {   'parent_key': ['pcolumn1', 'pcolumn2'],
#                             'parent_table': 'table_id1',
#                             'table_key': ['column1', 'column2']},
#                         {   'parent_key': ['pcolumnA'],
#                             'parent_table': 'table_id2',
#                             'table_key': ['columnA']}
#                     ],
#     'table': 'REST'
# }


data = yaml.load(open("test.yml"), Loader=yaml.Loader)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)

# {   
#     'users': {   'admins': [   {   1: {   'account': 'e-xact testing',
#                                           'password': 'password_1',
#                                           'username': 'admin_1'}},
#                                {   2: {   'account': 'e-xact testing pos',
#                                           'password': 'password_2',
#                                           'username': 'admin_2'}}],
#                  'merchants': [   {   'account': 'e-xact testing',
#                                       'password': 'password_1',
#                                       'username': 'merchant_1'},
#                                   {   'account': 'e-xact testing',
#                                       'password': 'password_2',
#                                       'username': 'merchant_2'
#                                     }
#                             ]
#             }
# }

