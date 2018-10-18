#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from random import *
import os.path as path
"""
	en la primer opcion:
		dada una lista de palabras tomadas de un archivo externo , crearemos una sopa de letra en base 
		a dichas palabras. definiremos crearSopaDeLetras, la cual recibira un lista de palabras de un archivo 
		o permitira al usuario crear un archivo con las palabras y retornara una lista de listas, representando 
		una sopa de letras.
	en la segunda opcion: 
		recibimos una sopa de letras representada por una lista de listas, y una lista de palabras las 
		estan representadas por una lista , y buscamos todas las palabras en en la sopa de  letras.
		y devolvemos en que posicion se encuentran , el sentido , y la direccion de cada palabra.
	se accede a ellas a traves de un menu en el cual el usuario pueda elegir cual de estas opciones usar.
		
"""
#crearLista: None -> String
#recibe un nombre en forma de string a traves de input, crea una lista de palabras
#ingresadas por el usuario en un archivo con ese nombre y devuelve el nombre

#--> comienzo de el codigo de la etapa 1:

def crearLista():
	nombre1=input("elija el nombre del archivo donde se guardara la lista: ")
	nombre=nombre1+".txt"
	archivo = open(nombre,"w")
	can=int(input("ingrese la cantidad de palabras que desea ingresar: "))
	while type(can)!=int or can<=0:
		can=int(input("ingrese la cantidad de palabras que desea ingresar: "))

	for x in range(can):
		l=input("ingrese la palabra a agregar: ")
		archivo.write(l+"\n")
	archivo.close()
	return nombre1

#leerLista: String -> List
#recibe el nombre de un archivo en forma de string
#y devuelve una lista con las palabras del archivo
def leerLista(a):
	a+=".txt"
	if path.exists(a):
		archivo=open(a,"r")
	else:
		while path.exists(a)==False:
			a=input("ingrese el nombre de el archivo: ")
			a+=".txt"
	archivo=open(a,"r")
	lista=[]
	for linea in archivo.readlines():
		string=""
		for i in linea:
			if i!="\n":
				string+=i
		lista+=[string]
	archivo.close() 
	return lista

#tamañoDeTablero: List -> Int
#recibe una lista de palabras y en base a ella calcula el tamaño del
#tablero de la sopa a crear
def tamañoDeTablero(lista):
	cantidadDeLetras=0
	cantidadDePalabras=0
	longitudMaxima=0
	for i in lista:
		if longitudMaxima < len(i):
			longitudMaxima=len(i)
		cantidadDePalabras+=1
		for j in i:
			cantidadDeLetras+=1
	if ((int(math.sqrt(cantidadDeLetras)))*2)<(longitudMaxima*2):
		tamaño=longitudMaxima*2
	else:
		tamaño=((int(math.sqrt(cantidadDeLetras)))*2)
	return tamaño

def test_tamañoDeTablero():
	assert tamañoDeTablero(["casa"]) == (8)
	assert tamañoDeTablero(["casa","perro","lucas","nose","doss","1234","loco","unos","tres"]) == (12)
	assert tamañoDeTablero(["casa","locomotora"]) == (20)
	assert tamañoDeTablero(["casa","pedrito","volar","libre"]) == (14)

#generarTablero: Int -> List
#recibe un tamaño n en forma de entero
#y crea una lista de n listas de n elementos " "
def generarTablero(tamaño):
	l=[]
	for i in range(tamaño):
		l.append([])
		for j in range(tamaño):
			l[i].append(" ")
	return l

def test_generarTablero():
	assert generarTablero(2) == ([" "," "],[" "," "])
	assert generarTablero(1) == ([" "])
	assert generarTablero(2) == ([" "," "," "],[" "," "," "],[" "," "," "])

#actualizarDisponibles: List -> List
#recibe la lista del tablero y devuelve
#una lista de las posiciones disponibles para agregar palabras
def actualizarDisponibles(tablero):
	listaDisponibles=[]
	i=0
	for x in tablero:
		j=0
		for y in x:
			if y==" ":
				listaDisponibles.append((i,j))
			j+=1
		i+=1
	return listaDisponibles

