#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""myLab Project
Coursework for: 5020B Programming for non-specialists

Includes a CMPLab class for Task 7 

@author: Shannon Jones 
@date:   21/03/2022

"""
import a1_basic as a1
import a3_component as a3
import a4_advanced as a4
import a5_game as a5


class MaxNumError(Exception):
    '''
    Execption Class 
    '''
    pass

class CMPLab():
    ''' 
    A class to represents a Computer Lab
    _______________________
    
    Attributes 
    ----------
    
    Name : str
        Name of acomputer lab
    ________________________
    '''
    
    
    
    def __init__(self, name):
        '''
        Construction Method
        '''
        self.name = name
        self.dicIDs ={}       # dictionary of computers and their IDs e.g. {0: cmpObj0, 1: cmpObj1, ...}
        self.maxNum = 10      # automatically sets the maximum number of computers to 10 for each lab instance
        
        
        
    def __str__(self):
        '''
        returns string version of computer lab instance
        '''
        return f'{self.name} has {len(self.dicIDs.values())} computers'
    
    
    
    def install(self, Software):
        '''
        Method to download a software instance to all computers in the lab and 
        returns the IDs of the computers of which was able to download
        '''
        cmp = list(self.dicIDs.values())
        IDs = list(self.dicIDs.keys())
        return [i for i in IDs if cmp[i].install(Software)]
           
    
    
    def addComputer(self, computers):
        '''
        Method to add computer to lab dictionary, however returns custom error 
        called MaxNumError if the number of computers added exceeds the maximum
        number of computers allowed in a lab.
        '''
        for slot in range(self.maxNum):
            if slot not in self.dicIDs:     # Check computer isnt already in dictionary
                try:
                    self.dicIDs[slot] = computers.pop(0)     #Add computer to dictionary and removes from list of computers
                except IndexError:
                    pass
        try:
            if len(computers)!=0:                             # If list is non-empty then there are more computer than could be alligated, so raises MaxNumError
                raise MaxNumError("Too many computers added")
        except MaxNumError:
            pass
         
            
           
    def removeComputer(self, ID):
        '''
        Method to remove computer from dictionary
        '''
        if ID in self.dicIDs:
            self.dicIDs.pop(ID)
            return True
        else:
            return False
        
        
        
    def fromFile(self,txt):
        '''
        Method which converts list of infromation of computers from a text file
        to the lab dictionary
        '''
        cmpList=[]
        with open(txt) as f:
            for line in f:
                myList=line.split()            # Splits each line into a list of words 
                if myList[0] == 'basic':       # check what type and creates appropiate computer instance
                    cmp=a1.BasicComputer(myList[1], myList[2], float(myList[3]),float(myList[4]),float(myList[5]))
                elif myList[0] == 'advanced':
                    cmp=a4.AdvComputer(myList[1], myList[2], a3.Processors("unknown","unknown", float(myList[4]), float(myList[3])),a3.RAM("unknown", "unknown", float(myList[5])), a3.HardDrive("unknown", "unknown", float(myList[6]), 0))
                elif myList[0] == 'game':
                    cmp=a5.GameComputer(myList[1], myList[2], a3.Processors("unknown","unknown", float(myList[4]), float(myList[3])),a3.RAM("unknown", "unknown", float(myList[5])), a3.HardDrive("unknown", "unknown", float(myList[6]), 0), a3.GPU("unknown", "unknown", float(myList[7])))
                cmpList.append(cmp)
        self.addComputer(cmpList) # Send to addComputer method which adds to dictionary
    
    
    
        
    def toFile(self,txt):
        '''
        Method which converts lab dictionary information to text file
        '''
        with open(txt, 'w') as f:
            cmp = list(self.dicIDs.values())   # List of computers
            IDs = list(self.dicIDs.keys())     # List of IDs
            for ID in range(len(cmp)):
                if type(cmp[ID])==a1.BasicComputer:   # Check which types and creates the appropiate text structure
                    f.write(f'{IDs[ID]} basic {cmp[ID].Make} {cmp[ID].Model} {cmp[ID].Processor} {cmp[ID].BitWidth} {cmp[ID].RAM} {cmp[ID].HardDrive} \n')
                elif type(cmp[ID])==a4.AdvComputer:
                    f.write(f'{IDs[ID]} advanced {cmp[ID].Make} {cmp[ID].Model} {cmp[ID].Processor.Speed} {cmp[ID].Processor.BitWidth} {cmp[ID].RAM.Capacity} {cmp[ID].HardDrive.Capacity} \n')
                elif type(cmp[ID])==a5.GameComputer:
                    f.write(f'{IDs[ID]} game {cmp[ID].Make} {cmp[ID].Model} {cmp[ID].Processor.Speed} {cmp[ID].Processor.BitWidth} {cmp[ID].RAM.Capacity} {cmp[ID].HardDrive.Capacity} {cmp[ID].GPU.Capacity} \n')
    
                    
    
    def typeCount(self):
        '''
        Method which returns a dictionary which keys representing computer type
        and values representing the number of computers of this type in the lab
        '''
        cmp = list(self.dicIDs.values())  # List of computers
        IDs = list(self.dicIDs.keys())    # List of IDs
        countDic={"basic": 0, "advanced":0, "game":0}  # New dictionary for computer type and number of each type (initally all set to 0)
        for ID in IDs:
            if type(cmp[ID])==a1.BasicComputer: # Checks what type and adds 1 to value for the appropiate keys
                countDic["basic"]+=1
            elif type(cmp[ID])==a4.AdvComputer:
                countDic["advanced"]+=1
            elif type(cmp[ID])==a5.GameComputer:
                countDic["game"]+=1
        return countDic
     
        
     
    def getComputers(self,cmpType):
        '''
        Method requires a string of a computer type (e.g. 'basic', 'advanced' 
        or 'game') and returns the list of IDs of the computers of this type
        '''
        cmp = list(self.dicIDs.values()) # List of computers
        IDs = list(self.dicIDs.keys())   # List of IDs
        if cmpType == 'basic':   # Check what type of computer and appends IDs to a list
            return [ID for ID in IDs if type(cmp[ID])==a1.BasicComputer]
        elif cmpType == 'advanced':
            return [ID for ID in IDs if type(cmp[ID])==a4.AdvComputer]
        elif cmpType == 'game':
            return [ID for ID in IDs if type(cmp[ID])==a5.GameComputer]
        
        
    def computerInfo(self):
        '''
        Method to add required computer information to a dictionary, 
        used to made a table for GUI.
        '''
        
        headings = {"ID": [], "Type": [] , "Make": [], "Model":[], "Processor Speed (GHz)": [], "Bitwidth (bits)": [], "RAM Capacity (GB)": [], "Hard-drive Capacity (GB)": [], "Hard-drive Free Space (GB)": [], "GPU Capacity (GB)": []}
        cmp=list(self.dicIDs.values())  # List of Computers
        for i in range(len(cmp)):    
            if type(cmp[i])==a1.BasicComputer: # Checks what type and appends dictionary with appropiate information
                headings["ID"].append(i)
                headings["Type"].append("Basic")
                headings["Make"].append(cmp[i].Make)
                headings["Model"].append(cmp[i].Model)
                headings["Processor Speed (GHz)"].append(cmp[i].Processor)
                headings["Bitwidth (bits)"].append(cmp[i].BitWidth)
                headings["RAM Capacity (GB)"].append(cmp[i].RAM)
                headings["Hard-drive Capacity (GB)"].append(cmp[i].HardDrive)
                headings["Hard-drive Free Space (GB)"].append(cmp[i].freeSpace())
                headings["GPU Capacity (GB)"].append("N/A")
            elif type(cmp[i])==a4.AdvComputer:
                headings["ID"].append(i)
                headings["Type"].append("Advanced")
                headings["Make"].append(cmp[i].Make)
                headings["Model"].append(cmp[i].Model)
                headings["Processor Speed (GHz)"].append(cmp[i].Processor.Speed)
                headings["Bitwidth (bits)"].append(cmp[i].Processor.BitWidth)
                headings["RAM Capacity (GB)"].append(cmp[i].RAM.Capacity)
                headings["Hard-drive Capacity (GB)"].append(cmp[i].HardDrive.Capacity)
                headings["Hard-drive Free Space (GB)"].append(cmp[i].HardDrive.freeSpace())
                headings["GPU Capacity (GB)"].append("N/A")
            elif type(cmp[i])==a5.GameComputer:
                headings["ID"].append(i)
                headings["Type"].append("Game")
                headings["Make"].append(cmp[i].Make)
                headings["Model"].append(cmp[i].Model)
                headings["Processor Speed (GHz)"].append(cmp[i].Processor.Speed)
                headings["Bitwidth (bits)"].append(cmp[i].Processor.BitWidth)
                headings["RAM Capacity (GB)"].append(cmp[i].RAM.Capacity)
                headings["Hard-drive Capacity (GB)"].append(cmp[i].HardDrive.Capacity)
                headings["Hard-drive Free Space (GB)"].append(cmp[i].HardDrive.freeSpace())
                headings["GPU Capacity (GB)"].append(cmp[i].GPU.Capacity)
        return headings
    
    
    def installedSoftware(self,software):
        '''
        Method to add required software information to a dictionary, used to 
        made a table for GUI.
        '''
        
        headings = {"ID": [] , "Make": [], "Model":[], "Software": []}
        cmp=list(self.dicIDs.values())    # List of computers
        for i in range(len(cmp)):
                headings["ID"].append(i)
                headings["Make"].append(cmp[i].Make)
                headings["Model"].append(cmp[i].Model)
                
        # Same method used in a6_Tester2 Line 60
        for computer in cmp:
            capability=[computer.install(softwares) for softwares in software]                                         
            yInstall =[software[i].Name for i in range(len(capability)) if capability[i]]   
            headings["Software"].append(yInstall)
        return headings
    