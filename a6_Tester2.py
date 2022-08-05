#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MyComputer Project
Coursework for: 5020B Programming for non-specialists

Includes a advTester function for Task 6 

@author: Shannon Jones 
@date:   21/03/2022

"""

import a3_component as a3
import a5_game as a5

def advTester():    
    
    # Five software instance with 2 not requring GPU. 
    sList = [ a3.Software("Python", 2, 32, 4, 2, 0), 
             a3.Software("Paint", 1.2, 16, 2, 5, 0),
             a3.Software("Adobe Photoshop", 3, 64, 8, 15, 1),
             a3.Software("Blender", 0.5, 32, 8, 20, 1),
             a3.Software("Minecraft", 0.9, 32, 8, 30, 1)]
    
    # Prints each software instance in string form
    print('Software list is: \n')
    for software in sList:
        print(f'{software} \n')
    
    print()            
    print("================================================================")
    print()
    
    # Computer list, two of which are advacned and two are game computers
    cTuple = [a5.AdvComputer("Dell", "XPS-17-9710", a3.Processors("Intel", "Core-i7-11800H", 32, 2.3), a3.RAM("Unknown", "Unknonw", 16), a3.HardDrive("Unknown", "Unknown", 1024, 0)),
                    a5.AdvComputer("ASUS", "ZenBook-Pro-Duo-UX582",a3.Processors("Intel", "Core-i9-10980HK", 32, 2.4), a3.RAM("Unknown", "Unknonw", 32), a3.HardDrive("Unknown", "Unknown", 1024, 0)),
                    a5.GameComputer("HP", "OMEN-25L", a3.Processors("AMD", "Ryzen-7-5700G", 64, 3.8), a3.RAM("Unknown", "Unknonw", 16), a3.HardDrive("Unknown", "Unknown", 1024, 0), a3.GPU("AMD", "Radeon-RX-6600-XT", 8)),
                    a5.GameComputer("GIGABYTE", "AERO-HDR-17YD", a3.Processors("Intel", "Core-i7-11800H", 32, 2.3), a3.RAM("Unknown", "Unknown", 32), a3.HardDrive("Unknown", "Unknown", 1024, 0), a3.GPU("NVIDIA", "GeForce-RTX-3070", 8))]
    
    # Prints each computer instance in string form
    print('Computer list is: \n')
    for computer in cTuple:
        print(f'{computer} \n')
    
    print()            
    print("================================================================")
    print()
    
    for computer in cTuple:
        capability=[computer.compatibleWith(software) for software in sList]                            # For each software check if computer is compatible, which returns True or False, then appends to capability list
        yInstall =[sList[i].Name for i in range(len(capability)) if capability[i]]                      # If capability[i] is True then software can be installed, thus finds name of software and appends to yInstall list
        nInstall =[sList[i].Name for i in range(len(capability)) if not(capability[i])]                 # If capability[i] is False then software cannot be installed, thus finds name of software and appends to yInstall list
        print(f'{computer.Make} {computer.Model} can install {yInstall} but cannot install {nInstall} \n' )
    
    print()            
    print("================================================================")
    print()
    
    print(f'Before swapping: \n \n {cTuple[2].Make}: {cTuple[2].GPU} \n {cTuple[3].Make}: {cTuple[3].GPU} \n')
    cTuple[2].GPU,cTuple[3].GPU =cTuple[3].GPU,cTuple[2].GPU                                              # Swaps GPU using property decorator
    print(f'After swapping: \n \n {cTuple[2].Make}: {cTuple[2].GPU} \n {cTuple[3].Make}: {cTuple[3].GPU} \n')
  
    print()            
    print("================================================================")
    print()
    
    
    for computer in cTuple:
        capability=[computer.install(software) for software in sList]                                         # For each software it tries to install onto computer, which returns True or False, then appends to capability list
        yInstall =[sList[i].Name for i in range(len(capability)) if capability[i]]                            # If capability[i] is True then software has be installed, thus finds name of software and appends to yInstall list
        nInstall =[sList[i].Name for i in range(len(capability)) if not(capability[i])]                       # If capability[i] is Flase then software has not be installed, thus finds name of software and appends to yInstall list
        print(f'{computer.Make} {computer.Model} has installed {yInstall} but could not install {nInstall}\n')

# ensured code is not run if module is imported elsewhere 
if __name__ == '__main__':
    print(advTester())
