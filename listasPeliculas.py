#Prograna que 
#Ponerle nombre a mi lista
peliculas=[]
#preguntar cuantas pelis
cantidadPelis=int(input("cuantas peliculas vas a agregar"))
#valor inicial para el while
i=0
#mientras i sea menor a cantidad ejecutada
while i<=cantidadPelis:
#preguntar peliculas
 pelis=input("ingresa peli: ") 
#agrega pelicula a la lista
 peliculas.append(pelis)
#muestra la lista
 print(peliculas)   
 i=i+1     
#buscar una pelicula en la lista
# preguntar la peli a buscar
peliBuscar=input("que peli buscas")   
if peliBuscar in peliculas:
    print("si esta")
else:
    print("no esta pero dejame la agrego")
peliculas.append(peliBuscar) 
print(peliculas)    
#solicita una pelicula para borrar 
peliBorrar=input("que peli quieres borrar")
#borra la pelicula
peliculas.remove(peliBorrar)                   
#muestra la lista
print(peliculas)