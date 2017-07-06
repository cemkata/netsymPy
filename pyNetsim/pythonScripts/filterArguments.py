from networkAddresses import is_valid_ipv4, is_valid_ipv6, is_valid_macaddr802
from numericChecks import is_valid_procent, is_port, is_int

def getArguments(request):
   filter = {
      'selIntface': request.forms.get('selIntface'),
      'txtBufferLimit': request.forms.get('txtBufferLimit'),
      'txtBandwidth': request.forms.get('txtBandwidth'),
      'selDelayDistribution': request.forms.get('selDelayDistribution'),

      'txtDelay': request.forms.get('txtDelay'),
      'txtDelayJitter': request.forms.get('txtDelayJitter'),
      'txtDelayCorrelation': request.forms.get('txtDelayCorrelation'),

      'txtReorder': request.forms.get('txtReorder'),
      'txtReorderCorrelation': request.forms.get('txtReorderCorrelation'),
      'txtGap': request.forms.get('txtGap'),

      'txtLoss': request.forms.get('txtLoss'),
      'txtLossCorrelation': request.forms.get('txtLossCorrelation'),

      'txtDup': request.forms.get('txtDup'),
      'txtDupCorrelation': request.forms.get('txtDupCorrelation'),

      'txtCurp': request.forms.get('txtCurp'),
      'txtCurptionCorrelation': request.forms.get('txtCurptionCorrelation'),

      'portSrc':request.forms.get('portSrc'),
      'portDst':request.forms.get('portDst'),
      'macSrc':request.forms.get('macSrc'),
      'macDest':request.forms.get('macDest'),
   }


   if request.forms.get('ipVer') == 'ipV6':
      filter['ipSrc'] = request.forms.get('ipSrcV6')
      filter['ipSrcSub'] = request.forms.get('ipSrcSubV6')
      filter['ipDest'] = request.forms.get('ipDestV6')
      filter['ipDestSub'] = request.forms.get('ipDestSubV6')
      filter['flowlabelTOS'] = request.forms.get('flowlabel')
      filter['ipVer'] = 'ipV6'
   else:
      filter['ipSrc'] = request.forms.get('ipSrc')
      filter['ipSrcSub'] = request.forms.get('ipSrcSub')
      filter['ipDest'] = request.forms.get('ipDest')
      filter['ipDestSub'] = request.forms.get('ipDestSub')
      filter['flowlabelTOS'] = request.forms.get('tos')
      filter['ipVer'] = 'ipV4'

   if request.forms.get('transport') == 'ALL':
      filter['transport'] = 'ALL'
      filter['transportPrtc'] = "0"
   elif request.forms.get('transport') == 'UDP':
      filter['transport'] = 'UDP'
      filter['transportPrtc'] = "17"
   elif request.forms.get('transport') == 'TCP':
      filter['transport'] = 'TCP'
      filter['transportPrtc'] = "6"
   else:
      filter['transport'] = request.forms.get('transport')
      filter['transportPrtc'] = request.forms.get('transportPrtc')

   errors = checkArguments(filter)
   if not errors:
      return prepereTCFilter(filter)
   else:#if there are errors
      #print("Error")
      return [errors, filter]

