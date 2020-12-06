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
##We ensure that the user has the tkinder module install
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

def minimizewindow():
    root.withdraw()
    root.overrideredirect(False)
    root.iconify()

def on_deiconify(event):
    root.deiconify()
    root.overrideredirect(True)

def ClickMenu(number):

    if number=="1":
        Menu.Option1.self.config(bg="#094771")
        Menu.Option2.self.config(bg="#252526")
        Menu.Option3.self.config(bg="#252526")
        Menu.Option4.self.config(bg="#252526")
        for widget in Frame.frame.winfo_children():
            widget.destroy()
        Frame.Ipscanner()
    elif number=="2":
        Menu.Option1.self.config(bg="#252526")
        Menu.Option2.self.config(bg="#094771")
        Menu.Option3.self.config(bg="#252526")
        Menu.Option4.self.config(bg="#252526")
        for widget in Frame.frame.winfo_children():
            widget.destroy()
        Frame.Iprange()

    elif number=="3":
        Menu.Option1.self.config(bg="#252526")
        Menu.Option2.self.config(bg="#252526")
        Menu.Option3.self.config(bg="#094771")
        Menu.Option4.self.config(bg="#252526")
        for widget in Frame.frame.winfo_children():
            widget.destroy()
        Frame.Portfinder()

    elif number=="4":
        Menu.Option1.self.config(bg="#252526")
        Menu.Option2.self.config(bg="#252526")
        Menu.Option3.self.config(bg="#252526")
        Menu.Option4.self.config(bg="#094771")
        for widget in Frame.frame.winfo_children():
            widget.destroy()
        Frame.Getbanner()

    elif number=="5":
        Menu.Option1.self.config(bg="#252526")
        Menu.Option2.self.config(bg="#252526")
        Menu.Option3.self.config(bg="#252526")
        Menu.Option4.self.config(bg="#252526")
        for widget in Frame.frame.winfo_children():
            widget.destroy()
        Frame.show()
    elif number=="6":
        Menu.Result.self.config(state="normal")
        Menu.Result.self.delete('1.0',tk.END)
        Menu.Result.self.insert(tk.INSERT,pc.dns_to_ip(Menu.DNS_Entry.self.get()))
        Menu.Result.self.config(state="disabled")
    elif number=="7":
        Frame.Result.self.config(state="normal")
        Frame.Result.self.delete('1.0',tk.END)
        Ping=pc.test_connection(Frame.IpEntry.self.get())
        if Ping==True:
            Frame.Result.self.insert(tk.INSERT,"The ip address has"+
                " responded successfully")
            Frame.Result.self.config(state="disabled")
        elif Ping==False:
            Frame.Result.self.insert(tk.INSERT,"The ip address did not"+
                " respond, try another ip \naddress")
            Frame.Result.self.config(state="disabled")

    elif number=="8":
        Frame.Result.self.config(state="normal")
        Ping=pc.trace_connection(Frame.IpEntry.self.get())
        Frame.Result.self.delete('1.0',tk.END)
        Frame.Result.self.insert(tk.INSERT,Ping)
        Frame.Result.self.config(state="disabled")
    
    elif number=="9":
        Frame.Result.self.config(state="normal")
        Frame.Result.self.delete('1.0',tk.END)
        range_ip = pc.inquire_ip(Frame.MinEntry.self.get(),Frame.MaxEntry.self.get())
        Frame.Result.self.insert(tk.INSERT,("<<IP scan result>>\n"))
        for x, y in range_ip.items():
            outcome = "IP: "+str(x)+" Outcome: "+str(y)+"\n"
            Frame.Result.self.insert(tk.INSERT,(outcome))
        Frame.Result.self.config(state="disabled")

    elif number=="10":
        Frame.Result.self.config(state="normal")
        Frame.Result.self.delete('1.0',tk.END)
        dic_port = pc.port_finder(Frame.IpEntry.self.get(), int(Frame.MinEntry.self.get()), int(Frame.MaxEntry.self.get()))
        Frame.Result.self.insert(tk.INSERT,("<<<Scan Port Result>>>\n"))
        for x, y in dic_port.items():
            outcome = "Port: "+str(x)+" Outcome: "+str(y)+"\n"
            Frame.Result.self.insert(tk.INSERT,(outcome))
        Frame.Result.self.config(state="disabled")

    elif number=="11":
        Frame.Result.self.config(state="normal")
        Frame.Result.self.insert(tk.INSERT,(pc.get_banner(Frame.IpEntry.self.get(), int(Frame.BannerEntry.self.get()))))
        Frame.Result.self.config(state="disabled")

