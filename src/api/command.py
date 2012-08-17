'''
Created on Aug 17, 2012

@author: samuel
'''

import subprocess

class Command(object):
    '''
    Convenience class for creating and running commands 
    (system calls) in different ways.
    '''


    def __init__(self, command_text):
        '''
        Constructor
        '''
        self.command = command_text
        
    def run_with_output(self):
        proc = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (stdout, stderr) = proc.communicate()
        stdout = stdout.rstrip("\n")
        stderr = stderr.rstrip("\n")
        return (stdout, stderr)