def checkArguments(filterArguments):

   errors_list = []
   #Ip check
   if filterArguments['ipVer'] == 'ipV4':#IPV4
      #Src IP
      if not is_valid_ipv4(filterArguments['ipSrc']):errors_list.append('ipV4SrcErr')
      if not is_valid_ipv4(filterArguments['ipSrcSub']):errors_list.append('ipV4SrcSubErr')
      #Dst IP
      if not is_valid_ipv4(filterArguments['ipDest']):errors_list.append('ipV4DestErr')
      if not is_valid_ipv4(filterArguments['ipDestSub']):errors_list.append('ipV4DestSubErr')
   else:#IPV6
      #Src IP
      if not is_valid_ipv6(filterArguments['ipSrc']):errors_list.append('ipV6SrcErr')
      if not is_int(filterArguments['ipSrcSub']):errors_list.append('ipV6SrcSubErr')
      #Dst IP
      if not is_valid_ipv6(filterArguments['ipDest']):errors_list.append('ipV6DestErr')
      if not is_int(filterArguments['ipDestSub']):errors_list.append('ipV6DestSubErr')

   #MAC check
   if not is_valid_macaddr802(filterArguments["macSrc"]):errors_list.append('macSrcErr')
   if not is_valid_macaddr802(filterArguments["macDest"]):errors_list.append('macDestErr')

   #Flowlabel/TOS check
   if not is_int(filterArguments["flowlabelTOS"]):errors_list.append('flowlabelTOSErr')

   #Port check
   if not is_port(filterArguments["portSrc"]):errors_list.append('portSrcErr')
   if not is_port(filterArguments["portDst"]):errors_list.append('portDstErr')

   if not is_int(filterArguments["txtDelay"]):errors_list.append('delayErr')
   if not is_int(filterArguments["txtDelayJitter"]):errors_list.append('delayJitterErr')
   if not is_valid_procent(filterArguments["txtDelayCorrelation"]):errors_list.append('delayCorrelationErr')

   #Reorder check
   if not is_valid_procent(filterArguments["txtReorder"]):errors_list.append('reorderErr')
   if not is_valid_procent(filterArguments["txtReorderCorrelation"]):errors_list.append('reorderCorrelationErr')
   if not is_int(filterArguments["txtGap"]):errors_list.append('gapErr')

   #Loss check
   if not is_valid_procent(filterArguments["txtLoss"]):errors_list.append('lossErr')
   if not is_valid_procent(filterArguments["txtLossCorrelation"]):errors_list.append('lossCorreErr')

   #Duplication check
   if not is_valid_procent(filterArguments["txtDup"]):errors_list.append('dupErr')
   if not is_valid_procent(filterArguments["txtDupCorrelation"]):errors_list.append('dupCorrelationErr')

   #Corruption Correlation check
   if not is_valid_procent(filterArguments["txtCurp"]):errors_list.append('curpErr')
   if not is_valid_procent(filterArguments["txtCurptionCorrelation"]):errors_list.append('curptionCorrelationErr')

   #Buffer Limit check
   if not is_int(filterArguments["txtBufferLimit"]):errors_list.append('bufferLimitErr')

   #Transport check
   transportPrtocol = ["UDP, TCP", "ALL"]
   if not filterArguments["transport"] is transportPrtocol:
      if not is_int(filterArguments["transportPrtc"]):errors_list.append('transportPrtcErr')

   #Bandwidth check
   if not is_int(filterArguments["txtBandwidth"]):errors_list.append('bandwidthErr')

   return errors_list

