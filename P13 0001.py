###p13 0001
## librarys
import time
##defined variables

active = 0

##functions of use
def activate(statment):
    global active
    acceptstatments = ["hey p1", "p1", "p13", "pie", "robobot"]
    for i in range(0, len(acceptstatments)):
        if statment == acceptstatments[i]:
            active = 1
            speak("system activated. issue command")
        else:
            continue

def speak(x):
    import pyttsx3
    text_speech = pyttsx3.init()
    text_speech.say(x)
    text_speech.runAndWait()

#def search(statment):
class Gsearch_python:
    def __init__(self,name_search):
        self.name = name_search
    def Gsearch(self):
        count = 0
        try :
            from googlesearch import search
        except ImportError:
            print("No Module named 'google' Found")
        for i in search(query=self.name,tld='co.in',lang='en',num=10,stop=1,pause=2):
            count += 1
            print (count)
            print(i + '\n')
#        if __name__=='__main__':


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
    
def search(statment):
    gs = Gsearch_python(statment)
    speak("searching")
    gs.Gsearch()
    speak("link found")

def searchyoutube(statment):
    narrowsearch = "youtube " + statment
    search(narrowsearch)

def searchnetflix(statment):
    narrowsearch = "netflix" + statment
    search(narrowsearch)


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
            speak("i was born 5/6/22 at aproximatly 2pm, you do the math")
        if statment == "gimme a link":
            speak("which link")
            search(input())
            print("control click link to open")
        if statment == "youtube please":
            speak("okay, what would you like to watch")
            searchyoutube(input())
        if statment == "netflix please":
            speak("what would you like to watch")
            searchnetflix(input())
        


##implimentation of functions in if statments and for loops
while True:
    activate(input())
    while active == 1:
        time.sleep(1)
        request(input())