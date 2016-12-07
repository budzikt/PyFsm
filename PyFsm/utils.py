'''
Created on 07.12.2016

@author: Tomek
'''
import argparse
import sys

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