def prepereTCFilter(tcArguments):
   tcFilter={}
   if tcArguments['ipVer'] == 'ipV4':#IPV4
      #Src IP
      if tcArguments['ipSrc'] == "0.0.0.0":
            pass
      elif tcArguments['ipSrc'].lower() == "any":
            pass
      else:
            tcFilter['ipSrc']=tcArguments['ipSrc']

      if tcArguments['ipSrcSub'] == "0.0.0.0":
            pass
      elif tcArguments['ipSrcSub'].lower() == "any":
            pass
      else:
            tcFilter['ipSrcSub']=tcArguments['ipSrcSub']
      #Dst IP
      if tcArguments['ipDest'] == "0.0.0.0":
            pass
      elif tcArguments['ipDest'].lower() == "any":
            pass
      else:
            tcFilter['ipDest']=tcArguments['ipDest']

      if tcArguments['ipDestSub'] == "0.0.0.0":
            pass
      elif tcArguments['ipDestSub'].lower() == "any":
            pass
      else:
            tcFilter['ipDestSub']=tcArguments['ipDestSub']
   else:#IPV6
      tcFilter['ipVer']='ipV6'
      #Src IP
      if tcArguments['ipSrc'] == "0000:0000:0000:0000:0000:0000:0000:0000":
           pass
      elif tcArguments['ipSrc'].lower() == "any":
           pass
      else:
           tcFilter['ipSrc']=tcArguments['ipSrc']
      if not tcArguments['ipSrcSub'] == "0":
            tcFilter['ipSrcSub']=tcArguments['ipSrcSub']
      #Dst IP
      if tcArguments['ipDest'] == "0000:0000:0000:0000:0000:0000:0000:0000":
           pass
      elif tcArguments['ipDest'].lower() == "any":
           pass

      else:
          tcFilter['ipDest']=tcArguments['ipDest']

      if not tcArguments['ipDestSub'] == "0":
            tcFilter['ipDestSub']=tcArguments['ipDestSub']

   #MAC check
   if tcArguments['macSrc'] == "00:00:00:00:00:00":
           pass
   elif tcArguments['macSrc'].lower() == "any":
           pass
   else:
            tcFilter['macSrc']=tcArguments['macSrc']
   if tcArguments['macDest'] == "00:00:00:00:00:00":
           pass
   elif tcArguments['macDest'].lower() == "any":
           pass
   else:
            tcFilter['macDest']=tcArguments['macDest']


   toCheck=['portSrc', 'portDst', 'txtDelay', 'txtDelayJitter', 'txtDelayCorrelation', 'txtReorder', 'txtReorderCorrelation', 'txtGap', 'txtLoss', 'txtLossCorrelation', 'txtDup', 'txtDupCorrelation', 'txtCurp', 'txtCurptionCorrelation', 'txtBandwidth']

   if not tcArguments['txtBufferLimit'] == "1000":
      tcFilter['txtBufferLimit']=tcArguments['txtBufferLimit']

   for item in toCheck:
      if not tcArguments[item] == "0":
            tcFilter[item]=tcArguments[item]
   if bool(tcFilter):
      tcFilter['selIntface']=tcArguments['selIntface']
      tcFilter['selDelayDistribution']=tcArguments['selDelayDistribution']
      tcFilter['transport']=tcArguments['transport']
      tcFilter['ipVer']=tcArguments['ipVer']
      tcFilter['transportPrtc']=tcArguments['transportPrtc']

   return tcFilter

def getDefaultArguments(ipVer):
    filter = {
      'selIntface':"",
      'txtBufferLimit': "1000",
      'txtBandwidth': "0",
      'selDelayDistribution': "",
      'txtDelay': "0",
      'txtDelayJitter': "0",
      'txtDelayCorrelation': "0",
      'txtReorder': "0",
      'txtReorderCorrelation': "0",
      'txtGap': "0",
      'txtLoss': "0",
      'txtLossCorrelation': "0",
      'txtDup': "0",
      'txtDupCorrelation': "0",
      'txtCurp': "0",
      'txtCurptionCorrelation': "0",
      'portSrc':"0",
      'portDst':"0",
      'macSrc':"00:00:00:00:00:00",
      'macDest':"00:00:00:00:00:00",
      'flowlabelTOS':"0",
      'transport': 'ALL',
      'transportPrtc': '0',
    }

    if ipVer == "ipV4":
          filter['ipSrc'] = "any"
          filter['ipSrcSub'] = "0.0.0.0"
          filter['ipDest'] = "any"
          filter['ipDestSub'] = "0.0.0.0"
          filter['ipVer'] = "ipV4"
    else:
          filter['ipSrc'] = "0000:0000:0000:0000:0000:0000:0000:0000"
          filter['ipSrcSub'] = "0"
          filter['ipDest'] = "0000:0000:0000:0000:0000:0000:0000:0000"
          filter['ipDestSub'] = "0"
          filter['ipVer'] = "ipV6"

    return filter
