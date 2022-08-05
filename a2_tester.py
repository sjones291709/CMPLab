#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WindFarm Project
Coursework for: 5020B Programming for non-specialists

Includes BasicTester fucntion for Task 2 

@author: dqk18fyu 
@date:   21/03/2022

"""

from a1_basic import BasicComputer

def BasicTester():
    '''
    Function to test the basic computer class methods in task 1
    '''
    
    # Two basic computer instances
    BC1 = BasicComputer("Apple", "MacBook-Air-2020", 1.1 , 8 , 256)
    BC2 = BasicComputer("HP", "Pavilion", 1.1 , 8 , 256)
    
    print(f'BC1 == BC2 prints {BC1 == BC2}') # Returns true
    print(f'BC1 < BC2 prints {BC1 < BC2}')  # Returns false

    
    # Five computer instances in a list
    BasicComputerList=[ BasicComputer("ACER", "Aspire", 2.4, 8, 512),
    BasicComputer("Apple", "MacBook-Air-2020", 1.1, 8, 256),
    BasicComputer("DELL", "XPS-17-9710", 2.5, 32, 128),
    BasicComputer("HP", "Pavilion", 3.0, 4, 256),                               #Third going by 0 indexing
    BasicComputer("MICROSOFT", "13.7-SurFace" , 1.3, 16, 512)]
    
    print()            
    print("================================================================")
    print() 
    
    # Prints list of computers using list 
    print("Computer List is: \n")     
    for i in range(len(BasicComputerList)):
        print(BasicComputerList[i])
    
    # Uses bubble sort to rearrange computer list so the highest prcoessor speed is first
    for i in range(len(BasicComputerList)):
        for j in range(len(BasicComputerList)-1):
            if BasicComputerList[j]> BasicComputerList[j+1]:
                BasicComputerList[j],BasicComputerList[j+1] = BasicComputerList[j+1],BasicComputerList[j]
                
    print()            
    print("================================================================")
    print()
     
    # Prints new ordered list
    print("Ordered List is:  \n")     
    for i in range(len(BasicComputerList)):
        print(BasicComputerList[i])
        
    print()            
    print("================================================================")
    print()
    
    #Compares the difference in processor speed and RAM capacity between each basic computer instances.    
    for i in range(len(BasicComputerList)-1):
        refComputer = BasicComputerList[i]
        remainingComputers = BasicComputerList[i+1:]
        print(f'Processing speed difference bewteen computer {i} and the remaining computers: {[round(Computer.Processor - refComputer.Processor,2) for Computer in remainingComputers]} ')
        print(f'RAM capacity difference computer {i} and the remaining computers: {[round(Computer.RAM-refComputer.RAM,2) for Computer in remainingComputers]} \n')
        

# ensured code is not run if module is imported elsewhere 
if __name__ == '__main__':
    print(BasicTester())

