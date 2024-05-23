import sys
from mylib import process_file

def main():
    #print(sys.argv)
    for filename in sys.argv[1:]:
        try:
            process_file(filename)
        # except FileNotFoundError:
        #     print(f"File {filename} was not found")
        # except ZeroDivisionError:
        #     print("Can't divide by zero")
        #     #break
        except Exception as err:
            print(f"There was some other exception: {err}")



# def main():
#     #print(sys.argv)
#     for filename in sys.argv[1:]:
#         try:
#             process_file(filename)
#         except FileNotFoundError:
#             print(f"File {filename} was not found")
#         except ZeroDivisionError:
#             print("Can't divide by zero")
#             #break



main()