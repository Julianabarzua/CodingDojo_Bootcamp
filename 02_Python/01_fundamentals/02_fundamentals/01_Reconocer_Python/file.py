num1 = 42 #variable declaration Numbers
num2 = 2.3 #variable declaration Numbers
boolean = True #variable declaration Boolean
string = 'Hello World' #variable declaration String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana') #tuple initialize
print(type(fruit)) #type check
print(pizza_toppings[1]) #list acces value
pizza_toppings.append('Mushrooms') #list add value
print(person['name']) #dictionary acces value
person['name'] = 'George' #dictionary change value
person['eye_color'] = 'blue' #dictionary add value
print(fruit[2]) #Tuple acces value

if num1 > 45:                       #conditional if-else
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:                 #length check - conditional else if
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):          #for loop start
    print(x)                #for loop stop
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)

x = 0                       #While loop
while(x < 5):               #while loop start
    print(x)
    x += 1                  #incremenet

pizza_toppings.pop()        #list delete last value
pizza_toppings.pop(1)       #list delete second value

print(person)               
person.pop('eye_color')     #delete element in dictionary
print(person)

for topping in pizza_toppings:          #el for e recorrerá hasta llegar a las olives
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():            #definiciond e funcion que imprime Hello diez veces
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):             #definiciond e funcion que imprime Hello 'x' veces
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):    #definiciond e funcion que imprime Hello 'x' veces y si no se le entrega dato, las imprime 10 veces
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)