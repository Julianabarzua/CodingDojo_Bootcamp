
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


cta1 = CuentaBancaria(0.01,200)
cta2 = CuentaBancaria(0.02)

cta1.depósito(100).depósito(100).depósito(100).retiro(200).generar_interés().mostrar_info_cuenta()
cta2.depósito(400).depósito(400).retiro(100).retiro(100).retiro(100).retiro(100).generar_interés().mostrar_info_cuenta()

CuentaBancaria.infoCuentas()