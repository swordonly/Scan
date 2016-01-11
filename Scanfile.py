#-*- coding: utf-8 -*- 
#Python初学者、我是代码搬运工、根据网上代码启发而成、大家勿喷
#author:water
  
import platform 
import sys 
import os 
import time 
import thread
import urllib
import socket 
  
def get_os(): 

  os = platform.system() 
  if os == "Windows": 
    return "n"
  else: 
    return "c"

def ping_ip(ip,port,para): 
  s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  try:
      s.connect((ip,int(port)))
      s.shutdown(2)
      url = "http://"+ip+":"+port+para
      status=urllib.urlopen(url).code
      if(status == 200 or status == 403 or status == 404 or status == 500):
        print '%s -------- %d' %(url, status)
  except:
      # print '%s is down' % ip
      return False
  
def find_ip(ip_prefix,port,para): 

  for i in range(1,256): 
    ip = '%s.%s'%(ip_prefix,i) 
    thread.start_new_thread(ping_ip, (ip,port,para)) 
    time.sleep(0.3) 
    
if __name__ == "__main__": 
  print "start time %s"%time.ctime() 
  commandargs = sys.argv[1] 
  args = "".join(commandargs)
  port = "".join(sys.argv[2])
  para = "".join(sys.argv[3])

    
  ip_prefix = '.'.join(args.split('.')[:-1]) 
  find_ip(ip_prefix,port,para) 
  print "end time %s"%time.ctime()
