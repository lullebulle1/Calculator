# Imports
import math  # Behöver för att kuna använd pi korrekt samt eulers numer (e)
import time  # Time.sleep
import os
# Global variables

# Functions
def cs():
    """
    Denna funktion gör så att det ser lite bättre ut och att allt inte ska komma på en gång, gjorde funktionen för att det skulle gå lite långsammare.
    Inputen är 'time.sleep' vilket gör så att programmet väntar lite innan nästa funktion körs igång och
    'os.system' vilket gör så att consolen blir ren och det gör det lättare att se vad som händer.
    """
    time.sleep(2)
    os.system('Clear')

def main():   
    """
    Menyn, tillåter dig att välja vad du vill calculera. Mellan varje if respektive elif i denna funktion kallar jag på en 
    annan funktion som innerhåller matematiken nödvändig för att calculera det du har tryckt in. exempelvis: Addition: 
    efter första if satsen har jag en funktion som heter Addition där jag har kodan så att man kan lägga in 2 numer och sedan får man ut summan.
    """
    print("\n\n\n\n\n")
    while True:
        print("""How would you like to calculate?
            [1] Addition                                                    
            [2] Subbtrakton
            [3] Multiplikation
            [4] Divitions
            [5] percantage
            [6] Square
            [7] e^x
            [8] pi
            [9] y=kx+m
            [#] Write '#' to quit or se history
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
        elif "9" == number:
            ykxm()
            cs()
        elif "#" == number:
            visit_saveeverything()
            cs()
            break
        else:
            print("sir/ma'ma, please insurt a number")

    """
    Här är första tället i koden där raden "with open("saveeverything.txt", "a", encoding="utf-8") as sav:".
    Jag har med den i varje funktion då jag vill spara svaret man får och så att man akn gå tillbaka och se vad man har gjort.
    """
def addition():
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:    
        number_choice = int(input("insert a number: "))
        number_yes = int(input("insert a number: "))
        number_addition = number_choice + number_yes
        number_combine = (f"{number_choice} + {number_yes} = {number_addition}")
        print(number_combine)
        sav.write(number_combine + "\n")    
        sav.close()
        cs()
        main()


def subbtraktion():
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        number_choice = int(input("insurt a number: "))
        number_yes = int(input("insurt a nother number: "))
        number_subbtraktion = number_choice - number_yes
        number_combine = (f"{number_choice} - {number_yes} = {number_subbtraktion}")
        print(number_combine)
        sav.write(number_combine + "\n")
        sav.close()
        cs()
        main()


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
        main()

def divition():
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        number_choice = int(input("insert a number: "))
        number_yes = int(input("insert a nother number: "))
        number_divition = number_choice / number_yes
        number_combine = (f"{number_choice} / {number_yes} = {number_divition}")
        print(number_combine)
        sav.write(number_combine + "\n")
        sav.close()
        cs()
        main()



def percentage():
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        print("how much is x percent of y")
        x = int(input("insurt x: "))
        y = int(input("insurt y: "))
        xy = x / y                         # ekv för att räkna ut procent.
        times=xy
        time = times * 100
        percent = (f"{x} is {time:.3f}% out of {y}")
        print(percent)
        sav.write(percent + "\n")
        sav.close()
        cs()
        main()


def square():
    """
    math.sqrt göt bara att man kan ta roten ur ett tal som användaren får välje.
    """
    number_square = int(input("insurt a number to Square root OBS x > 0: "))
    print(math.sqrt(number_square))
    main()

def e():
    """
    här har jag använt mig av math.e vilket ger ett par desimaler från konstanten e.
    Den här funktionen räknar ut e upphöjt till det tal du har skrivit in.
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
        main()


def pi():
    """
    jag importa math eftersom jag ville använda math.pi vilket ger hela eller många desimaler av pi.
    På varje ställe där man ska skriva in sitt numer skrev jag en variable i alfabetisk årdning, det gjorde det änklare för mig när jag koda.
    Samma sak med namnen, det vart lättare för mig när jag koda.
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
            main()

        elif "2" in number_x:
            print("x^pi, write your x: ")
            b = int(input(" "))
            py2 = b ** math.pi
            albion = (f"{b}^pi = {py2}")
            print(f"{b}^pi = {py2}")
            sav.write(albion + "\n")
            main()
        
        elif "3" in number_x:
            print("x/pi, write your x: ")
            c = int(input(" "))
            py3 = c / math.pi
            py35 = c // math.pi
            zion = (f"{c}/pi = {py3} ~ {py35}")
            print(f"{c}/pi = {py3} ~ {py35}")
            sav.write(zion + "\n")
            main()

        elif "4" in number_x:
            print("pi/x, write your x: ")
            d = int(input(" "))
            py4 = math.pi / d
            py45 = math.pi // d
            alexis = (f"pi/{d} = {py4} ~ {py45}")
            print(f"pi/{d} = {py4} ~ {py45}")
            sav.write(alexis + "\n")
            main()

        elif "5" in number_x:
            print("x*pi, write your x ")
            e = int(input(" "))
            py5 = e * math.pi
            victor = (f"{e}*pi = {py5}")
            print(f"{e}*pi = {py5}")
            sav.write(victor + "\n")
            main()

        elif "6" in number_x:
            print("x+pi, write your x ")
            f = int(input(" "))
            py6 = f + math.pi
            jakob = (f"{f} + pi = {py6}") 
            print(f"{f} + pi = {py6}")
            sav.write(jakob + "\n")
            main()

        elif "7" in number_x:
            print("x-pi, write your x: ")
            g = int(input(" "))
            py7 = g - math.pi
            max = (f"{g} - pi = {py7}")
            print(f"{g} - pi = {py7}")
            sav.write(max + "\n")
            main()

        elif "8" in number_x:
            print("pi-x, write your x: ")
            h = int(input(" "))
            py8 = math.pi - h
            tim = (f"pi - {h} = {py8}")
            print(f"pi - {h} = {py8}")
            sav.write(tim + "\n")
            main()
        else:
            main()
    sav.close()

def ykxm():
    """
    Den funktionen räknar ut den rätta linjerns ekvation med hjälp av de kordinater som du matar in.
    """
    with open("saveeverything.txt", "a", encoding="utf-8") as sav:
        print("""
        k= (y2-y1)/(x2-x1)
        """)
        y2 = int(input("put in your y2: "))
        y1 = int(input("put in your y1: "))
        x2 = int(input("put in your x2: "))
        x1 = int(input("put in your x1: "))
        ytot = y2 - y1
        xtot = x2 - x1
        k = ytot/xtot
        print(f"your k is {k} l.e")
        m1 = int(input("put in your x cordinat: "))
        m2 = int(input("put in your y cordinat:"))
        km1 = k*m1                          # Tog k från tidigare i funktionen.
        m = m2/km1
        print(f"{m}")
        print(f"your linjer ekv: y={k}x+{m}")
        spara = (f"your linjer ekv: y={k}x+{m}")
        sav.write(spara + "\n")
        sav.close()
        main() 

def visit_saveeverything():
    """
    Den här funktionen är enbart så man kan gå tillbaka för att kolla vilka uträkningar man har gjort tidigare.
    Jag frågar först om användaren vill avsluta eller inte, om de vill kommer man hitt och sedan kan man välja om man vill avluta eller ej.
    om man inte vill kommer man tillbaka till 'huvudsidan'.
    desutom 
    """
    with open("saveeverything.txt", "r", encoding="utf8") as sav:
        x = input("do you want to se what you have been calculated? (y/n)")
        if "y" in x:
            for s in sav.readlines():
                print(s)
            input(" ")
        else:
            y = input("whould you like to quit or continu? (q/c)")
            if "c" in y:
                main() 
            else:
                os._exit()

if __name__ == "__main__":
    main()  
    
