import os
import re

filepath = os.getcwd()
files = os.listdir("D:\JenkinsHome\workspace\PipelineOne\[REALEASE]")
files = sorted(files,key=os.path.getmtime)
for file in files[:11]:
    os.remove(file)
