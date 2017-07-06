import configparser

def getConfiguration(serverConfFile):
    config = configparser.ConfigParser()
    config.read(serverConfFile)
    if 'ServerParameters' in config:
            serverConfig={}
            if 'port' in config['ServerParameters']:
                serverConfig['port'] = config['ServerParameters'].getint('port')
            else:
                raise NameError('port')
            if 'address' in config['ServerParameters']:
                serverConfig['address'] = config['ServerParameters'].get('address')
            else:
                raise NameError('address')
            if 'accesslog' in config['ServerParameters']:
                serverConfig['accesslog'] = config['ServerParameters'].getboolean('accesslog')
            else:
                raise NameError('accesslog')
            if 'loginglevel' in config['ServerParameters']:
                serverConfig['loginglevel'] = config['ServerParameters'].get('loginglevel')
            else:
                raise NameError('loginglevel')
            if 'dbname' in config['ServerParameters']:
                serverConfig['dbname'] = config['ServerParameters'].get('dbname')
            else:
                serverConfig['dbname'] = 'rules.sqlite3'
            return serverConfig
    else:
         raise ValueError('Misssing configuration in server config')




