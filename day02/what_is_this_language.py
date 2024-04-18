
#if language.lower() == "python":
#print(language.capitalize)  # built-in method because we forgot yo add parentheses () 
#print(language.capitalize())

language = ""

while language.capitalize() != "Python":
    language = input("What is this programming language? ")

    if language.capitalize() == "Python":
        print(f"You are right it is {language}")
        print("still here")
    else:
        print("Not good")

# the better verion is the DRY version (Do not repeate yourself)

# while True:
#     language = input("What is this programming language? ")

#     if language.capitalize() == "Python":
#         print(f"You are right it is {language}")
#         print("still here")
#         break
#     else:
#         print("Not good")

print("done")


