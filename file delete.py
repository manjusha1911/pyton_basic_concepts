'''
To avoid getting an error, you might want to check if the file exists before you try to delete it:
'''


import os
# os.remove("delete.txt")
# os.remove("deletefile.txt")

if os.path.exists("delete.txt"):
    os.remove("delete.txt")
else:
    print("this file doesn't exist")