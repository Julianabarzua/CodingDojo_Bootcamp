
#1 - cuenta regresiva
def cuentaRegresiva(numero):

    result = []
    for x in range(numero,-1,-1):
        result.append(x)
    return result

x = int(input("Introduzca el número: "))
print(cuentaRegresiva(x))


#2 Imprimir y devolver
def imprimir_y_devolver(list):
    print(list[0])
    return(list[1])

x=imprimir_y_devolver([1,2])
print(x)


#3 Primero más longitud
def primero_mas_longitud(list):
    sum = list[0] + len(list)
    return sum

x = primero_mas_longitud([1,2,3,4,5])
print(x)


#4 Valores mayores que el segundo
def valores_mayores_que_el_segundo(lista):
    lista2 = []
    contador = 0
    
    if len(lista) > 2:
        for valor in lista:
            if valor > lista[1]:
                lista2.append(valor)
                contador +=1
        print(contador)
        return lista2
    else:
        print("False")

x = valores_mayores_que_el_segundo([5,2,3,2,1,4])
print(x)
valores_mayores_que_el_segundo([3])


#5 Esta longitud, ese valor
def length_and_value(lista):
    lista2=[]
    for x in range(lista[0]):
        lista2.append(lista[1])

    return lista2

x= length_and_value([4,7])
print(x)

y= length_and_value([6,2])
print(y)
