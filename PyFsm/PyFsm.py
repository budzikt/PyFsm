'''
Created on 07.12.2016

@author: Tomek
'''
import os
import glob
import shutil
import unittest
import argparse
import sys
from enum import Enum

class confKeys(Enum):
    initState = 0;
    stateList = 1;

class eventKeys(Enum):
    name = 0
    prevStates = 1
    nextStates = 2

configPart = {
            'initState': ['state_initialState', [], ['state_postInit', 'state_Run']],
            'stateList': []
              
              }


class FsmTests(unittest.TestCase):
    def testAlwaysPass(self):
        """This is sanity test for tests"""
        self.assertEqual(1, 1)
    
    def testCfgHasInit(self):
        """Configuration shall have a initialState"""

def parseCmdArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('-tr', '-testrun', '-TestRun', action='store_true', dest='tr')
    args = parser.parse_args(sys.argv)
    return vars(args)
    
def testNeeded(argsDict):
    if 'tr' in argsDict and argsDict['tr'] == True:
        return True
    else:
        return False
    
#Manage argvars to run unittests      
def mainTest():
    argsTemp = list(sys.argv)
    del sys.argv[1:]
    unittest.main()
    sys.argv = argsTemp
    
#RUN as script
if __name__ == "__main__":
    print("\n\n***RUN AS MAIN***\nRun as script with arglist: " + '\n' + str(sys.argv))
    argMap = parseCmdArgs()
    if(testNeeded(argMap)):
        print('Run Unit Tests')
        mainTest()
    else:
        print('No test running')  