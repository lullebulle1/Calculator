# Imports



import math

# behöver för att kuna använd api korrekt samt eulers numer (e)
import sympy as sp  # för derivering.
import time  # time.sleep
import os


# clearconsol.
# Global variables

# Classes
class Name:
    def __init__(self, name) -> None:
        self.name = name


# Functions
def cs():
    time.sleep(2)
    os.system('Clear')

def visit_saveeverything():
    with open("saveeverything.txt", "r", encoding="utf8") as sav:
        for elev in sav.readlines():
            print(elev)
        input(" ")
            

def name():
    name = input("write your name and klick ENTER to start. ")
    user = Name(name)
    main(user)


def main(user):
    print(f"\n\nwelcome {user.name}\n")
    visit = input("do you want to se what you have been calculating? (y/n) ")
    if "y" in visit:
        visit_saveeverything()
    else:
        pass
    while True:
        print("""how would you like to calculate?
            [1] Addition
            [2] Subbtrakton
            [3] Multiplikation
            [4] Divitions
            [5] percantage
            [6] Square
            [7] Derivaties
            [8] e^x
            [9] pi
            """)
        number = input("Chose a number: ")
        if "1" == number:
            addition(user)
            cs()
        elif "2" == number:
            subbtraktion(user)
            cs()
        elif "3" == number:
            multiplikation(user)
            cs()
        elif "4" == number:
            divition(user)
            cs()
        elif "5" == number:
            percentage(user)
            cs()
        elif "6" == number:
            square(user)
            cs()
        elif "7" == number:
            derivaties(user)
            cs()
        elif "8" == number:
            e(user)
            cs()
        elif "9" == number:
            pi(user)
            cs()
            break
        else:
            print("sir/ma'ma, please insurt a number")


def addition(user):
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        number_choice = int(input("insurt a number: "))
        number_yes = int(input("insurt a nother number: "))
        number_addition = number_choice + number_yes
        number_combine = (f"{number_choice} + {number_yes} = {number_addition}")
        print(number_combine)
        sav.write(str(number_combine) + "\n")
        sav.close()
        cs()
        main(user)


def subbtraktion(user):
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        number_Choice = int(input("insurt a number: "))
        number_yes = int(input("insurt a nother number: "))
        number_subbtraktion = number_Choice - number_yes
        number_combine = (f"{number_Choice} - {number_yes} = {number_subbtraktion}")
        print(number_combine)
        sav.write(number_combine + "\n")
        sav.close()
        cs()
        main(user)


def multiplikation(user):
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        number_choice = int(input("insurt a number: "))
        number_yes = int(input("insurt a nother number: "))
        number_multiplikation = number_choice * number_yes
        number_combine = (f"{number_choice} * {number_yes} = {number_multiplikation}")
        print(number_combine)
        sav.write(number_combine + "\n")
        sav.close()
        cs()
        main(user)

def divition(user):
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        number_choice = int(input("insurt a number: "))
        number_yes = int(input("insurt a nother number: "))
        number_divition = number_choice / number_yes
        number_divition1 = number_choice // number_yes
        number_combine = (f"{number_choice} / {number_yes} = {number_divition}")
        number_combine1 = (f"Rounded down: {number_choice} / {number_yes} = {number_divition1}")
        print(number_combine)
        print(number_combine1)
        sav.write(number_combine + "\n")
        sav.write(number_combine1 + "\n")
        sav.close()
        cs()
        main(user)



def percentage(user):
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        print("how much is x percent of y")
        x = int(input("insurt x: "))
        y = int(input("insurt y: "))
        xy = x / y
        times=xy
        percent = (f"{x} is {times}% out of {y}")
        print(percent)
        sav.write(percent + "\n")
        sav.close()
        cs()
        main(user)


def square(user):
    number_square = int(input("insurt a number to Square root OBS x > 0: "))
    print(math.sqrt(number_square))
    main(user)


def derivaties(user):
    x = sp.Symbol('x')
    y = 3 * x ** 2 + 1
    print(sp.diff(y, x))
    main(user)


def e(user):
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        print("write what you want in x (e^x): ")
        number_x = int(input(" "))
        number_e = math.e ** number_x
        oliver = (f"e^{number_x} = {number_e}")
        print(f"e^{number_x} = {number_e}")
        sav.write(oliver + "\n")
        sav.close()
        cs()
        main(user)


def pi(user):
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

        elif "2" in number_x:
            print("x^pi, write your x: ")
            b = int(input(" "))
            py2 = b ** math.pi
            albion = (f"{b}^pi = {py2}")
            print(f"{b}^pi = {py2}")
            sav.write(albion + "\n")
        
        elif "3" in number_x:
            print("x/pi, write your x: ")
            c = int(input(" "))
            py3 = c / math.pi
            py35 = c // math.pi
            zion = (f"{c}/pi = {py3} ~ {py35}")
            print(f"{c}/pi = {py3} ~ {py35}")
            sav.write(zion + "\n")

        elif "4" in number_x:
            print("pi/x, write your x: ")
            d = int(input(" "))
            py4 = math.pi / d
            py45 = math.pi // d
            alexis = (f"pi/{d} = {py4} ~ {py45}")
            print(f"pi/{d} = {py4} ~ {py45}")
            sav.write(alexis + "\n")

        elif "5" in number_x:
            print("x*pi, write your x ")
            e = int(input(" "))
            py5 = e * math.pi
            victor = (f"{e}*pi = {py5}")
            print(f"{e}*pi = {py5}")
            sav.write(victor + "\n")

        elif "6" in number_x:
            print("x+pi, write your x ")
            f = int(input(" "))
            py6 = f + math.pi
            jakob = (f"{f} + pi = {py6}") 
            print(f"{f} + pi = {py6}")
            sav,write(jakob + "\n")

        elif "7" in number_x:
            print("x-pi, write your x: ")
            g = int(input(" "))
            py7 = g - math.pi
            max = (f"{g} - pi = {py7}")
            print(f"{g} - pi = {py7}")
            sav.write(max + "\n")

        elif "8" in number_x:
            print("pi-x, write your x: ")
            h = int(input(" "))
            py8 = math.pi - h
            tim = (f"pi - {h} = {py8}")
            print(f"pi - {h} = {py8}")
            sav.write(tim + "\n")
        
        else:
            main(user)
    sav.close()
# fil som sparar allt man har räknat ut. och som kan hämta tillbak datan.
#
# Main-caller


if __name__ == "__main__":
    name()
