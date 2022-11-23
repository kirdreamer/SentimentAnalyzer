import configparser

import config

properties_file = configparser.ConfigParser()
properties_file.read(config.PROPERTIES_PATH)

db_properties = dict(properties_file.items("db"))


class DatabaseProperties:
    engine = db_properties.get('engine')
    hostname = db_properties.get('hostname')
    port = db_properties.get('port')
    password = db_properties.get('password')
    login = db_properties.get('login')
    name = db_properties.get('name')
    table = db_properties.get('table')
