

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def calculator():
    print("CALCULATOR")
    num1 = int(input("What's the first number? "))

    should_continue = True

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation = input("Pick and operation from the line above: ")

        num2 = int(input("What's the next number? "))

        answer = 0
        for symbol in operations:
            if(symbol == operation):
                answer = operations[symbol](num1,num2)

        print(f"{num1} {operation} {num2} = {answer}")

        check = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start over: ")

        if check == "y":
            num1 = answer
        elif check == "n":
            should_continue = False
            calculator()
        else:
            should_continue = False


calculator()