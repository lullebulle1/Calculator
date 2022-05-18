x = {
    1: 2007, 
    2: 2008, 
    3: 2009, 
    4: 2010,
    5: 2011, 
    6: 2012, 
    7: 2013, 
    8: 2014, 
    9: 2015, 
    10: 2016, 
    11: 2017,
}
y = {
    1: 383.79, 
    2: 385.60, 
    3: 387.43, 
    4: 389.90, 
    5: 391.65, 
    6: 393.85, 
    7: 396.52, 
    8: 398.65, 
    9: 400.83, 
    10: 404.21, 
    11: 406.53
    }
print(x)
yes = int(input("välj ett start år mellan (1 och 11)"))
yes1 = int(input("välj ett slut år mellan (1 och 11) "))    
a = x[yes]-x[yes1]

b = y[yes]-y[yes1]
k = b/a
print(f"ändringskvotten är {k}")

