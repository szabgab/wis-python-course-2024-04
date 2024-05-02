
def display(area):
    print(f"The area is {area}")

def main():
    length = input("Length: ")
    width = input("Width: ")

    area = int(length) * int(width)
    display(area)


main()
