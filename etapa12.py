import math
from random import *
"""
	en esta etapa dada una lista de palabras tomadas de un archivo esterno , crearemos una sopa de letra en base 
	a dichas palabras
	definiremos crearSopaDeLetras, la cual recibira un lista de palabas y retornara una lista de listas , representando 
	una sopa de letras.
		crearSopaDeLetras: lista(string)--> lista(listas(string))

"""
lista=["nose","casa","vaca","burro","auto","perro"]


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
#for i in generarTablero(tamañoDeTablero(lista)):
#	print(*i,sep="|")
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
#datos=actualizarDisponibles(generarTablero(tamañoDeTablero(lista)))
#for i in datos[0]:
#	print(*i,sep="|")
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
	#posicion=datos[0][2]	
	sentido=randint(0,1)
	direccion=randint(0,3)
	posver=verificarPosicion(sentido,direccion,pos,datos,palabra,tamaño)
        
	while posver==False:
		#return agregarPalabra(tablero,palabra)
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

#datos=generarTablero(tamañoDeTablero(lista))
#nose=agregarPalabra(datos,"casa")
#for i in nose:
#	print(*i,sep="|")

def crearSopaDeLetras(lista,tablero):
	for x in lista:
		tablero=agregarPalabra(tablero,x)
	return tablero

datos=generarTablero(tamañoDeTablero(lista))
nose1=crearSopaDeLetras(lista,datos)
for i in nose1:
	print(*i,sep="|")

def letraAlAzar():
	lista=["a","b","c","d","e"]
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


def sopaDeLetras(lista):
	tam=tamañoDeTablero(lista)
	tablero=generarTablero(tam)
	tableroconpalabras=crearSopaDeLetras(lista,tablero)
	tablerocompleto=rellenarTablero(tableroconpalabras)
	for i in tablerocompleto:
		print(*i,sep="|")

sopaDeLetras(lista)