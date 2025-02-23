#todo python files detection

import os

file_name = "C:\\Users\\Senthur\\Desktop\\NewGit"

if os.path.exists(file_name):
    print("file exists")
else:
    print("file does not exist")

if os.path.isfile(file_name):
    print("file is a regular file")
elif os.path.isdir(file_name):
    print("file is a directory")
else:
    print("file is a special file (socket, FIFO, device file)")
