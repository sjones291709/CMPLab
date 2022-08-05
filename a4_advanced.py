#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MyComputer Project
Coursework for: 5020B Programming for non-specialists

Includes a AdvComputer class for Task 4 

@author: Shannon Jones 
@date:   21/03/2022

"""


class AdvComputer():
    ''' 
    A class to represents a Advanced Computers
    _______________________
    
    Attributes 
    ----------
    
    Make : str
        make of advanced computer
        
    Model: str 
        model of advanced computer
        
    Processor: obj 
        processor object - ("Make", "Model", "BitWidth", "Speed")
        
    RAM: obj
        RAM object - ("Make", "Model", "Capacity")
        
    HardDrive: obj
        Hard drive object - ("Make", "Model", "Capcity", "usedSpace")
    ________________________
    '''
    
    
    
    def __init__(self, Make, Model, Processor, RAM, HardDrive):
        '''
        Construction Method
        '''
        self.Make = Make
        self.Model = Model
        self.Processor=Processor
        self.RAM = RAM
        self.HardDrive = HardDrive
        
        
        
    def __str__(self):
        '''
        returns string version of AdvComputer instnace
        '''
        return (f'Advance Computer: Make - {self.Make}, Model - {self.Model},  {self.Processor}, {self.RAM}, {self.HardDrive}')


        
    def compatibleWith(self, software):
        '''
        Method to check that processor speed, RAM capacity and free space of
        hard drive for an advanced computer instance is less than the required 
        processor speed, RAM capacity and hard drive space for software. 
        If software requires GPU then automatically return False as advanced 
        computer does not have GPU.
        '''
        if self.Processor.Speed < software.ReqProcessSpeed:
            return False
        if self.Processor.BitWidth < software.BitWidth:
            return False
        if self.RAM.Capacity < software.RAM:
            return False
        if self.HardDrive.freeSpace() < software.hardwareSpace: # Could run into issues when installing as there may be enough space for the apps individually but not all together.
            return False 
        if software.GPU > 0:
            return False
        return True
        
    
            
    def install(self, software):
        '''
        Method to install software onto advanced computer instance, firstly 
        checking the computer can support the software using compatibleWith 
        method. Then if computer is compactible, it will update the basic 
        computer hard drive capacity. 
        '''
        if self.compatibleWith(software) == True:
            self.HardDrive.usedSpace += software.hardwareSpace   # adds hardware space of software to computers used space
            return True 
        else:
            return False

