
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
    except ImportError:
        raise ImportError("Se requiere el modulo Tkinter")
else:
    try:
        import tkinter as tk
    except ImportError:
        raise ImportError("Se requiere el modulo tkinter")
##We ensure that the user has the tkinder module installed

def on_enter(e):
    Option_1['background'] = '#37373d'

def on_leave(e):
    Option_1['background'] = '#252526'
    
def on_enter1(e):
    Option_2['background'] = '#37373d'

def on_leave1(e):
    Option_2['background'] = '#252526'

def on_enter2(e):
    Option_3['background'] = '#37373d'

def on_leave2(e):
    Option_3['background'] = '#252526'

def on_enter3(e):
    Option_4['background'] = '#37373d'

def on_leave3(e):
    Option_4['background'] = '#252526'

def on_enter4(e):
    Option_5['background'] = '#37373d'

def on_leave4(e):
    Option_5['background'] = '#252526'



def ClickButton():
    pruebaLabel=tk.Label(root,text="AAA you click me :)")
    pruebaLabel.grid(row=1, column=0)

 

root = tk.Tk() ##Create the window
root.title("Beta Aplication") ## Title of the window
root.geometry("1200x700")
root.configure(bg='#1e1e1e')    
root.resizable(0,0)

##################################MENU#########################################

Menu= tk.LabelFrame(root,bg="#252526",
                    width=300,height=700,bd=0)
Menu.grid(row=1,column=0,sticky="nw")
Menu.grid_propagate(False)

Option_1= tk.Button(Menu,text="OPTION 1", bg="#252526", bd=0, height=3, 
                  width=10, anchor="w",command= ClickButton)
photo_option_1 = tk.PhotoImage(file = r"tesla_cybertruck.png") 
photo_option_1 = photo_option_1.subsample(4,4) 
Option_1.config(image=photo_option_1, width=300,height=100, compound="left")
Option_2= tk.Button(Menu,text="OPTION 2", bg="#252526", bd=0, height=3, 
                  width=10, anchor="w",command=ClickButton)
photo_option_2 = tk.PhotoImage(file = r"tesla_cybertruck.png") 
photo_option_2 = photo_option_2.subsample(4,4) 
Option_2.config(image=photo_option_2, width=300,height=100, compound="left")
Option_3= tk.Button(Menu,text="OPTION 3", bg="#252526", bd=0, height=3, 
                  width=10, anchor="w",command=ClickButton)
photo_option_3 = tk.PhotoImage(file = r"tesla_cybertruck.png") 
photo_option_3 = photo_option_3.subsample(4,4) 
Option_3.config(image=photo_option_3, width=300,height=100, compound="left")
Option_4= tk.Button(Menu,text="OPTION 4", bg="#252526", bd=0, height=3, 
                  width=10, anchor="w",command=ClickButton)
photo_option_4 = tk.PhotoImage(file = r"tesla_cybertruck.png") 
photo_option_4 = photo_option_4.subsample(4,4) 
Option_4.config(image=photo_option_4, width=300,height=100, compound="left")
Option_5= tk.Button(Menu,text="OPTION 5", bg="#252526", bd=0, height=3, 
                  width=10, anchor="w",command=ClickButton)
photo_option_5 = tk.PhotoImage(file = r"tesla_cybertruck.png") 
photo_option_5 = photo_option_5.subsample(4,4) 
Option_5.config(image=photo_option_5, width=300,height=100, compound="left")

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
                    width=1200,height=35,bd=0)
Top_bar.grid(row=0,column=0)

root.mainloop()

