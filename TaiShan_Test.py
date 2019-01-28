#!/usr/bin/python
import re
import time
import os,cmd,sys
import subprocess
import pdb

#loc=0
bench_test=''
bench=['cpu','stream','fio','iperf','ltp']
prj_path=os.getcwd()

class TaiShan_Test(cmd.Cmd):
    intro = 'Welcome to the TaiShan shell.   Type help or ? to list commands.\n'
    prompt = '(TaiShan) '
    __loc__ = 0
    #global loc
    global bench_test 
    file = None
    prj_path=os.getcwd()
 
    def __init__(self, completekey='tab', stdin=None, stdout=None):
        """Instantiate a line-oriented interpreter framework.

        The optional argument 'completekey' is the readline name of a
        completion key; it defaults to the Tab key. If completekey is
        not None and the readline module is available, command completion
        is done automatically. The optional arguments stdin and stdout
        specify alternate input and output file objects; if not specified,
        sys.stdin and sys.stdout are used.

        """
        import sys
        if stdin is not None:
            self.stdin = stdin
        else:
            self.stdin = sys.stdin
        if stdout is not None:
            self.stdout = stdout
        else:
            self.stdout = sys.stdout
        self.cmdqueue = []
        self.completekey = completekey
        self.loc=0
        self.endloc=0
        self.bench_test=''

    # ----- common performance commands -----
    def __com_process__(self, test_item, script_type, args):
        test_path = os.path.join( prj_path, test_item)
        #print "test_item %s test_path %s" % (test_item, test_path)
        #print "test_item args[0]:%s args[1]:%s" % (args[:loc],args[loc:] )
        os.chdir( test_path)
        if isinstance(args,list):
           para1=args[0]
           para2=args[1]
           #print "list %s, para0:%s  para1:%s" % (args, para1, para2)
        else:
           para1=''
           para2=args
           #print "list %s, para0:%s  para1:%s" % (args, para1, para2)
           
        process = subprocess.Popen('%s ./%s_test.%s %s 2>&1' % (para1, test_item, script_type, para2), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)         
        (output, exitcode) = process.communicate()
        print output

    # ----- basic performance commands -----
    def do_stream(self, args):
        #print "------loc------"
        #print "loc:%d test_item args[0]:%s args[1]:%s" % (self.loc, args[:self.loc],args[self.endloc:] )
        self.__com_process__( 'stream', 'sh', args)

    def help_stream(self):
        #print "loc:%d test_item args[0]:%s args[1]:%s" % (loc,args[:loc],args[loc:] )
        self.__com_process__( 'stream', 'sh', '-h')

    def do_fio(self, args):
        #print "arguments : %s" % (args)
        #print "loc:%d test_item args[0]:%s args[1]:%s" % (self.loc,args[:self.loc],args[self.endloc:] )
        self.__com_process__( 'fio', 'sh', args)
        #self.__com_process__( 'fio', 'sh', args)

    def help_fio(self):
        self.__com_process__( 'fio', 'sh', '-h')

    def do_cpu(self, args):
        self.__com_process__( 'cpu', 'sh', args)
        #self.__com_process__( 'cpu', 'py', args)

    def help_cpu(self):
        self.__com_process__( 'cpu', 'py', '-h')
        print "Example:"
        print "     cpu   462  -r 1"
        print "     cpu   fp   -r 1"
        print "     cpu   int  -r 1"
        print "     cpu   all  -r 1"
        print "     cpu   all  -r 64\n"

    def do_ltp(self, args):
        #self.__com_process__( 'ltp', 'sh', args[:self.loc],args[self.loc:])
        self.__com_process__( 'ltp', 'sh', args)
         
    def help_ltp(self):
        self.__com_process__( 'ltp', 'sh', '-h')

    def do_iperf(self, args):
        #print "arguments : %s" % (args)
        #print "loc:%d endloc:%d test_item args[0]:%s args[1]:%s" % (self.loc, self.endloc, args[:self.loc],args[self.endloc:] )
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
        cmd_list=[]
        for str_search in bench :
            pattern = re.compile(str_search) 
            str_match = pattern.search(line)
            if str_match != None :
                self.loc = str_match.start()
                self.endloc = str_match.end()
                #print " =====str_match start loc %d and end loc %d "%( self.loc, str_match.end())
                self.bench_test = str_search
        
        #pdb.set_trace()
        #print " cmd----bt:%s  loc:%d" %(self.bench_test, self.loc)
        return line

    def onecmd(self, line):
	"""Interpret the argument as though it had been typed in response
	to the prompt.

	This may be overridden, but should not normally need to be;
	see the precmd() and postcmd() methods for useful execution hooks.
	The return value is a flag indicating whether interpretation of
	commands by the interpreter should stop.

	"""
        args_list=[]
        #pdb.set_trace()
	cmd, arg, line = self.parseline(line)
	if not line:
		return self.emptyline()
	if cmd is None:
		return self.default(line)
	self.lastcmd = line
	if line == 'EOF' :
		self.lastcmd = ''
	if cmd == '':
		return self.default(line)
	else:
                if cmd != 'help' and self.loc != 0:
                    args_list.append(line[:self.loc])
                    args_list.append(line[self.endloc:])
                    #arg = line[self.endloc:]
                    arg=args_list
                    cmd = self.bench_test
                #print " cmd----cmd:%s arg:%s loc:%d" %(cmd,arg,self.loc)
		try:
			func = getattr(self, 'do_' + cmd)
		except AttributeError:
			return self.default(line)
		return func(arg)

if __name__ == "__main__":
    
    #Taishan = TaiShan_Test()
    #Taishan.cmdloop()
    TaiShan_Test().cmdloop()



