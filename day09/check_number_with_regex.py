import sys
import re

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} NUMBER")

#try:
#    number = int(sys.argv[1])
#except Exception:
#    exit("bad thing happened")

# if re.search(r'[0-9]', sys.argv[1]): # there is a digit somewhere in the string
# if re.search(r'^[0-9]$', sys.argv[1]): # there is exactly one character in the string and it is a digit
if re.search(r'^[0-9]+$', sys.argv[1]): # there are 1 or more digits in the string and nothing else
#if re.search(r'^\d+$', sys.argv[1]): # One or more unicode digits
    number = int(sys.argv[1])
else:
    exit(f"incorrect input '{sys.argv[1]}'")


print(number)
