import yaml

data = {
    'users': {
        'admins': [
            {
                'account': 'e-xact testing',
                'password': 'password_1',
                'username': 'admin_1'
            },
            {
                'account': 'e-xact testing pos',
                'password': 'password_2',
                'username': 'admin_2'
            },
        ],

        'merchants': [
            {
                'account': 'e-xact testing',
                'password': 'password_1',
                'username': 'merchant_1'
            },
        ],
    }
}

f = open("demo_write.yml", "w")
yaml.dump(data, f)
f.close()
