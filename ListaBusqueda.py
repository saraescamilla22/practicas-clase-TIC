nombres=["angel","karla","luis","mateo","maria","luis","karla"]
print(f"los nombres que se tienen son:{nombres}")
nombreBuscar=input("¿que nombre deseas buscar?:")
encontrado=False
contador=0
i=0
while i<len(nombres):
    if nombres[i]==nombreBuscar:
        encontrado=True
        contador=contador+1
        print("encontrado en la posicion:",i)
    i=i+1
if encontrado==true:
    print("nombre encontrado")
    print("aparece", contador,"veces")
else:
    print("nombre no encontrado")
    
