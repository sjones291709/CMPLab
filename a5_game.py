#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MyComputer Project
Coursework for: 5020B Programming for non-specialists

Includes a GameComputer which is a subclass of AdvComputer for Task 5 

@author: Shannon Jones 
@date:   21/03/2022

"""

from a4_advanced import AdvComputer

class GameComputer(AdvComputer):
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
        
    GPU: obj
        GPU object - ("Make", "Model", "Capacity")
    ________________________
    '''
    
    
    
    def __init__(self, Make, Model, Processor, RAM, HardDrive, GPU):
        '''
        Construction Method
        '''
        super().__init__(Make, Model, Processor, RAM, HardDrive)
        self._GPU = GPU
        
        
        
    def __str__(self):
        '''
        Returns string method of GameComputer instance
        '''
        return (f'Gaming Computer: Make - {self.Make}, Model - {self.Model}, {self.Processor}, {self.RAM}, {self.HardDrive}, {self.GPU}')
    
    
    
    @property
    def GPU(self):
        '''
        Allows user to change GPU 
        '''
        return self._GPU
    
    @GPU.setter
    def GPU(self, newGPU):
        self._GPU = newGPU
    
    
    
    def compatibleWith(self, software):
        '''
        Method to check that processor speed, RAM capacity, free space of
        hard drive and GPU capacity for a game computer instance is less than 
        the required processor speed, RAM capacity, hard drive space and GPU
        capacity for software. 
        '''
        if self.Processor.Speed < software.ReqProcessSpeed:
            return False
        if self.Processor.BitWidth < software.ReqProcessSpeed:
            return False
        if self.RAM.Capacity < software.RAM:
            return False
        if self.HardDrive.freeSpace() < software.hardwareSpace: # Could run into issues when installing as there may be enough space for the apps individually but not all together.
            return False 
        if self.GPU.Capacity < software.GPU:
            return False
        return True
       
            


