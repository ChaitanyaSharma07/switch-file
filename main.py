print("This is an interface for you to switch contents along with the")
print("option to write to file")

print("press 's' to start the program")

def write_and_read():
    file_inp = str(input("Enter the name of the file to which you would like to write: "))
    action_inp = str(input("Enter the action you would like to perform(read/write): "))

    if action_inp == "write":
        write_inp = input("Enter what you would like to write to the file: ")
        print("-----------------------------")
        with open(file_inp, 'w+') as v:
            v.writelines(write_inp)

    elif action_inp == "read":
        print("-----------------------------")
        with open(file_inp, 'r') as v:
    
            print("The contents of the file are " + str(v.readlines()))

def switch():
    file1 = input("enter files name:- ")
    file2 = input("enter files name:- ")


    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file2, 'r') as b:
        data_b = b.read()

    with open(file2, 'w') as c:
        c.write(data_a)

    with open(file1, 'w') as d:
        d.write(data_b)



def start():
    print("if you would like to write to file write the word 'write' in the console")
    print("----------------------------------------")

    print("if you would like to switch the contents of the file write the word 'switch' in the console")
    print("----------------------------------------")



while True:
    inp = input("")

    if inp == "s":
        start()
    elif inp == "write":
        write_and_read()
    elif inp == "switch":
        switch()
    
    