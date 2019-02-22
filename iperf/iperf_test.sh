#!/bin/bash
arch=`uname -m`

###################################################################################
# Usage
###################################################################################
Usage()
{
cat << EOF
Example:
      Server:
        iperf -s -w 256k

      Client:
        iperf -c ip_addr -P 1 -t 100 -i 1 -w 256k
        iperf -c ip_addr -P 4 -t 100 -i 1 -w 256k

EOF
}

./iperf.${arch} $*

if [ x$1 == x"-h" ];then
    Usage
fi



