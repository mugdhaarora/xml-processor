
import os, glob

#read file of file type from path specifed
def readFiles(path, filetype): 
    all_files = glob.glob(path + filetype,recursive=True)
    if len(all_files) ==0:
        print("Data folder is empty,no files with XML extension are not found")
    else:
        print(all_files)
    return all_files