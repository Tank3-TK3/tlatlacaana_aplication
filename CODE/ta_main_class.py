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
    

################################################################################
