import os
import re

filepath = "D:\JenkinsHome\workspace\PipelineOne\[REALEASE]"
files = os.listdir(filepath)
sorted_files = sorted(files)
for file in sorted_files[10:]:
    os.remove(file)
