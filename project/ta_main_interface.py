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
#               and Ernesto (Neto844) Adán Zurbía Flores Vivero                #
#                                                                              #
################################################################################

################################################################################
#                   MODULES

import sys
import os
import time
from ta_main_class import TlatlacaanaApplication

pc = TlatlacaanaApplication()
PYTHON_VERSION = sys.version_info.major ##Identify the installed python version
if PYTHON_VERSION < 3:
    try:
        import Tkinter as tk
        import Tkinter.scrolledtext as scrolledtext
        import Tkinter.font as font
        from Tkinter import messagebox
    except ImportError:
        raise ImportError("Se requiere el modulo Tkinter")
else:
    try:
        import tkinter as tk
        import tkinter.scrolledtext as scrolledtext
        import tkinter.font as font
        from tkinter import messagebox
    except ImportError:
        raise ImportError("Se requiere el modulo tkinter")
##We ensure that the user has the tkinder module installed
def close():
     root.destroy()

def minimize():
     root.withdraw()
     root.overrideredirect(False)
     root.iconify()

def on_deiconify(event):
     root.deiconify()
     root.overrideredirect(True)

def start_move(event):
     root._x = event.x
     root._y = event.y

def stop_move(event):
     root._x = None
     root._y = None

def on_move(event):
     deltax = event.x - root._x
     deltay = event.y - root._y
     new_pos = "+{}+{}".format(root.winfo_x() + deltax,root.winfo_y() + deltay)
     root.geometry(new_pos)

def on_enter(e):
    if Option_1['background']=='#094771':
        return
    else:
        Option_1['background'] = '#37373d'

def on_leave(e):
    if Option_1['background']=='#094771':
        return
    else:
        Option_1['background'] = '#252526'
    
def on_enter1(e):
    if Option_2['background']=='#094771':
        return
    else:
        Option_2['background'] = '#37373d'

def on_leave1(e):
    if Option_2['background']=='#094771':
        return
    else:
        Option_2['background'] = '#252526'

def on_enter2(e):
    if Option_3['background']=='#094771':
        return
    else:
        Option_3['background'] = '#37373d'

def on_leave2(e):
    if Option_3['background']=='#094771':
        return
    else:
        Option_3['background'] = '#252526'

def on_enter3(e):
    GetIp_button['background']='#404047'

def on_leave3(e):
    GetIp_button['background']='#37373d'

def on_enter4(e):
    X_button['background']='#e81123'

def on_leave4(e):
    X_button['background']='#333333'

def on_enter5(e):
    min_button['background']='#474748'

def on_leave5(e):
    min_button['background']='#333333'




