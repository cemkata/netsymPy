from networkAddresses import is_valid_ip
from numericChecks import is_port
import configparser
from os import chdir, listdir, remove

chdir('..')

config = configparser.RawConfigParser()

portCheck = True
while portCheck:
  port = input("Enter the port. Default is 8080 >>> ") or '8080'
  portCheck = not is_port(port)

IPCheck = True
while IPCheck:
  ipAddress = input("Enter the ip. Default is 0.0.0.0 >>> ") or '0.0.0.0'
  IPCheck = not is_valid_ip(port)

accesslogCheck = True
while accesslogCheck:
  choise = input("Do you want to enable the access.log (y/n)? >>> ")
  if choise.lower() == 'y':
     accesslog = 'True'
     accesslogCheck = False
  elif choise.lower() == 'n':
     accesslog = 'False'
     accesslogCheck = False

logLevelCheck = True
while logLevelCheck:
  print("(d)ebug")
  print("(e)rror")
  print("(w)arning")
  print("(c)ritical")
  print("(i)nfo")
  print("(n)one")
  choise = input("Do you want to enable the access.log (y/n)? >>> ")
  if choise.lower() == 'd':
     logLevel = 'debug'
     logLevelCheck = False
  elif choise.lower() == 'e':
     logLevel = 'error'
     logLevelCheck = False
  elif choise.lower() == 'w':
     logLevel = 'warning'
     logLevelCheck = False
  elif choise.lower() == 'c':
     logLevel = 'critical'
     logLevelCheck = False
  elif choise.lower() == 'i':
     logLevel = 'info'
     logLevelCheck = False
  elif choise.lower() == 'n':
     logLevel = 'none'
     logLevelCheck = False

dbName = input("Enter the database name. Default is rules.sqlite3 >>> ") or 'rules.sqlite3'

config.add_section('ServerParameters')
config.set('ServerParameters', ';Server port', '')
config.set('ServerParameters', 'port', port)
config.set('ServerParameters', ';Server address 0.0.0.0 for all intefaces', '')
config.set('ServerParameters', 'address', ipAddress)
config.set('ServerParameters', ';Enable loging', '')
config.set('ServerParameters', 'accesslog', accesslog)
config.set('ServerParameters', ';log levels: debug, error, warning, critical, info, notset (default = info)', '')
config.set('ServerParameters', 'loginglevel', logLevel)
config.set('ServerParameters', ';database name if none is defined the program will use the default one (rules.sqlite3)', '')
config.set('ServerParameters', 'dbname', dbName)

with open('networksym.ini', 'w') as configfile:
    config.write(configfile)


