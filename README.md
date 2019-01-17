# BasePerfiormaceTest
使用说明：
1. 进入交互界面
        python  TaiShan_Test.py
2. help 或 ？显示支持哪些基础性能测试(当前仅支持io和mem测试)
3. help <topic>，即help io 或help mem，提供测试用例说明
   按照example示例，执行基础性能测试

4. 当前测试输出会显示在终端窗口
5. 网络测试，需要两台服务器，在Server端与Client端分别执行指定命令
   1) 关防火墙
      systemctl status firewalld
      systemctl stop firewalld 
      systemctl status firewalld

   2) 关中断负载均衡
      systemctl status irqbalance
      systemctl stop irqbalance
      systemctl status irqbalance

   3) 绑中断net目录下，
      -n 指定网络接口，这里是enahisic2i0
      -C 绑定Core 11-15               
      ./set_irq.py -C 11-15 -n enahisic2i0 

   4) python TaiShan_Test.py进行网络测试
      配合的机器执行Server 
      Server
       network server=1
      用来主要性能测试的机器执行以下命令
      Client
      network client=1 host=ipaddr parallel=5 time=10 interval=1


