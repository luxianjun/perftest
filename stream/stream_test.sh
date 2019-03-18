#!/bin/bash
###################################################################################
# Default Variables
###################################################################################
#v=1
#P=1
#M=200M
#W=0
#N=1
arch=`uname -m`
max_core_num=`lscpu | grep "CPU(s)" | awk '{print $2}' | head -1`
###################################################################################
# Usage
###################################################################################
Usage()
{
cat << EOF
Usage: mem [Options]
Options:

    -v, --version     : Stream Version, alternative v1 or v2,default v1 
    -P, --parallelism : Number of parallel threads to run, only support single or all core
    -M <len>[K|M]     : Test memory size
    -W <warmup>]      : Test warmup
    -N <repetitions>  : Test repetitions

Example:

    stream -v 1 -M 200M -P 1  
    stream -v 1 -M 200M -P ${max_core_num}
    stream -v 2 -M 200M -P 1  
    stream -v 2 -M 200M -P ${max_core_num}

EOF
}

###################################################################################
# Get all args
###################################################################################

#while test $# != 0
#do
#    case $1 in
#        --*=*) ac_option=`expr "X$1" : 'X\([^=]*\)='` ; ac_optarg=`expr "X$1" : 'X[^=]*=\(.*\)'` ; ac_shift=: ;;
#        -*) ac_option=$1 ; ac_optarg=$2; ac_shift=shift ;;
#        *) ac_option=$1 ; ac_shift=: ;;
#    esac
#
#    case ${ac_option} in
#        -v | --version) v=$ac_optarg ;;
#        -P | --parallelism) P=$ac_optarg ;;
#        -M ) M=$ac_optarg ;;
#        -W ) W=$ac_optarg ;;
#        -N ) N=$ac_optarg ;;
#        -h | --help) Usage ; exit 0 ;;
#        #*) Usage ; echo "Unknown option $1" ; exit 1 ;;
#        #*) Usage ; echo "Unknown option $1" ; exit 1 ;;
#    esac
#
#    ${ac_shift}
#    shift
#done

#echo "args $* version :$v P :$P M :$M N: $N W :$W" 
echo "args $* " 

if [ x"$1" == x"-h" ];then
   Usage ; exit 0
fi

###################################################################################
# Exectue stream mem test
###################################################################################
echo "Stream Version V$v Core$P Memory$M \n"
    ./stream.${arch} $*
    #numactl --cpunodebind=0,1,2,3 --localalloc ./stream $*
    sleep 10

