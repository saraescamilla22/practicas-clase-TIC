numeros=[]
resultados=[]
i=0
while i<5:
    num=int(input("ingresa numero:"))
    numeros.append(num)
    i=i+1
multiplicador=int(input("¿por cuanto deseas multiplicar?:"))

from num in numeros:
resultado=num*multiplicador
resultados.append(resultado)

print("numeros originales:",numeros)
print("resultados:"resultados)
#EXTRA
numeros.append(numBuscar)
print(numeros)