def test_actualizarDisponibles():
	assert actualizarDisponibles([" "]) == ([(0,0)])
	assert actualizarDisponibles([["u"," "," "],[" ","n"," "],[" "," ","o"]]) == ([(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)])
	assert actualizarDisponibles([["h","o","l","a"],[" ","s"," "," "],[" "," ","o"," "],[" "," "," ","d"]]) == ([(1,0),(1,2),(1,3),(2,0),(2,1),(2,3),(3,0),(3,1),(3,2)])
	assert actualizarDisponibles([["u","n","o"],["d","o","s"],["e","s","o"]]) == ([])

#verificarIntersecciones: String String String Tupla List -> Boolean
#recibe la palabra que se quiere agregar, posicion, sentido (en forma de signos)
#y la lista de posiciones disponibles y devuelve si se puede ubicar la palabra o no en esa posicion
def verificarIntersecciones(signoX,signoY,palabra,pos,datos):
	#se especifica que los signos determinan la direccion y el sentido de como se intenta ubicar la palabra
	#vertical positiva=("mas","nulo")
	#vertical inversa=("menos","nulo")
	#horizontal positiva=("nulo","mas")
	#horizontal inversa=("nulo","menos")
	#diagonal derecha=("mas","mas")
	#diagonal derecha inversa=("menos","menos")
	#diagonal izquierda=("menos","mas")
	#diagonal izquierda inversa=("mas","menos")
	m=1
	b=True
	while m<len(palabra) and b==True:
		if signoX=="mas" and signoY=="menos":
			b=(pos[0]+m,pos[1]-m) in datos
		elif signoX=="mas" and signoY=="mas":
			b=(pos[0]+m,pos[1]+m) in datos
		elif signoX=="menos" and signoY=="mas":
			b=(pos[0]-m,pos[1]+m) in datos
		elif signoX=="menos" and signoY=="menos":
			b=(pos[0]-m,pos[1]-m) in datos
		elif signoX=="nulo" and signoY=="mas":
			b=(pos[0],pos[1]+m) in datos
		elif signoX=="nulo" and signoY=="menos":
			b=(pos[0],pos[1]-m) in datos
		elif signoX=="menos" and signoY=="nulo":
			b=(pos[0]-m,pos[1]) in datos
		else:
			b=(pos[0]+m,pos[1]) in datos
		m=m+1
	if b==True:
		return b
	else:
		return b

def test_verificarIntersecciones():
	#es correcto porque no se sale de rango y todas las posiciones estan disponibles
	assert verificarIntersecciones("mas","nulo","casa",(1,1),[(2,1),(3,1),(5,5),(4,1),(5,1)])==(True)
	#el ejemplo de abajo falla porque se va fuera de rango
	assert verificarIntersecciones("mas","menos","casa",(0,0),[(1,1),(1,2),(1,3)])==(False)
	#el ejemplo de abajo falla porque se va fuera de rango
	assert verificarIntersecciones("nulo","menos","casa",(0,2),[(0,0),(0,1),(0,3)])==(False)
	#falla porque una de las posiciones no esta disponible 
	assert verificarIntersecciones("mas","mas","casa",(0,0),[(1,1),(2,2),(4,4),(1,2),(0,2)])==(False)

#verificarPosicion: String Int Int Tupla List Int -> Boolean
#recibe una palabra con la direccion (0 horizontal, 1 vertical, 2 diagonal derecha y 3 diagonal izquierda),
#sentido (0 sentido normal y 1 sentido contrario) y posicion donde se quiere ubicar,
#mas la lista de posiciones disponibles y el tamaño del tablero
#y devuelve si se puede ubicar o no
def verificarPosicion(palabra,sen,dire,pos,datos,tam):
	if dire==0:
		if sen==0:
			if tam-pos[1]>len(palabra):
				return verificarIntersecciones("nulo","mas",palabra,pos,datos)
			else:
				return False
		else:
			if pos[1]>len(palabra):
				return verificarIntersecciones("nulo","menos",palabra,pos,datos)
			else:
				return False		
	elif dire==1:
		if sen==0:
			if tam-pos[0]>len(palabra):
				return verificarIntersecciones("mas","nulo",palabra,pos,datos)
			else:
				return False
		else:
			if pos[0]>len(palabra):
				return verificarIntersecciones("menos","nulo",palabra,pos,datos)
			else:
				return False
	elif dire==2:
		if sen==0:
			if tam-pos[0]>len(palabra) and tam-pos[1]>len(palabra):
				return verificarIntersecciones("mas","mas",palabra,pos,datos)
			else:
				return False
		else:
			if pos[0]>len(palabra) and pos[1]>len(palabra):
				return verificarIntersecciones("menos","menos",palabra,pos,datos)
			else:
				return False	
	else:
		if sen==0:
			if pos[0]>len(palabra) and tam-pos[1]>len(palabra):
				return verificarIntersecciones("menos","mas",palabra,pos,datos)
			else:
				return False
		else:
			if tam-pos[0]>len(palabra) and pos[1]>len(palabra):
				return verificarIntersecciones("mas","menos",palabra,pos,datos)
			else:
				return False	

