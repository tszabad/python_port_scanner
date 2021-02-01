import socket
from common_ports import ports_and_services

def get_open_ports(*args):
    open_ports = []
    host = args[0]
    port = args[1]
    host_ip = None
    host_name = None
    verbose = False
    ip = False

    if len(args) ==3:
      verbose = args[2]
    try:
      if host[0].isdigit() != True:
        host_ip =socket.gethostbyname(host)
        host_name = host
      else:
        ip = True
        try:
          host_name = socket.gethostbyaddr(host)[0]
        except:
          print("Error getting  ip address")
        host_ip = host

    
      for i in range(port[0],port[1]+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.2)
        result = s.connect_ex((args[0],int(i)))
        if result == 0:
          open_ports.append(i)
        s.close()
        
      str1=""
      if verbose == False:
        return open_ports
      else:
        if host_name is not None:
          str1 = str(host_name) + " (" + str(host_ip) + ")"
        else:
          str1 =  str(host_ip) 

      open_port = 'Open ports for ' + str(str1) +  '\n' + 'PORT     SERVICE'
      for i in open_ports:
        open_port += '\n' + str(i) + (9-len(str(i)))*' ' + str(ports_and_services[i])
        return open_port

    except socket.gaierror:
        if ip == True:
            return('Error: Invalid IP address')
        else:
            return('Error: Invalid hostname') 