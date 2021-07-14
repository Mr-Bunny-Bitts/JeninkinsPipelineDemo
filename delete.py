import os
files = os.listdir("C:\\Users\\HP\\Desktop\\SDPM\\")
for file in files[3:]:
    os.remove(file)
