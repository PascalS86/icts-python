bot = { "name":"Pyhton bot" }

print("Hello, my name is " + bot["name"])

message = input()

if "Hello" in message:
    print("Do you want to know the zen of python?")

    message = input()

    if "yes" in message:
        import this
    else:
        print("Do you want to know the answer of everything?")
        message = input()

        if "yes" in message:
            print(42)
        else:
            print("Well, than i cannot help you")


else:
    print("I'm sorry, i didn't get that.")

print("Bye now")