class Button():
    def __init__(self,place,text,row,column,columnspan,sticky="n",padx=0,pady=0):
        self.place=place
        self.text=text
        self.row=row
        self.column=column
        self.columnspan=columnspan
        self.sticky=sticky
        self.padx=padx
        self.pady=pady
    def menu(self):
        self.self=tk.Button(self.place,text=self.text, bd=0,foreground="#d1d1d1", 
                  bg="#252526",cursor="hand2",activebackground="#373742",
                  activeforeground="#d1d1d1",width=17,height=2)
        self.self['font']=font.Font(family="Consolas",size=25)
        self.self.grid(row=self.row,column=self.column,columnspan=self.columnspan)
    def funcionality(self):
        self.self=tk.Button(self.place,text=self.text, bd=0,foreground="#d1d1d1", 
                  bg="#37373d",cursor="hand2",activebackground="#373742",
                  activeforeground="#d1d1d1",width=10)
        self.self['font']=font.Font(family="Consolas",size=10)
        self.self.grid(row=self.row,column=self.column,columnspan=self.columnspan,sticky=self.sticky,padx=self.padx,pady=self.pady)
    def topbar(self,color):
        self.color=color
        self.self=tk.Button(self.place,bg="#333333", text=self.text, foreground="#d1d1d1"
                ,height=1,width=5,relief="flat",activebackground=self.color,
                bd=0,activeforeground="#fff")
        self.self['font']=font.Font(family="Consolas",size=15)
        self.self.grid(row=self.row,column=self.column,columnspan=self.columnspan,sticky=self.sticky,padx=self.padx)

class Label():

    def __init__(self,place,text,bg,foreground,height,size,row,column,columnspan,sticky="n",padx=0,pady=0):
        self.place=place
        self.text=text
        self.bg=bg
        self.foreground=foreground
        self.height=height
        self.size=size
        self.row=row
        self.column=column
        self.columnspan=columnspan
        self.sticky=sticky
        self.padx=padx
        self.pady=pady
        self.self=tk.Label(self.place,bg=self.bg,foreground=self.foreground,
                         text=self.text,height=self.height)
        self.self['font']=font.Font(family="Consolas",size=self.size)
        self.self.grid(row=self.row,column=self.column,columnspan=self.columnspan,sticky=self.sticky,padx=self.padx,pady=self.pady)

class Entry():
    def __init__(self,place,bg,width,size,row,column,columnspan,sticky="n",padx=0):
        self.place=place
        self.bg=bg
        self.width=width
        self.size=size
        self.row=row
        self.column=column
        self.columnspan=columnspan
        self.sticky=sticky
        self.padx=padx
        self.self=tk.Entry(self.place,bg=self.bg, relief="flat",
                          insertbackground="#fff",selectbackground="#0764d4"
                          ,width=self.width,foreground="#d1d1d1")
        self.self['font']=font.Font(family="Consolas",size=self.size)
        self.self.grid(row=self.row,column=self.column,columnspan=self.columnspan,sticky=self.sticky,padx=self.padx)

class Text():
    def __init__(self,place,height,width,bg,size,row,column,columnspan,sticky="n",padx=0):
        self.place=place
        self.bg=bg
        self.width=width
        self.height=height
        self.size=size
        self.row=row
        self.column=column
        self.columnspan=columnspan
        self.sticky=sticky
        self.padx=padx
        self.self=tk.Text(self.place,height=self.height,width=self.width,bg=self.bg,
                            relief="flat",foreground="#d1d1d1")
        self.self['font']=font.Font(family="Consolas",size=self.size)
        self.self.grid(row=self.row,column=self.column,columnspan=self.columnspan,sticky=self.sticky,padx=self.padx)
        self.self.config(state="disabled")

