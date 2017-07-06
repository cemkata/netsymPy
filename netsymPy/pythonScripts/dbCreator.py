from sqlHelper import createDB, setDBname
from aconfigParser import getConfiguration
from os import chdir
# this will change the folder wher the static files are set but doesnt work with automatic reload on file change
chdir('..')
serverConfig = getConfiguration('networksym.ini') # Here we are reading the server config file (ini)
setDBname(serverConfig['dbname'])

createDB()
