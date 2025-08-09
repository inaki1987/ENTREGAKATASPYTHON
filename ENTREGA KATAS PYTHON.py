#ENTREGA KATAS PYTHON

#1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
#de cada letra en la cadena. Los espacios no deben ser considerados.
def contar_letras(frase):
    frase_sin_espacios=frase.replace(" ","")
    lista_letras={}
    for a in frase_sin_espacios:
        if a in lista_letras:
            valor=lista_letras[a]
            lista_letras[a]=valor+1
        else:
            lista_letras[a]=1
    return lista_letras
#se utiliza un ejemplo
cadena_texto="Ejemplo de frase para contar letras"
frecuencia=contar_letras(cadena_texto)
print(frecuencia)
#FIN EJERCICIO

#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
lista=[2,3,4,8,10]
doblelista=map(lambda x: x*2,lista)
print(list(doblelista))
#FIN EJERCICIO

#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
#devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def filtro_lista(lista,objetivo):
    lista_filtrada=[]    
    for a in lista:
        if objetivo in a:
           lista_filtrada.append(a)    
    return lista_filtrada
#se utiliza un ejemplo
lista_palabras=["melón", "jamón", "natación", "atletismo", "pintura"]
buscar="ón"
filtro=filtro_lista(lista_palabras,buscar)
print(filtro)
#FIN EJERCICIO

#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

#from itertools import zip_longest
# def diferencia(lista1,lista2):
#        if len(lista1)==len(lista2):  
#                lista_diferencia=list(map(lambda x, y: x - y, lista1,lista2))
#       else:
#            Respuesta=input("Las listas no tienen el mismo numero de elementos,¿quieres completar con ceros la lista más corta para poder realizar la operación?(Si/No)")
#            if Respuesta=="Si":
#                listas=zip_longest(lista1, lista2, fillvalue=0) #Rellenamos con ceros la lista más corta
#                lista1mod, lista2mod = zip(*listas) #asignamos a cada lista el valor de las tuplas generadas en zip_longuest
#                lista_diferencia=list(map(lambda x, y: x - y, lista1mod, lista2mod))
#           else:
#                  lista_diferencia="No se puede relizar la diferencia de estas listas al no tener ambas el mismo número de elementos"
#       return lista_diferencia
"""Se añade corrección de PowerMBA
Aspectos positivos: Usas map y zip_longest correctamente para generar la diferencia.

Áreas de mejora:
Uso de input dentro de la función. Una función debería recibir parámetros y devolver un resultado, sin interactividad.
Tipos de retorno inconsistentes. A veces devuelves una lista y otras un string.


Tras corrección...
Ahora la función no interactúa con el usuario,
Siempre devuelve una lista o lanza excepción.
Usa un parámetro opcional (rellenar) en lugar de input.
"""

   
from itertools import zip_longest

def diferencia(lista1, lista2, rellenar=False):  
    if len(lista1) != len(lista2):
        if not rellenar:
            raise ValueError("Las listas deben tener igual longitud o habilitar 'rellenar'.")
        lista1, lista2 = zip(*zip_longest(lista1, lista2, fillvalue=0))
    return list(map(lambda x, y: x - y, lista1, lista2))


listaA=[2,4,6,8,10]
listaB=[1,3,5,7,9,20]
resultado=diferencia(listaA,listaB,True)
print(resultado)
#FIN EJERCICIO

#5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
#defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
#que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
#una tupla que contenga la media y el estado.

#import numpy as np #importamos numpy para hacer la media, si no deberíamos hacer suma de todos los elementos de la lista entre longitud de la lista

#def calificacion (lista,nota_minima):
#    media=round(np.mean(lista),2) #nos quedamos con dos decimales
#    if media >= nota_minima:
#        Resultado=(media,"Aprobado")
#    else:
#        Resultado=(media,"Suspenso")
#    return Resultado
#nota_aprobado=5
#calificaciones=[2,4,5,3,2,9,10,5,5]
#notas=calificacion(calificaciones,nota_aprobado)
#print(notas)

"""Se añade corrección de PowerMBA

#Aspectos positivos: Usas map y zip_longest correctamente para generar la diferencia.

#Áreas de mejora:

#Uso de input dentro de la función. Una función debería recibir parámetros y devolver un resultado, sin interactividad.
#Tipos de retorno inconsistentes. A veces devuelves una lista y otras un string."""

