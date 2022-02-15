import argparse

from modules import webget

if __name__ =="__main__":
    parser= argparse.ArgumentParser(description='A program that downloads a URL and stores it locally')
    parser.add_argument('url', help='an integer for the accumulator')
    parser.add_argument('--destination', help='The name of the file to store the url in')

print(parser.parse_args())