def count_digits(text):
    # counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    counter = [0] * 10
    # print(text)
    for ch in text:
        # print(ch)
        counter[int(ch)] += 1
    return counter

def main():
    text = "12341119"
    digit_counter = count_digits(text)

    #print(digits)
    for digit in range(0, 10):
        print(digit, digit_counter[digit])


main()