def ClickButton(number):
    if number=="1":
        Option_1.config(bg="#094771")
        Option_2.config(bg="#252526")
        Option_3.config(bg="#252526")

        for widget in Content_frame.winfo_children():
            widget.destroy()
        def Click(option):
            ResultBox.config(state="normal")
            ResultBox.delete('1.0',tk.END)
            ResultBox.insert(tk.INSERT,"The operation is in progress"+
                                    " please wait")
            time.sleep(1.0)
            if option=="1":
                ResultBox.delete('1.0',tk.END)
                Ping=pc.test_connection(Ip_entry.get())
                if Ping==True:
                    ResultBox.insert(tk.INSERT,"The ip address has"+
                    " responded successfully")
                    ResultBox.config(state="disabled")
                elif Ping==False:
                    ResultBox.insert(tk.INSERT,"The ip address did not"+
                    " respond, try another ip \naddress")
                    ResultBox.config(state="disabled")
            else:
                Ping=pc.trace_connection(Ip_entry.get())
                ResultBox.delete('1.0',tk.END)
                ResultBox.insert(tk.INSERT,Ping)
                ResultBox.config(state="disabled")


        def on_enter4(e):
            Ip_button['background'] = '#404047'
        def on_leave4(e):
             Ip_button['background'] = '#37373d'

        def on_enter5(e):
            Ip_button2['background'] = '#404047'
        def on_leave5(e):
             Ip_button2['background'] = '#37373d'

        Name_option=tk.Label(Content_frame, text="IP_SCANNER  ",bg="#1e1e1e",
                    foreground="#3179cb",padx=30,pady=10)
        Name_option.grid_propagate(False)
        Name_option['font']=font.Font(family="Consolas",size=40)
        space_1=tk.Label(Content_frame,height=5,bg="#1e1e1e")
        Ip_label=tk.Label(Content_frame,bg="#1e1e1e",
                         text="Enter an ip address:",foreground="#d1d1d1")
        Ip_label['font']=font.Font(family="Consolas",size=15)
        Ip_entry=tk.Entry(Content_frame,bg="#121212", relief="flat",
                          insertbackground="#fff",selectbackground="#0764d4"
                          ,width=20,foreground="#d1d1d1")
        Ip_entry['font']=font.Font(family="Consolas",size=15)
        Ip_button=tk.Button(Content_frame,bg="#37373d",text="Trace Route",
                            foreground="#d1d1d1",width=10,relief="flat",
                            activebackground="#373742",bd=0,
                            activeforeground="#d1d1d1",
                            command=lambda:Click("2"))
        Ip_button['font']=font.Font(family="Consolas",size=10)
        Ip_button2=tk.Button(Content_frame,bg="#37373d",text="Ping",width=10,
                            foreground="#d1d1d1",relief="flat",bd=0,
                            activebackground="#373742",
                            activeforeground="#d1d1d1"
                            ,command=lambda:Click("1"))
        Ip_button2['font']=font.Font(family="Consolas",size=10)
        space_2=tk.Label(Content_frame,height=5,bg="#1e1e1e")
        ResultBox=scrolledtext.ScrolledText(Content_frame,
                            height=20,width=80,bg="#121212",
                            relief="flat",foreground="#d1d1d1")
        ResultBox['font']=font.Font(family="Consolas",size=10)
        version=tk.Label(Content_frame,bg="#1e1e1e",foreground="#d1d1d1",
                         text="v1.0.0")
        version['font']=font.Font(family="Consolas",size=15)
        Ip_label.grid(row=2,column=0,sticky="E")
        space_1.grid(row=1,column=0)
        Name_option.grid(row=0,column=0)
        Ip_entry.grid(row=2,column=1,sticky="E",padx=50,columnspan=3)
        Ip_button2.grid(row=3,column=2,pady=10,sticky="E",padx=5)
        Ip_button.grid(row=3,column=3,pady=10,sticky="w",padx=10)
        ResultBox.grid(row=5,column=0,columnspan=4,sticky="e", padx=55)
        version.grid(row=6,column=5,pady=13,padx=72)
        space_2.grid(row=4,column=1)
        ResultBox.config(state="disabled")

        Ip_button.bind("<Enter>", on_enter4)
        Ip_button.bind("<Leave>", on_leave4)
        Ip_button2.bind("<Enter>", on_enter5)
        Ip_button2.bind("<Leave>", on_leave5)


    elif number=="2":
         Option_2.config(bg="#094771")
         Option_1.config(bg="#252526")
         Option_3.config(bg="#252526")


         for widget in Content_frame.winfo_children():
            widget.destroy()

         def Click():
            try:
                ResultBox.config(state="normal")
                ResultBox.delete('1.0',tk.END)
                range_ip = pc.inquire_ip(IpMin_entry.get(),IpMax_entry.get())
                ResultBox.insert(tk.INSERT,("<<IP scan result>>\n"))
                for x, y in range_ip.items():
                    outcome = "IP: "+str(x)+" Outcome: "+str(y)+"\n"
                    ResultBox.insert(tk.INSERT,(outcome))
                ResultBox.config(state="disabled")
            except:
                tk.messagebox.showerror(title="IP SACN FAILURE",
                                    message="ERROR: Not allowed values")

         def on_enter4(e):
             Ip_button['background'] = '#404047'
         def on_leave4(e):
             Ip_button['background'] = '#37373d'

         Name_option=tk.Label(Content_frame, text="IP_RANGE     ",bg="#1e1e1e",
                    foreground="#3179cb",padx=30,pady=10)
         Name_option.grid_propagate(False)
         Name_option['font']=font.Font(family="Consolas",size=40)
         space_1=tk.Label(Content_frame,height=5,bg="#1e1e1e")
         IpMin_label=tk.Label(Content_frame,bg="#1e1e1e",foreground="#d1d1d1",
                         text="Enter a minimum IP address:")
         IpMin_label['font']=font.Font(family="Consolas",size=15)
         IpMax_label=tk.Label(Content_frame,bg="#1e1e1e",foreground="#d1d1d1",
                         text="Enter a maximum IP address:")
         IpMax_label['font']=font.Font(family="Consolas",size=15)
         IpMin_entry=tk.Entry(Content_frame,bg="#121212", relief="flat",
                          insertbackground="#fff",selectbackground="#0764d4"
                          ,width=20,foreground="#d1d1d1")
         IpMin_entry['font']=font.Font(family="Consolas",size=15)
         IpMax_entry=tk.Entry(Content_frame,bg="#121212", relief="flat",
                          insertbackground="#fff",selectbackground="#0764d4"
                          ,width=20,foreground="#d1d1d1")
         IpMax_entry['font']=font.Font(family="Consolas",size=15)
         Ip_button=tk.Button(Content_frame,bg="#37373d",text="Ping",
                            foreground="#d1d1d1",width=10,relief="flat",
                            activebackground="#373742",bd=0,
                            activeforeground="#d1d1d1",
                            command=lambda:Click())
         Ip_button['font']=font.Font(family="Consolas",size=10)
         space_2=tk.Label(Content_frame,height=3,bg="#1e1e1e")
         ResultBox=scrolledtext.ScrolledText(Content_frame,height=12,
                                             width=50,bg="#121212",
                            relief="flat",foreground="#d1d1d1")
         ResultBox['font']=font.Font(family="Consolas",size=15)
         version=tk.Label(Content_frame,bg="#1e1e1e",foreground="#d1d1d1",
                         text="v1.0.0")
         version['font']=font.Font(family="Consolas",size=15)
         IpMin_label.grid(row=2,column=0,sticky="E",pady=10)
         IpMax_label.grid(row=3,column=0,sticky="E")
         space_1.grid(row=1,column=0)
         Name_option.grid(row=0,column=0)
         IpMin_entry.grid(row=2,column=1,sticky="E",padx=50,columnspan=3)
         IpMax_entry.grid(row=3,column=1,sticky="E",padx=50,columnspan=3)
         Ip_button.grid(row=4,column=3,pady=10,sticky="e",padx=50)
         ResultBox.grid(row=6,column=0,columnspan=4,sticky="e", padx=55)
         version.grid(row=7,column=4,pady=14,padx=44)
         ResultBox.config(state="disabled")
         space_2.grid(row=5,column=1)
         Ip_button.bind("<Enter>", on_enter4)
         Ip_button.bind("<Leave>", on_leave4)         

    elif number=="3":
         Option_3.config(bg="#094771")
         Option_1.config(bg="#252526")
         Option_2.config(bg="#252526")
         def Click(option):
             ResultBox.config(state="normal")
             ResultBox.delete('1.0',tk.END)
             if option=="1":
                 try:
                     dic_port = pc.port_finder(Ip_entry.get(), int(PortMin_entry.get()), int(PortMax_entry.get()))
                     ResultBox.insert(tk.INSERT,("<<<Scan Port Result>>>\n"))
                     for x, y in dic_port.items():
                         outcome = "Port: "+str(x)+" Outcome: "+str(y)+"\n"
                         ResultBox.insert(tk.INSERT,(outcome))
                 except:
                     tk.messagebox.showerror(title="PORT FINDER FAILURE", message="ERROR: Not allowed values")
                 ResultBox.config(state="disable")
             else:
                 try:
                     ResultBox.insert(tk.INSERT,(pc.get_banner(Ip_entry.get(), int(PortBanner_entry.get()))))
                 except:
                     tk.messagebox.showerror(title="PORT FINDER FAILURE", message="ERROR: Not allowed values")
                 ResultBox.config(state="disable")
         def on_enter4(e):
             Ip_button['background'] = '#404047'
         def on_leave4(e):
             Ip_button['background'] = '#37373d'
         def on_enter5(e):
             Banner_button['background'] = '#404047'
         def on_leave5(e):
             Banner_button['background'] = '#37373d'

         for widget in Content_frame.winfo_children():
            widget.destroy()
         Name_option=tk.Label(Content_frame, text="PORT FINDER  ",bg="#1e1e1e",
                    foreground="#3179cb",padx=30,pady=10)
         Name_option.grid_propagate(False)
         Name_option['font']=font.Font(family="Consolas",size=40)
         space_1=tk.Label(Content_frame,height=1,bg="#1e1e1e")
         Ip_label=tk.Label(Content_frame,bg="#1e1e1e",foreground="#d1d1d1",
                         text="Enter an ip address:")
         Ip_label['font']=font.Font(family="Consolas",size=15)
         PortMin_label=tk.Label(Content_frame,bg="#1e1e1e",
                        foreground="#d1d1d1",text="Enter a minium port:")
         PortMin_label['font']=font.Font(family="Consolas",size=15)
         PortMax_label=tk.Label(Content_frame,bg="#1e1e1e",
                         foreground="#d1d1d1",text="Enter a maximum port:")
         PortMax_label['font']=font.Font(family="Consolas",size=15)
         PortBanner_label=tk.Label(Content_frame,bg="#1e1e1e",
                     foreground="#d1d1d1",text="Get the banner of the port:")
         PortBanner_label['font']=font.Font(family="Consolas",size=15)
         Ip_entry=tk.Entry(Content_frame,bg="#121212", relief="flat",
                          insertbackground="#fff",selectbackground="#0764d4"
                          ,width=20,foreground="#d1d1d1")
         Ip_entry['font']=font.Font(family="Consolas",size=15)
         PortMin_entry=tk.Entry(Content_frame,bg="#121212", relief="flat",
                          insertbackground="#fff",selectbackground="#0764d4"
                          ,width=20,foreground="#d1d1d1")
         PortMin_entry['font']=font.Font(family="Consolas",size=15)
         PortMax_entry=tk.Entry(Content_frame,bg="#121212", relief="flat",
                          insertbackground="#fff",selectbackground="#0764d4"
                          ,width=20,foreground="#d1d1d1")
         PortMax_entry['font']=font.Font(family="Consolas",size=15)
         PortBanner_entry=tk.Entry(Content_frame,bg="#121212", relief="flat",
                          insertbackground="#fff",selectbackground="#0764d4"
                          ,width=20,foreground="#d1d1d1")
         PortBanner_entry['font']=font.Font(family="Consolas",size=15)
         Ip_button=tk.Button(Content_frame,bg="#37373d",text="Get Ports",
                            foreground="#d1d1d1",width=10,relief="flat",
                            activebackground="#373742",bd=0,
                            activeforeground="#d1d1d1",
                            command=lambda:Click("1"))
         Ip_button['font']=font.Font(family="Consolas",size=10)
         Banner_button=tk.Button(Content_frame,bg="#37373d",text="Get Banner",
                            foreground="#d1d1d1",width=10,relief="flat",
                            activebackground="#373742",bd=0,
                            activeforeground="#d1d1d1",
                            command=lambda:Click("2"))
         Banner_button['font']=font.Font(family="Consolas",size=10)
         space_2=tk.Label(Content_frame,height=1,bg="#1e1e1e")
         ResultBox=scrolledtext.ScrolledText(Content_frame,
                            height=18,width=80,bg="#121212",
                            relief="flat",foreground="#d1d1d1")
         ResultBox['font']=font.Font(family="Consolas",size=10)
         version=tk.Label(Content_frame,bg="#1e1e1e",foreground="#d1d1d1",
                         text="v1.0.0")
         version['font']=font.Font(family="Consolas",size=15)
         Ip_label.grid(row=2,column=0,sticky="E")
         PortMin_label.grid(row=3,column=0,sticky="E",pady=10)
         PortMax_label.grid(row=4,column=0,sticky="E")
         PortBanner_label.grid(row=6,column=0,sticky="E")
         space_1.grid(row=1,column=0)
         Name_option.grid(row=0,column=0)
         Ip_entry.grid(row=2,column=1,sticky="E",padx=50,columnspan=3)
         PortMin_entry.grid(row=3,column=1,sticky="E",padx=50,columnspan=3)
         PortMax_entry.grid(row=4,column=1,sticky="E",padx=50,columnspan=3)
         PortBanner_entry.grid(row=6,column=1,sticky="E",padx=50,columnspan=3)
         Banner_button.grid(row=7,column=3,pady=10,sticky="e",padx=50)
         Ip_button.grid(row=5,column=3,pady=10,sticky="e",padx=50)
         ResultBox.grid(row=9,column=0,columnspan=4,sticky="e", padx=55)
         version.grid(row=10,column=4,pady=12,padx=44)

         space_2.grid(row=8,column=1)

         
         Ip_button.bind("<Enter>", on_enter4)
         Ip_button.bind("<Leave>", on_leave4)
         Banner_button.bind("<Enter>", on_enter5)
         Banner_button.bind("<Leave>", on_leave5)



    elif number=="4":
         Option_1.config(bg="#252526")
         Option_2.config(bg="#252526")
         Option_3.config(bg="#252526")
         for widget in Content_frame.winfo_children():
            widget.destroy()

         Nombre_app1=tk.Label(Content_frame, text="TLATLACAANA",bg="#1e1e1e",
                            foreground="#3179cb")
         Nombre_app1['font']=font.Font(family="Consolas",size=40)
         Nombre_app2=tk.Label(Content_frame, text="ApPlIcAtIoN",bg="#1e1e1e",
                            foreground="#3179cb")
         Nombre_app2['font']=font.Font(family="Consolas",size=10)
         label1=tk.Label(Content_frame,bg="#1e1e1e",foreground="#d1d1d1",
                        text="“Software focused on the recognition phase of a "+ 
                        "computer security audit”")
         label1['font']=font.Font(family="Consolas",size=15)
         label2=tk.Label(Content_frame,bg="#1e1e1e",foreground="#3179cb",
                                text="Coded by:")
         label2['font']=font.Font(family="Consolas",size=15)
         label3=tk.Label(Content_frame,bg="#1e1e1e",foreground="#d1d1d1",
                                text="Roberto (Tank3) Cruz Lozano.")
         label3['font']=font.Font(family="Consolas",size=15)
         label4=tk.Label(Content_frame,bg="#1e1e1e",foreground="#d1d1d1",
                                text="Ernesto Adán (Neto844) Zurbía Flores Vivero.")
         label4['font']=font.Font(family="Consolas",size=15)
         label5=tk.Label(Content_frame,bg="#1e1e1e",foreground="#3179cb",
                                text="Summary:")
         label5['font']=font.Font(family="Consolas",size=15)
         Summary=tk.Text(Content_frame,height=12,width=61,bg="#1e1e1e",
                        relief="flat",foreground="#d1d1d1")
         Summary['font']=font.Font(family="Consolas",size=15)
         version=tk.Label(Content_frame,bg="#1e1e1e",foreground="#d1d1d1",
                                text="v1.0.0")
         version['font']=font.Font(family="Consolas",size=15)
         Nombre_app1.grid(row=0,column=0)
         Nombre_app2.grid(row=0,column=0, sticky="SE",padx=190)
         label1.grid(row=1,column=0,padx=10,pady=20)
         label2.grid(row=2,column=0,padx=100,sticky="W")
         label3.grid(row=3,column=0,padx=130,sticky="W",pady=20)
         label4.grid(row=4,column=0,padx=130,sticky="W")
         label5.grid(row=5,column=0,padx=100,sticky="W",pady=20)
         version.grid(row=7,column=1,sticky="W",pady=20)
         Summary.grid(row=6,column=0,sticky="E")
         Summary.insert(tk.INSERT,"The project presented here seeks to be a friendly"+
                    "tool with \nthe trained user, capable of doing IP and port"+
                    " recognition. \nIn the recognition phase of a computer "+
                    "security audit, we \nfind very useful and powerful tools, "+
                    "but not very friendly, \nthat is why our project focuses on "+
                    "bringing a useful and \neasy-to-use tool kit for the user as "+
                    "well as having an \ninterface in which all the tools and "+
                    "information obtained \nwill be displayed.")
         Summary.config(state="disabled")
    
    elif number == "5":
        try:
            IpResult.config(state="normal")
            IpResult.delete('1.0',tk.END)
            IpResult.insert(tk.INSERT,pc.dns_to_ip(DNS_entry.get()))
            IpResult.config(state="disabled")
        except:
            tk.messagebox.showerror(title="DNS INCORRECT",
                                    message="The domain"+
                                    "name is incorrect "+
                                    "please enter a new dns")
    else:
        return

