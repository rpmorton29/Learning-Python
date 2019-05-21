loop = True
while loop == True:

    data = input("Please enter the Math Expression you would liked solved: ") #input of the math
    first, op, second = data.split(" ")
    error = False

    if op == '+':
        output = int(first) + int(second)
    elif op == "-":
        output = int(first) - int(second)
    elif op == "*":
        output = int(first) * int(second)
    elif op == "/":
        if second == '0':
            print("Error division by zero")
        else:
            output = int(first) / int(second)
    elif op == "//":
        if second == '0':
            print("Error division by zero")
        else:
            output = int(first) // int(second)
    elif op == "%":
        if second == '0':
            print("Error division by zero")
        else:
            output = int(first) % int(second)
    elif op == "**":
        output = int(first) ** int(second)

    if error == False:
        print(first, op, second, " = ", output)
    else:
        error = True


    answer = input("would you like to preform another Operation Y/N: ")


    if answer.lower() == "y":
        loop = True
    elif answer.lower() == "n":
        loop = False




