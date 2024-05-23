import sys
from mylib import process_file

def main():
    #print(sys.argv)
    for filename in sys.argv[1:]:
        process_file(filename)


main()