root = tk.Tk() ##Create the window
root.title("Beta Aplication") ## Title of the window
root.geometry("1200x700")
root.resizable(0,0)
root.bind("<Map>", on_deiconify)
root.overrideredirect(True)

##################################MENU#########################################
Menu= tk.LabelFrame(root,bg="#252526",
                    width=300,height=700,bd=0)
Menu.grid(row=1,column=0,sticky="nw")
Menu.grid_propagate(False)
Option_1= tk.Button(Menu,text=" IP SCANER  ", bd=0, height=3, 
                  width=10,command=lambda :ClickButton("1"))
photo_option_1 = tk.PhotoImage(file=(os.path.dirname(__file__)+"/Scan.png")) 
photo_option_1 = photo_option_1.subsample(8,6) 
Option_1.config(image=photo_option_1, width=300,height=100, compound="left")
Option_1['font']=font.Font(family="Consolas",size=25)

Option_2= tk.Button(Menu,text="  IP RANGE   ", bd=0, height=3, 
                  width=10,command=lambda :ClickButton("2"))
photo_option_2 = tk.PhotoImage(file=(os.path.dirname(__file__)+"/Iprange.png")) 
photo_option_2 = photo_option_2.subsample(10,10) 
Option_2.config(image=photo_option_2, width=300,height=100, compound="left")
Option_2['font']=font.Font(family="Consolas",size=25)

