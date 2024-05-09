import sys

def count_digits(text):
    counter = [0] * 10
    for ch in text:
        if not ch.isnumeric():
            continue
        index = int(ch)
        counter[index] += 1
    return counter

def display(digit_counter):
    #print(digits)
    for digit in range(0, 10):
        print(digit, digit_counter[digit])

def main():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} FILENAME")

    filename = sys.argv[1]
    with open(filename) as fh:
        text = fh.read()

    digit_counter = count_digits(text)

    display(digit_counter)

main()

