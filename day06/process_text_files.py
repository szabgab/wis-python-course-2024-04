import sys

def main():
    #print(sys.argv)
    for filename in sys.argv[1:]:
        process_file(filename)

def process_file(filename):
    print(filename)
    try:
        with open(filename) as fh:
            content = fh.read()
    except FileNotFoundError:
        print(f"File {filename} was not found")
        return

    result = 100 / int(content)
    print(f"100 / {content}  = {result}")

main()