#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MyComputer Project
Coursework for: 5020B Programming for non-specialists

Includes a procossor class, RAM class, HardDrive class, GPU class
and software class for Task 3 

@author: Shannon Jones 
@date:   21/03/2022

"""



class Processors():
    ''' 
    A class to represents a Processor
    _______________________
    
    Attributes 
    ----------
    
    Make : str
        make of processor
        
    Model: str 
        model of processor
        
    BitWidth: int 
        bitwidth of processor (32-bit or 64-bit)
        
    Speed: int
        speed of processor (in GHz)
    ________________________
    '''
    
    
    
    def __init__(self, Make, Model, BitWidth, Speed):
        '''
        Construction Method
        '''
        self.Make = Make
        self.Model = Model
        self.BitWidth = BitWidth
        self.Speed = Speed
        
        
        
    def __str__(self):
        '''
        Returns string version of processor instance
        '''
        return (f'[Processor:  Make - {self.Make}, Model - {self.Model}, BitWidth - {self.BitWidth}-Bit, Speed - {self.Speed}GHz ]')
    
    
    
    def __eq__(self, other):
        ''' 
        Equal method which returns true if both processor instances have the 
        same bitwidth and speed.
        '''
        if self.BitWidth == other.BitWidth and self.Speed == other.Speed:
            return True
        else:
            return False
    
    
    
    def __lt__(self, other):
        '''
        Less than method which returns  true if bitwidth of the first instance 
        of processor is less than the bitwidth of second instance of processor 
        OR if speed of the first instance of processor is less than the speed 
        of second instance of processor
        '''
        if self.BitWidth < other.BitWidth or self.Speed < other.Speed:
            return True
        else:
            return False




class RAM():
    ''' 
    A class to represents RAM
    _______________________
    
    Attributes 
    ----------
    
    Make : str
        make of RAM
        
    Model: str 
        model of RAM
        
    Capacity: int 
        capacity of RAM (in GB)
    ________________________
    '''
    
    
    
    def __init__(self, Make, Model, Capacity):
        '''
        Construction Method
        '''
        self.Make = Make
        self.Model = Model
        self.Capacity = Capacity
      
        
      
    def __str__(self):
        '''
        Returns string version of RAM instance
        '''
        return (f'[RAM: Make - {self.Make}, Mdoel - {self.Model}, Capacity - {self.Capacity}GB]')
       
    
    
    def __eq__(self, other):
        ''' 
        Equal method which returns true if both RAM instances have the same 
        capacity
        '''
        if self.Capacity == other.Capacity:
            return True
        else:
            return False
      
        
      
    def __lt__(self, other):
        '''
        Less than method which returns true if frist instance of RAM has less 
        capacity than the second instance of RAM.
        '''
        if self.Capacity < other.Capacity:
            return True
        else:
            return False




class HardDrive():
    ''' 
    A class to represents HardDrive
    _______________________
    
    Attributes 
    ----------
    
    Make : str
        make of hard drive
        
    Model: str 
        model of hard drive
        
    Capacity: int 
        capacity of hard drive (in GB)
        
    usedSpace: int
        used space of hard drive which is automatically set to 0GB 
    ________________________
    '''
    
    
    
    def __init__(self, Make, Model, Capacity, usedSpace=0):
        '''
        Construction Method
        '''
        self.Make = Make
        self.Model = Model
        self.Capacity = Capacity
        self.usedSpace = usedSpace
      
        
      
    def __str__(self):
        '''
        Returns string version of RAM instance
        '''
        return (f'[Hard-Drive: Make - {self.Make}, Mdoel - {self.Model}, Capacity - {self.Capacity}GB], Used Space - {self.usedSpace}GB]')
      
    
    
    def __eq__(self, other):
        ''' 
        Equal method which returns true if both Hard drive instances have the 
        same capacity
        '''
        if self.Capacity == other.Capacity:
            return True
        else:
            return False
      
        
      
    def __lt__(self, other):
        '''
        Less than method which returns true if frist instance of hard drive has
        less capacity than the second instance of hard drive.
        '''
        if self.Capacity < other.Capacity:
            return True
        else:
            return False
    
    
    
    def freeSpace(self):
        '''
        Method to return free space of hard drive
        '''
        return self.Capacity-self.usedSpace




class GPU():
    ''' 
    A class to represents GPU
    _______________________
    
    Attributes 
    ----------
    
    Make : str
        make of GPU
        
    Model: str 
        model of GPU
        
    Capacity: int 
        capacity of GPU (in GBs)
    ________________________
    '''
    
    
    
    def __init__(self, Make, Model, Capacity):
        '''
        Construction Method
        '''
        self.Make = Make
        self.Model = Model
        self.Capacity = Capacity
      
        
      
    def __str__(self):
        '''
        Returns string version of CPU instance
        '''
        return (f'[GPU: Make - {self.Make}, Model - {self.Model}, Video Memmory Capacity - {self.Capacity}GB]')
      
    
    
    def __eq__(self, other):
        '''
        Equal method which returns if both GPU instances have the same capacity
        '''
        
        if self.Capacity == other.Capacity:
            return True
        else:
            return False
            
       
        
    def __lt__(self, other):
        ''' 
        Less than method which returns true if the first instance of GPU has 
        less capacity than the second instance of GPU.
        '''
        if self.Capacity < other.Capacity:
            return True
        else:
            return False




class Software():
    ''' 
    A class to represents Software
    _______________________
    
    Attributes 
    ----------
    
    Name : str
        name of software
        
    ReqProcessSpeed: int 
        Required processor speed for software (in GHz)
        
    BitWidth: int 
        Required processor bitwidth for software 
        
    RAM: int
        Required RAM capacity for software (in GB)
        
    hardwareSpace: int
        Required hardware space for software (in GB)
        
    GPU: bool
        0 if software does not require GPU, 1 otherwise
    ________________________
    '''
    
    
    
    def __init__(self, Name, ReqProcessSpeed, BitWidth, RAM, hardwareSpace, GPU):
        '''
        Construction Method
        '''        
        self.Name = Name 
        self.ReqProcessSpeed = ReqProcessSpeed
        self.BitWidth = BitWidth
        self.RAM = RAM
        self.hardwareSpace = hardwareSpace
        self.GPU = GPU
        
    def __str__(self):
        '''
        Returns string version of Software instance
        '''        
        return (f'[Software: Name of Software - {self.Name}, Required Processor Speed - {self.ReqProcessSpeed}GHz, Required BitWidth - {self.BitWidth}-Bit, Required RAM - {self.RAM}GB, Required Hardware Space - {self.hardwareSpace}GB, Required GPU - {self.GPU}]')
        
    
    
    def __eq__(self, other):
        '''
        Equal method which returns true if both software instance has the same 
        required processor speed, bidwidth, RAM, hardware space and GPU.
        '''
        if self.ReqProcessSpeed == other.ReqProcessSpeed and self.BitWidth == other.BitWidth and self.RAM == other.RAM and self.hardwareSpace == other.hardwareSpace and self.GPU == other.GPU:
            return True
        else:
            return False
       
        
       
    def __lt__(self, other):
        '''
        Less than method which returns true if the frist instance of software
        has less required processor speed than the second instance OR bidwidth,
        RAM, hardware sapce or GPU.
        '''
        if self.ReqProcessSpeed < other.ReqProcessSpeed or self.BitWidth < other.BitWidth or self.RAM < other.RAM or self.hardwareSpace < other.hardwareSpace or self.GPU < other.GPU:
            return True
        else:
            return False
        
        






        