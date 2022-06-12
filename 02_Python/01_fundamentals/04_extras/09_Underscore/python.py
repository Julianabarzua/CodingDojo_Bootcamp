class Underscore:
    def map(self, iterable, callback):
        for i in range(len(iterable)):
            iterable[i]=callback(iterable[i])
        print(iterable)

    def find(self, iterable, callback):

        list =[]
        for val in iterable:
            if callback(val):
                print(val)
                return val

    def filter(self, iterable, callback):
        list =[]
        for val in iterable:
            if callback(val):
                list.append(val)        
        print(list)

    def reject(self, iterable, callback):
        list =[]
        for val in iterable:
            if not(callback(val)):
                list.append(val)        
        print(list)


_ = Underscore()

_.map([1,2,3], lambda x: x*2) # debería devolver [2,4,6]
_.find([1,2,3,4,5,6], lambda x: x>4) # debería devolver el primer valor que sea mayor que 4
_.filter([1,2,3,4,5,6], lambda x: x%2==0) # debería devolver [2,4,6]
_.reject([1,2,3,4,5,6], lambda x: x%2==0) # debería devolver [1,3,5]


