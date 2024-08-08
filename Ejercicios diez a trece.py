#!/usr/bin/env python
# coding: utf-8

# In[10]:


ingresos = 1000
gastos = 400


# In[2]:


ingresos_text = "Los ingresos han sido altos"
ingresos_alt = 'Los ingresos han sido altos'
print(ingresos_text)
print(ingresos_alt)


# In[3]:


print("Los 'ingresos' han sido altos")


# In[4]:


ingresos_text = "Los "ingresos" han sido altos"


# In[5]:


ingresos
ingresos txt = "Los ingresos han sido altos"


# In[8]:


gastos = 200


# In[ ]:


#define the variables
ingresos = 1000
gastos = 400


# In[9]:


print("gastos :", gastos)


# In[11]:


beneficio = ingresos - gastos


# In[12]:


print(beneficio)


# In[13]:


beneficio = ingresos + gastos


# In[14]:


print(beneficio)


# In[1]:


ingresos = 1000
gastos = 400
beneficio = ingresos - gastos
print(beneficio)


# In[15]:


texto = 'error sin comillas


# In[16]:


2009_ingresos


# In[17]:


ingresos_2009 = 2500000


# In[18]:


print(ingresos_2009)


# In[2]:


import keyword
print(keyword.kwlist)


# In[ ]:


import keyword
print(keyword.kwlist)


# In[20]:


help("keywords")


# In[21]:


ingresos = 1000
gastos = 100
beneficios = ingresos - gastos


# In[22]:


print(ingresos)
print(gastos)
print('beneficios han sido de')
print(beneficios)


# In[5]:


mes = "Junio"
print("Los beneficios de %s han sido %d millones" %(mes, beneficios))


# In[29]:


print("Los beneficios de %s han sido de %s millones" %(beneficios,mes))


# In[8]:


mes = "agosto"
print("los beneficios de", mes, "han sido", beneficios, "millones")
mes = "Agosto"
print("los beneficios de", mes, "han sido", beneficios, "millones")


# In[32]:


#comentario de linea
#print("esto lo ignora")
print("esto lo ejecutara")


# In[34]:


print("fin del program") # esto indica que es el fin de progrma


# In[35]:


'''
comentario multilinea sin tener que usar#
'''
"""
comentario multilinea sin tener que usar#
print("no se va a ajecutar")
"""
print("si se va a ejecutar")


# In[36]:


ventas_jun_jul = ventas_jun + ventas_jul
ventas_jun = 100
ventas_jul = 200
print(ventas_jun_jul)


# In[9]:


ventas_jun = 100
ventas_jul = 200
ventas_jun_jul = ventas_jun + ventas_jul
print(ventas_jun_jul, type(ventas_jun_jul))


# In[37]:


ventas_jun = 100
ventas_jul = 150
ventas_jun_jul = ventas_jun + ventas_jul
print(ventas_jun_jul)


# In[38]:


altura = 1.80; peso = 103
print(altura, peso)
altura = 1.80; peso =103


# In[ ]:


x,z,y = 12,13,14
# seria lo mismo que lo de abajo
x = 12
z = 13
y = 14
#seria igual a lo de arriba
x = 12
y = 14
z = 13
x,y,z = 12,14,13


# In[39]:


altura = 1.85
del altura
print(altura)
#this happened as you deleted (del) altura so you cannot print it afterwards


# In[1]:


numero = 22
type(numero)


# In[10]:


numero_real = 22.1
type(numero_real)
numero_real1 = 31.2
print(type(numero_real1))


# In[4]:


print("Sumas y restas")
print(1 + 2)
print(1.0 +2.0)
print(1.0 - 2.0)


# In[6]:


print("Mult y divisiones")
print(2 * 2)
print(2.0 * 2)
print(2.0 /2)


# In[7]:


