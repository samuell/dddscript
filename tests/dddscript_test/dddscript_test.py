'''
Created on Aug 17, 2012

@author: samuel
'''

from dddscript import *

def test_evil_command_fail():
    cmdpart1 = "echo "
    cmdpart2 = "'some SQL injection'"
    cmd = Command(cmdpart1 + cmdpart2)
    out,err = cmd.run_with_output()
    cmdpart2tmp = cmdpart2.strip("'")
    out = out.strip()
    assert out == cmdpart2tmp 
        