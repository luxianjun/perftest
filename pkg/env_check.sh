#!/bin/sh
###################################################################################
# TEST ENVIRONMENT CHECK
###################################################################################
#envirocheck()
#{
if which numactl ; then
    echo -e "\n   numactl has install    \n"
    exit 1
else
   rpm -ivh numactl-2.0.9-7.el7.aarch64.rpm  
fi
exit 0
#}





