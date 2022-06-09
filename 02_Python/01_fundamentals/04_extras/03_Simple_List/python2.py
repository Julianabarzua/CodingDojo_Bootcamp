class SLnode:
    def __init__(self,value):
        self.value = value
        self.next = None

class SList:

    def __init__(self):
        self.head = None

    def add_to_front(self,val):
        new_node = SLnode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def remove_from_front(self):
        second_node = self.head.next
        self.head = second_node
        return self

    def add_to_back(self,val):
        if self.head == None :
            self.add_to_front(val)
            return self

        new_node = SLnode(val)
        runner = self.head
        while runner.next != None :
            runner = runner.next
        runner.next = new_node
        return self

    def remove_from_back(self):
        runner = self.head
        cont = 0
        while runner.next != None:
            runner = runner.next
            cont += 1
        
        runner = self.head
        for x in range(cont-1):
            runner = runner.next
        runner.next= None
        return self

    def remove_val(self,val):
        
        if self.head.value == val:
            self.head = self.head.next
            return self

        #para encontrar la posicion del valor y determinar el siguiente nodo
        runner = self.head
        pos = 0
        while (runner.value != val) :
            runner = runner.next
            pos += 1
        next_node = runner.next

        
        runner = self.head
        for x in range(pos-1):
            runner = runner.next
        runner.next= next_node
        return self

    def insert_at(self, val, n):
        
        if n == 0 :
            self.add_to_front(val)
            return self

        new_node = SLnode(val)
        runner = self.head
        for x in range(n-1):
            runner = runner.next
        next_node = runner.next
        runner.next= new_node
        new_node.next = next_node

        return self
        
    def print_values(self):

        runner = self.head
        while runner != None :
            print(runner.value)
            runner = runner.next
        return self


my_list = SList()	# crea una nueva instancia de una lista

my_list.add_to_front("son").add_to_front("enlazadas").add_to_front("Las listas ").add_to_back("divertidas!").print_values()

print("\n")
# my_list.remove_from_front().print_values()
# my_list.remove_from_back().print_values()

# #cuando es el primer valor
# my_list.remove_val("Las listas ").print_values()

# #cuando esta en medio
# my_list.remove_val("son").print_values()

# #cuando esta al final
# my_list.remove_val("divertidas!").print_values()

my_list.insert_at("perro",0).print_values()