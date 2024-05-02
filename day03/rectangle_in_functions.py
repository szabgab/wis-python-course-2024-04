
def display(data):
    print(f"The area is {data}")

def main():
    length = input("Length: ")
    width = input("Width: ")

    area = int(length) * int(width)
    display(area)


main()
