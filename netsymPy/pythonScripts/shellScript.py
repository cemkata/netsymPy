from subprocess import Popen, PIPE
def getInfaces():
    #4 difret ways to get the interfaces
    # if some is not working there are alternatives
    #comand="./shellScripts/printif1.sh" #"ifconfig -a | sed 's/[ \t].*//;/^\(lo\|\)$/d'"
                      #the output will generated with ":" a$
    #comand="./shellScripts/printif2.sh" #"ip -o link show | awk -F': ' '{print $2}'"
    #comand="./shellScripts/printif3.sh" #"ls /sys/class/net"
    #comand="./shellScripts/printif4.sh" #"ifconfig | expand | cut -c1-8 | sort | uniq -u | awk -F: '{print $1;}'"
    comand="./shellScripts/printif.sh" #to change this go to folder shellScripts and copy the script that works best to file printif.sh

    comandBash=["bash", comand]
    with Popen(comandBash, stdout=PIPE) as proc:
       outPutIntf=proc.stdout.read()
    outPutIntf = outPutIntf.split(b'\n')
    intf=[]
    for i in outPutIntf:
       if not i == b'':
          intf.append(i.decode("utf-8"))
    return intf

def checkROOT():
    comand="./shellScripts/checkroot.sh"
    comandBash=["bash", comand]
    with Popen(comandBash, stdout=PIPE) as proc:
       outPutIntf=proc.stdout.read()
    if outPutIntf == b'notroot\n':
       raise NameError('notROOT')
    else:
        pass


def startTC():
    stopTC()
    intf = getInfaces()
    for i in intf:
      comandBash=["bash", "./shellScripts/addrootrule.sh", i]
      with Popen(comandBash, stdout=PIPE) as proc:
           pass
    return True

def stopTC():
    intf = getInfaces()
    for i in intf:
      comandBash=["bash", "./shellScripts/delinftc.sh", i]
      with Popen(comandBash, stdout=PIPE) as proc:
           pass
    return False

