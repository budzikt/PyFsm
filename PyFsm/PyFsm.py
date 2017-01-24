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

#LocalImports
import utils

class eventKeys(Enum):
    prevStates = 0
    nextStates = 1

configPart= {   'initState': 'st_initial',
                'stateList': {      
                    'st_initial':  [ [],             ['st_Run', 'st_shutdown'] ]   ,
                    'st_Run':      [ ['st_initial'], ['st_shutdown'] ]             ,
                    'st_shutdown': [ ['st_initial','st_Run'], ['st_initial']]      ,
                              
                }, #End Statelist
            }
configActions = {
    }

class FsmTests(unittest.TestCase):
    
    testCfg = configPart
    
    def testCfgIsMap(self):
        """Configuration shall be stored in dictionary"""
        self.assertTrue(isinstance(FsmTests.testCfg, dict))
    def testCfgHasInitState(self):
        """Configuration shall have a initialState"""
        self.assertTrue('initState' in FsmTests.testCfg)
    def testInitStateHaveNextState(self):
        """Initial state shall have at least one succesor state"""
        initKey = FsmTests.testCfg['initState']
        self.assertTrue(FsmTests.testCfg['stateList'][initKey][eventKeys.nextStates.value] != [])
    def testInistalStateNotHavePrevState(self):
        """Initial state may not have previous state"""
        initKey = FsmTests.testCfg['initState']
        self.assertTrue(FsmTests.testCfg['stateList'][initKey][eventKeys.prevStates.value] == [])
   
#Manage argvars to run unittests      
def mainTest():
    argsTemp = list(sys.argv)
    del sys.argv[1:]
    unittest.main()
    sys.argv = argsTemp
    
#RUN as script
if __name__ == "__main__":
    print("\n\n***RUN AS MAIN***\nRun as script with arglist: " + '\n' + str(sys.argv))
    argMap = utils.parseCmdArgs()
    if(utils.testNeeded(argMap)):
        print('Run Unit Tests')
        mainTest()
    else:
        print('No test running')  