#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MyComputer Project 
Coursework for: 5020B Programming for non-specialists

Includes a BasicComputer class for Task 1 

@author: Shannon Jones 
@date:   21/03/2022

"""


class BasicComputer():
    ''' 
    A class to represents a basic computer 
    _______________________
    
    Attributes 
    ----------
    
    Make : str
        make of basic computer 
        
    Model: str 
        model of basic computer 
        
    Processor: int 
        processor speed of basic computer
        
    RAM: int
        RAM capacity of basic computer 
        
    HardDrive: int
        hard drive capacity
    ________________________
    '''
    
    
    # Automatically sets all basic computers instances to have BitWidth 32-bits
    BitWidth=32.0
    
    
    
    def __init__(self, Make, Model, Processor, RAM, HardDrive):
        '''
        Construction Method
        '''
        self.usedSpace = 0
        self.Make = Make 
        self.Model = Model 
        self.Processor = Processor
        self.RAM = RAM
        self.HardDrive = HardDrive
    
    
    
    def __str__(self):
        '''
        Returns string version of basic computer instance
        '''
        return (f'Basic Computer: Make - {self.Make}, Model - {self.Model}: Processor Speed - {self.Processor}GHz, RAM - {self.RAM}GB, Hard Drive Space - {self.HardDrive}GB')
        
    
    
    def __eq__(self, other):
        '''
        Equal method which returns true if both basic computer instances have 
        the same processor speed, RAM capacity and hard drive capacity.
        '''
        if self.Processor == other.Processor and self.RAM == other.RAM and self.HardDrive == other.HardDrive :
            return True
        else:
            return False
    
    
    
    def __lt__(self, other):
        '''
        Less than method which returns true if processor speed of the first 
        basic computer instance is less than the processor speed of the second 
        basic computer instance
        '''
        if self.Processor < other.Processor:
            return True
        else:
            return False
    
    
    
    # Added for a7 so install function can work for basic computer instance 
    def compatibleWith(self, software):
        '''
        Method to check that processor speed, RAM capacity and hard drive for 
        a basic computer instance is less than the required processor speed, 
        RAM capacity and hard drive space for software. 
        If software requires GPU then automatically return False as basic 
        computer does not have GPU.
        '''
        if self.Processor < software.ReqProcessSpeed:
            return False
        if self.RAM < software.RAM:
            return False
        if self.HardDrive < software.hardwareSpace: # Could run into issues when installing as there may be enough space for the apps individually but not all together.
            return False 
        if software.GPU > 0:
            return False
        return True
   
    
   
    # Added for a7 so install function can work for basic computer instance 
    def install(self, software):
        '''
        Method to install software onto basic computer instance, firstly 
        checking the computer can support the software using compatibleWith 
        method. Then if computer is compactible, it will update the basic 
        computer hard drive capacity. 
        '''
        if self.compatibleWith(software) == True:
            self.HardDrive += software.hardwareSpace  # adds hardware space of software to computers used space
            return True 
        else:
            return False
        
    def freeSpace(self):
        '''
        Method to return free space of hard drive
        '''
        return self.HardDrive-self.usedSpace
        
        
        