def activateRule(inputFilter, id):

    # TODO :
    # to check if this is needed
    comand="./shellScripts/gettcpath.sh"
    comandBash=["bash", comand]
    with Popen(comandBash, stdout=PIPE) as proc:
       tcPath=proc.stdout.read()
    tcPath = tcPath.decode("utf-8")[:-1] #to get the path as a string and without the ending new line charecter

    tcPath = "tc"
    id = int(id)
    qid=400 + id #Generate the id for qdisc
    fid=100 + qid #generate the id for filter

    #convert all ids to string for easyer work further
    id=str(id)
    qid=str(qid)
    fid=str(fid)

    comandClass = tcPath + " class add dev "+ inputFilter['selIntface'] +" parent 1:1 classid 1:"+id+" htb rate 1000Mbps"
    comandQdisc = tcPath + " qdisc add dev "+ inputFilter['selIntface'] +" parent 1:"+id+" handle "+qid+": netem"
    comandFilter = tcPath + " filter add dev "+ inputFilter['selIntface'] +" protocol ip parent 1: handle ::"+fid+" prio 1 u32"


    #OPTIONS := [ LIMIT ] [ DELAY ] [ LOSS ] [ CORRUPT ] [ DUPLICATION ] [ REORDERING ][ RATE ]


    if 'txtBufferLimit' in inputFilter:
       comandQdisc = comandQdisc + " limit " + inputFilter['txtBufferLimit']

    if 'txtDelay' in inputFilter:
        comandQdisc = comandQdisc + " delay "+inputFilter['txtDelay']+"ms"
        if 'txtDelayJitter' in inputFilter:
            comandQdisc = comandQdisc + " " + inputFilter['txtDelayJitter']
            if 'txtDelayCorrelation' in inputFilter:
               comandQdisc = comandQdisc + " " + inputFilter['txtDelayCorrelation'].lower()
        if inputFilter['selDelayDistribution'] in ['Normal', 'Pareto', 'Paretonormal']:
            comandQdisc = comandQdisc + " distribution " + inputFilter['selDelayDistribution'].lower()
        else:
             pass
             #comandQdisc = comandQdisc + " distribution uniform"

    if 'txtLoss' in inputFilter:
        comandQdisc = comandQdisc + " loss " + inputFilter['txtLoss'] +"%"
        if 'txtLossCorrelation' in inputFilter:
            comandQdisc = comandQdisc + " " +  inputFilter['txtLossCorrelation'] +"%"

    if 'txtCurp' in inputFilter:
        comandQdisc = comandQdisc +' corrupt ' + inputFilter['txtCurp'] +"%"
        if 'txtCurptionCorrelation' in inputFilter:
            comandQdisc = comandQdisc + " " + inputFilter['txtCurptionCorrelation'] +"%"

    if 'txtDup' in inputFilter:
        comandQdisc = comandQdisc + ' duplicate ' + inputFilter['txtDup'] +"%"
        if 'txtDupCorrelation' in inputFilter:
            comandQdisc = comandQdisc + " " +  inputFilter['txtDupCorrelation'] +"%"

    if 'txtReorder' in inputFilter:
        comandQdisc = comandQdisc + " reorder " + inputFilter['txtReorder'] +"%"
        if 'txtReorderCorrelation' in inputFilter:
            comandQdisc = comandQdisc + " " +  inputFilter['txtReorderCorrelation'] +"%"
        if 'txtGap' in inputFilter:
            comandQdisc = comandQdisc + " gap " + inputFilter['txtGap']

    if 'txtBandwidth' in inputFilter:
      comandQdisc = comandQdisc +" rate "+inputFilter['txtBandwidth']+"kbit"

    #OPTIONS := [ PORT ] [ MAC ] [ TRANSPORT ] [ IP ]


    if 'portSrc' in inputFilter:
        comandFilter = comandFilter + " match ip sport " + inputFilter['portSrc'] + " 0xffff"
    if 'portDst' in inputFilter:
        comandFilter = comandFilter + " match ip dport " + inputFilter['portDst'] + " 0xffff"
    if 'macSrc' in inputFilter:
        comandFilter = comandFilter + " match u16 0x0800 0xFFFF at -2 match u32 0x"+inputFilter['macSrc'].replace(':','')+" 0xFFFFFFFF at -8"

    if 'macDest' in inputFilter:
        comandFilter = comandFilter + " match u16 0x0800 0xFFFF at -2 match u32 0x"+inputFilter['macDest'].replace(':','')+" 0xFFFFFFFF at -12"


    if inputFilter['transport'] == "UDP":
        comandFilter = comandFilter + " match ip protocol 17 0xffff"
    elif inputFilter['transport'] == "TCP":
        comandFilter = comandFilter + " match ip protocol 6 0xffff"
    elif inputFilter['transport'] == "ALL":
        pass
    else:
        comandFilter = comandFilter + " match ip protocol " + inputFilter['transport'] +" 0xffff"

    if inputFilter['ipVer'] == "ipV4":

        if 'ipSrc' in inputFilter:
            if 'ipSrcSub' in inputFilter:
                comandFilter = comandFilter + " match ip src " + inputFilter['ipSrc'] + "/" + inputFilter['ipSrcSub']
            else:
                comandFilter = comandFilter + " match ip src " + inputFilter['ipSrc'] + "/255.255.255.255"
        if 'ipDest' in inputFilter:
            if 'ipDestSub' in inputFilter:
                comandFilter = comandFilter + " match ip dst " + inputFilter['ipDest'] + "/" + inputFilter['ipDestSub']
            else:
                comandFilter = comandFilter + " match ip dst " + inputFilter['ipDest'] + "/255.255.255.255"

        if 'flowlabelTOS' in inputFilter:
                comandFilter = comandFilter + " match ip tos "+inputFilter['flowlabelTOS']+" 0xff"

    else:
        comandFilter.replace("ip", "ip6")
        comandFilter.replace("protocol ip6", "protocol ipv6")
        if 'ipSrc' in inputFilter:
            if 'ipSrcSub' in inputFilter:
                comandFilter = comandFilter + " match ip6 src " + inputFilter['ipSrc'] + "/" + inputFilter['ipSrcSub']
            else:
                comandFilter = comandFilter + " match ip6 src " + inputFilter['ipSrc'] + "/255.255.255.255"
        if 'ipDest' in inputFilter:
            if 'ipDestSub' in inputFilter:
                comandFilter = comandFilter + " match ip6 dst " + inputFilter['ipDest'] + "/" + inputFilter['ipDestSub']
            else:
                comandFilter = comandFilter + " match ip6 dst " + inputFilter['ipDest'] + "/255.255.255.255"

        if 'flowlabelTOS' in inputFilter:
                comandFilter = comandFilter + " match ip6 flowlabel "+inputFilter['flowlabelTOS']+" 0xff"

    returnDebug = []

    with Popen(comandClass.split(' '), stdout=PIPE) as proc:
        outPutClass=proc.stdout.read()
    returnDebug.append(comandClass)
    returnDebug.append(outPutClass.decode("utf-8"))

    with Popen(comandQdisc.split(' '), stdout=PIPE) as proc:
        outPutQdisc=proc.stdout.read()
    returnDebug.append(comandQdisc)
    returnDebug.append(outPutQdisc.decode("utf-8"))

    comandFilter = comandFilter + " flowid 1:" + qid
    with Popen(comandFilter.split(' '), stdout=PIPE) as proc:
        outPutFilter=proc.stdout.read()
    returnDebug.append(comandFilter)
    returnDebug.append(outPutFilter.decode("utf-8"))

    return returnDebug

