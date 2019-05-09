bot = { "name":"Pyhton bot", "last_message": "" }

def hello ():
    bot["last_message"] = "Hello, my name is " + bot["name"]
    write_answer()

def write_answer():
    print(bot["last_message"] )

def create_response(n_message=""):
    if "Hello" in n_message:
        bot["last_message"] = "Do you want to know the zen of python?"
        write_answer()
    elif "Bye" in n_message:
        bot["last_message"] = "Bye now"
        write_answer()
    elif "yes" in n_message:
        if bot["last_message"] == "Do you want to know the zen of python?":
            import this
        elif bot["last_message"] == "Do you want to know the answer of everything?":
            bot["last_message"] = "42"
            write_answer()
    else:
        if bot["last_message"] == "Do you want to know the zen of python?":
            bot["last_message"] = "Do you want to know the answer of everything?"
            write_answer()
        elif bot["last_message"]== "Do you want to know the answer of everything?":
            bot["last_message"] = "Well, than i cannot help you"
            write_answer()
        else:
            bot["last_message"] = "I'm sorry, i didn't get that."
            write_answer()
       

def start_dialog():
    hello()
    while True:
        message = input()
        create_response(n_message=message)
        if bot["last_message"] == "Bye now":
            break

start_dialog()

