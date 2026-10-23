#programa para calcular areas
#area cuadrado; lado x lado 
lado=float(input("ingresa lado "))
areaCuadrado=lado*lado
print("el area es", areaCuadrado)
print(f"El area es {areaCuadrado}" )
#area triangulo; base x altura/2
base=float(input("ingresa la base"))
altura=float(input("ingresa la altura"))
areaTriangulo=(base*altura)/2
print("el area es", areaTriangulo)
#area trapecio; base mayor + base menor * altura/2
baseMayor=float(input("ingresa la base mayor"))
baseMenor=float(input("ingresa la base menor"))
altura=float(input("ingresa la altura"))
areaTrapecio= (baseMayor+baseMenor*altura/2)
print("el area es", areaTrapecio )
#area pentagono; perimetro*apotema/2
perimetro=float(input("ingresa el perimetro"))
apotema=float(input("ingresa el apotema"))
areaPentagono=(perimetro*apotema)/2
print("el area es", areaPentagono )
#area circulo; 3.14 r*r
radio=float(input ("ingresa radio") )
areaCirculo=(3.14 * radio*radio)
print("el area es", areaTriangulo)