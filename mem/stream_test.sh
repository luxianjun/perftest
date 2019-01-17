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
Usage: mem [Options]
Options:
    version     : Stream Version, alternative v1 or v2,default v1 
    core_num    : Core number specified by Test Server, only support single core and all core,default 1core
    test_num    : Test number ,used to get acculate average,default 5
Example:

    mem version=1  core_num=1   test_num=5
    mem version=1  core_num=64   test_num=5 
    mem version=2  core_num=1  test_num=5
    mem version=2  core_num=64  test_num=5

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
        --version) version=$ac_optarg ;;
        --core_num) core_num=$ac_optarg ;;
        --test_num) test_num=$ac_optarg ;;
        -h | --help) Usage ; exit 0 ;;
        *) Usage ; echo "Unknown option $1" ; exit 1 ;;
    esac

    ${ac_shift}
    shift
done


###################################################################################
# Exectue stream mem test
###################################################################################


function stream_test() {
if [ $core_num -eq 1 ];then
   if [ $version -eq 1 ];then       
        echo ": streamv1core0"
        numactl -C 0 --localalloc ./stream -v 1 -M 200M -P 1 -W 5
        sleep 10
   fi

   if [ $version -eq 2 ];then       
        echo ": streamv2core0"
        numactl -C 0 --localalloc ./stream -v 2 -M 200M -P 1 -W 5
        sleep 10
   fi
fi
if [ $core_num -eq 64 ];then
   if [ $version -eq 1 ];then
        echo ": streamv1core0-63"
        numactl --cpunodebind=0,1,2,3 --localalloc ./stream -v 1 -M 200M -P 64 -W 5
        sleep 10
  fi

  if [ $version -eq 2 ];then
        echo ": streamv2core0-63"
        numactl --cpunodebind=0,1,2,3 --localalloc ./stream -v 2 -M 200M -P 64 -W 5
        sleep 10
  fi
fi
}

for ((i=0;i< $test_num;i++));do
    echo "======No $i Test======"
	stream_test
done





