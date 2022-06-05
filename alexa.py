###p13 0001
## librarys
import time
##defined variables

active = 0

##functions of use
def speak(x):
    import pyttsx3
    text_speech = pyttsx3.init()
    text_speech.say(x)
    text_speech.runAndWait()

def activate(statment):
    global active
    acceptstatments = ["hey p1", "p1", "p13", "pie", "robobot"]
    for i in range(0, len(acceptstatments)):
        if statment == acceptstatments[i]:
            active = 1
            speak("system activated. issue command")
        else:
            continue
def calculate(statment):
    speak("input operation")
    symbol = input()
    speak("input x and y")
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

def countdown():
    for i in range(10,0,-1):
        speak(i)
        time.sleep(1)
    




def request(statment):
    if active == 1:
        if statment == "hello":
            speak("good day")
        if statment == "calculate something":
            calculate(statment)
        if statment == "e":
            while True:
                speak("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        if statment == "kill yourself":
            speak("uno reverse card, mother ducker")
            exit()
        if statment == "deploy missles":
            speak("initiateing missl launch protocal")
            countdown()
            speak("gotcha")
        if statment == "thanks":
            speak("it is in my programming to be a good algorithm")
        if statment == "shutdown":
            speak("bye,, initiating shut down sequence")
            time.sleep(0.5)
            exit()
        if statment == "what is your name":
            print("p13 0001")
            speak("my name is p13 0001 but you can call me p1 or p13")
        if statment == "how old are you":
            speak("i was born 6/6/22 at aproximatly 2pm, you do the math")
        

        


##implimentation of functions in if statments and for loops
#activate p1
while True:
    activate(input())
    while active == 1:
        time.sleep(1)
        request(input())