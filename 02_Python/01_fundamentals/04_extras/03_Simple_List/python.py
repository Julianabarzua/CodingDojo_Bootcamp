
class SLNode:

    def __init__(self, val):
        self.value = val
        self.next = None


class SList:

    def __init__(self):
        self.head = None

    def add_to_front(self, val):    # agregó esta línea, toma un valor
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next 	# establece runner a su vecino
        return self             # una vez terminado el ciclo, devuelve self para permitir el encadenamiento

    def add_to_back(self, val):

        if self.head == None:	    # si la lista está vacía
            self.add_to_front(val)	# ejecuta el método add_to_front
            return self             # asegurémonos de que el resto de esta función no suceda si agregamos al comienzo

        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node      # incrementa runner al siguiente nodo de la lista
        return self                 # return self para permitir el encadenamiento


my_list = SList()	# crea una nueva instancia de una lista
my_list.add_to_front("son").add_to_front("Las listas enlazadas").add_to_back("divertidas!").print_values()