Option_3= tk.Button(Menu,text=" PORT FINDER", bd=0, height=3, 
                  width=10, anchor="w",command=lambda :ClickButton("3"))
photo_option_3 = tk.PhotoImage(file=(os.path.dirname(__file__)+"/Port_finder.png")) 
photo_option_3 = photo_option_3.subsample(4,4) 
Option_3.config(image=photo_option_3, width=300,height=100, compound="left")
Option_3['font']=font.Font(family="Consolas",size=25)

for widget in Menu.winfo_children():
    widget.config(foreground="#d1d1d1", bg="#252526",cursor="hand2",
                  activebackground="#373742",activeforeground="#d1d1d1")

space_1=tk.Label(Menu,height=15,bg="#252526")
Converter_label=tk.Label(Menu,bg="#252526",foreground="#3179cb",
                         text="DNS Converter")
Converter_label['font']=font.Font(family="Consolas",size=15)
DNS_label=tk.Label(Menu,bg="#252526",foreground="#d1d1d1",
                         text="Enter a domain name:")
DNS_label['font']=font.Font(family="Consolas",size=10)
DNS_entry=tk.Entry(Menu,bg="#121212", relief="flat",
                          insertbackground="#fff",selectbackground="#0764d4"
                          ,width=18,foreground="#d1d1d1")
