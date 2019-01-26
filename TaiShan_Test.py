#!/usr/bin/python
import re
import time
import os,cmd,sys
import subprocess

prj_path=os.getcwd()

class TaiShan_Test(cmd.Cmd):
    intro = 'Welcome to the TaiShan shell.   Type help or ? to list commands.\n'
    prompt = '(TaiShan) '
    file = None
    prj_path=os.getcwd()

    # ----- common performance commands -----
    def __com_process__(self, test_item, script_type, args):
        test_path = os.path.join( prj_path, test_item)
        print "test_item %s test_path %s" % (test_item, test_path)
        os.chdir( test_path)
        process = subprocess.Popen('./%s_test.%s %s 2>&1' % ( test_item, script_type, args), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)         
        (output, exitcode) = process.communicate()
        print output

    # ----- basic performance commands -----
    def do_stream(self, args):
        self.__com_process__( 'stream', 'sh', args)

    def help_stream(self):
        self.__com_process__( 'stream', 'sh', '-h')

    def do_fio(self, args):
        self.__com_process__( 'fio', 'sh', args)

    def help_fio(self):
        self.__com_process__( 'fio', 'sh', '-h')

    def do_cpu(self, args):
        self.__com_process__( 'cpu', 'py', args)

    def help_cpu(self):
        self.__com_process__( 'cpu', 'py', '-h')
        print "Example:"
        print "     cpu   462  -r 1"
        print "     cpu   fp   -r 1"
        print "     cpu   int  -r 1"
        print "     cpu   all  -r 1"
        print "     cpu   all  -r 64\n"

    def do_ltp(self, args):
        self.__com_process__( 'ltp', 'sh', args)
         
    def help_ltp(self):
        self.__com_process__( 'ltp', 'sh', '-h')

    def do_iperf(self, args):
        self.__com_process__( 'iperf', 'sh', args)

    def help_iperf(self):
        self.__com_process__( 'iperf', 'sh', '-h')
        print "Example:"
        print "   Server: "
        print "     iperf -s -w 256k"
        print "   Client:"
        print "     iperf -c ip_addr -P 1 -t 100 -i 1 -w 256k"
        print "     iperf -c ip_addr -P 4 -t 100 -i 1 -w 256k\n"

    def do_envcheck(self, args):
        self.__com_process__( 'envcheck', 'sh', args)
    def help_envcheck(self):
        self.__com_process__( 'envcheck', 'sh', '-h')

    def emptyline(self):
        pass

    def precmd(self, line):
        #print "---line : %s---"%line
        #line = line.lower()
        return line

if __name__ == "__main__":
    
    TaiShan_Test().cmdloop()



