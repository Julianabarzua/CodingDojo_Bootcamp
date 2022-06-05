#1 Actualizar valores en diccionarios y listas

x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

################    RESPUESTA1    ##########################
x[1][0] = 15
estudiantes[0]['last_name'] = "Bryant"
directorio_deportes['fútbol'][0] = "Andrés"
z[0]['y'] = 30


estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]



#2 Iterar a través de una lista de diccioanrios

def iterateDictionary(some_list):
    for dicc in some_list:
        print(f"first_name - {dicc['first_name']}, last_name - {dicc['last_name']}")

iterateDictionary(estudiantes) 



#3 Obtener valores de una lista de diccionarios

def iterateDictionary2(key_name, some_list):
    for dicc in some_list:
        print(dicc[key_name])

iterateDictionary2('first_name',estudiantes)
print("\n")
iterateDictionary2('last_name',estudiantes)


#4 Iterar a traves de un diccioanrio con valores de lista

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for k in some_dict:
        print("\n")
        print(len(some_dict[k]),k.upper())
        for value in some_dict[k]:
            print(value)

printInfo(dojo)