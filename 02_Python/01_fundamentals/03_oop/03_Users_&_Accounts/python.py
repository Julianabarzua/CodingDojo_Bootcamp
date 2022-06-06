class CuentaBancaria:
    cuentas=[]

    def __init__(self, tasa_interés, balance = 0): 
        self.balance = balance
        self.tasa = tasa_interés
        CuentaBancaria.cuentas.append(self)

    def depósito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        self.balance -= amount
        return self

    def mostrar_info_cuenta(self):
        print(f'Balance: {self.balance}')
        return self

    def generar_interés(self):
        if self.balance > 0:
            self.balance*=(1+self.tasa)
        return self

    @classmethod
    def infoCuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()


class Usuario:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuenta_savings = CuentaBancaria(0.04)
        self.cuenta_cheking = CuentaBancaria(0.01)
    
    # agregando el método de depósito
    def hacer_deposito(self, amount, account):
        
        if account == "checking":
            self.cuenta_cheking.depósito(amount)
        elif account == "savings":
            self.cuenta_savings.depósito(amount)
        else:
            print("ERROR: no se realiza deposito")
        
        return self

    def hacer_retiro(self,amount,account):
        if account == "checking":
            self.cuenta_cheking.retiro(amount)
        elif account == "savings":
            self.cuenta_savings.retiro(amount)
        return self


    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, Balance checking account: ${self.cuenta_cheking.balance}, Balance savings account: ${self.cuenta_savings.balance}")
        return self

    def transfer_dinero(self,user2,account1, account2, amount):
        if account1 == "checking":
            self.cuenta_cheking.balance -= amount
        elif account1 == "savings":
            self.cuenta_savings.balance -= amount

        if account2 == "checking":
            user2.cuenta_cheking.balance += amount
        elif account2 == "savings":
            user2.cuenta_savings.balance += amount

        return self



dani = Usuario("Daniela Andrade", "daniand@jmail.com")
pancho = Usuario('Francisco Fuentes', 'franfu@jmail.com')
juli = Usuario('Julian Abarzua', 'juaba@jmail.com')

juli.hacer_deposito(100,"checking")
dani.hacer_deposito(100,"savings")

juli.mostrar_balance_usuario()
dani.mostrar_balance_usuario()
pancho.mostrar_balance_usuario()

juli.transfer_dinero(pancho,"checking","checking",50)

juli.mostrar_balance_usuario()
pancho.mostrar_balance_usuario()