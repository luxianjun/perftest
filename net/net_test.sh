#!/bin/bash
###################################################################################
# Default Variables
###################################################################################
version=1
core_num=1
test_num=5
###################################################################################
# Usage
###################################################################################
Usage()
{
cat << EOF
Sorry to say that Network test is manual, need to execute the following commands on the Server and  Client side(shown in example).

Usage: network [Options]

Options:
    server    : run in server mode
    client    : run in client mode, connecting to <host>, default host equal to server ipaddr
    parallel  : number of parallel client threads to run
    interval  : seconds between periodic bandwidth reports
    time      : time in seconds to transmit for (default 10 secs)
Example: 

    Server
     network server=1
    Client
     network client=1 host=ipaddr parallel=5 time=10 interval=1

EOF
}
###################################################################################
# Get all args
###################################################################################
while test $# != 0
do
    case $1 in
        --*=*) ac_option=`expr "X$1" : 'X\([^=]*\)='` ; ac_optarg=`expr "X$1" : 'X[^=]*=\(.*\)'` ; ac_shift=: ;;
        -*) ac_option=$1 ; ac_optarg=$2; ac_shift=shift ;;
        *) ac_option=$1 ; ac_shift=: ;;
    esac

    case ${ac_option} in
        --host) host=$ac_optarg ;;
        --time) time=$ac_optarg ;;
        --server) server=$ac_optarg ;;
        --client) client=$ac_optarg ;;
        --parallel) parallel=$ac_optarg ;;
        --interval) interval=$ac_optarg ;;
        -h | --help) Usage ; exit 0 ;;
        *) Usage ; echo "Unknown option $1" ; exit 1 ;;
    esac

    ${ac_shift}
    shift
done

###################################################################################
# Exectue network test
###################################################################################

if [ x"$server" == x"1" ];then
        echo "iperf run in server mode"
        numactl -C 0 --localalloc ./iperf -s & 
fi


if [ x"$client" == x"1" ];then
        echo "iperf run in client mode"
        numactl -C 0-4 --localalloc ./iperf -c $host -P 5 -i 1 -t $time
fi





