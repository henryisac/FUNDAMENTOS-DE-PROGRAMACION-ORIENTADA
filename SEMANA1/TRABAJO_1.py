#arreglo bidimencional 3*3
arreglo_bidim= [
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
]
#valor que estamos buscando
valor_buscar = 20

#Indagamos las variables para buscar la posicion del valor
fila_localizada = -1
columna_localizada = -1

#Recorrer la matriz para buscar el valor
for fila in range (len(arreglo_bidim)):
    for columna in range (len(arreglo_bidim[fila])):
        if arreglo_bidim [fila][columna] == valor_buscar:
            fila_localizada = fila
            columna_localizada = columna
            break
    #Salir del bucle exterior si se encuentra el valor
    #verificar si se encuentra el valor y mas tras la posicion
#
if fila_localizada != -1:
    print(f"se encontro{ valor_buscar} en la fila {fila_localizada} y columna {columna_localizada}")
else:
    print(f"{valor_buscar}no se encontro en arreglo_bidim")