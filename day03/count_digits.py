def count_digits(text):
    # counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    counter = [0] * 10
    # print(text)
    for ch in text:
        # print(ch)
        # if ch == " ":
        #     continue
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
    text = "12=34 1119"
    digit_counter = count_digits(text)

    display(digit_counter)

main()

