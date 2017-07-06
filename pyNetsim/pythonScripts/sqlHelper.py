import sqlite3
from pathlib import Path

dbFileName = ''

def setDBname(name):
    global dbFileName
    dbFileName = name

def connectToDB():
   global dbFileName
   my_file = Path(dbFileName)
   if my_file.is_file():
      return sqlite3.connect(dbFileName)
   else:
      import errno
      import os
      raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), dbFileName)

def insertRuleSQL(tcArguments):
   conn = connectToDB()
   toCheck=['portSrc', 'portDst', 'txtDelay', 'txtDelayJitter', 'txtDelayCorrelation', 'txtReorder', 'txtReorderCorrelation',
            'txtGap', 'txtLoss', 'txtLossCorrelation', 'txtDup', 'txtDupCorrelation', 'txtCurp', 'txtCurptionCorrelation',
            'txtBufferLimit', 'transportPrtc', 'txtBandwidth', 'ipSrc', 'ipSrcSub', 'ipDest', 'ipDestSub', 'macSrc', 'macDest',
            'selIntface', 'selDelayDistribution','flowlabelTOS','transport','ipVer']
   fiterArguments = {}
   for item in toCheck:
    if item not in tcArguments:
        fiterArguments[item] = 'NULL'
    else:
        fiterArguments[item] = '"'+str(tcArguments[item])+'"'
   try:
     with open('./sqlScripts/insertRule.sql', 'r') as content_file:
      content = content_file.read()
     sqlQuery=content.format('NULL', fiterArguments['selIntface'], fiterArguments['txtBufferLimit'], fiterArguments['txtBandwidth'],
                             fiterArguments['selDelayDistribution'], fiterArguments['txtDelay'], fiterArguments['txtDelayJitter'],
                             fiterArguments['txtDelayCorrelation'], fiterArguments['txtReorder'], fiterArguments['txtReorderCorrelation'],
                             fiterArguments['txtGap'], fiterArguments['txtLoss'], fiterArguments['txtLossCorrelation'],
                             fiterArguments['txtDup'], fiterArguments['txtDupCorrelation'], fiterArguments['txtCurp'],
                             fiterArguments['txtCurptionCorrelation'], fiterArguments['portSrc'], fiterArguments['portDst'],
                             fiterArguments['macSrc'], fiterArguments['macDest'], fiterArguments['flowlabelTOS'],
                             fiterArguments['transport'], fiterArguments['transportPrtc'], fiterArguments['ipSrc'],
                             fiterArguments['ipSrcSub'], fiterArguments['ipDest'], fiterArguments['ipDestSub'], fiterArguments['ipVer'], '"On"'
                          )
     conn.execute(sqlQuery)
     conn.commit()
     #this will take the next available ID from the sqlite_sequence table. Where the name is 'rules'
     with open('./sqlScripts/getIDofLastRule.sql', 'r') as content_file:
       content = content_file.read()
     ruleID=conn.execute(content).fetchone()[0] #this takes the next available ID from the sqlite_sequence table. Where the name is 'rules'
     conn.close()
     intRuleID=int(ruleID)
     intRuleID=intRuleID-1#Because the ruleID is the next ID but we need the previous we subtract 1
   except (sqlite3.DataError, sqlite3.IntegrityError, sqlite3.Warning, sqlite3.Error, sqlite3.OperationalError, sqlite3.DatabaseError, sqlite3.InternalError, sqlite3.InterfaceError, sqlite3.ProgrammingError, sqlite3.NotSupportedError) as err:
       intRuleID=[]
       intRuleID.append(str(err.args))
       intRuleID.append(sqlQuery)
   except FileNotFoundError as err:
       intRuleID=[]
       intRuleID.append("Sql query file not found " + str(err.args))
   return intRuleID

