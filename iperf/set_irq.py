#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import subprocess
import sys
import re
import json
import collections
from argparse import ArgumentParser

def set_eth_irq_affinity():
    tmp = []
    cpu_list = []
    tmp_status = []

    #cmd_str = "/bin/systemctl status irqbalance.service"
    #print("cmd:%s"%cmd_str)
    #cmd_str = str(cmd_str)
    #ret = os.system(cmd_str)
   # cmd_str = "rm tmp_status"
   # cmd_str = str(cmd_str)
   # ret = os.system(cmd_str)
    p = subprocess.Popen('/bin/systemctl status irqbalance.service', shell = True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
	if(line.find('active (running)') >= 0):
	#if(re.search('active (running)', line)):	
	    print "!irqbalance.service has already start! Exit!"
	    print "!You need to stop irqbalance.service first!"
	    sys.exit(0),
	    #print line,
    retval = p.wait()

    #cmd_str = "/bin/systemctl stop irqbalance.service"
    #cmd_str = str(cmd_str)
    #ret = os.system(cmd_str)
    cmd_str = "cat /proc/interrupts |grep "+ str(eth_num)+ "-"+ "|awk -F: '{print $1}'|tr -d ' ' >> data_irq_t"
    print("cmd:%s"%cmd_str)
    #cmd_str = "cat /proc/interrupts | grep "+ str(eth_num)+ "  | cut  -d:  -f1 | sed 's/ //g' >> tmp"
    
    # process input string
    # eg.input form: ./get_eth_irq.py -C 29,30,31,61-63 -n eth2 -- this program used to transfer input string to an array for cpu core [29,30,31,61,62,63]
    # first: get the irq_list
    cmd_str=str(cmd_str)
    ret=os.system(cmd_str)
    f = file('data_irq_t')
    tmp = f.read()
    #print tmp
    irq_list_tmp = re.split(r'\s*', tmp)
    cmd_str = "rm data_irq_t"
    cmd_str = str(cmd_str)
    ret = os.system(cmd_str)
    irq_list_tmp.remove('')
    #irq_list = irq_list_tmp
    irq_list = irq_list_tmp[0:(len(irq_list_tmp))]
    #for index in range(len(irq_list_tmp)):
    #    if (irq_list_tmp[index] != null):
    #        irq_list.append(irq_list_tmp[index])
    print "********************"
    print irq_list


    length = len(cpu_range)
    i = 0
    while i < length:
        tmp_cpu = cpu_range[i]
	if re.search("-", tmp_cpu):
	    child_cpu_range = re.split(r'-', tmp_cpu)
	    tmp_cpu_start = child_cpu_range[0]
	    tmp_cpu_end = child_cpu_range[1]
	    j = int(tmp_cpu_start)
	    k = int(tmp_cpu_end)
	    while(j < k + 1):
		#cpu_str = str(j)
		#cpu_list.append(cpu_str)
		cpu_list.append(j)
		j = j + 1
		
	else:
	    cpu_list.append(int(tmp_cpu))
	i = i + 1
    print cpu_list

    # begin to bind
    len_irq = len(irq_list)
    len_cpu = len(cpu_list)
    print len_irq, len_cpu
    bind_num = len_irq / len_cpu
    bind_more = len_irq % len_cpu
    print bind_num, bind_more
    x = 0
    while(x < len(cpu_list)):
	cur_cpu = cpu_list[x]
	cpu_hex_num = (0x1 << cur_cpu)
	cpu_hex_num = str(hex(cpu_hex_num))	
	if cpu_hex_num.startswith('0x'):
	    cpu_hex_num = cpu_hex_num[2:]
	    #print cpu_hex_num
	if str(cpu_hex_num)[-1] == "L":
	    cpu_hex_num = cpu_hex_num[:-1]
	#print("cpu: %s"%cpu_hex_num)
	print str(cpu_hex_num)[:-8],str(cpu_hex_num)[-8:]
	y = 0
	while(y < bind_num):	
	    if len(str(cpu_hex_num)[:-16]) > 0:
                cmd_str = "echo " + str(cpu_hex_num)[:-16]+","+str(cpu_hex_num)[-16:-8]+","+str(cpu_hex_num)[-8:] + " > " + "/proc/irq/"+str(irq_list[x*bind_num+y])+"/smp_affinity"
		#print irq_list[x*bind_num+y]
	    elif len(str(cpu_hex_num)[:-8]) > 0:
                cmd_str = "echo " + str(cpu_hex_num)[:-8]+","+str(cpu_hex_num)[-8:] + " > " + "/proc/irq/"+str(irq_list[x*bind_num+y])+"/smp_affinity"
		#print irq_list[x*bind_num+y]
	    else:
                cmd_str = "echo " + str(cpu_hex_num) + " > " + "/proc/irq/"+str(irq_list[x*bind_num+y])+"/smp_affinity"
		#print irq_list[x*bind_num+y]
	    y += 1

	    print("cmd:%s"%cmd_str)
	    cmd_str = str(cmd_str)
	    ret = os.system(cmd_str)
	x += 1
    
    z = 0
    if bind_more > 0:
        while(z < bind_more):
	    cur_cpu = cpu_list[z]
	    cpu_hex_num = (0x1 << cur_cpu)
	    cpu_hex_num = str(hex(cpu_hex_num))	
	    if cpu_hex_num.startswith('0x'):
	        cpu_hex_num = cpu_hex_num[2:]
	        #print cpu_hex_num
	    if str(cpu_hex_num)[-1] == "L":
	        cpu_hex_num = cpu_hex_num[:-1]
	    #print("cpu: %s"%cpu_hex_num)
	    print str(cpu_hex_num)[:-8],str(cpu_hex_num)[-8:]

	    if len(str(cpu_hex_num)[:-16]) > 0:
                cmd_str = "echo " + str(cpu_hex_num)[:-16]+","+str(cpu_hex_num)[-16:-8]+","+str(cpu_hex_num)[-8:] + " > " + "/proc/irq/"+str(irq_list[len_cpu*bind_num+z])+"/smp_affinity"
	        #print irq_list[len_cpu*bind_num+z]
	    elif len(str(cpu_hex_num)[:-8]) > 0:
                cmd_str = "echo " + str(cpu_hex_num)[:-8]+","+str(cpu_hex_num)[-8:] + " > " + "/proc/irq/"+str(irq_list[len_cpu*bind_num+z])+"/smp_affinity"
	        #print irq_list[len_cpu*bind_num+z]
	    else:
                cmd_str = "echo " + str(cpu_hex_num) + " > " + "/proc/irq/"+str(irq_list[len_cpu*bind_num+z])+"/smp_affinity"
	        #print irq_list[len_cpu*bind_num+z]
	    print("cmd:%s"%cmd_str)
	    cmd_str = str(cmd_str)
	    ret = os.system(cmd_str)
	    z += 1
	

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-C", "--cpunum", action="store", dest="cpu_num", default="", help="set the cpu core numbers")

    parser.add_argument("-n", "--ethnum", action="store", dest="eth_num", default="", help="set the eth num")


    args = parser.parse_args()
    if args.eth_num:
        eth_num = args.eth_num
    else:
        sys.exit(0)

    if args.cpu_num:
        cpu_num = args.cpu_num
	cpu_range = re.split(r',', cpu_num)
    else:
        sys.exit(0)

    set_eth_irq_affinity()



