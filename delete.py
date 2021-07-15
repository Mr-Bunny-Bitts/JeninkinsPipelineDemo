import os
import re

filepath = "D:\\JenkinsHome\\workspace\\PipelineOne\\[REALEASE]\\*.zip"
files = os.listdir(filepath)

sorted_files = sorted(files,key=os.path.getmtime, reverse=False)


for files in (sorted_files):
	
	os.remove(files)
	files1 = os.listdir(filepath)
	sorted_files = sorted(files1,key=os.path.getmtime, reverse=False)
	count=len(sorted_files)
	print (count)
	if count <=10:
		break;
