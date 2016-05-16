from configobj import ConfigObj
config = ConfigObj()
config.filename = 'write_config.ini'


virtual_desktops = {
    'AT_WXPPRO32_H45': {
        'os':'WINDOWS', 
        'os_version':'5.1', 
        'theme':'Classic'}, 
    'AT_W7PRO32_H50': {
        'os':'WINDOWS', 
        'os_version':'6.1', 
        'theme':'Classic'},
    }

config['virtual_desktops'] = virtual_desktops

credentials = {
    'teralab': 'tera%%lab', 
    'teraauto': 'tera%%lab'
    }    
config['credentials'] = credentials

config['section3'] = {}
config['section3']['keyword 1'] = [5, 'dragan', True]
config['section3']['keyword 2'] = ['value11', 'value12', 'value13']

config.write()