def test_verificarPosicion():
	#es correcto porque las pociciones en la direccion y el sentido indicado estan disponibles.
	assert verificarPosicion("casa",0,1,(1,1),[(2,1),(3,1),(5,5),(4,1),(5,1)],8)==(True)
	#el ejemplo de abajo falla porque se va fuera de rango
	assert verificarPosicion("casa",1,3,(0,0),[(1,1),(1,2),(1,3)],10)==(False)
	#el ejemplo de abajo falla porque se va fuera de rango
	assert verificarPosicion("casa",1,0,(0,2),[(0,0),(0,1),(0,3)],10)==(False)
	#falla porque una de las posiciones no esta disponible 
	assert verificarPosicion("casa",0,2,(0,0),[(1,1),(2,2),(4,4),(1,2),(0,2)],8)==(False)	

#elegirAlazar: List -> Tupla
#recibe una lista de posiciones disponibles y elige una posicion al azar							
def elegirAlazar(lista):
	if len(lista)==1:
		return lista[0]
	else:
		pos=randint(0,len(lista)-1)
		return lista[pos]

#el testeo de la funcion elegirAlazar no lo hacemos porque no podemos predecir el resultado

#agregarPalabra: Lista String -> List
#recibe un tablero en forma de lista de listas y una palabra y devuelve
#el tablero con la palabra agregada
def agregarPalabra(tablero,palabra):
	tamaño=len(tablero)
	datos=actualizarDisponibles(tablero)
	pos=elegirAlazar(datos)
	sentido=randint(0,1)
	direccion=randint(0,3)
	posver=verificarPosicion(palabra,sentido,direccion,pos,datos,tamaño)
        
	while posver==False:
		pos=elegirAlazar(datos)
		posver=verificarPosicion(palabra,sentido,direccion,pos,datos,tamaño)
	if direccion==0:
		if sentido==0:
			for x in range(0,len(palabra)):
				tablero[pos[0]][pos[1]+x]=palabra[x]
		else:
			for x in range(0,len(palabra)):
				tablero[pos[0]][pos[1]-x]=palabra[x]
	elif direccion==1:
		if sentido==0:
			for x in range(0,len(palabra)):
				tablero[pos[0]+x][pos[1]]=palabra[x]
		else:
			for x in range(0,len(palabra)):
				tablero[pos[0]-x][pos[1]]=palabra[x]
	elif direccion==2:
		if sentido==0:
			for x in range(0,len(palabra)):
				tablero[pos[0]+x][pos[1]+x]=palabra[x]
		else:
			for x in range(0,len(palabra)):
				tablero[pos[0]-x][pos[1]-x]=palabra[x]
	else:
		if sentido==0:
			for x in range(0,len(palabra)):
				tablero[pos[0]-x][pos[1]+x]=palabra[x]
		else:
			for x in range(0,len(palabra)):
				tablero[pos[0]+x][pos[1]-x]=palabra[x]
	return tablero

#el testeo de esta funcion no podemos calcularlo ya que las posicion de las palabra en la lista resultante es al azar

#crearSopaDeLetras: List List -> List
#recibe un tablero de la forma de lista de listas y una lista de palabras 
#y devuelve tablero con todas las palabras de la lista agregadas
def crearSopaDeLetras(lista,tablero):
	for x in lista:
		tablero=agregarPalabra(tablero,x)
	return tablero

#el testeo de esta funcion no podemos calcularlo ya que las posicion de las palabra en la lista resultante es al azar

#letraAlAzar: None -> String 
#elige una letra al azar de una lista del alfabeto y nos las devuelve
def letraAlAzar():
	lista=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	if len(lista)==1:
		return lista[0]
	else:
		pos=randint(0,len(lista)-1)
		return lista[pos]