def deleteRule(id, intface):
    id = int(id)
    qid=400 + id #Generate the id for qdisc
    fid=100 + qid #generate the id for filter

    #convert all ids to string for easyer work further
    id=str(id)
    qid=str(qid)
    fid=str(fid)

    tcPath = "tc"

    comandClass = tcPath + " class del dev "+ intface +" parent 1:1 classid 1:"+id
    comandQdisc = tcPath + " qdisc del dev "+ intface +" parent 1:"+id
    comandFilter = tcPath + " filter del dev "+ intface +" parent 1: handle 800::"+ fid +" prio 1 protocol ip u32"

    returnDebug = []

    comandFilter = comandFilter + " flowid 1:" + qid
    with Popen(comandFilter.split(' '), stdout=PIPE) as proc:
        outPutFilter=proc.stdout.read()
    returnDebug.append(comandFilter)
    returnDebug.append(outPutFilter.decode("utf-8"))

    with Popen(comandQdisc.split(' '), stdout=PIPE) as proc:
        outPutQdisc=proc.stdout.read()
    returnDebug.append(comandQdisc)
    returnDebug.append(outPutQdisc.decode("utf-8"))

    with Popen(comandClass.split(' '), stdout=PIPE) as proc:
        outPutClass=proc.stdout.read()
    returnDebug.append(comandClass)
    returnDebug.append(outPutClass.decode("utf-8"))

    return returnDebug

def getStatistic():
    statOutput=[]
    intf = getInfaces()
    for i in intf:
       statistic = {}
       statistic['interface']=i

       #Filter statistic
       comand="./shellScripts/getfilterstats.sh"
       comandBash=["bash", comand, i]
       with Popen(comandBash, stdout=PIPE) as proc:
            outPutFilter=proc.stdout.read()
       if outPutFilter == b'':
          statistic['filterstatistic']='Empty'
       else:
          statistic['filterstatistic']=outPutFilter.decode("utf-8")

       #Qdisc statistic
       comand="./shellScripts/getqdiscstats.sh"
       comandBash=["bash", comand, i]
       with Popen(comandBash, stdout=PIPE) as proc:
            outPutQdisc=proc.stdout.read()
       if outPutQdisc == b'':
          statistic['qdiscstatistic']='Empty'
       else:
          statistic['qdiscstatistic']=outPutQdisc.decode("utf-8")


       statOutput.append(statistic.copy())

    return statOutput
