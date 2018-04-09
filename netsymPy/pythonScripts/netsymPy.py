from bottle import Bottle, run, static_file, request, redirect, template
from filterArguments import getArguments, getDefaultArguments
from loging import log_to_access, LoggingPlugin, EmptyLoggingPlugin, configErrorsLogging
from aconfigParser import getConfiguration
from sqlHelper import insertRuleSQL, insertRootRuleSQL, setDBname, exportDB, deleteDB, getAllrules, disableRules, deleteRules, getAllEnabledRules,\
                      getIPversionByID, getRuleByID, getIntByRuleID, updateRuleSQL
from shellScript import checkROOT, getInfaces, startTC, stopTC, activateRule, getStatistic, deleteRule

from os import chdir
# this will change the folder wher the static files are set but doesnt work with automatic reload on file change
chdir('..')
try:
      serverConfig = getConfiguration('networksym.ini') # Here we are reading the server config file (ini) if there
                                                   #are any exceptions we loggthem other wise we output all is ok.
                                                   # And change use the toExit flag to skip the progrma exiting
except NameError as err:
      configErrorsLogging("Server config error. Missing filed " + str(err.args))
except ValueError as err:
      configErrorsLogging("Server config error. " + str(err.args))
except FileNotFoundError as err:
      configErrorsLogging("Server config is missing. " + str(err.args))
else:
      configErrorsLogging("Server config parsed server is starting. ", toExit=False)

try:
      checkROOT()
except NameError as err:
      configErrorsLogging("You are not root!")


app = Bottle()

if serverConfig['accesslog']:
   app.install(log_to_access) # this log only in access.log

if serverConfig['loginglevel'] is not 'notset':#Set the log level
   event=LoggingPlugin()
   event.setup(app=app, logLevel = serverConfig['loginglevel']) #This logs to all other errors
else:
   event=EmptyLoggingPlugin()
   event.setup(app=app) #Empty loger just to save code refactoring if there is no log level

setDBname(serverConfig['dbname'])


static_files = './static/'
existingLinks = ['AddV4', 'AddV6', 'StartTC', 'StopTC', 'ClearRules', 'EditRules', 'Statistic', 'Help']

sqlComman = insertRootRuleSQL() #Here we reserve ID 1 for the root rule

if isinstance(sqlComman, list): #if the return is list there is an error
 for item in sqlComman:
   event.log(item, level='debug')
else:
   event.log(sqlComman, level='debug')

intfList = getInfaces()
tcStatus = False

@app.route('/')
def index():
    event.log("Index", level='info')
    global tcStatus
    return template('index', tcCheck = tcStatus, title='Home')

@app.route('/action')
def actionHandlerError():
       redirect("/")

@app.route('/action', method='POST')
def actionHandler():
    action = request.forms.get('exsecutionAction')
    #check if action and if not check for button pressed
    if(action in existingLinks): #if there is not configured a action we return to index
       event.log("Redirect " + action, level='debug')
       redirect("/" + action)
    event.log("Error in action", level='error')
    event.log("In put arguments: "+action, level='error')
    redirect("/")

@app.route('/AddV4')
def addRuleIPV4():
    if tcStatus:
       return template('iprules', errors = "", filter=getDefaultArguments("ipV4"), interfaces = intfList, title='Add a rule set (ipV4)')
    else:
      redirect('/')

@app.route('/AddV6')
def addRuleIPV6():
    if tcStatus:
       return template('iprules', errors = "", filter=getDefaultArguments("ipV6"), interfaces = intfList, title='Add a rule set (ipV6)')
    else:
      redirect('/')

@app.route('/AddV4', method='POST')
@app.route('/AddV6', method='POST')
def addRuleIPPost():
    event.log("Parsing Arguments", level='debug')
    TCfilter = getArguments(request)
    event.log(TCfilter, level='debug')
    ipver = request.forms.get('ipVer')
    if isinstance(TCfilter, dict): #if the ouput is dictionary we are ok because we can proces it further
        if not bool(TCfilter): #check if the filter for tc is empty if yes we have to ask the user for new input.
                               #We consider the filter for emty if the values of the request is the same as the default ones
            event.log("The filter is empty", level='debug')
            return template('iprules', errors = "", filter = getDefaultArguments(ipver), emptyRule = True,\
                             interfaces = intfList, title='Add a rule set ('+ipver+')')

        else:
           event.log("Adding rule with the given filter", level='debug')
           id = insertRuleSQL(TCfilter)
           if isinstance(id, list): #if the return is list there is an error
             for item in id:
               event.log(item, level='debug')
               return str("Error")
           elif int(id) < 499:
               activateRule(TCfilter, id)
               return template('ruleadd', title='Rule added successfully')
           else:
               return "DB over fill please clean unused rules and compact the DB!"
    elif isinstance(TCfilter, list): #if the output is list error we return the values to the user
                                     #to fixed. The values contain illegal characters as letters.
       return template('iprules', errors = TCfilter[0], filter = TCfilter[1], showErrors = True, interfaces = intfList,\
                       title='Add a rule set ('+ipver+')')
    else:#if there is any other case
       event.log("Some went wrong", level='warning')
       for i in request.forms:
        event.log(i+" "+request.forms.get(i), level='warning')
       return "Other error"