#el testeo de esta funcion no podemos hacerlo ya que el resultado es una letra al azar dentro de la lista

#rellenarTablero: List -> List
#recibe una lista de listas que representan un tablero y 
#rellena los espacios vacios con letras
def rellenarTablero(tablero):
	for x in range(0,len(tablero)):
		for j in range(0,len(tablero)):
			if tablero[x][j]==" ":
				tablero[x][j]=letraAlAzar()
	return tablero

#el testeo de esta funcion no podemos realizarlo , ya que nos retornara un tablero con los espacios 
#rellenados con letras al azar

#sopaDeLetras: None -> None
#permite al usuario elegir entre leer un archivo externo con palabras o crear uno
#y en base a este crea una sopa de letras, luego la imprime y la guarda en otro archivo
def sopaDeLetras():
	opcion=input("ingrese 1 para crear un archivo con las palabras o 2 para abrir un archivo: ")
	if opcion=="1":
		lista=leerLista(crearLista())
	else:
		lista=leerLista(input("ingrese el nombre del archivo: "))
	tam=tamañoDeTablero(lista)
	tablero=generarTablero(tam)
	tableroconpalabras=crearSopaDeLetras(lista,tablero)
	tablerocompleto=rellenarTablero(tableroconpalabras)
	print('Palabras:')
	for i in lista:
		print(i)
	print(' ')
	for i in tablerocompleto:
		print(*i,sep="|")
	sopa=input("ingrese el nombre con el que desea guardar el archivo: ")
	sopa+=".txt"	
	archivo=open(sopa,"w")
	for x in tablerocompleto:
		for l in x:
			archivo.write(l)
		archivo.write("\n")
	archivo.close()

#--> comienzo de el codigo de la etapa 2:

#laPalabraEsCorrecta: String List Int Int -> Tupla
#recibe una palabra , un tablero de sopa y una posicion representada por enteros
#evalua la palabra en la posicion , eliminando las direcciones en la cual la palabra 
#no entra , y luega pasa a evaluarla en las restantes con las posiciones siguientes
#y devuelve una tupla con True , la direccion y sentido correcto si esta en esa posicion
#o una tupla con False sino esta 
def laPalabraEsCorrecta(palabra,SopaDeLetras,i,j):
	diagonalIzquierdaNegativa=True
	diagonalDerechaPositiva=True
	diagonalIzquierdaPositiva=True
	diagonalDerechaNegativa=True
	verticalPositivo=True
	verticalNegativo=True
	horizontalPositivo=True
	horizontalNegativo=True
	if (i+(len(palabra)-1))>(len(SopaDeLetras)) or (j-(len(palabra)-1))<0:
		diagonalIzquierdaNegativa=False
	if i+(len(palabra)-1)>(len(SopaDeLetras)-1) or j+(len(palabra)-1)>(len(SopaDeLetras)-1):
		diagonalDerechaPositiva=False
	if j+(len(palabra)-1)>(len(SopaDeLetras)-1) or i-(len(palabra)-1)<0:
		diagonalIzquierdaPositiva=False
	if j-(len(palabra)-1)<0 or i-(len(palabra)-1)<0:
		diagonalDerechaNegativa=False
	if i+(len(palabra)-1)>(len(SopaDeLetras)-1):
		verticalPositivo=False
	if i-(len(palabra)-1)<0:
		verticalNegativo=False
	if j+(len(palabra)-1)>(len(SopaDeLetras)-1):
		horizontalPositivo=False
	if j-(len(palabra)-1)<0:
		horizontalNegativo=False
	if verticalPositivo==True:
		posp=1
		while posp<len(palabra):
			if SopaDeLetras[i+posp][j]==palabra[posp]:
				posp+=1
			else:
				verticalPositivo=False
				posp=len(palabra)
		if verticalPositivo==True:
			return (True,"vertical","normal")
	if verticalNegativo==True:
		posp=1
		while posp < len(palabra):
			if SopaDeLetras[i-posp][j]==palabra[posp]:
				posp+=1
			else:
				verticalNegativo=False
				posp=len(palabra)
		if verticalNegativo==True:
			return (True,"vertical","inverso")
	if horizontalPositivo==True:
		posp=1
		while posp < len(palabra):
			if SopaDeLetras[i][j+posp]==palabra[posp]:
				posp+=1
			else:
				horizontalPositivo=False
				posp=len(palabra)
		if horizontalPositivo==True:
			return (True,"horizontal","normal")
	if horizontalNegativo==True:
		posp=1
		while posp < len(palabra):
			if SopaDeLetras[i][j-posp]==palabra[posp]:
 				posp+=1
			else:
				horizontalNegativo=False
				posp=len(palabra)
		if horizontalNegativo==True:
			return (True,"horizontal","inverso")

	if diagonalIzquierdaPositiva==True:
		posp=1
		while posp < len(palabra):
			if SopaDeLetras[i-posp][j+posp]==palabra[posp]:
				posp+=1
			else:
				diagonalIzquierdaPositiva=False
				posp=len(palabra)
		if diagonalIzquierdaPositiva==True:
			return (True,"diagonal izquierda","normal")
	if diagonalIzquierdaNegativa==True:
		posp=1
		while posp < len(palabra):
			if SopaDeLetras[i+posp][j-posp]==palabra[posp]:
				posp+=1
			else:
				diagonalIzquierdaNegativa=False
				posp=len(palabra)
		if diagonalIzquierdaNegativa==True:
			return (True,"diagonal izquierda","inverso")
	if diagonalDerechaNegativa==True:
		posp=1
		while posp < len(palabra):
			if SopaDeLetras[i-posp][j-posp]==palabra[posp]:
				posp+=1
			else:
				diagonalDerechaNegativa=False
				posp=len(palabra)
		if diagonalDerechaNegativa==True:
			return (True,"diagonal derecha","inverso")
	if diagonalDerechaPositiva==True:
		posp=1
		while posp < len(palabra):
			if SopaDeLetras[i+posp][j+posp]==palabra[posp]:
				posp+=1
			else:
				diagonalDerechaPositiva=False
				posp=len(palabra)
		if diagonalDerechaPositiva==True:
			return (True,"diagonal derecha","normal")
	return (False,"","")

