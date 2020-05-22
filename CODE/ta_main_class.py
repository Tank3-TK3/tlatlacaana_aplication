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

################################################################################
#                   CLASS

class Scanner():
    operating_system = "" #Computer operating system.
    computer_name = "" #Computer name.
    ip_range = "" #Ip range to scan.
    host_ip = "" #Host ip to scan.
    ping_result = False #Ping result.
    trace_result = "" #Trace result.
    ip_scan = {} #Ip scanner result. (Key = str and value = bool)
    host_dns = "" #DNS of the target.
    port_range = "" #Port range.
    port_result = {} #Port scan result.
    
    def __init__(self):
        self.operating_system = platform.system()
        self.computer_name = socket.gethostname()

    def test_connection(self):
        if self.operating_system is "Windows":
            if os.system("ping -n 1 " + self.host_ip) is 0:
                self.ping_result = True
            else:
                self.ping_result = False
        else:
            if os.system("ping -c 1 " + self.host_ip) is 0:
                self.ping_result = True
            else:
                self.ping_result = False
        return self.ping_result

    def trace_connection(self):
        if self.operating_system is "Windows":
            if self.test_connection() is True:
                self.trace_result = os.popen("tracert " + self.host_ip).read()
            else:
                self.trace_result = ">>>Destination host not accessible<<<"
        else:
            if  self.test_connection() is True:
                self.trace_result = os.popen("tracerout " + self.host_ip).read()
            else:
                self.trace_result = ">>>Destination host not accessible<<<"
        return self.trace_result
################################################################################