def insertRootRuleSQL():
   conn = connectToDB()
   try:
      sqlQuery = "Select `seq` from `sqlite_sequence` where `name`='rules_tbl' ;"
      sqlOutput = conn.execute(sqlQuery)
      if sqlOutput.fetchone()[0] is '1':
          sqlQuery = "Update `sqlite_sequence` set `seq` = 2 where `name`='rules_tbl' ;"
          conn.execute(sqlQuery)
      else:
           pass
      conn.commit()
      conn.close()
      sqlComand = "No problem all have passed."
   except (sqlite3.DataError, sqlite3.IntegrityError, sqlite3.Warning, sqlite3.Error, sqlite3.OperationalError, sqlite3.DatabaseError, sqlite3.InternalError, sqlite3.InterfaceError, sqlite3.ProgrammingError, sqlite3.NotSupportedError) as err:
       sqlComand=[]
       sqlComand.append(str(err.args))
       sqlComand.append(sqlQuery)
   except FileNotFoundError as err:
       sqlComand=[]
       sqlComand.append("Sql query file not found " + str(err.args))
   return sqlComand

def exportDB():
   con = connectToDB()
   from datetime import datetime
   with open('./backups/dump_'+str(datetime.now()).replace(":", "_")+'.sql', 'w') as f:
      for line in con.iterdump():
        f.write('%s\n' %line)

def deleteDB():
  conn = connectToDB()
  sqlQuery =  "delete from rules_tbl;"
  conn.execute(sqlQuery)
  sqlQuery = "UPDATE `sqlite_sequence` SET `seq`= 2 WHERE `name`='rules_tbl';"
  conn.execute(sqlQuery)
  conn.commit()
  conn.close()

def getAllrules():
   conn = connectToDB()
   try:
     with open('./sqlScripts/selectAll.sql', 'r') as content_file:
        sqlQuery = content_file.read()

     sqlOutput = conn.execute(sqlQuery)
     rules=[]
     for argument in sqlOutput:
         curenRule={}
         curenRule['selIntface'] = argument[0]
         curenRule['txtBufferLimit'] = argument[1]
         curenRule['txtBandwidth'] = argument[2]
         curenRule['distribution'] = argument[3]
         curenRule['txtDelay'] = argument[4]
         curenRule['txtDelayJitter'] = argument[5]
         curenRule['txtDelayCorrelation'] = argument[6]
         curenRule['txtReorder'] = argument[7]
         curenRule['txtReorderCorrelation'] = argument[8]
         curenRule['txtGap'] = argument[9]
         curenRule['txtLoss'] = argument[10]
         curenRule['txtLossCorrelation'] = argument[11]
         curenRule['txtDup'] = argument[12]
         curenRule['txtDupCorrelation'] = argument[13]
         curenRule['txtCurp'] = argument[14]
         curenRule['txtCurptionCorrelation'] = argument[15]
         curenRule['portSrc'] = argument[16]
         curenRule['portDst'] = argument[17]
         curenRule['macSrc'] = argument[18]
         curenRule['macDest'] = argument[19]
         curenRule['flowlabelTOS'] = argument[20]
         curenRule['transport'] = argument[21]
         curenRule['transportPrtc'] = argument[22]
         curenRule['ipSrc'] = argument[23]
         curenRule['ipSrcSub'] = argument[24]
         curenRule['ipDest'] = argument[25]
         curenRule['ipDestSub'] = argument[26]
         curenRule['ipVersion'] = argument[27]
         curenRule['rulestatus'] = argument[28]
         curenRule['ruleID'] = argument[29]
         rules.append(curenRule.copy())
     return rules
     conn.commit()
     conn.close()

   except (sqlite3.DataError, sqlite3.IntegrityError, sqlite3.Warning, sqlite3.Error, sqlite3.OperationalError, sqlite3.DatabaseError, sqlite3.InternalError, sqlite3.InterfaceError, sqlite3.ProgrammingError, sqlite3.NotSupportedError) as err:
     conn.commit()
     conn.close()

