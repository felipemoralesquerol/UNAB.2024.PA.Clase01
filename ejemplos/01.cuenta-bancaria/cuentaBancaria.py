class CuentaBancaria():
    
    def __init__(self, saldo_inicial, nombre, apellido):
        self.saldo = saldo_inicial
        self.nombre = nombre
        self.apellido = apellido

    def depositar(self, monto):
        self.saldo = self.saldo + monto


    def extraer(self, monto):
        self.saldo = self.saldo - monto
        

    def datos_titular(self):
        return self.apellido + ', ' + self.nombre
    
    def datos_saldo(self):
        return self.saldo

# felipe_morales = CuentaBancaria('Felipe', 'Morales')

# # Invocación de métodos
# print(felipe_morales.datos_titular())


# # Operación de deposito
# felipe_morales.depositar(100000)
# print(felipe_morales.datos_saldo())        