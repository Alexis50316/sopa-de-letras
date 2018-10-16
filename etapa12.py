#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from random import *
"""
	en esta etapa dada una lista de palabras tomadas de un archivo externo , crearemos una sopa de letra en base 
	a dichas palabras
	definiremos crearSopaDeLetras, la cual recibira un lista de palabras de un archivo 
	o permitira al usuario crear un archivo con las palabras y retornara una lista de listas, representando 
	una sopa de letras.
		
"""
def crearLista():
	nombre=input("elija el nombre del archivo donde se guardara la lista terminando con .txt: ")
	archivo = open(nombre,"w")
	can=int(input("ingrese la cantidad de palabras que desea ingresar: "))
	for x in range(can):
		l=input("ingrese la palabra a agregar: ")
		archivo.write(l+"\n")
	archivo.close()
	return nombre
	
def leerLista(a):
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

def generarTablero(tamaño):
	l=[]
	for i in range(tamaño):
		l.append([])
		for j in range(tamaño):
			l[i].append(" ")
	return l
def actualizarDisponibles(tablero):
	listaDisponibles=[]
	listaOcupados=[]
	i=0
	for x in tablero:
		j=0
		for y in x:
			if y==" ":
				listaDisponibles.append((i,j))
			else:
				listaOcupados.append((i,j))
			j+=1
		i+=1
	return (listaDisponibles,listaOcupados)
def verificarIntersecciones(signoX,signoY,palabra,pos,datos):
	m=1
	b=True
	while m<len(palabra) and b==True:
		if signoX=="mas" and signoY=="menos":
			b=(pos[0]+m,pos[1]-m) in datos[0]
		elif signoX=="mas" and signoY=="mas":
			b=(pos[0]+m,pos[1]+m) in datos[0]
		elif signoX=="menos" and signoY=="mas":
			b=(pos[0]-m,pos[1]+m) in datos[0]
		elif signoX=="menos" and signoY=="menos":
			b=(pos[0]-m,pos[1]-m) in datos[0]
		elif signoX=="nulo" and signoY=="mas":
			b=(pos[0],pos[1]+m) in datos[0]
		elif signoX=="nulo" and signoY=="menos":
			b=(pos[0],pos[1]-m) in datos[0]
		elif signoX=="menos" and signoY=="nulo":
			b=(pos[0]-m,pos[1]) in datos[0]
		else:
			b=(pos[0]+m,pos[1]) in datos[0]
		m=m+1
	if b==True:
		return b
	else:
		return b
def verificarPosicion(sen,dire,pos,datos,palabra,tam):
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
							
def elegirAlazar(lista):
	if len(lista)==1:
		return lista[0]
	else:
		pos=randint(0,len(lista)-1)
		return lista[pos]

def agregarPalabra(tablero,palabra):
	tamaño=len(tablero)
	datos=actualizarDisponibles(tablero)
	pos=elegirAlazar(datos[0])
	sentido=randint(0,1)
	direccion=randint(0,3)
	posver=verificarPosicion(sentido,direccion,pos,datos,palabra,tamaño)
        
	while posver==False:
		pos=elegirAlazar(datos[0])
		posver=verificarPosicion(sentido,direccion,pos,datos,palabra,tamaño)
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

def crearSopaDeLetras(lista,tablero):
	for x in lista:
		tablero=agregarPalabra(tablero,x)
	return tablero

def letraAlAzar():
	lista=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	if len(lista)==1:
		return lista[0]
	else:
		pos=randint(0,len(lista)-1)
		return lista[pos]


def rellenarTablero(tablero):
	for x in range(0,len(tablero)):
		for j in range(0,len(tablero)):
			if tablero[x][j]==" ":
				tablero[x][j]=letraAlAzar()
	return tablero


def sopaDeLetras():
	opcion=input("ingrese 1 para crear un archivo con las palabras o 2 para abrir un archivo: ")
	if opcion=="1":
		lista=leerLista(crearLista())
	else:
		lista=leerLista(input("ingrese el nombre del archivo con .txt: "))
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
	archivo=open("sopa.txt","w")
	for x in tablerocompleto:
		for l in x:
			archivo.write(l)
		archivo.write("\n")
	archivo.close()

sopaDeLetras()