def removeEmptyArguments(argument):
         curenRule={}
         if argument[0] is not None:
            curenRule['selIntface'] = argument[0]
         if argument[1] is not None:
            curenRule['txtBufferLimit'] = argument[1]
         if argument[2] is not None:
            curenRule['txtBandwidth'] = argument[2]
         if argument[3] is not None:
            curenRule['selDelayDistribution'] = argument[3]
         if argument[4] is not None:
            curenRule['txtDelay'] = argument[4]
         if argument[5] is not None:
            curenRule['txtDelayJitter'] = argument[5]
         if argument[6] is not None:
            curenRule['txtDelayCorrelation'] = argument[6]
         if argument[7] is not None:
            curenRule['txtReorder'] = argument[7]
         if argument[8] is not None:
            curenRule['txtReorderCorrelation'] = argument[8]
         if argument[9] is not None:
            curenRule['txtGap'] = argument[9]
         if argument[10] is not None:
            curenRule['txtLoss'] = argument[10]
         if argument[11] is not None:
            curenRule['txtLossCorrelation'] = argument[11]
         if argument[12] is not None:
            curenRule['txtDup'] = argument[12]
         if argument[13] is not None:
            curenRule['txtDupCorrelation'] = argument[13]
         if argument[14] is not None:
            curenRule['txtCurp'] = argument[14]
         if argument[15] is not None:
            curenRule['txtCurptionCorrelation'] = argument[15]
         if argument[16] is not None:
            curenRule['portSrc'] = argument[16]
         if argument[17] is not None:
            curenRule['portDst'] = argument[17]
         if argument[18] is not None:
            curenRule['macSrc'] = argument[18]
         if argument[19] is not None:
            curenRule['macDest'] = argument[19]
         if argument[20] is not None:
            curenRule['flowlabelTOS'] = argument[20]
         if argument[21] is not None:
            curenRule['transport'] = argument[21]
         if argument[22] is not None:
            curenRule['transportPrtc'] = argument[22]
         if argument[23] is not None:
            curenRule['ipSrc'] = argument[23]
         if argument[24] is not None:
            curenRule['ipSrcSub'] = argument[24]
         if argument[25] is not None:
            curenRule['ipDest'] = argument[25]
         if argument[26] is not None:
            curenRule['ipDestSub'] = argument[26]
         if argument[27] is not None:
            curenRule['ipVer'] = argument[27]
         if argument[28] is not None:
            curenRule['rulestatus'] = argument[28]
         if argument[29] is not None:
            curenRule['ruleID'] = argument[29]
         return curenRule


def getAllEnabledRules():
   conn = connectToDB()
   try:
     with open('./sqlScripts/selectAllEnabled.sql', 'r') as content_file:
        sqlQuery = content_file.read()

     sqlOutput = conn.execute(sqlQuery)
     rules=[]
     for e in sqlOutput:
         rules.append(removeEmptyArguments(e).copy())
     return rules
     conn.commit()
     conn.close()

   except (sqlite3.DataError, sqlite3.IntegrityError, sqlite3.Warning, sqlite3.Error, sqlite3.OperationalError, sqlite3.DatabaseError, sqlite3.InternalError, sqlite3.InterfaceError, sqlite3.ProgrammingError, sqlite3.NotSupportedError) as err:
     conn.commit()
     conn.close()

def deleteRules(ruleID):
   conn = connectToDB()
   try:
     with open('./sqlScripts/deleteRuleByID.sql', 'r') as content_file:
       content = content_file.read()
       sqlQuery=content.format(ruleID)
       conn.execute(sqlQuery)
       conn.commit()
       conn.close()

   except (sqlite3.DataError, sqlite3.IntegrityError, sqlite3.Warning, sqlite3.Error, sqlite3.OperationalError, sqlite3.DatabaseError, sqlite3.InternalError, sqlite3.InterfaceError, sqlite3.ProgrammingError, sqlite3.NotSupportedError) as err:
     conn.commit()
     conn.close()