DNS_entry['font']=font.Font(family="Consolas",size=10)
GetIp_button=tk.Button(Menu,bg="#37373d",text="Get Ip",
                            foreground="#d1d1d1",width=10,relief="flat",
                            activebackground="#373742",bd=0,
                            activeforeground="#d1d1d1",
                            command=lambda:ClickButton("5"))
GetIp_button['font']=font.Font(family="Consolas",size=10)
Ip_label=tk.Label(Menu,bg="#252526",foreground="#d1d1d1",
                         text="Ip obtained: ")
Ip_label['font']=font.Font(family="Consolas",size=10)
IpResult=tk.Text(Menu,height=1,width=18,bg="#121212",
                            relief="flat",foreground="#d1d1d1")
IpResult['font']=font.Font(family="Consolas",size=10)
Option_1.grid(row=0,column=0,columnspan=2)
Option_2.grid(row=1,column=0,columnspan=2)
Option_3.grid(row=2,column=0,columnspan=2)
space_1.grid(row=3,column=0,columnspan=2)
Converter_label.grid(row=4,column=0,columnspan=2)
DNS_label.grid(row=5,column=0,sticky="W",padx=5)
DNS_entry.grid(row=5,column=1,sticky="W")
GetIp_button.grid(row=6,column=1,sticky="e",pady=5, padx=10)
Ip_label.grid(row=7,column=0,sticky="E",padx=5)
IpResult.grid(row=7,column=1,sticky="w")

