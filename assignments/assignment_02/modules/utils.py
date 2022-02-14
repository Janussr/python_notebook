import os
import argparse


""" takes a path to a folder and writes all filenames in the folder to a specified output file"""
def get_file_names(folderpath,out="output.txt"):
   with open(out, 'w') as file_object:
     for f in os.listdir(folderpath):
        file_object.write(f + "\n")


"""takes a path to a folder and write all filenames recursively (files of all sub folders too)"""
def get_all_file_names(folderpath,out="output.txt"):
    with open(out, 'w') as file_object:
      for (root, dirs, files) in os.walk(folderpath):
        file_object.write("".join(files) + '\n')
    
"""takes a list of filenames and print the first line of each"""
def print_line_one(file_names, folderpath):
    for file in os.listdir(folderpath):
        with open(file) as file_object:
         print(file_object.readline())


"""takes a list of filenames and print each line that contains an email (just look for @)"""
def print_emails(folderpath):
    for file in os.listdir(folderpath):
        with open(file) as file_object:
            for line in file_object.readlines():
                if '@' in line: print(line)


"""takes a list of md files and writes all headlines (lines starting with #) to a file"""
def write_headlines( folderpath,md_files, out="output.txt"):
    for file in os.listdir( folderpath):
        if file.endswith('md'):
            with open(file) as fileObject:
                for line in fileObject.readlines():
                    if line.startswith('#'):
                        with open(out, 'w'):
                            out.write(line + '\n')


if __name__ == '__main__':
    #1get_file_names('/home/jovyan/my_notebooks')
    #2get_all_file_names('/home/jovyan/my_notebooks')
    #3print_line_one
    print("hello world")