def disableRules(ruleID):
   conn = connectToDB()
   try:
     with open('./sqlScripts/selectRuleStatusByID.sql', 'r') as content_file:
      content = content_file.read()

     ids=ruleID.split(';')
     for currentID in ids:
         sqlQuery=content.format(currentID)
         sqlOutput = conn.execute(sqlQuery)
         with open('./sqlScripts/updateRuleStatus.sql', 'r') as content_file:
              content = content_file.read()
         if sqlOutput.fetchone()[0] is 'on':
            sqlQuery=content.format("'off'", currentID)
         else:
            sqlQuery=content.format("'on'", currentID)
         conn.execute(sqlQuery)
     conn.commit()
     conn.close()

   except (sqlite3.DataError, sqlite3.IntegrityError, sqlite3.Warning, sqlite3.Error, sqlite3.OperationalError, sqlite3.DatabaseError, sqlite3.InternalError, sqlite3.InterfaceError, sqlite3.ProgrammingError, sqlite3.NotSupportedError) as err:
     conn.commit()
     conn.close()

def getIPversionByID(ruleID):
   conn = connectToDB()
   try:
     sqlQuery="select `ipVer` from `rules_tbl` where `id`='{}'".format(ruleID)
     sqlOutput = conn.execute(sqlQuery)
     ipver =  sqlOutput.fetchone()[0]
     conn.commit()
     conn.close()
     return ipver

   except (sqlite3.DataError, sqlite3.IntegrityError, sqlite3.Warning, sqlite3.Error, sqlite3.OperationalError, sqlite3.DatabaseError, sqlite3.InternalError, sqlite3.InterfaceError, sqlite3.ProgrammingError, sqlite3.NotSupportedError) as err:
     conn.commit()
     conn.close()

def getRuleByID(ruleID):

   conn = connectToDB()
   try:
     with open('./sqlScripts/selectRuleByID.sql', 'r') as content_file:
        content = content_file.read()
     sqlQuery = content.format(ruleID)
     sqlOutput = conn.execute(sqlQuery)
     rule = removeEmptyArguments(sqlOutput.fetchone()).copy()
     conn.commit()
     conn.close()
     return rule

   except (sqlite3.DataError, sqlite3.IntegrityError, sqlite3.Warning, sqlite3.Error, sqlite3.OperationalError, sqlite3.DatabaseError, sqlite3.InternalError, sqlite3.InterfaceError, sqlite3.ProgrammingError, sqlite3.NotSupportedError) as err:
     conn.commit()
     conn.close()

def getIntByRuleID(ruleID):

   conn = connectToDB()
   try:
     sqlQuery="select `selIntface` from `rules_tbl` where `id`='{}'".format(ruleID)
     sqlOutput = conn.execute(sqlQuery)
     infName =  sqlOutput.fetchone()[0]
     conn.commit()
     conn.close()
     return infName

   except (sqlite3.DataError, sqlite3.IntegrityError, sqlite3.Warning, sqlite3.Error, sqlite3.OperationalError, sqlite3.DatabaseError, sqlite3.InternalError, sqlite3.InterfaceError, sqlite3.ProgrammingError, sqlite3.NotSupportedError) as err:
     conn.commit()
     conn.close()

