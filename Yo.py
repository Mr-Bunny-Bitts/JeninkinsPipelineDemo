import os
import re

filepath = os.getcwd()
files = os.listdir(filepath)
files = sorted(files,key=os.path.getmtime)
for file in files[:11]:
    os.remove(file)