def calificacion(lista, nota_minima=5):
    """
    Calcula la media de 'lista' y devuelve (media, estado).
    """
    media = round(sum(lista) / len(lista), 2)
    estado = "Aprobado" if media >= nota_minima else "Suspenso"
    return media, estado

calificaciones=[2,4,0,8,0,9,10,5,5]
notas=calificacion(calificaciones)
print(notas)

#Ahora no hace falta instalar/importar librerías externas.
#El parámetro nota_minima tiene un valor por defecto.
#Para más sobre sum y len: https://docs.python.org/3/library/functions.html#sum
#FIN EJERCICIO

#6. Escribe una función que calcule el factorial de un número de manera recursiva.

#def calculo_factorial(numero):
#    factorial_acumulado=numero 
#    for i in range(numero, 1,-1): #paramos el ciclo en  i=2 ya que en el ciclo vamos a usar i-1 y no queremos que lo multiplique x 0 cuando el elemenot sea i=1.
#        factorial_acumulado=factorial_acumulado*(i-1) 
#    return factorial_acumulado

#factorial=calculo_factorial(10)
#print(factorial)


"""Se añade corrección de PowerMBA
#Error principal: Pide una implementación recursiva, pero usas un bucle for.
#Cumple la definición de recursividad.
#Maneja el caso base 0! = 1.
#Documentación sobre recursión y factorial: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
"""
def factorial(n):
    """
    Calcula factorial de n de forma recursiva.
    """
    if n < 0:
        raise ValueError("El número debe ser >= 0.")
    return 1 if n in (0, 1) else n * factorial(n - 1)

calculo_factorial=factorial(0)
print(calculo_factorial)
#FIN EJERCICIO

#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def convertir_a_string(lista): 
    lista_strings=list(map(str,lista))
    return lista_strings


lista_tuplas=[(1,"perro"),(2,"gato"),(3,"raton")]
resultado=convertir_a_string(lista_tuplas)
print(resultado)
#FIN EJERCICIO

#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
#o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
#indicando si la división fue exitosa o no.

#def comprobar_dividendo(dividendo):
#    try:
#        comprobacion_D=float(dividendo)
#        return comprobacion_D
#    except ValueError:
#         return(print ("Por favor intente de nuevo con un dividendo válido."))


#def comprobar_divisor(divisor):
#    try:
#        comprobacion_d = float(divisor)
#        if comprobacion_d != 0:
#            return(comprobacion_d)
#        else:
#            return(print("El divisor debe ser distinto de 0."))
#   except ValueError:
#        return(print("Por favor intente de nuevo con un divisor válido."))

#A=(input("Este programa calculará la división entre dos numeros A/B. Por favor introduzca el dividendo (A):"))
#a=comprobar_dividendo(A) #verificamos si A es un numero

#B=input("Por favor introduzca el valor del divisor(B):")
#b=comprobar_divisor(B)

#print (f"El resultado de la división es: {round(a/b,2)}")
""""
Se añade corrección de PowerMBA    
Áreas de mejora:
Las funciones comprobar_dividendo y comprobar_divisor imprimen y devuelven None, lo que puede romper el flujo.
La lógica final hace a/b sin garantizar que a y b sean válidos.
"""
def pedir_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada no válida. Inténtalo de nuevo.")

def dividir():
    a = pedir_numero("Dividendo (A): ")
    while True:
        b = pedir_numero("Divisor (B): ")
        if b == 0:
            print("El divisor no puede ser cero.")
        else:
            break
    print(f"Resultado: {round(a / b, 2)}")

División=dividir()
#FIN EJERCICIO

#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
#excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
#"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def filtro_mascotas(lista):
    lista_excluidos=["Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"]
    lista_filtrada=list(filter(lambda animal: animal not in lista_excluidos,lista))
    return lista_filtrada                   

mascotas=["Perro", "Gato", "Loro","Mapache"]
print (filtro_mascotas(mascotas))
#FIN EJERCICIO

#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
#excepción personalizada y maneja el error adecuadamente.

#def promedio(lista):
#    sum_elementos=sum(lista)   
#    num_elementos=len(lista)
#    calculo_prom=round(sum_elementos/num_elementos)
#   return calculo_prom

