#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MyComputer Project
Coursework for: 5020B Programming for non-specialists

Includes a GUI for Task 9. 

Has a inital window which greets the user and tells them how many computers 
there are in lab. "Basic" button which when it is clicked gives user 
information about what computer IDs are basic. Similarily, for "Advanced" and 
"game" buttons. Further two buttons are presented which one gives a table of 
the computers in the lab and relevent information about computers. The other
button gives a table of computers and their installed software.

@author: Shannon Jones 
@date:   21/03/2022

"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import a7_cmplab as a7
import a3_component as a3
import a4_advanced as a4

def GUI():
    myLab = a7.CMPLab("myLab")
    myLab.fromFile('myLab.txt')
    
    cmp = list(myLab.dicIDs.values())  # List of computers in myLab
    
    sList = [ a3.Software("Python", 2, 32, 4, 2, 0), 
                 a3.Software("Paint", 1.2, 16, 2, 5, 0),
                 a3.Software("Adobe_Photoshop", 3, 64, 8, 15, 1),
                 a3.Software("Blender", 0.5, 32, 8, 20, 1),
                 a3.Software("Minecraft", 0.9, 32, 8, 30, 1)]
    
    # Installs list of software to all computers (if it can)
    # This is for GUI list of software option
    for i in cmp:
        for j in sList:
            i.install(j)
    
    
    # When basic button is clicked, shows IDs of computers which are basic
    # and gives further buttons to click on
    def basicID():
        basic = myLab.getComputers('basic')
        labelIDcmp[
            "text"] = f"Computers {basic} are basic computers. \n For more options click one of the following: "
        
        # unpacks computer and software info buttons
        getInfo.pack()
        btn_softInfo.pack()
    
    # When advance button is clicked, shows IDs of computers which are advacned
    # and gives further buttons to click on
    def advancedID():
        advanced = myLab.getComputers('advanced')
        labelIDcmp[
            "text"] = f"Computers {advanced} are advanced computers. \n For more options click one of the following: "
        
        # unpacks computer and software info buttons
        getInfo.pack()
        btn_softInfo.pack()
    
    # When gaming button is clicked, shows IDs of computers which are gaming
    # and gives further buttons to click on
    def gameID():
        game = myLab.getComputers('game')
        labelIDcmp[
            "text"] = f"Computers {game} are gaming computers. \n  For more options click one of the following: "
        
        # unpacks computer and software info buttons
        getInfo.pack()
        btn_softInfo.pack()
        
        
    

    # When 'Computer Information' is clicked opens a new window with table
    def openNewWindowGetInfo():
        
        #Removes button after clicking
        getInfo.pack_forget() 
        btn_softInfo.pack_forget()
        
        dic=myLab.computerInfo()  # Calls method to get computer info from a7_CMPLab
        
        cmpValues =list(dic.values())  #Sets to list
        
        cmp0,cmp1,cmp2,cmp3,cmp4,cmp5,cmp6,cmp7,cmp8,cmp9 = [],[],[],[],[],[],[],[],[],[]
        
        for j in range(len(cmpValues)):   # Sets up data for table correctly
            cmp0.append(cmpValues[j][0])
            cmp1.append(cmpValues[j][1])
            cmp2.append(cmpValues[j][2])
            cmp3.append(cmpValues[j][3])
            cmp4.append(cmpValues[j][4])
            cmp5.append(cmpValues[j][5])
            cmp6.append(cmpValues[j][6])
            cmp7.append(cmpValues[j][7])
            cmp8.append(cmpValues[j][8])
            cmp9.append(cmpValues[j][9])
       
        # From https://www.delftstack.com/howto/python-tkinter/tkinter-table/
        # Author - Unknown
        
        # Table class
        class Table:
            # Initialize a constructor
            def __init__(self, gui):
        
                # An approach for creating the table
                for i in range(total_rows):
                    for j in range(total_columns):
                        if i ==0:
                            self.entry = Entry(gui, width=20, bg='LightSteelBlue',fg='Black',
                                               font=('Arial', 11, 'bold'))
                        else:
                            self.entry = Entry(gui, width=20, fg='blue',
                                       font=('Arial', 11, ''))
        
                        self.entry.grid(row=i, column=j)
                        self.entry.insert(END, computer_data[i][j])
        
        
        # take the data
        computer_data = [list(dic.keys()), 
            cmp0, cmp1, cmp2, cmp3, cmp4, cmp5, cmp6, cmp7, cmp8, cmp9]
              
        # find total number of rows and
        # columns in list
        total_rows = len(computer_data)
        total_columns = len(computer_data[0])
        
        # create root window
        gui = Tk()
        gui.title("Computer Information")
        table = Table(gui)
    
        gui.mainloop()
      
    
    # When 'Software Information' is clicked opens a new window with table   
    def softwareInfoWindow():
       
       #Removes button after clicking 
       getInfo.pack_forget() 
       btn_softInfo.pack_forget() 
       
       dic=myLab.installedSoftware(sList)  # Calls to get software info method from a7_CMPLab
       
       cmpValues =list(dic.values()) 
       
       cmp0,cmp1,cmp2,cmp3,cmp4,cmp5,cmp6,cmp7,cmp8,cmp9 = [],[],[],[],[],[],[],[],[],[]
       
       for j in range(len(cmpValues)):    # Sets up data for table correctly
           cmp0.append(cmpValues[j][0])
           cmp1.append(cmpValues[j][1])
           cmp2.append(cmpValues[j][2])
           cmp3.append(cmpValues[j][3])
           cmp4.append(cmpValues[j][4])
           cmp5.append(cmpValues[j][5])
           cmp6.append(cmpValues[j][6])
           cmp7.append(cmpValues[j][7])
           cmp8.append(cmpValues[j][8])
           cmp9.append(cmpValues[j][9])
        
       class Table:
            # Initialize a constructor
            def __init__(self, gui):
        
                # An approach for creating the table
                for i in range(total_rows):
                    for j in range(total_columns):
                        if i ==0:
                            self.entry = Entry(gui, width=50, bg='LightSteelBlue',fg='Black',
                                               font=('Arial', 11, 'bold'))
                        else:
                            self.entry = Entry(gui, width=50, fg='blue',
                                       font=('Arial', 11, ''))
        
                        self.entry.grid(row=i, column=j)
                        self.entry.insert(END, installed_Software[i][j])
        
        
        # take the data
       installed_Software = [list(dic.keys()), 
           cmp0, cmp1, cmp2, cmp3, cmp4, cmp5, cmp6, cmp7, cmp8, cmp9]
              
        # find total number of rows and
        # columns in list
       total_rows = len(installed_Software)
       total_columns = len(installed_Software[0])
        
        # create root window
       gui = Tk()
       gui.title("Installed Software")
       table = Table(gui)
    
       gui.mainloop()
    
    
    # Fromm https://realpython.com/python-gui-tkinter/ by David Amos
    # Creates window and Frames
    window =  Tk()             
    window.title("myLab")
    
    greetingFrame =  Frame()
    numCmpFrame =  Frame()
    IDcmpFrame =  Frame()
    
    # Greeting with number of computers in myLab
    labelGreeting =  Label(master=greetingFrame, text="Welcome to myLab!")
    labelGreeting.pack()
    labelNumCmp =  Label(master=numCmpFrame, text=f'{myLab}')
    labelNumCmp.pack()
    
    
    greetingFrame.pack()
    numCmpFrame.pack()
    
    # Creates button frame
    frm_buttons =  Frame()
    frm_buttons.pack(fill= X, ipadx=5, ipady=5)
    
    
    # Creates option buttons which appear once either the 'Basic',
    # 'Advanced' or 'Game' button is clicked on
    getInfo =  Button(window,text="All Computer Information",command=openNewWindowGetInfo)
    btn_softInfo=Button(window, text="All Software Information", command=softwareInfoWindow)
    
    
    
    #Creates the 'Basic', 'Advacned', 'Gaming' buttons
    btn_basic =  Button(master=frm_buttons, text="Basic", command=basicID)
    btn_basic.pack(side= LEFT, padx=50, ipadx=10)
    btn_advanced =  Button(master=frm_buttons, text="Advanced", command=advancedID)
    btn_advanced.pack(side= LEFT, padx=50, ipadx=10)
    btn_game =  Button(master=frm_buttons, text="Gaming", command=gameID)
    btn_game.pack(side= LEFT, padx=50, ipadx=10)
    
    
    
    # Shows 'No computers selected!' if none of the 'Basic', 'Advanced'
    # 'Gaming' button is pressed
    labelIDcmp =  Label(master=IDcmpFrame, text="No computers selected!")
    labelIDcmp.pack()
    IDcmpFrame.pack()
    
    window.mainloop()

# ensured code is not run if module is imported elsewhere 
if __name__ == '__main__':
    print(GUI())
