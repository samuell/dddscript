'''
Created on Aug 17, 2012

@author: samuel
'''

import subprocess, re

class Command(object):
    '''
    Convenience class for creating and running commands 
    (system calls) in different ways.
    '''

    def __init__(self, command_txt):
        '''
        Constructor
        '''
        # command_txt = self.escape_unallowed_chars(command_txt)
        command_lst = command_txt.split(" ")
        command_lst = self.escape_unallowed_chars(command_lst)
        self.command = command_lst
        
    def run_with_output(self):
        proc = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (stdout, stderr) = proc.communicate()
        return (stdout, stderr)

    def escape_unallowed_chars(self, command_lst):
        for i, part in enumerate(command_lst):
            part = part.strip()
            command_lst[i] = ''.join(c for c in part if c.isalnum()) 
        return command_lst