#lista_num=[5,7]
#if len(lista_num)==0:
#    print("La lista está vacía")
#else:
#    print(f"El promedio de la lista es {promedio(lista_num)}")



""""
Se añade corrección de PowerMBA 
Error: No defines ni usas una excepción personalizada: simplemente compruebas longitud fuera de la función.
Ahora la función lanza la excepción.
El manejo queda en el try/except.
"""


class ListaVaciaError(Exception):
    pass

def promedio(lista):
    if not lista:
        raise ListaVaciaError("La lista está vacía.")
    return round(sum(lista) / len(lista), 2)

# Uso:
try:
    print(promedio([3,5]))
except ListaVaciaError as e:
    print(e)
#FIN EJERCICIO

#11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
#valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
#adecuadamente.

edad=input("Por favor, introduzca su edad: ")

try:
    comprobacion_edad=float(edad)
    if comprobacion_edad<0:
        print("Vaya... parece que usted todavía no ha nacido. Su edad no puede ser inferior a cero.")
    elif comprobacion_edad>120:
         print("Vaya... parece que su edad es un nuevo Record Guiness. Puede parecer que el dato no es correcto.")
    else:
        print (f"Su edad es {comprobacion_edad} año(s)")
except:
    print("El valor introducido no es un número.")
#FIN EJERCICIO

#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def contar_letras_palabras(frase):
    palabras=frase.split()
    longitud=list(map(len,palabras))
    return longitud

texto=input("Introduzca texto para contar longitud de cada palabra:")
respuesta=contar_letras_palabras(texto)
print(respuesta)
#FIN EJERCICIO

#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
#mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

#def Mayus_minus(texto):
#    parejas = []
#    tuplas_unicas=[]
 #   for caracter in texto:
#        parejas.append(list(map(lambda c: (c.upper(), c.lower()),caracter)))
#
#    for tupla in parejas:
#        if tupla not in tuplas_unicas:
#            tuplas_unicas.append(tupla)
#    return tuplas_unicas

#cadena=input("Introduzca una cadena detexto para indicar las diferentes letras únicas que aparecen en el mismo. Las letras se motraran por parejas de mayúsculas y minúsculas")
#tuplas_uni=Mayus_minus (cadena)
#print(tuplas_uni)

"""
Corrección PowerMBA
Error de estructura: Construyes parejas como lista de listas en lugar de tuplas únicas y desanidadas
Uso de set(texto) para unificar caracteres.
Solo letras (.isalpha()), y cada tupla correctament
"""
def mayus_minus(texto):
    resultado = set()
    for c in set(texto):
        if c.isalpha():
            resultado.add((c.upper(), c.lower()))
    return list(resultado)

cadena=input("Introduzca una cadena detexto para indicar las diferentes letras únicas que aparecen en el mismo. Las letras se motraran por parejas de mayúsculas y minúsculas")
tuplas_uni=mayus_minus(cadena)
print(tuplas_uni)
#FIN EJERCICIO

#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
#función filter()

def filtro_palabras(lista, letra):
    letra_min=letra.lower()#compararemos siempre la letra inicial y la letra filtro en minuscula
    lista_filtrada=[]
    for palabra in lista:
        if palabra.lower().startswith(letra_min):#converimos cada palabra de la lista a minuscula y vemos si empieza con la letra "filtro"
            lista_filtrada.append(palabra)
    return lista_filtrada

palabras=["Juan","casa","leña","Loro"]
letra_ini="C"
palabras_filtradas=filtro_palabras(palabras,letra_ini)
print(palabras_filtradas)
#FIN EJERCICIO

#15. Crea una función lambda que sume 3 a cada número de una lista dada.
lista=[2,3,4,5,6,7]
lista_mod=list(map(lambda x: x+3,lista))
print(lista_mod)
#FIN EJERCICIO

#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
#todas las palabras que sean más largas que n. Usa la función filter()

# def palabras_mas_largas(texto, longitud_palabra):
#     palabras = texto.split()
#     return list(filter(lambda palabra: len(palabra) > longitud_palabra, palabras))

# B=float(input("Este programa devuelve una lista de todas las palabras que sean más largas que n. Introzuca un valor para n:"))

# A=input("Introduzca un texto en el que quiera filtrar las palabras de más de {B} letras")  

