#!/bin/bash
###################################################################################
# Default Variables
###################################################################################
#rw_type=randread
#blksize=4k
#runtime=10
#filename=/dev/sdb

###################################################################################
# Usage
###################################################################################
Usage()
{
cat << EOF
Usage: io [Options]
Options:
    rw         : IO direction, readwrite, values(randread randwrite read write)
    bs         : Block size unit
    name       : Name of this job
    direct     : Use O_DIRECT IO (negates buffered)
    numjobs    : Duplicate this job this many times
    runtime    : Stop workload when this amount of time has passed,default 10s
    iodepth    : Number of IO buffers to keep in flight
    ioengine   : IO engine to use
    filename   : File(s) to use for the workload, default(Device descriptor like: /dev/sdb\n
    
Example:
    fio -name=iops -rw=randread  -bs=4k -runtime=180 -iodepth=64 -filename=/dev/sdb -ioengine=libaio -direct=1
    fio -name=iops -rw=randwrite -bs=4k -runtime=180 -iodepth=64 -filename=/dev/sdb -ioengine=libaio -direct=1
    fio -name=iops -rw=read   -bs=1m -runtime=180 -iodepth=64 -filename=/dev/sdb -ioengine=libaio -direct=1
    fio -name=iops -rw=write  -bs=1m -runtime=180 -iodepth=64 -filename=/dev/sdb -ioengine=libaio -direct=1

EOF
}

###################################################################################
# Get all args
###################################################################################

#echo -$me-$filename

if [ x"$1" == x"-h" ];then
   Usage ; exit 0
fi


#while test $# != 0
#do
#    case $1 in
#        --*=*) ac_option=`expr "X$1" : 'X\([^=]*\)='` ; ac_optarg=`expr "X$1" : 'X[^=]*=\(.*\)'` ; ac_shift=: ;;
#        -*) ac_option=$1 ; ac_optarg=$2; ac_shift=shift ;;
#        *) ac_option=$1 ; ac_shift=: ;;
#    esac
#
#    case ${ac_option} in
#	#-rw |--rw_type) eval rw_type=$ac_optarg ;;
#	#-bs | --blksize) eval blksize=$ac_optarg ;;
#        #--runtime) runtime=$ac_optarg ;;
#        #--filename) filename=$ac_optarg ;;
#        -h | --help) Usage ; exit 0 ;;
#        #*) Usage ; echo "Unknown option $1" ; exit 1 ;;
#        #*) Usage ; echo "Unknown option $1" ; exit 1 ;;
#    esac
#
#    ${ac_shift}
#    shift
#done

#echo -$rw_type-$blksize-$runtime-$filename
###################################################################################
# Exectue fio test
###################################################################################
#echo "===$*==="
./fio $*
#taskset -c 0-4 ./fio -name=fio_test -rw=$rw_type -bs=$blksize -runtime=$runtime -iodepth=64 -filename=$filename -ioengine=libaio -direct=1	
#taskset -c 0-4 fio -name=iops -rw=randread -bs=4k -runtime=10 -iodepth=64 -filename=/dev/sda -ioengine=libaio -direct=1
#taskset -c 0-4 fio -name=iops -rw=randwrite -bs=4k -runtime=10 -iodepth=64 -filename=/dev/sda -ioengine=libaio -direct=1
#taskset -c 0-4 fio -name=iops -rw=read -bs=1m -runtime=10 -iodepth=64 -filename=/dev/sda -ioengine=libaio -direct=1
#taskset -c 0-4 fio -name=iops -rw=write -bs=1m -runtime=10 -iodepth=64 -filename=/dev/sda -ioengine=libaio -direct=1




