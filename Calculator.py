# Imports



import math          # behöver för att kuna använd pi korrekt samt eulers numer (e)
import time  #time.sleep
import os

# clearconsol.

# Global variables

# Classes
class Name:
    def __init__(self, name) -> None:
        self.name = name


# Functions
def cs():
    """
    denna funktion gör så att det ser lite bättre ut och att allt inte ska komma på en gång, gjorde funktionen för att det skulle gå lite långsammare
    Inputen är 'time.sleep' vilket gör så att programmet väntar lite innan nästa funktion körs igång och
    'os.system' vilket gör så att consolen blir ren och det gör det lättare att se vad som händer.
    """
    time.sleep(2)
    os.system('Clear')

def name():
    name = input("write your name and klick ENTER to start. ")
    user = Name(name)
    main(user)

def mainmain():
    """
    här är sidomenyn, jag har 2 som är ungefär lika dana eftersom jag inte vet hur man kan ta bort en sak ur en funktion efter den 
    har använts en gång. gjorde 2 olika metoder som gör samma bara att hen här inte har 'welcome' och den har 'press '#' if you want to quit'.
    den här funktionen tillåter dig enbart att välja hur du vill calkulera.
    """
    while True:
        print("""how would you like to calculate?
            [1] Addition
            [2] Subbtrakton
            [3] Multiplikation
            [4] Divitions
            [5] percantage
            [6] Square
            [7] e^x
            [8] pi
            [#] press '#' if you want to quit.
            """)
        number = input("Chose a number: ")
        if "1" == number:
            addition()
            cs()
        elif "2" == number:
            subbtraktion()
            cs()
        elif "3" == number:
            multiplikation()
            cs()
        elif "4" == number:
            divition()
            cs()
        elif "5" == number:
            percentage()
            cs()
        elif "6" == number:
            square()
            cs()
        elif "7" == number:
            e()
            cs()
        elif "8" == number:
            pi()
            cs()
            break
        elif "#" == number:
            visit_saveeverything()
        else:
            print("sir/ma'ma, please insurt a number")


def main(user):   
    """
    först menyn, tillåter dig att välja vad du vill calculera.
    """
    print(f"\n\nwelcome {user.name}\n")
    while True:
        print("""how would you like to calculate?
            [1] Addition                                                    
            [2] Subbtrakton
            [3] Multiplikation
            [4] Divitions
            [5] percantage
            [6] Square
            [7] e^x
            [8] pi
            """)
        number = input("Chose a number: ")
        if "1" == number:
            addition()
            cs()
        elif "2" == number:
            subbtraktion()
            cs()
        elif "3" == number:
            multiplikation()
            cs()
        elif "4" == number:
            divition()
            cs()
        elif "5" == number:
            percentage()
            cs()
        elif "6" == number:
            square()
            cs()
        elif "7" == number:
            e()
            cs()
        elif "8" == number:
            pi()
            cs()
            break
        else:
            print("sir/ma'ma, please insurt a number")

def addition():
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        number_choice = int(input("insurt a number: "))
        number_yes = int(input("insurt a nother number: "))
        number_addition = number_choice + number_yes
        number_combine = (f"{number_choice} + {number_yes} = {number_addition}")
        print(number_combine)
        sav.write(number_combine + "\n")    
        sav.close()
        cs()
        mainmain()


def subbtraktion():
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        number_Choice = int(input("insurt a number: "))
        number_yes = int(input("insurt a nother number: "))
        number_subbtraktion = number_Choice - number_yes
        number_combine = (f"{number_Choice} - {number_yes} = {number_subbtraktion}")
        print(number_combine)
        sav.write(number_combine + "\n")
        sav.close()
        cs()
        mainmain()


def multiplikation():
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        number_choice = int(input("insurt a number: "))
        number_yes = int(input("insurt a nother number: "))
        number_multiplikation = number_choice * number_yes
        number_combine = (f"{number_choice} * {number_yes} = {number_multiplikation}")
        print(number_combine)
        sav.write(number_combine + "\n")
        sav.close()
        cs()
        mainmain()

def divition():
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        number_choice = int(input("insert a number: "))
        number_yes = int(input("insert a nother number: "))
        number_divition = number_choice / number_yes
        number_divition1 = number_choice // number_yes     #rundar av exempelvis om det blir 0,6 eller 0,9 så rundas det ned till 0.
        number_combine = (f"{number_choice} / {number_yes} = {number_divition}")
        number_combine1 = (f"Rounded down: {number_choice} / {number_yes} = {(number_divition1):.2f}") #":.2f" genom att skriva detta så avrundar datorn talet till 2 decimaler.
        print(number_combine)
        print(number_combine1)
        sav.write(number_combine + "\n")
        sav.write(number_combine1 + "\n")
        sav.close()
        cs()
        mainmain()