# palabras_filtradas=palabras_mas_largas(A,B)
# print(palabras_filtradas)
"""
Corrección PowerMBA
Áreas de mejora:

Convierte n a float, pero len() devuelve int.
La cadena en el prompt no usa f-string correctamente.

n es int.
Strings formateados con f"..."."""

def palabras_mas_largas(texto, n):
    palabras = texto.split()
    return list(filter(lambda p: len(p) > n, palabras))

# Uso:
n = int(input("Filtrar palabras con longitud mayor que n: "))
texto = input(f"Introduce el texto para filtrar (> {n} caracteres): ")
print(palabras_mas_largas(texto, n))
#FIN EJERCICIO

#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
#corresponde al número quinientos setenta y dos (572). Usa la función reduce()

# def convertir_en_numero(lista_digitos):
#     digito=reduce(lambda x, y : x*10+y,lista_digitos)
#     return digito

# from functools import reduce
# digitos=[4,5,6,5,4,3]
# print(convertir_en_numero(digitos))

"""
Corrección PowerMBA
a función antes de from functools import reduce, provocando NameError.
Importación por encima de la definición"""

from functools import reduce

def convertir_en_numero(lista_digitos):
    digito=reduce(lambda x, y : x*10+y,lista_digitos)
    return digito

from functools import reduce
digitos=[4,5,6,5,4,3]
print(convertir_en_numero(digitos))
#FIN EJERCICIO

#18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
#(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

estudiante_1={"Nombre":"Juan", "Edad":28,"Calificación":100}
estudiante_2={"Nombre":"Manuel", "Edad":30,"Calificación":70}
estudiante_3={"Nombre":"Aaron", "Edad":40,"Calificación":77}
estudiante_4={"Nombre":"Enrique", "Edad":45,"Calificación":80}
estudiante_5={"Nombre":"Pedro", "Edad":35,"Calificación":90}
estudiante_6={"Nombre":"Sergio", "Edad":43,"Calificación":91}
estudiante_7={"Nombre":"Jose", "Edad":26,"Calificación":50}

Alumnos_clase=[estudiante_1,estudiante_2,estudiante_3,estudiante_4,estudiante_5,estudiante_6,estudiante_7]

Alumnos_sobresalientes=list(filter(lambda alumno: alumno["Calificación"]>=90, Alumnos_clase))
print (Alumnos_sobresalientes)
#FIN EJERCICIO

#19. Crea una función lambda que filtre los números impares de una lista dada.

lista=[3,4,5,9,11,33]
filtrar_impares=list(filter(lambda x: x%2==1,lista))
print(filtrar_impares)
#FIN EJERCICIO

#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
filter()
lista=[3,4,5,"hola",11,33]
filtrar_enteros=list(filter(lambda x: isinstance(x, int),lista))
print(filtrar_enteros)
#FIN EJERCICIO

#21. Crea una función que calcule el cubo de un número dado mediante una función lambda

def calcular_cubo(numero):
        cubo=lambda x: x**3
        return cubo(numero)
   
try:
    A=float(input("Introduzca un valor para calcular su cubo:"))
    numero_cubo=calcular_cubo(A)
    
    print(numero_cubo)
except ValueError:
    print("El valor introducido no es un número")
#FIN EJERCICIO

#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

from functools import reduce

numeros = [1, 2, 3, 4, 5]
producto = reduce(lambda x, y: x * y, numeros)
print(producto)  
#FIN EJERCICIO

#23. Concatena una lista de palabras.Usa la función reduce() .

from functools import reduce

palabras=["Juan","casa","leña","Loro"]
concatena = reduce(lambda x, y: x + y, palabras)
print(concatena)  
#FIN EJERCICIO

#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

from functools import reduce

numeros = [1, 2, 3, 4, 5]
diferencia = reduce(lambda x, y: x - y, numeros)
print(diferencia)  
#FIN EJERCICIO

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

#Se trata de recrear el funcionamiento de la función len 
def longitud(texto):
  n=0
  for a in texto:
    n=n+1
  return n

A=input("Introduzca una cadena de texto para contar el número de caracteres:")
numero_caracteres=longitud(A)
print(numero_caracteres)
#FIN EJERCICIO

#26. Crea una función lambda que calcule el resto de la división entre dos números dados.

n1=6
n2=5
resto=lambda x,y: x%y
print(resto(n1,n2))
#FIN EJERCICIO