@app.route('/StartTC')
def enableTC():
    global tcStatus
    tcStatus = startTC()
    filter = getAllEnabledRules()
    for TCfilter in filter:
        activateRule(TCfilter, TCfilter['ruleID'])
    redirect("/")

@app.route('/StopTC')
def disableTC():
    global tcStatus
    tcStatus = stopTC()
    redirect("/")

@app.route('/ClearRules')
def clearRules():
    exportDB()
    deleteDB()
    return template('clearrules', title='Rules deleted')

@app.route('/EditRules')
def showRules():
    return template('rulestemplate', title='Edit Rules', filter = getAllrules())

@app.route('/Statistic')
def statisticsTC():
    if tcStatus:
      return template('tcstatistic', title='Statistic', tcstatistic = getStatistic())
    else:
      return template('tcstatistic', title='Statistic', tcnotrun=True)

@app.route('/editHandler', method='POST')
def actionHandler():
    action = request.forms.get('editFormAction')
    ruleID = request.forms.get('ruleID')
    #check if action and if not check for button pressed
    if(action in ['delete', 'edit', 'disable', 'copy', 'changeIp']):
       if action == 'delete':
         ids=ruleID.split(';')
         ids.pop()
         for currentID in ids:
            deleteRules(currentID)
            deleteRule(id= currentID, intface = getIntByRuleID(currentID))
         return template('clearrules', title='Rules deleted')

       elif action == 'disable':
         ids=ruleID.split(';')
         ids.pop()
         for currentID in ids:

            disableRules(currentID)
            deleteRule(id= currentID, intface = getIntByRuleID(currentID))

         return template('clearrules', title='Rules disabled')

       elif action == 'edit':
         redirect("/EditRule?ruleID="+ruleID)

       elif action == 'copy':
         redirect("/EditRule?ruleID="+ruleID+"&copy=Yes")

       else:
         redirect("/EditRule?ruleID="+ruleID+"&changeIP=Yes")

    else:
      return("Error")

@app.route('/EditRule', method='GET')
def ruleEdit():
    ruleID = request.query.ruleID or -1
    copyRule = request.query.copy or 'no'
    changeIP = request.query.changeIP or 'no'

    if ruleID is -1:
      redirect("/EditRules")

    ipver=getIPversionByID(ruleID)
    editFilter=getRuleByID(ruleID)
    pageName = 'Update rule ('+ipver+')'

    if changeIP == 'Yes':
       if ipver == 'ipV4':
         arguments = getDefaultArguments('ipV6')
         pageName = 'Change IP to ver 4'
       else:
         arguments = getDefaultArguments('ipV4')
         pageName = 'Change IP to ver 4'
    else:
       arguments = getDefaultArguments(ipver)


    if 'selIntface' in editFilter:
     arguments['selIntface'] = editFilter['selIntface']
    if 'txtBufferLimit' in editFilter:
     arguments['txtBufferLimit'] = editFilter['txtBufferLimit']
    if 'txtBandwidth' in editFilter:
     arguments['txtBandwidth'] = editFilter['txtBandwidth']
    if 'selDelayDistribution' in editFilter:
     arguments['selDelayDistribution'] = editFilter['selDelayDistribution']
    if 'txtDelay' in editFilter:
     arguments['txtDelay'] = editFilter['txtDelay']
    if 'txtDelayJitter' in editFilter:
     arguments['txtDelayJitter'] = editFilter['txtDelayJitter']
    if 'txtDelayCorrelation' in editFilter:
     arguments['txtDelayCorrelation'] = editFilter['txtDelayCorrelation']
    if 'txtReorder' in editFilter:
     arguments['txtReorder'] = editFilter['txtReorder']
    if 'txtReorderCorrelation' in editFilter:
     arguments['txtReorderCorrelation'] = editFilter['txtReorderCorrelation']
    if 'txtGap' in editFilter:
     arguments['txtGap'] = editFilter['txtGap']
    if 'txtLoss' in editFilter:
     arguments['txtLoss'] = editFilter['txtLoss']
    if 'txtLossCorrelation' in editFilter:
     arguments['txtLossCorrelation'] = editFilter['txtLossCorrelation']
    if 'txtDup' in editFilter:
     arguments['txtDup'] = editFilter['txtDup']
    if 'txtDupCorrelation' in editFilter:
     arguments['txtDupCorrelation'] = editFilter['txtDupCorrelation']
    if 'txtCurp' in editFilter:
     arguments['txtCurp'] = editFilter['txtCurp']
    if 'txtCurptionCorrelation' in editFilter:
     arguments['txtCurptionCorrelation'] = editFilter['txtCurptionCorrelation']
    if 'portSrc' in editFilter:
     arguments['portSrc'] = editFilter['portSrc']
    if 'portDst' in editFilter:
     arguments['portDst'] = editFilter['portDst']
    if 'macSrc' in editFilter:
     arguments['macSrc'] = editFilter['macSrc']
    if 'macDest' in editFilter:
     arguments['macDest'] = editFilter['macDest']
    if 'flowlabelTOS' in editFilter:
     arguments['flowlabelTOS'] = editFilter['flowlabelTOS']
    if 'transport' in editFilter:
     arguments['transport'] = editFilter['transport']
    if 'transportPrtc' in editFilter:
     arguments['transportPrtc'] = editFilter['transportPrtc']
    if changeIP == 'no':
        if 'ipSrc' in editFilter:
         arguments['ipSrc'] = editFilter['ipSrc']
        if 'ipSrcSub' in editFilter:
         arguments['ipSrcSub'] = editFilter['ipSrcSub']
        if 'ipDest' in editFilter:
         arguments['ipDest'] = editFilter['ipDest']
        if 'ipDestSub' in editFilter:
         arguments['ipDestSub'] = editFilter['ipDestSub']
        if 'ipVer' in editFilter:
         arguments['ipVer'] = editFilter['ipVer']


    if copyRule == 'Yes' and changeIP == 'no':
       arguments['ruleID']=ruleID
       pageName = 'Copy rule'


    return template('iprules', errors = "", filter = arguments,\
                          interfaces = intfList, title=pageName, ruleID=ruleID)


