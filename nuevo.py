print("Hola Mundo !!", 'Desde Python')

#! VARIABLES Y CONSTANTES

VALOR = 10 #? Constante por estar escrita en Mayuscula | No se debe modificar

numero = 19
print(numero)

#! Estructuras de datos, variable, array, list, tuple, dic, class

array = [20,35,55,65]

lista_num = [1, 2, 3, 4, 5,]
lista_num2 = [0] * 5 #? Da n veces las cantidad de posiciones que queremos en la lista.
print(lista_num2)

lista_num3 = []
lista_num3.append(1) #? Funcion append agrega elementos a la lista SIEMPRE AL FINAL DE LA LISTA.
lista_num3.append(10)
lista_num3.append(5)
lista_num3[0] = 3 #? Asigna un valor a la posicion seleccionada en el Array.
print(lista_num3)
print(lista_num3[1]) #? Muestra lo que hay en la segunda posicion del array.

lista_num3.insert(1, 4) #? En la segunda posicion se insertara el valor 4.
print(lista_num3)

#lista_num3.clear() limpia la lista
print(lista_num3.count(10)) #? Funcion count cuenta los elementos del mismo valor que se encuentran en la lista. 

print(lista_num3)
print(lista_num3.pop(1)) #? Elimina el elemento seleccionado. Si no indicamos que elemento, (), elimina el ultimo. Si la posicion no existe da error.
print(lista_num3)

print(lista_num3.remove(5)) #? Elimina el valor seleccionado, no por posicion. Elimina el primero que encuentra de izquierda a derecha.
print(lista_num3)


list_num4 = [4, 4, 7, 5, 25, 4, 2, 3, 4]

print(list_num4)
print(list_num4.remove(4))
print(list_num4)

print(list_num4.sort()) #? Ordena elementos de menor a mayor.
print(list_num4)

print(list_num4.sort(reverse=True)) #? Ordena elementos de mayor a menor.
print(list_num4)

#! Tupla

tupla_num = (1,2) #? No soporta asignaciones, no se puede modificar, basicamente una constante.
print(tupla_num)



#! funciones   (parametros variables y valor) --> primitivos valor | no primitivo referencia

def suma_resta(num1, num2): #? Valores primitivos (int, float, bool, str)
    num1 = 100
    return num1 + num2

suma = suma_resta(5, 9)
print('la suma es:', suma)



def mi_funcion_prueba(lista): #? Valores No Primitivos (Estructura de Datos, listas, tuplas, diccionarios y conjuntos). Al trabajar con variables no primitivas, el cambio se podra ver en el exterior de la funcion.
    lista.append(1)
    lista[0] = 49

lista_test = [1, 2, 3]

mi_funcion_prueba(lista_test)

print(lista_test)



lista_test2 = [1, 7, 2, 33, 99]
lista_test2.insert(3, 99)

print(len(lista_test2)) #? Devuelve la cantidad de elementos que tengo en una lista

for i in range(len(lista_test2)): #?range, devuelve una lista de numeros.
    print("valor", lista_test2[i])

for elemento in lista_test2: #?For each, mejor el anterior for. Hace que sea mas legible el codigo.
    print(elemento)


#! Diccionario

dic = {'1' : 'hola', '2' : 'chau', 0 : 'dsadadjk'} #? Key --> value
dic['3'] = 49
print(dic['2'])

print(dic.get(0)) #? Indicas la clave y te devuelve el valor asociado. Se utilioza basicamente para quie el programa no estalle, dado que si no encuentra el valor devuelve un None en vez de hace run overflow

print(dic.keys()) #? Devuelve todas las claves del diccionario.
print(dic.values())
print(dic.items())

dic.pop('3')
print(dic)

dic.update({'1' : 567, '33' : True}) #? Actualiza el valor de una Key mediante el metodo update. Aparte de la asignacion.
print(dic)

for key, value in dic.items(): #? Asi es como se debe de recorrer un diccionario para que quede legible
    print(key, value)


#! Modulos / Librerias

import mi_libreria

print(mi_libreria.suma(1, 1))
print(mi_libreria.resta(1, 1))
print(mi_libreria.producto(1, 1))
print(mi_libreria.division(1, 1))

#! Otra Forma de importar de una libreria

from mi_libreria import suma, resta #? De esta forma queda mas legible el cosdigo

print(suma(1, 1))
print(resta(1, 1))


#! Tercera forma de importar librerias

import mi_libreria as ml #? Se importan dadas las funcioness de la libreria. Es mas dificil Mockearr al hacer un test

print(ml.producto(2, 2))

from math import factorial

print(factorial())