print("resto de division")
print(10/3)
print(int(10/3))
print(10 % 3)
print(10 // 3)


# In[11]:


print("resto de la division)
print(10/3)
print(int(10/3))
print(10 % 3)
print(10 // 3)


# In[9]:


print("resto de la division")
print(3 / 10)
print(int(3/10))
print(3 % 10)
print(3 //10)


# In[1]:


print('resto de la division')
print(3/10)
print(3%10)
print(int(3/10))
print(3//10)


# In[14]:


n = 23
print("es", n, "par")
resto = n % 2
print("el resto es", resto)
if resto == 0:
    print("resto es par")
else:
    print("resto es impar")


# In[12]:


n = 23
print (n, "es par")
resto = n / 2
if resto == 0:
    print(n, "es par")

else:
    print(n, "es impar")
    


# In[2]:


n = 23
resto = n % 2
if resto == 0:
    print('resto es par')
else:
    print('resto es impar')
    


# In[15]:


n = 23
print("es", n, "par")
resto = 23 % 2
if resto == 0:
    print("n es par")
else:
    print("n es impar")


# In[16]:


n = 2500000
print("es", n, "par")
resto = n % 2
if resto == 0:
    print(n, "es par")
else:
    print(n,"es impar")


# In[3]:


print("string con 'simples'")
print('string con "dobles"')
print("string con \"simples o dobles\"")

print("string con 'simples'"
print('strings con "dobles"')
print("strings con \"simples o dobles"")
# In[21]:


print("primera linea\n segunda linea\n \ttercera linea tabulada")

print("primera linea\n segunda linea\n ttercera linea tabulada")
# In[4]:


print("primera linea\n segunda linea\n\ttercera linea tabulada")


# In[29]:


mi_string = "primera linea\nsegundalinea\n\tTercera linea, tabulada"
print(mi_string)


# In[21]:


mi_string = "primera linea\n segunda linea\n tTercera linea tabulada"
print(mi_string)


# In[19]:


print("jola")


# In[33]:


nombre = "anton"
ap = "tolo"
nombre_ap = nombre + " " + ap
print(nombre_ap)


# In[ ]:





# In[34]:


nombre = "anton"
numero = 5
#no puedes mezclar numeros con strings
sum = nombre + numero
print(sum)


# In[35]:


True 


# In[36]:


ya_se_de_python = False
print(type(ya_se_de_python))


# In[8]:


ya_se_de_python = True
print(type(ya_se_de_python))


# In[38]:


dinerito = 5
dinerito >= 15


# In[22]:


dinerito = 45
dinerito >= 50


# In[9]:


dinerito = 13
dinerito >= 15


# In[40]:


dinerito = 5 
cond_1 = dinerito >= 15 
cond_2 = dinerito <= 15
cond_3 = dinerito == 5
print(cond_1)
print(cond_2)
print(cond_3)


# In[23]:


dinerito = 10
cond1 = dinerito >= 14
cond2 = dinerito <= 9
cond3 = dinerito == 10
print (cond1, cond2, cond3)


# In[41]:


print(type(56.7))


# In[42]:


print(type(False))


# In[43]:


print(type(cond_1))


# In[45]:


num_real = 34.78
print(type(num_real))
num_entero = int(num_real)
print(type(num_entero))
print(num_entero)


# In[10]:


num_real = 45.56
print(type(num_real))
num_ent = int(num_real)
print(type(num_ent))


# In[48]:


numero_real = 34.56756
numero_redondeado = round(numero_real, 2)
print(numero_redondeado)


# In[24]:


numero_real2 = 35.687
print(round(numero_real2, 2))


# In[51]:


numero_redondeado
numero_int_convert = int(numero_redondeado)
print(type(numero_int_convert), numero_int_convert)
print(numero_int_convert)


# In[53]:


#para convertir numeros reales en strings
num_real = 56.77
num_real_string = str(num_real)
print(num_real_string)
print(type(num_real_string))


# In[54]:


numero_real = 34.5
numero_entero = 25
numero_real_string = str(numero_real)
numero_entero_string = str(numero_entero)
print(type(numero_real_string), numero_real_string, type(numero_entero_string), numero_entero_string)


# In[26]:


numero_real = 12.123
numero_entero = int(numero_real)
numero_string = str(numero_real)
print(type(numero_real), numero_entero, type(numero_entero), type(numero_string))


# In[ ]:





# In[55]:


print(numero_real + numero_entero)
print(numero_real_string + numero_entero_string)


# In[58]:


# De cadena a entero
mi_cadena = "98"
mi_entero = int(mi_cadena)
print("this is the type", type(mi_entero), mi_entero, mi_cadena, type(mi_cadena))


# In[60]:


mi_cadena = "98"
mi_entero = int(mi_cadena)
mi_entero_dec = float(mi_cadena)
print(type(mi_cadena), mi_cadena, type(mi_entero), mi_entero, type(mi_entero_dec), mi_entero_dec)


# In[61]:


mi_cadena_dec = 98.34
mi_cadena_real = float(mi_cadena_dec)
print(type(mi_cadena_real), mi_cadena_real)


# In[27]:


mi_cadena_dec = 12.123
mi_cadena_real = float(mi_cadena_dec)
print(mi_cadena_real, type(mi_cadena_real))


# In[13]:


mi_cadena_dec = 54.19
print("mi_cadena_dec type is", type(mi_cadena_dec))
mi_cadena_float = float(mi_cadena_dec)
print(type(mi_cadena_float), mi_cadena_float)


# In[62]:


boolean = bool(123)
print(type(boolean), boolean)


# In[63]:


boolean = bool(0)
print(type(boolean), boolean)


# In[64]:


booleano = bool("")
booleano_2 = bool("This is another type of booleano")
print(booleano, type(booleano), booleano_2, type(booleano_2))


# In[29]:


booleno = bool("")
booleano2 = bool("este es otro tipo de booleano")
print(booleno, type(booleno), booleano2, type(booleano2))


# In[ ]:





# In[66]:


bool_strg = str(booleano)
bool_strg2 = str(booleano_2)
print(bool_strg, type(bool_strg), bool_strg2, type(bool_strg2))


# In[14]:


real_string = "64,67"
real_n = float(real_string)


# In[15]:


real_string.replace(",", ".")


# In[16]:


print(type(real_string))


# In[17]:


nuevo_string = real_string.replace(",",".")
float(nuevo_string)


# In[18]:


real_string = "64,67"
real_n = float(real_string)


# In[20]:


real_string = "64,67"
nuevo_string = real_string.replace(",",".")
real_no = float(nuevo_string)
print(type(real_no), real_no)


# In[30]:


real_string = "34;34"
nuevo_string = real_string.replace(";",".")
real_no = float(nuevo_string)
print(real_no, type(real_no))


# In[31]:


real_string = "34.23"
nuevo_string = real_string.replace(",",".")
print(type (nuevo_string), nuevo_string)


# In[32]:


print(600 + (360 * 4))


# In[21]:


primer_input = input("Escribeme argo mi arma")


# In[34]:


primer_input = input("Escribeme argo mi arma")
#aqui hamos almacenado el primer input
print(type(primer_input), primer_input)


# In[22]:


#aqui hemos almacenado algo en la variable primer_input
print(type(primer_input), primer_input)


# In[24]:


nombre = input("Como te llamas?")
print("encantado de conocerte", nombre)
preferencias = input('Y que te parece este magnifico video')
print("me encanta")


# In[35]:


nombre = input("como te llamas")
print("encantado de conocerte", nombre)
preferencias = input("que te parece este video")


# In[27]:


nombre = input('tu nombre')
print('encantado')
preferencias = input("te mola el video?")


# nombre = input('te llamas')
# print("encantado de conocerte", nombre)

# In[36]:


print(type(None))
"" == None
0 == None
False == None


# In[29]:


print(type(None))
"" == None


# In[30]:


0 == None


# In[32]:


False == None


# In[33]:


import this


# In[4]:


numero = 5
real = 12.34
sum = numero + real
print(type(sum), sum)
elevar = real**numero
print(elevar)
multiplica_v = numero * real
print(multiplica_v)
divide_v = real / numero
resto_v = real % numero
cociente_v = real // numero
print(divide_v, resto_v, cociente_v)


# In[37]:


numero = 5
num_real = 5.4
print(numero + num_real)
print(num_real * numero)
print(num_real / numero)
print(num_real // numero)
print(num_real % numero)


# In[5]:


print((3 + 4)/(4*2))


# In[8]:


import math
print(math.sqrt(25))
print(math.cos(0))
print(math.fabs(-200.2))


# In[9]:


print (4/0)


# In[10]:


assign = 1
print(assign)
assign == 5


# In[14]:


print ("AAA" == "BBB")
print ("AAA" == "AAA")
print (5 > 3)
print (1 == 1.0)
print (93 < 12)

print("AAA" == "BBB")
# In[38]:


print("AAA" == "BBB")
print("AAA" == "BBB")
print(5 > 3)
print(5 > 3)
print(1 == 1.0)


# In[15]:


# no podemos equiparar strings a valores
print (1 == "1")
print ("Hola" == True)


# In[40]:


print(1 == "1")
print("Yes" == True)


# In[19]:


#primer ordenador
ram1 = 32
process1 = "1E"
disco1 = 500
precio1 = 850
cond_ram1 = (ram1 == 16 or ram1 == 32 or ram1 == 64) 
cond_process1 = (process1 == "1E" and disco1 == 500)
cond_precio1 = (precio1 < 800)
con_total1 = cond_ram1 and cond_process1 and cond_precio1
print(con_total1)
print (cond_ram1, cond_process1, cond_precio1, con_total1)


# In[21]:


ram1 = 32
process1 = "1E"
disco1 = 500
precio1 = 850
cond_ram1 = (ram1 == 32 or ram1 == 16 or ram1 == 64)
cond_process1 = (disco1 == "1E" and disco1 == 500)
cond_precio1 = (precio1 < 800)
print(cond_ram1, cond_process1, cond_precio1)


# In[28]:


#segundo ordenador
ram2 = 8
process2 = "1E"
disco2 = 500
precio2 = 600

print((ram2 == 16 or ram2 == 32 or ram2 == 64) and (process2 == "1E" or disco2 == 500) and (precio2 < 800))

#tercer ordenador
ram3 = 32
process3 = "1E"
disco3 = 500
precio3 = 780
print((ram3 == 16 or ram3 == 32 or ram3 == 64) and (process3 == "1E" and disco3 == 500) and (precio3 < 800))


# In[47]:


print((ram2 == 16  or ram2 == 32 or ram2 == 64) and (process2 == "1E" and disco2 == 500) and (precio2 < 800))


# In[29]:


print((ram2 == 16 or ram2 == 32 or ram2 == 64) and (process2 == "1E" and disco2 == 500) and (precio2 < 800))


# In[52]:


ram3 = 32
process3  = "1E"
disco3 = 500
precio3 = 800
print((ram3 == 16 or ram3 == 32 or ram3 == 64) and (process3 == "1E" and disco3 == 500) and (precio3 < 800))


# In[30]:


var_new_len = "tetrabirck"
print(type(var_new_len), len(var_new_len), var_new_len)


# In[54]:


var_new = "prueba_de_len_function"
print(var_new, len(var_new), type(var_new))


# In[33]:


var_new_len2 = "prueba"
print(len(var_new_len2), type(var_new_len2))


# In[1]:


ver_try = 45.67
round(ver_try, 1)
print(ver_try)


# In[ ]:





# In[2]:


print(len("toca la trompeta"))


# In[3]:


print(max(7,5,45,45,64))


# In[55]:


print(max(3,45,67,89))


# In[6]:


cadena = "esto es una cadena"
print(cadena, len(cadena), sep = "**test**")


# In[7]:


cadena = "esto es una cadena"
print(cadena, len(cadena), sep = "**test**")
print("esto va en otra linea")


# In[9]:


cadena = "esto es una cadena"
print(cadena, len(cadena), sep = "**test**", end = "")
print("esto va en otra linea")


# In[58]:


cadena = "esto es una cadena"
separador = "**test**"
print(len(cadena), separador, end = " ")


# In[60]:


cadena = "esto es la cadena"
separador = "**test**"
print(len(cadena), separador, end = " ")


# In[17]:


cadena = "esto es una cadena"
print(cadena, len(cadena), sep = "**test**, end = "")


# In[24]:


string_ejemplo = "string en minusculas"
#metodo para poner todo en minusculas
print(string_ejemplo.upper())
#Metodo para poner todo en minusculas
print(string_ejemplo.lower())
#metodo para cambiar un caracter o varios
print(string_ejemplo.replace("s", "c"))
print(string_ejemplo.replace("minusculas", "minuuusculas"))


# In[33]:


string_ejemplo = "string en minusculas"
#metodo para poner todo en mayusculas
print(string_ejemplo.upper())
#metodo para poner todo en minusculas
print(string_ejemplo.lower())
print(string_ejemplo.replace("s","c"))
print(string_ejemplo.replace("minusculas", "minussssculas"))
print(string_ejemplo.replace("s", ""))
#metodo para covertir un string en una lista en string en el caso de abajo cada espacio
print("va a convertir esto un una lista desde string".split(" "))
#si queremos hacer un split incluso en una palabra podemos mira ejemplo abajo Jose
print("va a convertir esto en una lista de string".split("convertir"))
#Metodo para ver un caracter dentro de una lista
print(string_ejemplo.index("m"))


# In[61]:


string_ejemplo = "pon en minusculas, separa etc"
print(string_ejemplo.upper())
print(string_ejemplo.split())
print(string_ejemplo.split("en"))


# In[63]:


string_ejemplo = "pon en minusculas, separa etc"
print(string_ejemplo.lower())
print(string_ejemplo.split())
print(string_ejemplo.split(","))
print(string_ejemplo.index("m"))
print(string_ejemplo.replace("m","t"))


# In[43]:


string_ejemplo = "strong in minusculas"
#how to put things in upper case
print(string_ejemplo.upper())
#how to put things lower case
print(string_ejemplo.lower())
#replace
print(string_ejemplo.replace("s","t"))
print(string_ejemplo.replace("minusculas", "la la la"))
#metodo para convertir un string en una lista en string
print("esto va a convertir una lista to strig".split(" "))
print("esto va a convertir una lista to string".split("covertir"))
#metodo para ver en que posicion esta un caracter
print(string_ejemplo.index(m))


# In[34]:


#Cuando un metodo necesita varios argumentos y no se los damos erros typico
print(string_ejemplo.replace())


# In[35]:


#Cuando un metodo necesita varios argumentos y no se los damos erros typico
print(string_ejemplo.replace("m" , "t"))


# In[44]:


print(((17 * 50000) / 12) - 20000)


# In[49]:


var_ent = 5
var_float = 5.6
var_ent_float = var_ent + var_float
print(var_ent_float, type(var_ent_float))
var_div = var_float / var_ent
var_exp = var_float ** var_ent
var_resto = var_float % var_ent
var_cociente = var_float // var_ent
print(var_ent_float,"\n", var_div,"\n", var_exp, "\n", var_resto,"\n", var_cociente,"\n")  


# In[50]:


#Lista de numeros
numeros = {4, 5, 7, 8}
print(type(numeros), numeros)


# In[44]:


#lista de numeros
numero =[4,5,6,7]
print(type(numero), numero)


# In[51]:


#Lista de strings
string = {"esto", "es", "una", "lista"}
print(string)


# In[45]:


#lista de string
string = ["hola", "lola", "trenda"]
print(type(string), string)


# In[52]:


#lista de booleanos
Booleanos ={True, False, not False, True or False, True and False}
print(Booleanos)


# In[64]:


Lista_ejemplo = [2, 3, "patata"]
#podemos imprimir elementos escogigos de la lista
print(Lista_ejemplo[0])
print(Lista_ejemplo[-1])


# In[65]:


asignaturas = ["fisica", "quimica", "lengua"]
#anadir un elemento a una list
asignaturas.append("filosofia")
print(asignaturas)
#para anadir elementos en una posicion determinada
asignaturas.insert(1, "educacion fisica")
print(asignaturas)
asignaturas.sort()
print(asignaturas)


# In[67]:


asignaturas = ["fisica", "qimica", "lengua"]
#anadir elemento lista
asignaturas.append("filosofia")
print(asignaturas)
#anadir elemento en una posicion determinada
asignaturas.insert(1, "literatura")
print(asignaturas)
asignaturas.sort()
print(asignaturas)


# In[59]:


#quitar elementos
asignaturas.clear()
print(asignaturas)


# In[62]:


#quitar elmentos dependiendo de su indice y posicion
asignaturas.pop(1)
print(asignaturas)


# In[63]:


#Metodo para ordenar la lista
asignaturas.sort()
print(asignaturas)


# In[ ]:


#Ejercicio 1
#1.	Crea dos variables numéricas: un int y un float.
#2.	Comprueba sus tipos.
#3.	Súmalas en otra nueva.
#4.	¿De qué tipo es la nueva variable?
#5.	Elimina las dos primeras variables creadas.


# In[68]:


var_int1 = 5
var_float = 5.6
print(type(var_int1), type(var_float))
var3 = var_int1 + var_float
print(type(var3))


# In[70]:


del(var_int1, var_float)
print(var_int1, var_float)


# In[ ]:


#Ejercicio 2
#Escribe un programa para pasar de grados a radianes. Hay que usar input. Recuerda que la conversión se realiza mediante:
#radianes=grados×(π180)\text{radianes} = \text{grados} \times \left( \frac{\pi}{180} \right)radianes=grados×(180π)


# In[78]:


import math

grados = float(input("introduce los grados "))
radianes = grados * (math.pi*180)
# Mostrar el resultado
print(f"{grados} grados son {radianes} radianes.")


# In[ ]:


#Ejercicio 3
#Escribe un programa que calcule el área de un paralelogramo (base x altura). También con input.


# In[84]:


base = float(input("introduce la base"))
altura = float(input("introduce la altura"))
area = base * altura
print(area," es el area")


# In[ ]:


#Ejercicio 4
#Escribe un programa que calcule el área de un paralelogramo (base x altura). También con input.
#En este caso debe ser capaz de admitir valores reales, con decimales, para base y altura en español. (PISTA: Recuerda que tendrás que hacer uso del método replace).


# In[89]:


base_input = input("introduce la base: ")
altura_input = input("introduce la altura: ")
base = float(base_input.replace(",","."))
altura = float(altura_input.replace(",","."))
area = base * altura
print(area, "es el area resultante")


# In[ ]:


#Completa el siguiente código para solicitar al usuario su nombre y su edad. Luego, calcule en qué año nació el usuario y muestre el resultado.
#python
#nombre = _______("¿Cuál es tu nombre? ")
#edad = _____(input("¿Cuál es tu edad? "))
#año_actual = 2023  # Puedes cambiarlo según el año en curso
#año_nacimiento = año_actual - _____

#print(f"{nombre}, naciste en el año {año_nacimiento}.")


# 
# 

# In[95]:


nombre = input("cual es tu nombre?: ")
edad = float(input("que edad tienes?: "))
ano_de_nacimiento = 2023 - edad
print(nombre, "naciste en", int(ano_de_nacimiento))


# In[ ]:


1.	Calcula el máximo de la lista: [4, 6, 8, -1]
2.	Suma todos los elementos de la lista anterior
3.	Redondea este float a 3 dígitos decimales: 63.451256965
4.	Valor absoluto de: -74


# In[102]:


lista_11 = [4,6,8,-1]
print(max(lista_11))


# In[103]:


print(lista_11[-1] + lista_11[0] + lista_11[1] + lista_11[2])


# In[110]:


numero = 63.451256965
numero_redondeado = round(numero,3)
print(numero_redondeado)


# In[112]:


import math
valor = -74
valor_abs = abs(-74)
print(valor_abs)


# In[8]:


#1.	Pásalo todo a mayúsculas
#2.	Pásalo todo a minúsculas
#3.	Solo la primera letra de cada palabra en mayúscula, el resto en minúscula
#4.	Crea una lista dividiéndolo por sus espacios
#5.	Sustituye las comas , por puntos y comas ;
#6.	Elimina las a minúsculas


string_ejemplo = "En un lugar de la Mancha, de cuyo nombre no puedo acordarme"
print(string_ejemplo.upper())
print(string_ejemplo.lower())
#para escribir la pirmera letra de cada palabra en mayuscula el resto en minuscula utilizamos la palabra title
print(string_ejemplo.title())
print(string_ejemplo.split(" "))
print(string_ejemplo.replace(",","."))



# In[42]:


#1.	Crea una lista con 3 elementos numéricos
#2.	Añade un cuarto elemento
#3.	Calcula la suma de todos
#4.	Elimina el segundo elemento de la lista
#5.	Añade otro elemento en la posición 3 de la lista
#6.	Crea otra lista con 4 elementos y concaténala a la que ya tenías
#7.	Ordena la lista de menor a mayor
#8.	BONUS: Ordena la lista de mayor a menor.

num_list = ["4","5","6"]
num_list.append("7")
print(num_list)
# Convertir cada elemento a un número entero y sumarlos
suma = sum(int(num) for num in num_list)
#4.	Elimina el segundo elemento de la lista
del num_list[1]
print(num_list)
#6.	Crea otra lista con 4 elementos y concaténala a la que ya tenías
num_list2 = ["8","9","0"]
sum_lists = num_list + num_list2
print(sum_lists)
sum_lists.sort()
print(sum_lists)


# In[45]:


#Ejercicio 1
#Para este ejercicio vamos a poner en práctica las funciones built-in.

#Calcula el máximo de la lista: [4, 6, 8, -1]
#Suma todos los elementos de la lista anterior
#Redondea este float a 3 dígitos decimales: 63.451256965
#Valor absoluto de: -74

num_list = [4, 6, 8, -1]
print(max(num_list))
sum(int(num) for num in num_list)
print(sum)
real_num = 63.451256965
print(round(real_num, 3))
num2 = -74
print(abs(num2))


# In[48]:


#Ejercicio 2
#Para el siguiente string se pide imprimir por pantalla los siguientes casos:

#"En un lugar de la Mancha, de cuyo nombre no quiero acordarme."
#Pásalo todo a mayúsculas
#Pásalo todo a minúsculas
#Solo la primera letra de cada palabra en mayúscula, el resto en minúscula
#Crea una lista dividiéndolo por sus espacios
#Sustituye las comas , por puntos y comas ;
#Elimina las a minúsculas

string_quijote = ("En un lugar de la Mancha, de cuyo nombre no quiero acordarme.")
print(string_quijote.upper())
print(string_quijote.lower())
print(string_quijote.title())
print(string_quijote.split(" "))
print(string_quijote.replace(",","."))


# In[63]:


#Ejercicio 3
#Crea una lista con 3 elementos numéricos
#Añade un cuarto elemento
#Calcula la suma de todos
#Elimina el segundo elemento de la lista
#Añade otro elemento en la posición 3 de la lista
#Crea otra lista con 4 elementos y concaténala a la que ya tenías
#Ordena la lista de menor a mayor
#BONUS: Ordena la lista de mayor a menor.

list3 = [3,4,5]
list3.append(6)
print(list3)
sum(int(num) for num in list3)
print(sum)
print(sum(list3))
del(list3[1])
print(list3)
list3.insert(2,10)
print(list3)
list4 = [6,7,8]
new_list = list3 + list4
print(new_list)
new_list.sort()
print(new_list)


# In[66]:


#"Buenas tardes, bienvenido al servicio de pedido online, el precio de nuestra pizzas es de 8,95 para la familiar o de 9,90 para la mediana ¿Cuántas pizzas familiares desea?"
#El usuario tiene que introducir un número de pizzas en una variable llamada pizz_familiar.
#El chatbot debe responder:
#"Estupendo, ¿cuántas pizzas medianas desea?"
#Y guardar el número de pizzas medianas en otra variable pizz_mediana.
#Además, el chatbot debe responder:
#"Estupendo, se están preparando 'pizz_familiar' pizzas familiares y 'pizz_mediana' pizzas medianas. Dígame su dirección"
#El usuario tiene que introducir una dirección en formato String en otra variable llamada direcc.
#El programa debe calcular el monto total.
#Respuesta final del chatbot:
#"Le mandaremos las '(número total de pizzas)' pizzas a la dirección 'direcc'. Serán <precio total a pagar en euros>. Muchas gracias por su pedido."

pizz_familiar = int(input("Buenas tardes, bienvenido al servicio de pedido online, el precio de nuestra pizzas es de 8,95 para la familiar o de 9,90 para la mediana ¿Cuántas pizzas familiares desea?"))

big_pizza = pizz_familiar * 9.90

pizza_mediana = int(input("Estupendo, ¿cuántas pizzas medianas desea?"))

m_size_pizza = pizza_mediana * 8.95


direction = str(input("Estupendo, se están preparando 'pizz_familiar' pizzas familiares y 'pizz_mediana' pizzas medianas. Dígame su dirección"))


print("Le mandaremos las", pizz_familiar + pizza_mediana, "pizzas a la direccion",direction, "seran", (big_pizza +  m_size_pizza))



# In[78]:


#Parte II
#Crea un programa que realice las siguientes acciones:

#Solicite al usuario que introduzca 3 números enteros separados por comas (por ejemplo: 1,2,3).
#Convierta esa entrada en una lista de números enteros.
#Utilizando funciones built-in, determine el número máximo, el número mínimo y la suma total de los números introducidos.
#Determine la verdad o falsedad de la siguiente afirmación:
#"El número máximo menos el número mínimo es igual a la suma total dividida por 5".
#Muestre los resultados utilizando print.

#Solicite al usuario que introduzca 3 números enteros separados por comas (por ejemplo: 1,2,3).
#Convierta esa entrada en una lista de números enteros.
lista_numero = int[input("introduzca 3 números enteros separados por comas (por ejemplo: 1,2,3). :")]
lista_numeros = [int(num) for num in numeros.split(',')]
max_numero = max(lista_numero)
min_numero = min(lista_numero)
sum_num = sum(lista_numeros)
verification = (max_numero - min_numero) == ((max_numero + min_numero)/5)
print(max_numero, min_numero, sum_num, verification)



# In[ ]:




