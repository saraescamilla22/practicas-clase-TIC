#programa que me indica si reprobe o aprobe
#solicitar dato, calif
calif=float(input("ingresa la calificacion"))
#si la calif >=6 aprobo
if calif>=6:
    print("aprobaste yei")
else: 
    print("reprobaste")
#programa que solicita mi edad: indica si mayor/menor de edad
edad=float(input("ingresa tu edad"))
if edad>=18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")
    #programa que solicita una temp>=35 mucho calor, sino no hace tanto calor 
    temp=float(input("ingresa la temperatura"))
    if temp>=35:
        print("hace mucho calor")
    else:
        print("no hace tanto calor")