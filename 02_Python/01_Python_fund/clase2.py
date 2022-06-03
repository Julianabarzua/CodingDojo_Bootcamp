def esPrimo(iterador):
    contador = 0
    for x in range(1,iterador + 1):
        if iterador % x == 0:
            contador +=1
    
    if contador == 2:
        return True
    else:
        return False



def numerosPrimos(n):
    
    arreglo = []
    for i in range(1,n):
        
        if esPrimo(i) == True:
            arreglo.append(i)
    
    return arreglo

print(numerosPrimos(30))