#!/bin/bash

arch=`uname -m`

###################################################################################
# Usage
###################################################################################
Usage()
{
cat << EOF
Usage: unixbench [ -q | -v ] [-i <n> ] [-c <n> [-c <n> ...]] [test ...]

The option flags are:

  -q            Run in quiet mode.
  -v            Run in verbose mode.
  -i <count>    Run <count> iterations for each test -- slower tests
                use <count> / 3, but at least 1.  Defaults to 10 (3 for
                slow tests).
  -c <n>        Run <n> copies of each test in parallel.
    
Example:
    unixbench -c 1
    unixbench -c 64
    unixbench -c 1 -c 64

EOF
}

###################################################################################
# Get all args
###################################################################################

#echo -$me-$filename

if [ x"$1" == x"-h" ];then
   Usage ; exit 0
fi

cd ./unixbench.${arch}
./Run $*
