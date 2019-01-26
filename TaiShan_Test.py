#!/usr/bin/python
import re
import time
import os,cmd,sys
import subprocess

import pdb

envirn_path=os.getcwd()
pkg_path=os.path.join(os.getcwd(),'pkg')
ltp_path=os.path.join(os.getcwd(),'ltp')
cpu_path=os.path.join(os.getcwd(),'cpu')
mem_path=os.path.join(os.getcwd(),'mem')
fio_path=os.path.join(os.getcwd(),'fio')
net_path=os.path.join(os.getcwd(),'net')

class TaiShan_Test(cmd.Cmd):
    intro = 'Welcome to the TaiShan shell.   Type help or ? to list commands.\n'
    prompt = '(TaiShan) '
    file = None
    os.getcwd()
    # ----- basic performance commands -----

    def do_cpu(self, args):
        os.chdir(cpu_path)
        print "speccpu2006 test" 
    def help_cpu(self):
        print "\nThis function is developing ... \n"

    def do_ltp(self, args):
        for i in args.split():
            if re.match('runtime', i):
                runtime = i.split('=')[1]

        os.chdir(ltp_path)
        print "ltp test"
        process = subprocess.Popen('./testscripts/ltpstress.sh -n -t %s 2>&1' % ( runtime), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        (output, exitcode) = process.communicate()
        print output
         
    def help_ltp(self):
        os.chdir(ltp_path)
        process = subprocess.Popen('./ltp_test.sh -h 2>&1', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        (output, exitcode) = process.communicate()
        print output


    def do_io(self, args):
        for i in args.split():
            if re.match('rw_type', i):
                rw = i.split('=')[1]
            if re.match('blksize', i):
                bs = i.split('=')[1]
            if re.match('runtime', i):
                runtime = i.split('=')[1]
            if re.match('filename', i):
                filename = i.split('=')[1]
        os.chdir(fio_path) 
        process = subprocess.Popen('./fio_test.sh --rw_type=%s --blksize=%s --runtime=%s --filename=%s 2>&1' % ( rw, bs, runtime, filename), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        (output, exitcode) = process.communicate()
        print output

    def help_io(self):
        os.chdir(fio_path)
        process = subprocess.Popen('./fio_test.sh -h 2>&1', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        (output, exitcode) = process.communicate()
        print output

#        print "\nUsage: io [rw_type] [blksize] [blksize] [runtime] [device]\n"
#        print "  rw_type   : : IO direction, readwrite, values(randread randwrite read write),default randread"
#        print "  bs        : Block size unit, default 4k"
#        print "  runtime   : Stop workload when this amount of time has passed,default 10s"
#        print "  filename  : File(s) to use for the workload, default(Device descriptor like: /dev/sdc\n"
#        print "example: \n"
#        print "     io rw_type=randread blksize=4k runtime=10 filename=/dev/sdc"
#        print "     io rw_type=randwrite blksize=4k runtime=10 filename=/dev/sdc"
#        print "     io rw_type=randread blksize=1m runtime=10 filename=/dev/sdc"
#        print "     io rw_type=randwrite blksize=1m runtime=10 filename=/dev/sdc\n"
 

    def do_mem(self, args):
        for i in args.split():
            if re.match('version', i):
                version = i.split('=')[1]
            if re.match('core_num', i):
                core_num = i.split('=')[1]
            if re.match('test_num', i):
                test_num = i.split('=')[1]

        os.chdir(mem_path)
        process = subprocess.Popen('./stream_test.sh --version=%s --core_num=%s --test_num=%s 2>&1' % ( version, core_num, test_num), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        (output, exitcode) = process.communicate()
        print output

    def help_mem(self):
        os.chdir(mem_path)
        process = subprocess.Popen('./stream_test.sh -h 2>&1', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        (output, exitcode) = process.communicate()
        print output

    def do_network(self, args):
        #pdb.set_trace()
        os.chdir(net_path)
        content = re.findall("server", args)
        if content:
           print "ready to test server"
           for i in args.split():  
               if re.match('server', i):
                 server = i.split('=')[1]
           process = subprocess.Popen('./net_test.sh --server=%s 2>&1' % ( server), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
           (output, exitcode) = process.communicate()

        content = re.findall("client", args)
        if content :
          print "ready to test server"
          for i in args.split():
            if re.match('time', i):
                time = i.split('=')[1]
            if re.match('parallel', i):
                parallel = i.split('=')[1]
            if re.match('host', i):
                host = i.split('=')[1]
            if re.match('client', i):
                client = i.split('=')[1]
            if re.match('interval', i):
                interval = i.split('=')[1]
          process = subprocess.Popen('./net_test.sh --client=%s --host=%s --parallel=%s--time=%s --interval=%s 2>&1' % ( client, host, parallel, time, interval), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)   
          (output, exitcode) = process.communicate()
        print output

    def help_network(self):
        os.chdir(net_path)
        process = subprocess.Popen('./net_test.sh -h 2>&1', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        (output, exitcode) = process.communicate()
        print output

    def emptyline(self):
        pass

    def precmd(self, line):
        line = line.lower()
        return line

def env_check():
    os.chdir(pkg_path)
    process = subprocess.Popen('./env_check.sh 2>&1', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (output, exitcode) = process.communicate()
    print output


if __name__ == "__main__":
    print "server test environment checking ... "
    time.sleep(1)
    env_check()
    time.sleep(1)
    print "server test environment checking ok \n"
    TaiShan_Test().cmdloop()


