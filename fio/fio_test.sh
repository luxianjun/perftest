#!/bin/bash
###################################################################################
# Default Variables
###################################################################################
rw_type=randread
blksize=4k
runtime=10
filename=/dev/sdb

###################################################################################
# Usage
###################################################################################
Usage()
{
cat << EOF
Usage: io [Options]
Options:
    rw_type     : IO direction, readwrite, values(randread randwrite read write),default randread
    blksize     : Block size unit, default 4k
    runtime     : Stop workload when this amount of time has passed,default 10s
    filename    : File(s) to use for the workload, default(Device descriptor like: /dev/sdb\n

Example:
    io rw_type=randread  blksize=4k runtime=180 filename=/dev/sdb 
    io rw_type=randwrite blksize=4k runtime=180 filename=/dev/sdb 
    io rw_type=read      blksize=1m runtime=180 filename=/dev/sdb 
    io rw_type=write     blksize=1m runtime=180 filename=/dev/sdb 

EOF
}

#Usage()
#{
#cat << EOF
#Usage: io [Options]
#Options:
#    -h, --help: Display this information
#    --rw_type     : IO direction, readwrite, values(randread randwrite read write),default randread
#    --blksize     : Block size unit, default 4k
#    --runtime     : Stop workload when this amount of time has passed,default 10s
#    --filename    : File(s) to use for the workload, default(Device descriptor like: /dev/sdb\n
#
#Example:
#    ./fio_test.sh --rw_type=randread --blksize=4k --runtime=180 --filename=/dev/sdb 
#    ./fio_test.sh --rw_type=randwrite --blksize=4k --runtime=180 --filename=/dev/sdb 
#    ./fio_test.sh --rw_type=read --blksize=1m --runtime=180 --filename=/dev/sdb 
#    ./fio_test.sh --rw_type=write --blksize=1m --runtime=180 --filename=/dev/sdb 
#
#EOF
#}
#
#    -rw,--rw_type     : IO direction, readwrite, values(randread randwrite read write),default randread
#    -bs,--blksize : Block size unit, default 4k


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
	-rw |--rw_type) eval rw_type=$ac_optarg ;;
	-bs | --blksize) eval blksize=$ac_optarg ;;
        --runtime) runtime=$ac_optarg ;;
        --filename) filename=$ac_optarg ;;
        -h | --help) Usage ; exit 0 ;;
        *) Usage ; echo "Unknown option $1" ; exit 1 ;;
    esac

    ${ac_shift}
    shift
done

#echo -$rw_type-$blksize-$runtime-$filename
###################################################################################
# Exectue fio test
###################################################################################
taskset -c 0-4 ./fio -name=fio_test -rw=$rw_type -bs=$blksize -runtime=$runtime -iodepth=64 -filename=$filename -ioengine=libaio -direct=1	
#taskset -c 0-4 fio -name=iops -rw=randread -bs=4k -runtime=10 -iodepth=64 -filename=/dev/sda -ioengine=libaio -direct=1
#taskset -c 0-4 fio -name=iops -rw=randwrite -bs=4k -runtime=10 -iodepth=64 -filename=/dev/sda -ioengine=libaio -direct=1
#taskset -c 0-4 fio -name=iops -rw=read -bs=1m -runtime=10 -iodepth=64 -filename=/dev/sda -ioengine=libaio -direct=1
#taskset -c 0-4 fio -name=iops -rw=write -bs=1m -runtime=10 -iodepth=64 -filename=/dev/sda -ioengine=libaio -direct=1