IpResult.config(state="disabled")

Option_1.bind("<Enter>", on_enter)
Option_1.bind("<Leave>", on_leave)
Option_2.bind("<Enter>", on_enter1)
Option_2.bind("<Leave>", on_leave1)
Option_3.bind("<Enter>", on_enter2)
Option_3.bind("<Leave>", on_leave2)
GetIp_button.bind("<Enter>", on_enter3)
GetIp_button.bind("<Leave>", on_leave3)

##################################TOP_BAR######################################
Top_bar= tk.LabelFrame(root,bg="#333333",
                    width=1200,height=40,bd=0)
Top_bar.grid(row=0,column=0, columnspan=2)
Top_bar.columnconfigure(0,minsize=300)
Top_bar.columnconfigure(1,minsize=900)
X_button=tk.Button(Top_bar,bg="#333333", text="X", foreground="#d1d1d1"
                ,height=1,width=5,relief="flat",activebackground="#f1707a",
                bd=0,activeforeground="#fff",command=close)
X_button['font']=font.Font(family="Consolas",size=15)
min_button=tk.Button(Top_bar,bg="#333333", text="-", foreground="#d1d1d1"
                ,height=1,width=5,relief="flat",activebackground="#424242",
                bd=0,activeforeground="#fff",command=minimize)
