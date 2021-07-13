from random import sample
import os

files = os.listdir('D:\\JenkinsHome\\workspace\\PipelineOne\\[REALEASE]\\*.zip')
for file in sample(files,11):
    os.remove(file)
