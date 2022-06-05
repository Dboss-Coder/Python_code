###p13 0001
## librarys
import time
##defined variables
trigger = 0
active = 0

##functions of use
def activate(statment):
    global active
    acceptstatments = ["hey p1", "p1", "p13", "pie", "robobot"]
    for i in range(0, len(acceptstatments)):
        if statment == acceptstatments[i]:
            active = 1
            print("boop beep")
        else:
            continue
def calculate(statment):
    symbol = input("symbol?    ")
    x = int(input("x    "))
    y = int(input("y    "))
    if symbol in ["+", "-", "*", "/"]:
        if symbol == "+":
            print(x + y)
        if symbol == "-":
            print(x - y)
        if symbol == "*":
            print(x * y)
        if symbol == "/":
            print(x / y)
    else:
        print("?")

      
def request(statment):
    if active == 1:
        if statment == "hello":
            print("bweep boo")
        if statment == "calculate something":
            calculate(statment)
        


##implimentation of functions in if statments and for loops
#activate p1
activate("hey p1")
time.sleep(1)
request(input("say something:      "))