#27. Crea una función que calcule el promedio de una lista de números.

def promedio(lista):
    n=0
    s=0
    for a in lista:
        s=s+a
        n=n+1
    prom=round(s/n,2)
    return prom

A=[3,3,3,3,5,5,3]
calculo_promedio=promedio(A)

print(calculo_promedio)
#FIN EJERCICIO

#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    n = 0
    guardado = []
    while n < len(lista):
        if lista[n] in guardado:
            return lista[n]
        guardado.append(lista[n])
        n += 1
    return None

A=["casa", "perro", "juan", "perro"]
dupli=primer_duplicado(A)
print(dupli)
#FIN EJERCICIO

#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
#carácter '#', excepto los últimos cuatro.

def enmascarar(variable):
    texto=str(variable)
    
    texto_enmasc="#"*(len(texto)-4)+texto[-4:]
    return texto_enmasc


A=input("Introduzca texto a enmascarar")
enmascarado=enmascarar(A)
print(enmascarado)
#FIN EJERCICIO

#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
#pero en diferente orden.

#Utilizamos la funcion definida en ejercicio 1, pero la vamos a modificar haciendo que no se distingan mayúsculas de minúsculas
def contar_letras_mod(frase):
    frase_sin_espacios=frase.replace(" ","")
    frase_minusculas=frase_sin_espacios.lower()
    lista_letras={}
    for a in frase_minusculas:
        if a in lista_letras:
            valor=lista_letras[a]
            lista_letras[a]=valor+1
        else:
            lista_letras[a]=1
    return lista_letras


def anagrama(palabra1,palabra2):
    dic1=contar_letras_mod(palabra1)
    dic2=contar_letras_mod(palabra2)
    if dic1==dic2:
        resultado="Las palabras son anagramas"
    else:
        resultado="Las palabras no son anagramas"
    return resultado

A=input("Este programa comprobará si las dos palabras introducidas son anagramas. Por favor introduzca la primera palabra:")
B=input("Introduzca la segunda palabra:")
comprobar_anagrama=anagrama(A,B)

print(comprobar_anagrama)
#FIN EJERCICIO

#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
#esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
#lanza una excepción.

def buscar_nombre():
    try:
        lista_nombres = input("Ingresa una lista de nombres separados por coma: ")
        nombres = [nombre.strip() for nombre in lista_nombres.split(",")]
        nombre_buscado = input("Ingresa el nombre que quieres buscar: ")
        if nombre_buscado in nombres:
            print(f"El nombre '{nombre_buscado}' fue encontrado en la lista.")
        else:
            raise ValueError(f"El nombre '{nombre_buscado}' no está en la lista.")

    except ValueError as e:
        print(e)

buscar_nombre()
#FIN EJERCICIO

#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
#devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
#no trabaja aquí.

def buscar_puesto(lista_empleados, nombre_completo):
    for empleado in lista_empleados:
        if empleado.get('nombre')==nombre_completo:
            return f"El empleado {nombre_completo} tiene el puesto {empleado.get('puesto')}."
    return f"El empleado {nombre_completo} no figura en la lista de empleados."


empleados=[
    {"nombre":"Ana García","puesto":"enfermera"},
    {"nombre":"Jesus Gomez","puesto":"dentista"},
    {"nombre":"Javier Ordoñez","puesto":"médico"},
    {"nombre":"Ignacio Fernandez","puesto":"ingeniero"}]

A=input("Introduzca el nombre completo del empleado del que quiera saber el puesto:")

print(buscar_puesto(empleados,A))
#FIN EJERCICIO

#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

lista1 = [10, 23, 8]
lista2 = [1, 5, 7]

suma = list(map(lambda x, y: x + y, lista1, lista2))

print(suma)
#FIN EJERCICIO

#34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
#crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
#manipular la estructura del árbol.
#Código a seguir:
#1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
#6. Implementar el método
#info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las
#mismas.


