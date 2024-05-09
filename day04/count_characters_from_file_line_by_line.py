import sys

def count_characters(filename):
    counter = {}

    with open(filename) as fh:
        for line in fh:
            line = line.rstrip()
            # print(f"line: {line}")
            for ch in line:
                # if ch == "\n":
                #     continue
                if ch not in counter:
                    counter[ch] = 1
                else:
                    counter[ch] += 1
                
    return counter

def display(counter):
    # print(counter)
    for character in sorted(counter.keys()):
        # print(character, counter[character])
        print(f"'{character}' {counter[character]}")

def main():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} FILENAME")

    filename = sys.argv[1]
    counter = count_characters(filename)

    display(counter)

main()

