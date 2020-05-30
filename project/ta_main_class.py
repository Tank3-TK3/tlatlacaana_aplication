################################################################################

 ##### #       #   ##### #       #   #####   #     #   #   #   #    v1.0.0
   #   #      # #    #   #      # #  #      # #   # #  ##  #  # #
   #   #     #####   #   #     ##### #     ##### ##### # # # #####
   #   ##### #   #   #   ##### #   # ##### #   # #   # #  ## #   # ApPlIcAtIoN

# *(From Nahuatl Tlatlacaana, which is defined as: Stalking or spy on another)
################################################################################

################################################################################
#                                                                              #
#                    Coded by Roberto (Tank3) Cruz Lozano                      #
#                   and Ernesto Adán Zurbía Flores Vivero                      #
#                                                                              #
################################################################################

################################################################################
#                   MODULES

import os #Provides tools for using the operating system.
import platform #Access to the identification data of the computer.
import socket #Provides access to the socket interface.
import dns.resolver #DNS toolkit for Python.

################################################################################
#                   CLASS

class TlatlacaanaApplication():
    operating_system = "" #Computer operating system.
    computer_name = "" #Computer name.
    ping_result = False #Ping result.
    trace_result = "" #Trace result.
    ip_scan = {} #Ip scanner result.
    port_result = False #Port result.
    port_scan = {} #Port scan result.
    
    def __init__(self):
        self.operating_system = platform.system()
        self.computer_name = socket.gethostname()

    def dns_to_ip(self, host_dns):
        return socket.gethostbyname(host_dns)

    def test_connection(self, host_ip):
        if self.operating_system is "Windows":
            if "TTL=" in os.popen("ping -n 1 " + host_ip).read():
                self.ping_result = True
            else:
                self.ping_result = False
        else:
            if "ttl=" in os.popen("ping -c 1 " + host_ip).read():
                self.ping_result = True
            else:
                self.ping_result = False
        return self.ping_result

    def trace_connection(self, host_ip):
        if self.operating_system is "Windows":
            if self.test_connection(host_ip) is True:
                self.trace_result = os.popen("tracert " + host_ip).read()
            else:
                self.trace_result = ">>>Destination host not accessible<<<"
        else:
            if  self.test_connection(host_ip) is True:
                self.trace_result = os.popen("tracerout " + host_ip).read()
            else:
                self.trace_result = ">>>Destination host not accessible<<<"
        return self.trace_result
    
    def inquire_ip(self, ip_min, ip_max):
        current_ip = ip_min.split(".")
        ip_max = ip_max.split(".")
        flag = True
        while flag:
            key_ip = ".".join(current_ip)
            if current_ip == ip_max:
                self.ip_scan[key_ip] = self.test_connection(key_ip)
                flag = False
            else:
                self.ip_scan[key_ip] = self.test_connection(key_ip)
                if(int(current_ip[3]) < 254):
                    current_ip[3] = str(int(current_ip[3])+1)
                elif(int(current_ip[2]) < 254):
                    current_ip[2] = str(int(current_ip[2])+1)
                    current_ip[3] = "1"
                elif(int(current_ip[1]) < 254):
                    current_ip[1] = str(int(current_ip[1])+1)
                    current_ip[2] = "0"
                    current_ip[3] = "1"
                elif(int(current_ip[0]) < 254):
                    current_ip[0] = str(int(current_ip[0])+1)
                    current_ip[1] = "0"
                    current_ip[2] = "0"
                    current_ip[3] = "1"
                else:
                    return self.ip_scan
        return self.ip_scan

    def check_port(self,host_ip, port):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.settimeout(1.0)
        ruling = my_socket.connect_ex((host_ip, port))
        if ruling == 0:
            self.port_result = True
        else:
            self.port_result = False
        my_socket.close()
        return self.port_result

    def port_finder(self, host_ip, port_min, port_max):
        for port in range(port_min, port_max+1):
            self.port_scan[port] = self.check_port(host_ip, port)
        return self.port_scan

    def get_banner(self, host_ip, port):
        if self.check_port(host_ip, port) is True:
            my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            my_socket.connect((host_ip, port))
            my_socket.send(b'GET /\n\n')
            banner = str(my_socket.recv(1024)).replace("\\r\\n", "\n")
        else:
            banner = ">>>Destination port not accessible<<<"
        return banner
################################################################################