class Arbol:
    def __init__(self):
        self.tronco=1
        self.ramas=[]
    def crecer_tronco(self):
        self.tronco +=1
    def nueva_rama(self, longitud_rama=1):
        self.ramas.append(longitud_rama)
    def crecer_ramas(self):
        self.ramas=list(map(lambda n: n+1, self.ramas))
    def quitar_rama(self,num_rama):
        if 0<=num_rama<len(self.ramas):
            del self.ramas[num_rama]
        else:
            print(f" la posición {num_rama} no existe en este arbol")
    def info_arbol(self):
        #print(f"El arbol tiene un tronco de {self.tronco} m de longitud y {len(self.ramas)} ramas, cada una de las cuales tiene {self.ramas} m de longitud respectivamente")
        """corrección powerMBA
        Error de retorno: info_arbol hace print internamente y no devuelve nada (None), luego print(manzano.info_arbol()) imprime None.
        """
        return(f"El arbol tiene un tronco de {self.tronco} m de longitud y {len(self.ramas)} ramas, cada una de las cuales tiene {self.ramas} m de longitud respectivamente")
#1. Crear un árbol.
manzano=Arbol()
#2. Hacer crecer el tronco del árbol una unidad.
manzano.crecer_tronco()
#3. Añadir una nueva rama al árbol.
manzano.nueva_rama()
#4. Hacer crecer todas las ramas del árbol una unidad.
manzano.crecer_ramas()
#5. Añadir dos nuevas ramas al árbol.
for i in range(2):
    manzano.nueva_rama()
#6. Retirar la rama situada en la posición 2.
manzano.quitar_rama(1)
#7. Obtener información sobre el árbol.
print (manzano.info_arbol())          
#FIN EJERCICIO

#36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
#corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
#agregar dinero al saldo.
#Código a seguir:
#1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
#2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no
#poder hacerse.
#3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
#Lanzará un error en caso de no poder hacerse.
#4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
#Caso de uso:

# class UsuarioBanco:
#     def __init__(self,nombre,saldo,cuenta):
#         self.nombre= nombre
#         self.saldo= saldo
#         self.cuenta= cuenta
#     def retirar_dinero(self, cantidad,cuenta):
#         if cuenta:
#             if cantidad < self.saldo:
#                 self.saldo= self.saldo-cantidad
#             else: print("La cantidad excede el saldo de la cuenta")
#         else: print("El usuario no tiene cuenta en este banco")
#     def agregar_dinero (self,cantidad,cuenta):
#         if cuenta:
#              self.saldo=self.saldo+cantidad
#         else: print("El usuario no tiene cuenta en este banco")
   
#     def transferir_dinero(self,receptor, cantidad):
#         if cantidad>self.saldo:
#             print (f"{self.nombre} no tiene suficiente saldo")
#         else:
#             receptor.saldo +=cantidad 
#             self.saldo -=cantidad
              

#     def info (self):
#         print(f" {self.nombre} tiene {(self.saldo)} euros")
        
# #1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
# Alicia=UsuarioBanco("Alicia",100,True)
# Bob=UsuarioBanco("Bob",80, True)
# Alicia.info()
# Bob.info()
# #2. Agregar 20 unidades de saldo de "Bob".
# Bob.agregar_dinero(20,True)
# Bob.info()
# #3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
# Bob.transferir_dinero(Alicia,80)
# Bob.info()
# Alicia.info()
# #4. Retirar 50 unidades de saldo a "Alicia".
# Alicia.retirar_dinero(50,True)
# Alicia.info()


"""Corrección PowerMBA
Áreas de mejora:

No es necesario pasar cuenta a cada método; ya es atributo de la instancia.
Mejor lanzar excepciones en caso de error que hacer print.

Usa siempre self.tiene_corriente.
Errores como excepciones, no silenciosos prints."""

