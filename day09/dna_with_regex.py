import sys
import re

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} SEQUENCE")

#if re.search(r'(.+).*\1', sys.argv[1]):
match = re.search(r'([GATC]{2}).*\1', sys.argv[1])
if match:
    word = match.groups(1)
else:
    exit(f"not found in input")

print(word)


