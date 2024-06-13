import sys
import re

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} WORD")

if re.search(r'(.)\1', sys.argv[1]): # match two characters one-after-the-other that are the same
    word = sys.argv[1]
else:
    exit(f"incorrect input '{sys.argv[1]}'")


print(word)


# loop
# cat