min_button['font']=font.Font(family="Consolas",size=15)
app1=tk.Button(Top_bar, text="TLATLACAANA",bg="#333333",height=1,
                    foreground="#d1d1d1",relief="flat",bd=0,
                    activebackground="#333333",activeforeground="#d1d1d1",
                    command=lambda:ClickButton("4"))
app1['font']=font.Font(family="Consolas",size=15)
Op_System=tk.Label(Top_bar,bg="#333333",foreground="#d1d1d1",
                    text="Current OP System: ")
Op_System['font']=font.Font(family="Consolas",size=10)
Computer=tk.Label(Top_bar,bg="#333333",foreground="#d1d1d1",
                         text="Computer Name:")
Computer['font']=font.Font(family="Consolas",size=10)
Op_System_entry=tk.Text(Top_bar,height=1,width=24,bg="#333333",
                            relief="flat",foreground="#d1d1d1")
Op_System_entry['font']=font.Font(family="Consolas",size=10)
Computer_entry=tk.Text(Top_bar,height=1,width=24,bg="#333333",
                            relief="flat",foreground="#d1d1d1")
Computer_entry['font']=font.Font(family="Consolas",size=10)
Top_bar.grid_propagate(False)
X_button.grid(row=0,column=1,sticky="E")
min_button.grid(row=0,column=1,sticky="E",padx=60)
app1.grid(row=0,column=0,sticky="wn",pady=3)
Op_System.grid(row=0,column=1,sticky="w")
Op_System_entry.grid(row=0,column=1,sticky="w",padx=133)
Computer_entry.grid(row=0,column=1,sticky="e",padx=200)
Computer.grid(row=0,column=1,)

Op_System_entry.insert(tk.INSERT,pc.operating_system)
Computer_entry.insert(tk.INSERT,pc.computer_name)
Op_System_entry.config(state="disabled")
Computer_entry.config(state="disabled")

Top_bar.bind("<ButtonPress-1>",start_move)
Top_bar.bind("<ButtonRelease-1>",stop_move)
Top_bar.bind("<B1-Motion>",on_move)
X_button.bind("<Enter>", on_enter4)
X_button.bind("<Leave>", on_leave4)
min_button.bind("<Enter>", on_enter5)
min_button.bind("<Leave>", on_leave5)
app1.bind("<ButtonPress-1>",start_move)
app1.bind("<ButtonRelease-1>",stop_move)
app1.bind("<B1-Motion>",on_move)

