# Our quiz!


def quiz():

    question1()
    question2()
    question3()
        
    

def question1():
    global score

    print("who is the jedi in the force awakens")
    print("A. Yoda")
    print("B. Rey")
    print("C. Finn")
    answer = input("Chose an option: ")

    if answer.lower() == "b":
        print("The force is strong with this one...you succeded")

    else:
        print("Do or do not there is no try...you failed")


def question2():
    global score

    print("who is rey's parents")
    print("A. darth vader")
    print("B. obi wan kenobi")
    print("C. jaba the hut")
    print("D. none of the above")
    answer = input("Chose an option: ")

    if answer.lower() == "d":
        print("The force is strong with this one...you succeded")

    else:
        print("Do or do not there is no try...you failed")


def question3():
    global score

    print("who is the most powerful jedi")
    print("A. darth vader")
    print("B. obi wan kenobi")
    print("C. yoda")
    answer = input("Chose an option: ")

    if answer.lower() == "c":
        print("The force is strong with this one...you failed")

    else:
        print("Do or do not there is no try...you failed")

    

    

    





# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
