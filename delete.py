import os
import re

filepath = "D:\JenkinsHome\workspace\PipelineOne\[REALEASE]"
files = os.listdir(filepath)
files = sorted(files,key=os.path.getmtime)
for file in files[10:]:
    os.remove(file)
