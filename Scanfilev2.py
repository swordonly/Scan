#-*- coding: utf-8 -*- 
#Python初学者、我是代码搬运工、根据网上代码改写而成、大家勿喷
#author:water/w4ter
  
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
    
if __name__ == "__main__": 
  print "start time %s"%time.ctime() 
  uri = "".join(sys.argv[1])
  para = "".join(sys.argv[2])

  f = open(uri, 'a+')
  # print f.readlines()
  for ipport in f.readlines():
  	ipport = ipport.strip('\n')
  	flag = ipport.rfind(":")
  	if flag != -1:
  		port = ipport[flag+1:]
  	else:
  		port = str(80)
	ip = ipport[:flag]
  	# print ip, port
  	# find_ip(ip,port,para) 
  	thread.start_new_thread(ping_ip, (ip,port,para)) 
  	time.sleep(0.3)
  f.close()
  print "end time %s"%time.ctime()
