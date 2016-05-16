from configobj import ConfigObj

def print_param(param, value):
    print '%s: %s' % (param, value)
    
config = ConfigObj('default.ini')
user_config = ConfigObj('user.ini')
config.merge(user_config)


print_param('name', config['name'])
print_param('DOB', config['DOB'])

print_param('[Favourites][food]', config['Favourites']['food'])

print_param("['virtual_machines']['AT_W7P32H']['ip']", config['virtual_machines']['AT_W7P32H']['ip'])
print_param("['virtual_machines']['AT_XPP32H']['ip']", config['virtual_machines']['AT_XPP32H']['ip'])