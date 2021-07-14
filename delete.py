import os
files = "D:\JenkinsHome\workspace\PipelineOne\[REALEASE]"
for file in files[7:]:
    os.remove(file)