class ResultBox():
    def __init__(self,place,size,row,column,columnspan,sticky="n",padx=0):
        self.place=place
        self.size=size
        self.row=row
        self.column=column
        self.columnspan=columnspan
        self.sticky=sticky
        self.padx=padx
        self.self=scrolledtext.ScrolledText(self.place,height=20,width=80,bg="#121212",
                            relief="flat",foreground="#d1d1d1")
        self.self['font']=font.Font(family="Consolas",size=self.size)
        self.self.grid(row=self.row,column=self.column,columnspan=self.columnspan,sticky=self.sticky,padx=self.padx)
        self.self.config(state="disabled")


class menu():
    def __init__(self,place):
        self.place=place
    def show(self,DNS_Entry=None,Result=None,Option1=None,Option2=None,Option3=None,Option4=None):
        self.DNS_Entry=DNS_Entry
        self.Result=Result
        self.Option1=Option1
        self.Option2=Option2
        self.Option3=Option3
        self.Option4=Option4
        Menu= tk.LabelFrame(self.place,bg="#252526",
                width=300,height=700,bd=0)
        Menu.grid(row=1,column=0,sticky="nw")
        Menu.grid_propagate(False)
        self.Option1=Button(Menu,"Ip Scanner",0,0,2)
        self.Option1.menu()
        self.Option1.self.config(command=lambda:ClickMenu("1"))
        self.Option2=Button(Menu,"IP Range",1,0,2)
        self.Option2.menu()
        self.Option2.self.config(command=lambda:ClickMenu("2"))
        self.Option3=Button(Menu,"Port Finder",2,0,2)
        self.Option3.menu()
        self.Option3.self.config(command=lambda:ClickMenu("3"))
        self.Option4=Button(Menu,"Get Banner",3,0,2)
        self.Option4.menu()
        self.Option4.self.config(command=lambda:ClickMenu("4"))
        Label(Menu,"","#252526","#ffffff",4,0,4,0,2)
        Label(Menu,"DNS Converter","#252526","#3179cb",0,15,5,0,2)
        Label(Menu,"Enter a domain name:","#252526","#d1d1d1",0,10,6,0,1,"w")
        self.DNS_Entry=Entry(Menu,"#121212",18,10,6,1,1,"w")
        IpButton=Button(Menu,"Get IP",7,1,1,"e",20,10)
        IpButton.funcionality()
        IpButton.self.config(command=lambda:ClickMenu("6"))
        Label(Menu,"Ip Obtained:","#252526","#d1d1d1",0,10,8,0,1,"e",25)
        self.Result=Text(Menu,1,18,"#121212",10,8,1,1,"w")

class TopBar():
    def __init__(self,place):
        self.place=place
    def show(self,computer=None,opsystem=None):
        self.computer=computer
        self.opsystem=opsystem
        Topbar= tk.LabelFrame(self.place,bg="#333333",
                width=1200,height=40,bd=0)
        Topbar.grid(row=0,column=0, columnspan=2)
        Topbar.columnconfigure(0,minsize=300)
        Topbar.columnconfigure(1,minsize=900)
        Topbar.grid_propagate(False)
        close=Button(Topbar,"X",0,1,1,"e")
        close.topbar("#f1707a")
        close.self.config(command=lambda: root.destroy())
        minimize=Button(Topbar,"-",0,1,1,"e",60)
        minimize.topbar("#ddd")
        minimize.self.config(command=lambda:minimizewindow())
        app=Button(Topbar,"TLATLACAANA",0,0,1,"wn",0,3)
        app.topbar("#333333")
        app.self.config(command=lambda:ClickMenu("5"))
        app.self.config(width=0)
        Label(Topbar,"Current OP System: ","#333333","#d1d1d1",0,10,0,1,1,"w")
        Label(Topbar,"Computer Name:","#333333","#d1d1d1",0,10,0,1,1,"n",0,7)
        self.computer=Text(Topbar,1,24,"#333333",10,0,1,1,"w",133)
        self.opsystem=Text(Topbar,1,24,"#333333",10,0,1,1,"e",200)
        Topbar.bind("<ButtonPress-1>",start_move)
        Topbar.bind("<ButtonRelease-1>",stop_move)
        Topbar.bind("<B1-Motion>",on_move)
        for widget in Topbar.winfo_children():
            widget.bind("<ButtonPress-1>",start_move)
            widget.bind("<ButtonRelease-1>",stop_move)
            widget.bind("<B1-Motion>",on_move)

