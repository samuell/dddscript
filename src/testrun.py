'''
Created on Aug 17, 2012

@author: samuel
'''

from dddscript import *

cmd = Command("echo hej")
(stdout, stderr) = cmd.run_with_output()
print("Output: " + stdout)