def updateRuleSQL(tcArguments, id):
   conn = connectToDB()
   toCheck=['portSrc', 'portDst', 'txtDelay', 'txtDelayJitter', 'txtDelayCorrelation', 'txtReorder', 'txtReorderCorrelation',
            'txtGap', 'txtLoss', 'txtLossCorrelation', 'txtDup', 'txtDupCorrelation', 'txtCurp', 'txtCurptionCorrelation',
            'txtBufferLimit', 'transportPrtc', 'txtBandwidth', 'ipSrc', 'ipSrcSub', 'ipDest', 'ipDestSub', 'macSrc', 'macDest',
            'selIntface', 'selDelayDistribution','flowlabelTOS','transport','ipVer']
   fiterArguments = {}
   for item in toCheck:
    if item not in tcArguments:
        fiterArguments[item] = 'NULL'
    else:
        fiterArguments[item] = '"'+str(tcArguments[item])+'"'
   try:
     with open('./sqlScripts/updateRule.sql', 'r') as content_file:
      content = content_file.read()
     sqlQuery=content.format(fiterArguments['selIntface'], fiterArguments['txtBufferLimit'], fiterArguments['txtBandwidth'],
                             fiterArguments['selDelayDistribution'], fiterArguments['txtDelay'], fiterArguments['txtDelayJitter'],
                             fiterArguments['txtDelayCorrelation'], fiterArguments['txtReorder'], fiterArguments['txtReorderCorrelation'],
                             fiterArguments['txtGap'], fiterArguments['txtLoss'], fiterArguments['txtLossCorrelation'],
                             fiterArguments['txtDup'], fiterArguments['txtDupCorrelation'], fiterArguments['txtCurp'],
                             fiterArguments['txtCurptionCorrelation'], fiterArguments['portSrc'], fiterArguments['portDst'],
                             fiterArguments['macSrc'], fiterArguments['macDest'], fiterArguments['flowlabelTOS'],
                             fiterArguments['transport'], fiterArguments['transportPrtc'], fiterArguments['ipSrc'],
                             fiterArguments['ipSrcSub'], fiterArguments['ipDest'], fiterArguments['ipDestSub'], fiterArguments['ipVer'], '"On"', id
                          )
     conn.execute(sqlQuery)
     conn.commit()
   except (sqlite3.DataError, sqlite3.IntegrityError, sqlite3.Warning, sqlite3.Error, sqlite3.OperationalError, sqlite3.DatabaseError, sqlite3.InternalError, sqlite3.InterfaceError, sqlite3.ProgrammingError, sqlite3.NotSupportedError) as err:
       intRuleID=[]
       intRuleID.append(str(err.args))
       intRuleID.append(sqlQuery)
       return intRuleID
   except FileNotFoundError as err:
       intRuleID=[]
       intRuleID.append("Sql query file not found " + str(err.args))
       return intRuleID


def compactDB():
   conn = connectToDB()
   try:
       f=[]
       for line in conn.iterdump():
           if line.startswith('INSERT INTO "rules_tbl" VALUES('):
              line = 'INSERT INTO "rules_tbl" VALUES( NULL,' + line.split(",", 1)[1]
              f.append(line)
       conn.commit()
       conn.close()
       exportDB()
       deleteDB()
       conn = connectToDB()
       for line in f:
          conn.execute(line)
       conn.commit()
       conn.close()
   except (sqlite3.DataError, sqlite3.IntegrityError, sqlite3.Warning, sqlite3.Error, sqlite3.OperationalError, sqlite3.DatabaseError, sqlite3.InternalError, sqlite3.InterfaceError, sqlite3.ProgrammingError, sqlite3.NotSupportedError) as err:
     pass

def createDB():
   global dbFileName
   try:
     with open('./sqlScripts/DBCreator.sql', 'r') as content_file:
        sqlQuery = content_file.read()
        sqlQuerys = sqlQuery.split('/* */')
        for s in sqlQuerys:
           conn = sqlite3.connect(dbFileName)
           conn.execute(s)
           conn.commit()
           conn.close()
   except (sqlite3.DataError, sqlite3.IntegrityError, sqlite3.Warning, sqlite3.Error, sqlite3.OperationalError, sqlite3.DatabaseError, sqlite3.InternalError, sqlite3.InterfaceError, sqlite3.ProgrammingError, sqlite3.NotSupportedError) as err:
     conn.commit()
     conn.close()