class Content():
    def __init__(self,place,frame=None):
        self.place=place
        self.frame=frame
        self.frame=tk.LabelFrame(self.place,bg="#1e1e1e",
                width=900,height=700,bd=0)
    def show(self):
        self.frame.grid_propagate(False)
        self.frame.grid(row=1,column=1,sticky="nw")
        Label(self.frame,"TLATLACAANA","#1e1e1e","#3179cb",0,40,0,0,1,"w",150,0)
        Label(self.frame,"ApPlIcAtIoN","#1e1e1e","#3179cb",0,10,0,0,1,"SE",400)
        Label(self.frame,"“Software focused on the recognition phase of a "+ 
                "computer security audit”","#1e1e1e","#d1d1d1",0,15,1,0,1,"n",10,20)
        Label(self.frame,"Coded by:","#1e1e1e","#3179cb",0,15,2,0,1,"w",100)
        Label(self.frame,"Roberto (Tank3) Cruz Lozano","#1e1e1e","#d1d1d1",0,15,3,0,1,"w",130,20)
        Label(self.frame,"Ernesto Adán (Neto844) Zurbía Flores Vivero.","#1e1e1e","#d1d1d1",0,15,4,0,1,"w",130)
        Label(self.frame,"Summary:","#1e1e1e","#3179cb",0,15,5,0,1,"w",100,20)
        Summary=Text(self.frame,12,61,"#1e1e1e",15,6,0,1,"E")
        Summary.self.config(state="normal")
        Summary.self.insert(tk.INSERT,"The project presented here seeks to be a friendly"+
              "tool with \nthe trained user, capable of doing IP and port"+
              " recognition. \nIn the recognition phase of a computer "+
              "security audit, we \nfind very useful and powerful tools, "+
              "but not very friendly, \nthat is why our project focuses on "+
              "bringing a useful and \neasy-to-use tool kit for the user as "+
              "well as having an \ninterface in which all the tools and "+
              "information obtained \nwill be displayed.")
        Summary.self.config(state="disabled")
    def Ipscanner(self,IpEntry=None,Result=None):
        self.IpEntry=IpEntry
        self.Result=Result
        Label(self.frame,"IP_SCANNER  ","#1e1e1e","#3179cb",0,40,0,0,1)
        Label(self.frame,"","#1e1e1e","#1e1e1e",0,40,1,0,1)
        Label(self.frame,"Enter an ip address:","#1e1e1e","#d1d1d1",0,15,2,0,1,"e")
        self.IpEntry=Entry(self.frame,"#121212",20,15,2,1,3,"e",50)
        Button1=Button(self.frame,"Trace Route",3,3,1,"w",10,10)
        Button1.funcionality()
        Button1.self.config(command=lambda:ClickMenu("8"))
        Button2=Button(self.frame,"Ping",3,2,1,"e",5,10)
        Button2.funcionality()
        Button2.self.config(command=lambda:ClickMenu("7"))
        self.Result=ResultBox(self.frame,10,5,0,4,"e",75)
        Label(self.frame,"v1.0.0","#1e1e1e","#d1d1d1",0,15,6,5,1,"n",76,13)
        Label(self.frame,"","#1e1e1e","#1e1e1e",4,0,4,1,1)
        Button3=Button(self.frame,"Save",6,3,1,"w")
        Button3.funcionality()
    def Iprange(self,MinEntry=None,MaxEntry=None,Result=None):
        self.MinEntry=MinEntry
        self.MaxEntry=MaxEntry
        self.Result=Result
        Label(self.frame,"IP_RANGE     ","#1e1e1e","#3179cb",0,40,0,0,1)
        Label(self.frame,"","#1e1e1e","#1e1e1e",2,0,1,0,1)
        Label(self.frame,"Enter a minimum IP address:","#1e1e1e","#d1d1d1",0,15,2,0,1,"e",0,10)
        Label(self.frame,"Enter a maximum IP address:","#1e1e1e","#d1d1d1",0,15,3,0,1,"e")
        self.MinEntry=Entry(self.frame,"#121212",20,15,2,1,3,"e",50)
        self.MaxEntry=Entry(self.frame,"#121212",20,15,3,1,3,"e",50)
        Button1=Button(self.frame,"Ping",4,3,1,"e",50,10)
        Button1.funcionality()
        Button1.self.config(command=lambda:ClickMenu("9"))
        Label(self.frame,"","#1e1e1e","#1e1e1e",2,0,5,1,1)
        self.Result=ResultBox(self.frame,10,6,0,4,"e",75)
        Label(self.frame,"v1.0.0","#1e1e1e","#d1d1d1",0,15,7,5,1,"n",76,13)
        Button2=Button(self.frame,"Save",7,3,1,"e",70)
        Button2.funcionality()
    def Portfinder(self,IpEntry=None,MinEntry=None,MaxEntry=None,Result=None):
        self.IpEntry=IpEntry
        self.MinEntry=MinEntry
        self.MaxEntry=MaxEntry
        self.Result=Result
        Label(self.frame,"PORT FINDER  ","#1e1e1e","#3179cb",0,40,0,0,1)
        Label(self.frame,"","#1e1e1e","#1e1e1e",2,0,1,0,1)
        Label(self.frame,"Enter an ip address:","#1e1e1e","#d1d1d1",0,15,2,0,1,"e")
        Label(self.frame,"Enter a minium port:","#1e1e1e","#d1d1d1",0,15,3,0,1,"e",0,10)
        Label(self.frame,"Enter a maximum port:","#1e1e1e","#d1d1d1",0,15,4,0,1,"e")
        self.IpEntry=Entry(self.frame,"#121212",20,15,2,1,3,"e",50)
        self.MinEntry=Entry(self.frame,"#121212",20,15,3,1,3,"e",50)
        self.MaxEntry=Entry(self.frame,"#121212",20,15,4,1,3,"e",50)
        Button1=Button(self.frame,"Get Ports",5,3,1,"e",50,10)
        Button1.funcionality()
        Button1.self.config(command=lambda:ClickMenu("10"))
        Label(self.frame,"","#1e1e1e","#1e1e1e",1,0,6,1,1)
        self.Result=ResultBox(self.frame,10,7,0,4,"e",75)
        Label(self.frame,"v1.0.0","#1e1e1e","#d1d1d1",0,15,8,5,1,"n",76,13)
        Button2=Button(self.frame,"Save",8,3,1,"e",70)
        Button2.funcionality()
    def Getbanner(self,IpEntry=None,BannerEntry=None,Result=None):
        self.IpEntry=IpEntry
        self.BannerEntry=BannerEntry
        self.Result=Result
        Label(self.frame,"Get Banner  ","#1e1e1e","#3179cb",0,40,0,0,1)
        Label(self.frame,"","#1e1e1e","#1e1e1e",2,0,1,0,1)
        Label(self.frame,"Enter an ip address:","#1e1e1e","#d1d1d1",0,15,2,0,1,"e",0,10)
        Label(self.frame,"Get the banner of port:","#1e1e1e","#d1d1d1",0,15,3,0,1,"e")
        self.IpEntry=Entry(self.frame,"#121212",20,15,2,1,3,"e",50)
        self.BannerEntry=Entry(self.frame,"#121212",20,15,3,1,3,"e",50)
        Button1=Button(self.frame,"Get Banner",4,3,1,"e",50,10)
        Button1.funcionality()
        Button1.self.config(command=lambda:ClickMenu("11"))
        Label(self.frame,"","#1e1e1e","#1e1e1e",2,0,5,1,1)
        self.Result=ResultBox(self.frame,10,6,0,4,"e",75)
        Label(self.frame,"v1.0.0","#1e1e1e","#d1d1d1",0,15,7,5,1,"n",76,13)
        Button2=Button(self.frame,"Save",7,3,1,"e",70)
        Button2.funcionality()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x700")
    root.resizable(0,0)
    Topbar=TopBar(root)
    Topbar.show()
    Menu=menu(root)
    Menu.show()
    Frame=Content(root)
    Frame.show()
    root.bind("<Map>", on_deiconify)
    root.overrideredirect(True)
    root.mainloop()
