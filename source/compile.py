
import os
import shutil
import compileall

from utilities import *

DIR = get_dir()
DIR_SRC = DIR + "source\\"
DIR_CACHE = DIR_SRC + "__pycache__\\"
DIR_BUILD = DIR + "build\\"

"""
    ******************************************************************************

    Module: compile
    
    Description: Is called from a batch file, will compile the project source into
    bytecode, which can be launched from launch.exe.
    
    Author: Jason Milhaven
    
    History: 
    
    ******************************************************************************
"""

if os.path.exists(DIR_BUILD):
    shutil.rmtree(DIR_BUILD)
else:
    os.makedirs(DIR_BUILD)

compileall.compile_dir(DIR_SRC, DIR_BUILD, force=True)

for f in os.listdir(DIR_CACHE):
    if "compile" not in f:
        newF = f.replace(".cpython-35", "")
        os.rename(DIR_CACHE + f, DIR_BUILD + newF)