Op_System.bind("<ButtonPress-1>",start_move)
Op_System.bind("<ButtonRelease-1>",stop_move)
Op_System.bind("<B1-Motion>",on_move)

Op_System_entry.bind("<ButtonPress-1>",start_move)
Op_System_entry.bind("<ButtonRelease-1>",stop_move)
Op_System_entry.bind("<B1-Motion>",on_move)

Computer.bind("<ButtonPress-1>",start_move)
Computer.bind("<ButtonRelease-1>",stop_move)
Computer.bind("<B1-Motion>",on_move)

Computer_entry.bind("<ButtonPress-1>",start_move)
Computer_entry.bind("<ButtonRelease-1>",stop_move)
Computer_entry.bind("<B1-Motion>",on_move)

##############################CONTENT_FRAME####################################
Content_frame= tk.LabelFrame(root,width=900,height=700,bd=0,bg="#1e1e1e")
Content_frame.grid_propagate(False)
Content_frame.grid(row=1,column=1)
Nombre_app1=tk.Label(Content_frame, text="TLATLACAANA",bg="#1e1e1e",
                    foreground="#3179cb")
Nombre_app1['font']=font.Font(family="Consolas",size=40)
Nombre_app2=tk.Label(Content_frame, text="ApPlIcAtIoN",bg="#1e1e1e",
                    foreground="#3179cb")
Nombre_app2['font']=font.Font(family="Consolas",size=10)
label1=tk.Label(Content_frame,bg="#1e1e1e",foreground="#d1d1d1",
                text="“Software focused on the recognition phase of a "+ 
                "computer security audit”")
label1['font']=font.Font(family="Consolas",size=15)
label2=tk.Label(Content_frame,bg="#1e1e1e",foreground="#3179cb",
                         text="Coded by:")
label2['font']=font.Font(family="Consolas",size=15)
label3=tk.Label(Content_frame,bg="#1e1e1e",foreground="#d1d1d1",
                         text="Roberto (Tank3) Cruz Lozano.")
label3['font']=font.Font(family="Consolas",size=15)
label4=tk.Label(Content_frame,bg="#1e1e1e",foreground="#d1d1d1",
                         text="Ernesto Adán (Neto844) Zurbía Flores Vivero.")
label4['font']=font.Font(family="Consolas",size=15)
label5=tk.Label(Content_frame,bg="#1e1e1e",foreground="#3179cb",
                         text="Summary:")
label5['font']=font.Font(family="Consolas",size=15)
Summary=tk.Text(Content_frame,height=12,width=61,bg="#1e1e1e",
                 relief="flat",foreground="#d1d1d1")
Summary['font']=font.Font(family="Consolas",size=15)
version=tk.Label(Content_frame,bg="#1e1e1e",foreground="#d1d1d1",
                         text="v1.0.0")
version['font']=font.Font(family="Consolas",size=15)
Nombre_app1.grid(row=0,column=0)
Nombre_app2.grid(row=0,column=0, sticky="SE",padx=190)
label1.grid(row=1,column=0,padx=10,pady=20)
label2.grid(row=2,column=0,padx=100,sticky="W")
label3.grid(row=3,column=0,padx=130,sticky="W",pady=20)
label4.grid(row=4,column=0,padx=130,sticky="W")
label5.grid(row=5,column=0,padx=100,sticky="W",pady=20)
version.grid(row=7,column=1,sticky="W",pady=20)
Summary.grid(row=6,column=0,sticky="E")
Summary.insert(tk.INSERT,"The project presented here seeks to be a friendly"+
              "tool with \nthe trained user, capable of doing IP and port"+
              " recognition. \nIn the recognition phase of a computer "+
              "security audit, we \nfind very useful and powerful tools, "+
              "but not very friendly, \nthat is why our project focuses on "+
              "bringing a useful and \neasy-to-use tool kit for the user as "+
              "well as having an \ninterface in which all the tools and "+
              "information obtained \nwill be displayed.")
Summary.config(state="disabled")

root.mainloop()