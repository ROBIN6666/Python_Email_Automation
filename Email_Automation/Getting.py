#Getting the Files and Folder as per requirements

import os
from zipfile import ZipFile
dir_path = input("Please Enter the directory path")
Files_with_Ex=[]
if os.path.isfile(dir_path):
   print(f"Sorry user please enter the directory path")
else:
     all_files=os.listdir(dir_path)
     if len(all_files)==0:
        print(f"The given path is empty")
     else:
        req_ex=input("Enter the file Extension you want")
        for files in all_files:
             print(files)
             if files.endswith(req_ex):
                 Files_with_Ex.append(files)
     print(Files_with_Ex)


   