def percentage():
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        print("how much is x percent of y")
        x = int(input("insurt x: "))
        y = int(input("insurt y: "))
        xy = x / y
        times=xy
        time = times * 100
        percent = (f"{x} is {time:.3f}% out of {y}")
        print(percent)
        sav.write(percent + "\n")
        sav.close()
        cs()
        mainmain()


def square():
    """
    math.sqrt göt bara att man kan ta roten ur ett tal som användaren får välje.
    """
    number_square = int(input("insurt a number to Square root OBS x > 0: "))
    print(math.sqrt(number_square))
    mainmain()

def e():
    """
    här har jag använt mig av math.e vilket ger ett par desimaler från konstanten e.
    """

    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        print("write what you want in x (e^x): ")
        number_x = int(input(" "))
        number_e = math.e ** number_x
        oliver = (f"e^{number_x} = {number_e}")
        print(f"e^{number_x} = {number_e}")
        sav.write(oliver + "\n")
        sav.close()
        cs()
        mainmain()


def pi(user):
    """
    jag importa math eftersom jag ville använda math.pi vilket ger hela eller många desimaler av pi.
    """
    print("""
    [1] pi^
    [2] ^pi
    [3] /pi
    [4] pi/
    [5] *pi
    [6] +pi
    [7] -pi
    [8] pi-
    """)
    number_x = input("write what you want to to with pi ")
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        if "1" in number_x:
            print("pi^x, write your x: ")
            a = int(input(" "))
            py1 =  math.pi ** a
            lukas = (f"pi^{a} = {py1}")
            print(f"pi^{a} = {py1}")
            sav.write(lukas + "\n")
            mainmain(user)

        elif "2" in number_x:
            print("x^pi, write your x: ")
            b = int(input(" "))
            py2 = b ** math.pi
            albion = (f"{b}^pi = {py2}")
            print(f"{b}^pi = {py2}")
            sav.write(albion + "\n")
            mainmain(user)
        
        elif "3" in number_x:
            print("x/pi, write your x: ")
            c = int(input(" "))
            py3 = c / math.pi
            py35 = c // math.pi
            zion = (f"{c}/pi = {py3} ~ {py35}")
            print(f"{c}/pi = {py3} ~ {py35}")
            sav.write(zion + "\n")
            mainmain(user)

        elif "4" in number_x:
            print("pi/x, write your x: ")
            d = int(input(" "))
            py4 = math.pi / d
            py45 = math.pi // d
            alexis = (f"pi/{d} = {py4} ~ {py45}")
            print(f"pi/{d} = {py4} ~ {py45}")
            sav.write(alexis + "\n")
            mainmain(user)

        elif "5" in number_x:
            print("x*pi, write your x ")
            e = int(input(" "))
            py5 = e * math.pi
            victor = (f"{e}*pi = {py5}")
            print(f"{e}*pi = {py5}")
            sav.write(victor + "\n")
            mainmain(user)

        elif "6" in number_x:
            print("x+pi, write your x ")
            f = int(input(" "))
            py6 = f + math.pi
            jakob = (f"{f} + pi = {py6}") 
            print(f"{f} + pi = {py6}")
            sav.write(jakob + "\n")
            mainmain(user)

        elif "7" in number_x:
            print("x-pi, write your x: ")
            g = int(input(" "))
            py7 = g - math.pi
            max = (f"{g} - pi = {py7}")
            print(f"{g} - pi = {py7}")
            sav.write(max + "\n")
            mainmain(user)

        elif "8" in number_x:
            print("pi-x, write your x: ")
            h = int(input(" "))
            py8 = math.pi - h
            tim = (f"pi - {h} = {py8}")
            print(f"pi - {h} = {py8}")
            sav.write(tim + "\n")
            mainmain(user)
        
        else:
            mainmain(user)
    sav.close()

def visit_saveeverything():
    """
    Den här funktionen är enbart så man kan gå tillbaka för att kolla vilka uträkningar man har gjort tidigare.
    Jag frågar först om användaren vill avsluta eller inte, om de vill kommer man hitt och sedan kan man välja om man vill avluta eller ej.
    om man inte vill kommer man tillbaka till 'huvudsidan' """
    with open("saveeverything.txt", "r", encoding="utf8") as sav:
        x = input("do you want to se what you have been calculated? (y/n)")
        if "y" in x:
            for s in sav.readlines():
                print(s)
            input(" ")
        
        else:
            y = input("whould you like to quit or continu? (q/c)")
            if "c" in y:
                mainmain()  #huvudsidan
            else:
                quit()
# fil som sparar allt man har räknat ut. och som kan hämta tillbak datan.
#
# Main-caller


if __name__ == "__main__":
    name()
    
    
