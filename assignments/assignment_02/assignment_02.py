import csv
import platform
import argparse

"""Exercise 1
    Create a python file with 3 functions:
        def print_file_content(file) that can print content of a csv file to the console
        def write_list_to_file(output_file, lst) that can take a list or tuple of strings and write each element to a new line in file
            rewrite the function so that it gets an arbitrary number of strings instead of a list
        def read_csv(input_file) that take a csv file and read each row into a list. Print the list.
        
    
"""
#func 1
filename = './text.csv'

def func_read_from_csv(filename):

    with open(filename) as f_obj:
     content = f_obj.readlines()

    for line in content[:20]:
     print(line.strip().split(','))

#print(func_read_from_csv(filename))


#func 2
list_new = ["42","42232","haweha","jawioea"]

def write_list_to_file(output_file, lst):
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None
    with open(output_file, 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        output_writer.writerow(lst)
#print(write_list_to_file(filename, list_new))

#func 2.5

string1 = "hej med dig Julius"
string2 = "hej med dig thor"
string3 = "hej med dig sigurd"

def print_file_content(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
      #  print(header_row)

# func that takes an unlimited amount of strings as arguments and then print them to agiven csv file.
def write_strings_to_file(output_file, *strings):
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None
    with open(output_file, 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        output_writer.writerow(strings)
#print_file_content(filename)
#write_strings_to_file(filename, string1, string2, string3)


#func 3
def func_read_from_csv_to_list(filename):
    with open(file) as f_obj:
        content = f_obj.readlines()
    return content


"""
Add a functionality so that the file can be called from cli with 2 arguments:
path to csv file
an argument --file file_name that if given will write the content to file_name or otherwise will print it to the console.
Add a --help cli argument to describe how the module is used
"""

#func 4

parser = argparse.ArgumentParser()

# Prints the content of any given csv file to the console. 
def print_file_content(file):
    parser.add_argument('-file', help = "Enter path to file.")
    args = parser.parse_args()
    print(file)
    with open(args.file) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        print(header_row)

print_file_content("")
