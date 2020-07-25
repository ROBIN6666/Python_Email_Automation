# Getting the Files and Folder as per requirements

import os
import shutil
import sys


def find_file_with_ext(directory, extension, new_zip_file_name):
    global folder_name, new_zip
    try:
        all_files = os.listdir(directory)
        if len(all_files) == 0:
            print(f"The given path is empty")
        else:
            # req_ex=input("Enter the file Extension you want")
            req_ex = extension
            folder_name = os.path.join(directory, new_zip_file_name)
            os.mkdir(folder_name)
            for file in all_files:
                # print(files)
                if file.endswith(req_ex):
                    shutil.copyfile(os.path.join(directory, file), os.path.join(folder_name, file))
            shutil.make_archive(os.path.join(directory, new_zip_file_name), "zip", folder_name)
        shutil.rmtree(folder_name)

        for zip_file in os.listdir(directory):
            if zip_file.startswith(new_zip_file_name):
                new_zip = os.path.join(directory, zip_file)
        return new_zip
    except Exception as e:
        print('Error: line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
