
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

PYTHON_VERSION = sys.version_info.major ##Identify the installed python version

if PYTHON_VERSION < 3:
    try:
        import Tkinter as tk
        import Tkinter.scrolledtext as scrolledtext
        import Tkinter.font as font

    except ImportError:
        raise ImportError("Se requiere el modulo Tkinter")
else:
    try:
        import tkinter as tk
        import tkinter.scrolledtext as scrolledtext
        import tkinter.font as font
    except ImportError:
        raise ImportError("Se requiere el modulo tkinter")
##We ensure that the user has the tkinder module installed

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
    if Option_4['background']=='#094771':
        return
    else:
        Option_4['background'] = '#37373d'

def on_leave3(e):
    if Option_4['background']=='#094771':
        return
    else:
        Option_4['background'] = '#252526'

def on_enter4(e):
    if Option_5['background']=='#094771':
        return
    else:
        Option_5['background'] = '#37373d'

def on_leave4(e):
    if Option_5['background']=='#094771':
        return
    else:
        Option_5['background'] = '#252526'

def on_enter5(e):
    if Option_5['background']=='#094771':
        return
    else:
        Option_5['background'] = '#37373d'

def on_leave5(e):
    if Option_5['background']=='#094771':
        return
    else:
        Option_5['background'] = '#252526'



def ClickButton(number):
    if number=="1":
        Option_1.config(bg="#094771")
        Option_2.config(bg="#252526")
        Option_3.config(bg="#252526")
        Option_4.config(bg="#252526")
        Option_5.config(bg="#252526")
        Name_option=tk.Label(Content_frame, text="IP_SCANNER  ",bg="#1e1e1e",
                    foreground="#d1d1d1",padx=30,pady=10)
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
        Ip_button=tk.Button(Content_frame,bg="#37373d",text="SCAN",
                            foreground="#d1d1d1",width=10,relief="flat")
        Ip_button['font']=font.Font(family="Consolas",size=10)
        space_2=tk.Label(Content_frame,height=5,bg="#1e1e1e")
        ResultBox=tk.Text(Content_frame,height=12,width=44,bg="#121212",
                            relief="flat",foreground="#d1d1d1")
        ResultBox['font']=font.Font(family="Consolas",size=15)
        Ip_label.grid(row=2,column=0,sticky="E")
        space_1.grid(row=1,column=0)
        Name_option.grid(row=0,column=0)
        Ip_entry.grid(row=2,column=1,sticky="E",padx=50)
        Ip_button.grid(row=3,column=1,pady=10,sticky="e",padx=50)
        ResultBox.grid(row=5,column=0,columnspan=2,sticky="e", padx=55)
        space_2.grid(row=4,column=1)

    elif number=="2":
         Option_2.config(bg="#094771")
         Option_1.config(bg="#252526")
         Option_3.config(bg="#252526")
         Option_4.config(bg="#252526")
         Option_5.config(bg="#252526")
    elif number=="3":
         Option_3.config(bg="#094771")
         Option_1.config(bg="#252526")
         Option_2.config(bg="#252526")
         Option_4.config(bg="#252526")
         Option_5.config(bg="#252526")
    elif number=="4":
         Option_4.config(bg="#094771")
         Option_1.config(bg="#252526")
         Option_2.config(bg="#252526")
         Option_3.config(bg="#252526")
         Option_5.config(bg="#252526")
    elif number=="5":
         Option_5.config(bg="#094771")
         Option_1.config(bg="#252526")
         Option_2.config(bg="#252526")
         Option_3.config(bg="#252526")
         Option_4.config(bg="#252526")
    else:
        return

 

root = tk.Tk() ##Create the window
root.title("Beta Aplication") ## Title of the window
root.geometry("1200x700")
root.resizable(0,0)

##################################MENU#########################################

Menu= tk.LabelFrame(root,bg="#252526",
                    width=300,height=700,bd=0)
Menu.grid(row=1,column=0,sticky="nw")
Menu.grid_propagate(False)

Option_1= tk.Button(Menu,text=" IP SCANER  ", bd=0, height=3, 
                  width=10,command=lambda :ClickButton("1"))
photo_option_1 = tk.PhotoImage(file = r"Scan.png") 
photo_option_1 = photo_option_1.subsample(8,6) 
Option_1.config(image=photo_option_1, width=300,height=100, compound="left")
Option_1['font']=font.Font(family="Consolas",size=25)

Option_2= tk.Button(Menu,text="OPTION 2", bd=0, height=3, 
                  width=10, anchor="w",command=lambda :ClickButton("2"))
photo_option_2 = tk.PhotoImage(file = r"tesla_cybertruck.png") 
photo_option_2 = photo_option_2.subsample(4,4) 
Option_2.config(image=photo_option_2, width=300,height=100, compound="left")
Option_3= tk.Button(Menu,text="OPTION 3", bd=0, height=3, 
                  width=10, anchor="w",command=lambda :ClickButton("3"))
photo_option_3 = tk.PhotoImage(file = r"tesla_cybertruck.png") 
photo_option_3 = photo_option_3.subsample(4,4) 
Option_3.config(image=photo_option_3, width=300,height=100, compound="left")
Option_4= tk.Button(Menu,text="OPTION 4", bd=0, height=3, 
                  width=10, anchor="w",command=lambda :ClickButton("4"))
photo_option_4 = tk.PhotoImage(file = r"tesla_cybertruck.png") 
photo_option_4 = photo_option_4.subsample(4,4) 
Option_4.config(image=photo_option_4, width=300,height=100, compound="left")
Option_5= tk.Button(Menu,text="OPTION 5", bd=0, height=3, 
                  width=10, anchor="w",command=lambda :ClickButton("5"))
photo_option_5 = tk.PhotoImage(file = r"tesla_cybertruck.png") 
photo_option_5 = photo_option_5.subsample(4,4) 
Option_5.config(image=photo_option_5, width=300,height=100, compound="left")

for widget in Menu.winfo_children():
    widget.config(foreground="#d1d1d1", bg="#252526",cursor="hand2",
                  activebackground="#373742")


Option_1.grid(row=0)
Option_2.grid(row=1)
Option_3.grid(row=2)
Option_4.grid(row=3)
Option_5.grid(row=4)

Option_1.bind("<Enter>", on_enter)
Option_1.bind("<Leave>", on_leave)
Option_2.bind("<Enter>", on_enter1)
Option_2.bind("<Leave>", on_leave1)
Option_3.bind("<Enter>", on_enter2)
Option_3.bind("<Leave>", on_leave2)
Option_4.bind("<Enter>", on_enter3)
Option_4.bind("<Leave>", on_leave3)
Option_5.bind("<Enter>", on_enter4)
Option_5.bind("<Leave>", on_leave4)

##################################TOP_BAR######################################
Top_bar= tk.LabelFrame(root,bg="#333333",
                    width=1200,height=40,bd=0)
Top_bar.grid(row=0,column=0, columnspan=2)
Top_bar.grid_propagate(False)

##############################CONTENT_FRAME####################################
Content_frame= tk.LabelFrame(root,width=900,height=700,bd=0,bg="#1e1e1e")
Content_frame.grid_propagate(False)
Content_frame.grid(row=1,column=1)
Nombre_app=tk.Label(Content_frame, text="IP_SCANNER",bg="#1e1e1e",
                    foreground="#d1d1d1",padx=30,pady=10)
Nombre_app.grid_propagate(False)
Nombre_app['font']=font.Font(family="Consolas",size=40)


root.mainloop()

root.mainloop()