#leerSopa: None -> List 
#abre un archivo a traves de input y tranforma ese archivo a un tablero
# en forma de listas de listas
def leerSopa():
	a=input("ingrese el nombre de el archivo donde se encuentra la sopa: ")
	a+=".txt"
	if path.exists(a):
		archivo=open(a,"r")
	else:
		while path.exists(a)==False:
			a=input("ingrese el nombre de el archivo: ")
			a+=".txt"
	archivo=open(a,"r")
	d2=[]
	pos=0
	for linea in archivo.readlines():
		d2.append([])
		for i in linea:
			if i!="\n":
				d2[pos].append(i)
		pos+=1
	archivo.close()
	return d2

#resolverSopa: None -> None
#abre una sopa de letras y una lista de palabras que estan en la sopa desde archivos externos, 
#e imprime la posicion, direccion y sentido que tiene cada palabra en la sopa
def resolverSopa():
	SopaDeLetras=leerSopa()
	listaDePalabras=leerLista(input("ingrese el nombre del archivo donde se encuentra la lista de palabras seguido de .txt: "))
	listaDeSolucion=[]
	for l in listaDePalabras:
		i=0
		buscar=True
		while i<(len(SopaDeLetras)) and buscar==True:
			j=0
			while j <(len(SopaDeLetras)) and buscar==True:
				if l[0]==SopaDeLetras[i][j]:
					valor=laPalabraEsCorrecta(l,SopaDeLetras,i,j)
					if valor[0]:
						listaDeSolucion+=[(l,(i,j),valor[1],valor[2])]
						buscar=False
					j+=1
				else:
					j+=1
			i+=1
	for i in listaDeSolucion:
		print(i[0],"se encuentra en posicion ",i[1][0],"|",i[1][1],"en direccion ",i[2],"con sentido ",i[3])

#menu: None -> None
#recibe la opcion que el usuario desea realizar, 1 para crear una sopa o 2 para resolver una sopa
#y llama a la funcion correspondiente
def menu():
	opcion=input("ingrese: \n 1 para crear una sopa de letras \n 2 para resolver una sopa existente \n 0 para salir \n ")
	while opcion!="0":
		if opcion=="1":
			sopaDeLetras()
		elif opcion=="2":
			resolverSopa()
		opcion=input("ingrese: \n 1 para crear una sopa de letras \n 2 para resolver una sopa existente \n 0 para salir \n ")

menu()
