#!/bin/sh
###################################################################################
arch=`uname -m`
###################################################################################
# Usage
###################################################################################
Usage()
{
cat << EOF
Instruction:

    1. Check firewalld stauts, and stop it for network testing;
    2. Install the dependency packages required for testing;
       .e.g. numactl
    3. Curently Only the following OS is suppoeted, CentOS NeoKylin and RedHat;
EOF
}

###################################################################################
# Get all args
###################################################################################

if [ x"$1" == x"-h" ];then
   Usage ; exit 0
fi


###################################################################################
# TEST ENVIRONMENT CHECK
###################################################################################
fire_stat=`systemctl status firewalld | grep Active | awk '{print $2}'`
if which numactl ; then
    echo -e "\n   numactl has install    \n"
else
   rpm -ivh numactl-2.0.9-7.el7.${arch}.rpm  
fi

if [ x"$fire_stat" = x"inactive" ] ; then
    echo -e "\n   firewalld inactive \n"
    exit 1
else                                         
    echo -e "\n   firewalld active , execute cmd to stop it  \n"
    systemctl stop firewalld
    sleep 3 
    fire_stat=`systemctl status firewalld | grep Active | awk '{print $2}'`
    if [ x"$fire_stat" = x"inactive" ] ; then
        echo -e "   firewalld has been inactive \n"
        exit 1
    else                                         
        echo -e " firewalld cannot stop , maybe execute cmd [systemctl stop firewalld] to stop it manully  \n"
        exit 2   
    fi 
fi


