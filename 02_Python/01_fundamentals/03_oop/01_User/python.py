class Usuario:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0
    
    # agregando el método de depósito
    def hacer_deposito(self, amount):
        self.balance_cuenta += amount
        return self

    def hacer_retiro(self,amount):
        self.balance_cuenta -= amount
        return self


    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, Balance: ${self.balance_cuenta}")
        return self

    def transfer_dinero(self,other_user,amount):
        self.balance_cuenta -=amount
        other_user.balance_cuenta +=amount
        return self

dani = Usuario("Daniela Andrade", "daniand@jmail.com")
pancho = Usuario('Francisco Fuentes', 'franfu@jmail.com')
juli = Usuario('Julian Abarzua', 'juaba@jmail.com')

dani.hacer_deposito(100)
dani.hacer_deposito(100)
dani.hacer_deposito(100)
dani.hacer_retiro(200)
dani.mostrar_balance_usuario()

pancho.hacer_deposito(50)
pancho.hacer_deposito(100)
pancho.hacer_retiro(50)
pancho.hacer_retiro(50)
pancho.mostrar_balance_usuario()

juli.hacer_deposito(500)
juli.hacer_retiro(100)
juli.hacer_retiro(100)
juli.hacer_retiro(100)
juli.mostrar_balance_usuario()

dani.transfer_dinero(juli,100)
dani.mostrar_balance_usuario()
juli.mostrar_balance_usuario()