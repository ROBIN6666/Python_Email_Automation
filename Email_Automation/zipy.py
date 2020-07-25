# importing required modules
from zipfile import ZipFile
import os
def main():
 
 file_paths = []
 directory = 'D:\Working_logs'
 for root, directories, files in os.walk(directory):
      for filename in files:
         filepath = os.path.join(root, filename)
         file_paths.append(filepath)

 # writing files to a zipfile
 with ZipFile('myzipfile.zip','w') as zip:
  # writing each file one by one
  for file in file_paths:
     print(file)
     zip.write(file)

 print('All files zipped successfully!')


if __name__ == "__main__":
    main()