def process_file(filename):
    print(filename)
    with open(filename) as fh:
        content = fh.read()
   
    result = 100 / int(content)
    print(f"100 / {content}  = {result}")


# def process_file(filename):
#     print(filename)
#     try:
#         with open(filename) as fh:
#             content = fh.read()
#     except FileNotFoundError:
#         print(f"File {filename} was not found")
#         return

#     if int(content) == 0:
#         print("Can't divide by zero")
#         return
    
#     result = 100 / int(content)
#     print(f"100 / {content}  = {result}")
