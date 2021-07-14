import os
files = os.listdir("D:\JenkinsHome\workspace\PipelineOne\[REALEASE]")
for file in files[11:]:
    os.remove(file)
