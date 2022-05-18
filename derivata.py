"""
def derivata_funktioner():
    def funktion(x):
        # Funktionen vi vill derivera
        return 4x**2

    def derivata1(x,h):
        # 
        return (funktion(x+h)-funktion(x))/h

    def derivata2(x,h):
        # 
        return (funktion(x)-funktion(x-h))/h

    def derivata3(x,h):
        # Central differenskvot
        return (funktion(x+h)-funktion(x-h))/(h2)

    def deriviataloop():
        x = int(input("Vilket X-värde vill du derivera? "))
        h = 1
        for  in range(10):
            # Enkel for-loop för att skriva ut hur h går från 110^-1 till 110^-10
            h /= 10 
            print(f"\t{derivata1(x,h)}\t{derivata2(x,h)}\t{derivata3(x,h)}")
    deriviata_loop()
#derivata_funktioner()
"""

