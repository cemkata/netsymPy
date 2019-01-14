#!/bin/bash

instalService()
{
  tar -C /opt/ -zxvf netsymPy.tar.gz &> /dev/null
  rm  netsymPy.tar.gz
  #Logs folder
  mkdir /var/log/netsymPyLogs/
  # clear
  rm -r /opt/netsymPy/log
  ln -s /var/log/netsymPyLogs/ /opt/netsymPy/log
  #Configuration
  mkdir /etc/netsymPy
  cd /opt/netsymPy/pythonScripts/
  python3 configEditor.py
  cd - &> /dev/null
  mv /opt/netsymPy/networksym.ini /etc/netsymPy/networksym.ini
  ln -s /etc/netsymPy/networksym.ini /opt/netsymPy/networksym.ini
  mv /opt/netsymPy/uninstall.sh /etc/netsymPy/uninstall.sh
  #Start after reboot
  mv /opt/netsymPy/netsymPy.sh /etc/init.d/netsymPy
  ln -s /etc/init.d/netsymPy /etc/rc3.d/S99netsymPy
  cd /opt/netsymPy/
  ./createDB.sh
  cd - &> /dev/null
  rm /opt/netsymPy/createDB.sh
  #Finish the installation
  echo Done! | tee /etc/netsymPy/deployment
}

instalStandalone()
{
  tar -C ~/ -zxvf netsymPy.tar.gz &> /dev/null
  rm  netsymPy.tar.gz
  cd ~/netsymPy/pythonScripts/
  python3 configEditor.py
  cd ..
  ./createDB.sh
  rm createDB.sh
  rm netsymPy.sh
  rm uninstall.sh
  echo Done!
}

checkdep()
{
    PROG_TC=`which tc`
    PROG_PY=`which python3`

    if [ -z ${PROG_TC} ]; then
        read -d '' msg <<- EOM
Warning: tc is missing

Please install the iproute or iproute2 package

The instalation will stop

Press any key
EOM
        echo "$msg"
        read
        exit 3
    fi
    if [ -z ${PROG_PY} ]; then

        read -d '' msg <<- EOM
Warning: python3 is missing

Please install the python3

The instalation will stop

Press any key
EOM
        echo "$msg"
        read
        exit 3
    fi
}


if [ `id -u` = 0 ] ; then
   echo "Root check OK"
else
   echo "You are not root OK"
   exit 0
fi

base64 -d<<EOD >> netsymPy.tar.gz
BASE64FILE
EOD


while true; do
    read -p "Do you wish to install netsymPy as a service (deamon)? yes/no/cancel: " yn
    case $yn in
        [Yy]* ) instalService; break;;
        [Nn]* ) instalStandalone; exit;;
        [Cc]* ) exit;;
        * ) echo "Please answer yes, no or cancel.";;
    esac
done

while true; do
    read -p "Do you wish to start netsymPy? yes/no/cancel: " yn
    case $yn in
        [Yy]* ) /etc/init.d/netsymPy start; break;;
        [Nn]* ) break;;
        [Cc]* ) exit;;
        * ) echo "Please answer yes, no or cancel.";;
    esac
done
