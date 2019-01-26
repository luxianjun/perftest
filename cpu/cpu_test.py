#!/usr/bin/env python

import os
import re
import pdb
import sys
import time
#import logging
import argparse
import subprocess
#from scipy import stats

cpu2006={
    "int": { "400.perlbench":{ "reftime":9770, "num":3 }, "401.bzip2":{ "reftime":9650, "num":6 } , "403.gcc":{ "reftime":8050, "num":9 }, "429.mcf":{ "reftime":9120, "num":1 } , "445.gobmk":{ "reftime":10490, "num":5 }, "456.hmmer":{ "reftime":9330, "num":2 }, "458.sjeng":{ "reftime":12100, "num":1 }, "462.libquantum":{ "reftime":20720, "num":1 }, "464.h264ref":{ "reftime":22130, "num":3 },"471.omnetpp":{ "reftime":6250, "num":1 }, "473.astar":{ "reftime":7020, "num":2 }, "483.xalancbmk":{ "reftime":6900, "num":1 }}, 

    "fp":  { "410.bwaves":{ "reftime":13590, "num":1 }, "416.gamess":{ "reftime":19580, "num":3 },"433.milc":{ "reftime":9180, "num":1 }, "434.zeusmp":{ "reftime":9100, "num":1} , "435.gromacs":{ "reftime":7140, "num":1 }, "436.cactusADM":{ "reftime":11950, "num":1 }, "437.leslie3d":{ "reftime":9400, "num":1 }, "444.namd":{ "reftime":8020, "num":1 }, "447.dealII":{ "reftime":11440, "num":1 },"450.soplex":{ "reftime":8340, "num":2 }, "453.povray":{ "reftime":5320, "num":1 }, "454.calculix":{ "reftime":8250, "num":1 }, "459.GemsFDTD":{ "reftime":10610, "num":1 }, "465.tonto":{ "reftime":9840, "num":1 },"470.lbm":{ "reftime":13740, "num":1 }, "481.wrf":{ "reftime":11170, "num":1 },"482.sphinx3":{ "reftime":19490, "num":1 }}
}

bench_spec={ 
    "400":{ "reftime":9770, "num":3 }, "401":{ "reftime":9650, "num":6 } , "403":{ "reftime":8050, "num":9 }, "429":{ "reftime":9120, "num":1 },
    "445":{ "reftime":10490, "num":5 }, "456":{ "reftime":9330, "num":2 },
    "458":{ "reftime":12100, "num":1 },  "462":{ "reftime":20720, "num":1 },
    "464":{ "reftime":22130, "num":3 }, "471":{ "reftime":6250, "num":1 }, "473":{ "reftime":7020, "num":2 }, "483":{ "reftime":6900, "num":1 }, 
    "410":{ "reftime":13590, "num":1 }, "416":{ "reftime":19580, "num":3 },"433":{ "reftime":9180, "num":1 }, "434":{ "reftime":9100, "num":1}, "435":{ "reftime":7140, "num":1 }, 
    "436":{ "reftime":11950, "num":1 }, "437":{ "reftime":9400, "num":1 }, "444":{ "reftime":8020, "num":1 }, "447":{ "reftime":11440, "num":1 }, "450":{ "reftime":8340, "num":2 },
    "453":{ "reftime":5320, "num":1 }, "454":{ "reftime":8250, "num":1 }, "459":{ "reftime":10610, "num":1 }, "465":{ "reftime":9840, "num":1 }, "470":{ "reftime":13740, "num":1 }, 
    "481":{ "reftime":11170, "num":1 }, "482":{ "reftime":19490, "num":1 }
}


spec_item={"400": "400.perlbench","401":"401.bzip2","403":"403.gcc","429":"429.mcf" ,"445":"445.gobmk","456":"456.hmmer","458":"458.sjeng","462":"462.libquantum","464":"464.h264ref","471":"471.omnetpp","473":"473.astar","483":"483.xalancbmk","410":"410.bwaves","416":"416.gamess","433":"433.milc","434":"434.zeusmp" ,"435":"435.gromacs","436":"436.cactusADM","437":"437.leslie3d","444":"444.namd","447":"447.dealII","450":"450.soplex","453":"453.povray","454":"454.calculix","459":"459.GemsFDTD","465":"465.tonto","470":"470.lbm","481":"481.wrf","482":"482.sphinx3"}


prj_path = os.getcwd()

