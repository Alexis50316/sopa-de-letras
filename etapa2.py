"""
	crearemos un programa que resuelva una sopa de letra , teniendo la sopa de letras definida y las palabras a buscar 
	para eso definiremos la funcion principal ResolverSopa() que recibira una sopa tomada de un archivo esterno,
	y una lista de palabras tambien tomada de un archivo esterno.
	y nos devolvera una lista de tuplas de tipo dispocicion.
	la tupla dispocion esta conformada por 4 parametros, 
	    (
		primer elemento: palabra(String)
		segundo elemento: posicion(int)
		tercer elemento: direccion(string)
		cuarto elemneto: sentido(string)
		)
	funciones complementarias:
		#aca van las funciones secundarias

"""
def obterDatos():





def evaluarPosicion(palabra,SopaDeLetras,i,j):
	#sabemos que en (i,j) la sopa coinside con el primer elemento de la palabra
	#y hay 3 direcciones posibles solamente(vertical, diagonal,horizontal)
	#evaluaremos en todas las posiciones
	diagonalIzquierdaNegativa=True
	diagonalDerechaPositiva=True
	diagonalIzquierdaPositiva=True
	diagonalDerechaNegativa=True
	verticalPositivo=True
	verticalNegativo=True
	horizontalPositivo=True
	horizontalNegativo=True


	if i+(len(palabra)-1)>(len(SopaDeLetras)-1) and j+(len(palabra)-1)<j:
		diagonalIzquierdaNegativa=False
	if i+(len(palabra)-1)>(len(SopaDeLetras)-1) and j+(len(palabra)-1)>(len(SopaDeLetras)-1):
    	diagonalDerechaPositiva=False
    if j+(len(palabra)-1)>(len(SopaDeLetras)-1) and i+(len(palabra)-1)>i:
    	diagonalIzquierdaPositiva=False
    if j+(len(palabra)-1)>(len(SopaDeLetras)-1) and i+(len(palabra)-1)>(len(SopaDeLetras)-1):
    	diagonalDerechaNegativa=False

	if i+(len(palabra)-1)>(len(SopaDeLetras)-1):
		verticalPositivo=False

	if i+(len(palabra)-1)>i:
		verticalNegativo=False

	if j+(len(palabra)-1)>(len(SopaDeLetras)-1):
		horizontalPositivo=False

	if j+(len(palabra)-1)<j:
		horizontalNegativo=False	

    verificar=True

    while verificar==True:
    	if verticalPositivo==True:
    		posp=1
    		while posp < len(palabra):
    			if SopaDeLetras[i+posp][j]==palabra[posp]:
    				pass
    			posp+=1

    	if verticalNegativo==True:
    		pass

    	if diagonalIzquierdaPositiva==true:
    		posp=1
    		while posp < len(palabra):
    			if SopaDeLetras[i+posp][j+posp]==palabra[posp]:
    				pass
    			posp+=1




    if verticalNegativo==True:

	return datos=(valor,direccion,sentido)



def resolverSopa(listaDePalabras,SopaDeLetras):
	listaDeSolucion=[]
	for l in listaDePalabras:
		i=0
		buscar=True
		while i<=(len(SopaDeLetras)-1) and buscar==True:
			j=0
			while j <=(len(SopaDeLetras)-1):
				if l[0]==SopaDeLetras[i][j]:
                    valor=evaluarPosicion(l,SopaDeLetras,i,j)
                if valor[0]==True:
                	listaDeSolucion+=(l,(i,j),valor[1],valor[2])
                	buscar=False




