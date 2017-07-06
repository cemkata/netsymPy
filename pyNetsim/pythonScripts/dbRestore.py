import sqlite3
from aconfigParser import getConfiguration
from os import chdir, listdir, remove

chdir('..')

serverConfig = getConfiguration('networksym.ini') # Here we are reading the server config file (ini)

def createPages():
  backups = listdir("./backups/")
  a=[]
  c=[]
  while backups:
      if len(backups) % 10 == 0 and c:
         a.append(list(c))
         c=[]
      else:
         b = backups.pop()
         c.append(b)
  a.append(list(c))

  return a

def menu():
  pages = createPages()
  indexPage = 0
  while True:
    i = 0
    for item in pages[indexPage]:
       print( str(i) + '. ' + item)
       i = i + 1
    print('For next page press n for previous press p.')
    print('Enter the number of the backup you want to restore')
    print('To exit press x.')
    while True:
       choise = input('>>>')
       if (choise == 'n' or choise == 'N') and indexPage < len(pages):
          indexPage = indexPage + 1
       if (choise == 'p' or choise == 'P') and indexPage > 0:
          indexPage = indexPage + 1
       if (choise == 'x' or choise == 'X'):
          exit()
       if choise in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
          remove(serverConfig['dbname'])
          with open('./backups/'+ pages[indexPage][int(choise)], 'r') as content_file:
               sqlQuery = content_file.read()
          sqlQuerys = sqlQuery.split(';')
          conn = sqlite3.connect(serverConfig['dbname'])
          for s in sqlQuerys:
              if s.endswith('COMMIT'):
                 break
              conn.execute(s)
              conn.commit()
          conn.close()
          print('Done!')
          return

menu()
