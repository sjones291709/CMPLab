#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MyComputer Project
Coursework for: 5020B Programming for non-specialists

Includes a simulator function for Task 8

@author: Shannon Jones 
@date:   21/03/2022

"""
import matplotlib.pyplot as plt 
import a7_cmplab as a7
import a3_component as a3

def simulator():
    
    myLab = a7.CMPLab("myLab")      # CMPLab instance named myLab
    myLab.fromFile('myLab.txt')     # adds computers to lab dictionary from myLab text file

   
    software = a3.Software("Adobe Photoshop", 3, 64, 8, 15, 1) # software instance
    print(f'The computers which installed {software.Name} are {myLab.install(software)} \n') # Returns the list of IDs of computers which have sucessfully installed Adobe Photoshop
  
    
    
    cmpType = [i for i in myLab.typeCount().keys()]   # List of computer types e.g. ['basic','advanced','game']
    cmpNum = [j for j in myLab.typeCount().values()]  # List of number of each computer type 


    
    # Creates a pie and bar chart to show the number of each computer type 
    # From https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html 
    # By John Hunter, Darren Dale, Eric Firing, Michael Droettboom and the Matplotlib development team
    fig, axs = plt.subplots(1,2)
    axs[0].bar(cmpType,cmpNum)
    axs[1].pie(cmpNum, labels = cmpType)
    plt.savefig('zfigFst.png')            # Saves figure to png
    
    
    
    sndLab = a7.CMPLab("sndLab")    # new CMPLab instance named sndLab
    sndLab.fromFile('sndLab.txt')   # adds computers to lab dictorionary from sndLab text file
    sndLab.toFile('sndLabInfo.txt') # Creates a new file with the updated lab dictorionary information
    
    
    
    cmpType = [i for i in sndLab.typeCount().keys()]  # List of computer types 
    cmpNum = [j for j in sndLab.typeCount().values()] # List of number of each computer type 
    
    
    
    #Creates a pie and bar chart to show the number of each computer type 
    fig, axs = plt.subplots(1,2)
    axs[0].bar(cmpType,cmpNum)
    axs[1].pie(cmpNum, labels = cmpType)
    plt.savefig('zfigSnd.pdf')           # Saves figure to pdf
    
    
    
# ensured code is not run if module is imported elsewhere 
if __name__ == '__main__':
    print(simulator())