class UsuarioBanco:
    def __init__(self, nombre, saldo, tiene_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_corriente = tiene_corriente

    def retirar(self, cantidad):
        if not self.tiene_corriente:
            raise RuntimeError("No tiene cuenta corriente.")
        if cantidad > self.saldo:
            raise RuntimeError("Saldo insuficiente.")
        self.saldo -= cantidad

    def agregar(self, cantidad):
        if not self.tiene_corriente:
            raise RuntimeError("No tiene cuenta corriente.")
        self.saldo += cantidad

    def transferir(self, otro, cantidad):
        self.retirar(cantidad)
        otro.agregar(cantidad)

    def __str__(self):
        return f"{self.nombre}: {self.saldo} €"

# Caso de uso:
 #1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
A = UsuarioBanco("Alicia", 100, True)
B = UsuarioBanco("Bob", 80, True)

#2. Agregar 20 unidades de saldo de "Bob".
B.agregar(20)

#3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
B.transferir(A, 80)
#4. Retirar 50 unidades de saldo a "Alicia".
A.retirar(50)
print(A, B)
#FIN EJERCICIO

#37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
#reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
#de la función procesar_texto .
#Código a seguir:


#1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
#Se usa como base el ejercicio uno de contar letras de una frase
def contar_palabras(frase):
    texto=frase.lower()
    palabras=texto.split()
    lista_palabras={}
    for palabra in palabras:
        if palabra in lista_palabras:
            valor=lista_palabras[palabra]
            lista_palabras[palabra]=valor+1
        else:
            lista_palabras[palabra]=1
    return lista_palabras

#2.Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
def reemplazar_palabras(texto,palabra_original, palabra_nueva):
    texto_modificado=texto.replace(palabra_original,palabra_nueva)
    return(texto_modificado)
#3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
def eliminar_palabra(texto,palabra):
    texto_modificado=texto.replace(palabra,'')
    return(texto_modificado)

def procesar_texto(opcion,texto,*args):
    if opcion=="contar":
        return contar_palabras(texto)
    elif opcion=="reemplazar":
        return reemplazar_palabras(texto, args[0],args[1])
    elif opcion=="eliminar":
        return eliminar_palabra(texto,args[0])


cadena_texto="Ejemplo de frase para contar palabras palabras palabras"
consulta=procesar_texto("eliminar",cadena_texto,"de")
print(consulta)
#FIN EJERCICIO

#38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
def clasificar(Hora):
    match Hora:
        case e if 0 <= e < 6:
            return "Es de noche"
        case e if 6 <= e < 12:
            return "Es de día"
        case e if 12 <= e < 21:
            return "Es por la tarde"
        case e if 21 <= e <= 24:
            return "Es de noche"
        case _:
            return "Hora no válida"
        
Hora=input("Introduzca una hora válida(0-24h):")
Hora=float(Hora)
Momento=clasificar(Hora)
print(Momento)
#FIN EJERCICIO

#39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
#Las reglas de calificación son:
#- 0 - 69 insuficiente
#- 70 - 79 bien
#- 80 - 89 muy bien
#- 90 - 100 excelente

def calificar(Nota):
    match Nota:
        case e if 0 <= e <= 69:
            return "Insuficiente"
        case e if 70 <= e <= 79:
            return "Bien"
        case e if 80 <= e <= 89:
            return "Muy bien"
        case e if 90 <= e <= 100:
            return "Excelente"
        case _:
            return "Nota no válida"

A=input("Introduzca una nota numérica (0-100):")
try:
    a=float(A)
    print(calificar(a))
except ValueError:
    print("Nota no válida")
#FIN EJERCICIO

#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
#"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).
import math #para poder usar el numero PI
def calculo_area(figura,datos):
   match figura:
        case "rectangulo":
            base, altura=datos
            Area= base* altura
            return print(f"El area del rectángulo es {Area}")
      
        case "triangulo":
            base, altura=datos
            Area= base* altura /2
            return print(f"El area del triángulo es {Area}")
        
        case "circulo":
            (radio,)=datos
            Area= math.pi*radio*radio
            return print(f"El area del círculo es {Area}")

Figura="circulo" #elegimos la figura 
Parametros=[2,]
Area=calculo_area(Figura,Parametros)
#FIN EJERCICIO

#41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
#monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
#siguiente:
#1. Solicita al usuario que ingrese el precio original de un artículo.
#2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
#3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
#4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
#a cero). Por ejemplo, descuento de 15€.
#5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
#6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
#programa de Python.

Precio_original=input("Introduzca el precio original del objeto:")
Descuento=input("Dispone de un cupón de descuento?(Si/No):")
if Descuento=="Si":
    Valor_descuento=input("Introduzca el valor de su cupón de descuento:")
    if float(Valor_descuento)>0:
        if float(Precio_original)>=float(Valor_descuento):
            Precio_final=float(Precio_original)-float(Valor_descuento)
        else :
            Precio_final= 0
    else:
        print("El descuento debe ser un numero positivo")
        Precio_final=float(Precio_original)
else:
     Precio_final=float(Precio_original)

print (f"El precio final es de {Precio_final} euros")
#FIN EJERCICIO

#FIN DE TAREA