@app.route('/UpdateRule', method='POST')
def updateRuleID():
    event.log("Parsing Arguments", level='debug')
    TCfilter = getArguments(request)
    event.log(TCfilter, level='debug')
    ipver = request.forms.get('ipVer')
    ruleID = request.forms.get('ruleID')

    if isinstance(TCfilter, dict): #if the ouput is dictionary we are ok because we can proces it further
        if not bool(TCfilter): #check if the filter for tc is empty if yes we have to ask the user for new input.
                               #We consider the filter for emty if the values of the request is the same as the default ones
            event.log("The filter is empty", level='debug')
            return template('iprules', errors = "", filter = getDefaultArguments(ipver), emptyRule = True, interfaces = intfList,\
                             title='Update rule ('+ipver+')', ruleID=id)
        else:
           event.log("Adding rule with the given filter", level='debug')
           #update the rule

           # We read the inteface name from the db because the interface can be changed after the edit.
           deleteRule(id = ruleID, intface = getIntByRuleID(ruleID))
           updateRuleSQL(TCfilter, ruleID)
           activateRule(TCfilter, ruleID)
           return template('ruleadd', title='Rule updated successfully')
    elif isinstance(TCfilter, list): #if the output is list error we return the values to the user to fixed. The values
                                     # contain illegal characters as letters.
       return template('iprules', errors = TCfilter[0], filter = TCfilter[1], showErrors = True, interfaces = intfList, title='Add a rule set ('+ipver+')')
    else:#if there is any other case
       event.log("Some went wrong", level='warning')
       for i in request.forms:
        event.log(i+" "+request.forms.get(i), level='warning')
       return "Other error"


@app.route('/Help')
@app.route('/help')
def help():
    return template('help', title='Help')
    return "help"

@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=static_files)

# def configureServer():
    # global serverConfig
    # serverConfig= getConfiguration('myapp.ini')

    # if serverConfig['accesslog']:
       # app.install(log_to_access) # this log only in access.log

    # global event
    # if serverConfig['loginglevel'] is not 'notset':#Set the log level
       # event=LoggingPlugin()
       # event.setup(app=app, logLevel = serverConfig['loginglevel']) #This logs to all other errors
    # else:
       # event=EmptyLoggingPlugin()
       # event.setup(app=app) #Empty loger just to save code refactoring if there is no log level

    # global static_files
    # static_files = './static/'

    # global existingLinks
    # existingLinks = ['AddV4', 'AddV6', 'StartTC', 'StopTC', 'ClearRules', 'ShowRules', 'Status', 'Help']

run(app, host=serverConfig['address'], port=serverConfig['port'])

#run(app, host='localhost', port=8080, reloader=True)
