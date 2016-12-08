'''
Created on 08.12.2016

@author: Tomek
'''

def sameDefRef(a = []):
    """Python uses references to SAME object in case of usinf defaukt arguments"""
    a.append(1) #same A referenced
    print(a)

for i in range(3):
    sameDefRef()