def runbench( key, rate, log):
    print "run test item %s" % (key)
    test_path = os.path.join(prj_path,'cpu2006', key)
    os.chdir(test_path)
    process = subprocess.Popen(' ./%s.sh %s 2>&1' % ( key, rate), stdout=log, stderr=subprocess.PIPE, shell=True)
    (output, exitcode) = process.communicate()
    print output

def spec_runbench( test_type, rate, log):
    if test_type == 'all' :
      print "run all bench"
      for key,value in cpu2006["int"].items():
        runbench( key, rate, log)

      for key,value in cpu2006["fp"].items():
        runbench( key, rate, log)

    elif test_type == 'int' :
      print "run int bench"
      for key,value in cpu2006["int"].items():
        runbench( key, rate, log)
    elif test_type == 'fp' :
      print "run fp bench"
      for key,value in cpu2006["fp"].items():
        runbench( key, rate, log)
    else:
        if spec_item.has_key(test_type) :
          runbench( spec_item[test_type], rate, log)

def spec_sortresult( filename, rate, spec_timelist, spec_scorelist):
    count=0
    reftime=0
    case_num=0
    totalcase_num=0
    score=[]
    #Function Part
    spec_fd = open( filename,'r')
    data_lines = spec_fd.readlines()
    for line in data_lines:
      #print line
      bench_item = re.findall(r'(^[0-9]+$)',line.strip())
      item = ''.join(bench_item)

      if bench_item != [] and spec_item.has_key(item) :
          ref_item = ''.join(bench_item)
          reftime = bench_spec[ref_item]['reftime']
          case_num = bench_spec[ref_item]['num']
          totalcase_num = case_num * rate
          tmp_list = []
          sum_list = [0]*rate
          #print "bench reftime : %d reftime %d " %(bench_spec[item]['reftime'],reftime)
          #print "bench num : %d case num %d" %(bench_spec[item]['num'],case_num)

      if re.findall(r'(real\s)', line.strip()) != [] :
          count+=1
          cnt_point=0
          real_time = re.findall(r'([0-9]+)m([0-9]+\.[0-9]+)s', line.strip())
          #print "real_time %s "%real_time
          for item in real_time :
            time = float(item[0])*60+float(item[1])
            tmp_list.append(time)
          cnt_point = count%rate
          
          if cnt_point == 0:  
            sum_list=[ sum_list[i]+tmp_list[i] for i in range(0,rate) ]
            tmp_list = []
          #calcuate speccpu2006 score per benchspec
          if count == totalcase_num :
              count = 0
              for i in range(0,rate):
                spec_timelist[ref_item] = sum_list[i]
                #print "sum_list %s"%(sum_list)
                #print "spec_timelist %s"%(spec_timelist)
            
              for i in range(0,rate):
                spec_scorelist[ref_item]=(rate*reftime/sum_list[i])

              #print "spec scorelist  %s"%(spec_scorelist)


def spec_resultshow( rate, spec_timelist, spec_scorelist):
    print("\nBenchmarks\t  Base Copies\t   Base Run Time\t   Estimated Base Rate ")
    print("-----------\t ------------\t ---------------\t ---------------------\n")
    for key,value in spec_scorelist.items():
        print ("%s        \t       %d    \t       %d       \t       %.1f           \n") %( spec_item[key], rate, spec_timelist[key],spec_scorelist[key])





if __name__=="__main__":
    parser = argparse.ArgumentParser(prog='speccpu2006',description='cpu ability estimate.')
    #parser.add_argument("test_log", type = str,  help = 'specify test log, used to parsing score')
    parser.add_argument("test_item", type = str,  help = 'specify test type, default all or int or fp or item_number ', default = 'all')
    parser.add_argument('-r',"--rate", type = str,  help = 'Do a throughput (rate) run of [N] copies (if [N] is specified).',default = 1)

    args = parser.parse_args()

    log_name = time.strftime('%Y.%m.%d-%H:%M',time.localtime(time.time()))
    #log_name = 'testlog'
    test_record = os.path.join(prj_path,log_name)
    logFile = open(test_record ,'w')
    rate = int(args.rate )
    test_item = args.test_item
    
    spec_runbench( test_item, rate , logFile)
    logFile.close()

    spec_timelist = {} 
    spec_scorelist = {}
    
    #According the log, get speccpu2006 time per benchspec
    spec_sortresult( test_record, rate, spec_timelist, spec_scorelist )
    
    #Show Parse Spec Reslut
    spec_resultshow( rate, spec_timelist, spec_scorelist)






















