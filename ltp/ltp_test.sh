#!/bin/bash
###################################################################################
# Default Variables
###################################################################################

###################################################################################
# Usage
###################################################################################
Usage()
{
cat << EOF
Help info:
Usage: ltpstress [Options]

Options:

    -t duration : Execute the testsuite for given duration in hours. Default is 24.

Example:

    ltp runtime=168

EOF
}
###################################################################################
# Get all args
###################################################################################

#if [ x"$1" == x"-h" ];then
#   Usage ; exit 0
#fi

#while test $# != 0
#do
#    case $1 in
#        --*=*) ac_option=`expr "X$1" : 'X\([^=]*\)='` ; ac_optarg=`expr "X$1" : 'X[^=]*=\(.*\)'` ; ac_shift=: ;;
#        -*) ac_option=$1 ; ac_optarg=$2; ac_shift=shift ;;
#        *) ac_option=$1 ; ac_shift=: ;;
#    esac
#
#    case ${ac_option} in
#        -runtime) time=$ac_optarg ;;
#        -h | --help) Usage ; exit 0 ;;
#        *) Usage ; echo "Unknown option $1" ; exit 1 ;;
#    esac
#
#    ${ac_shift}
#    shift
#done

./testscripts/ltpstress.sh $*




