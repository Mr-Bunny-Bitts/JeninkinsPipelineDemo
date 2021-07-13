from random import sample
import os

files = os.listdir('D:\JenkinsHome\workspace\PipelineOne\[REALEASE]')
for file in sample(files,11):
    os.remove(file)
