class CuentaBancaria():
    ''' Clase que nos permite la gestión de una Cuenta Bancaria genérica!
    '''
    
    def __init__(self, saldo_inicial, nombre, apellido, moneda = '$'):
        # TODO: Ver la forma de soportar cajas de ahorro y/o cuentas corrientes
        self.movimientos = []
        self.saldo = saldo_inicial
        self.nombre = nombre
        self.apellido = apellido
        self.moneda = moneda

    def depositar(self, monto):
        '''Método que nos permite realizar un depósito bancario'''
        self.movimientos.append('DEPOSITO: ' + str(monto))
        self.saldo = self.saldo + monto


    def extraer(self, monto):
        '''Método que nos permite realizar una extracción de un cuenta bancaria'''
        if self.saldo - monto >= 0:
            self.movimientos.append('EXTRACCION: ' + str(monto))
            self.saldo = self.saldo - monto
        else:
           self.movimientos.append('SALDO INSUFICIENTE: ' + str(monto)) 
           print("Saldo insuficiente")
        

    def datos_titular(self):
        '''Método que nos permite mostrar los datos del titular y su saldo'''
        return self.apellido + ', ' + self.nombre + " con el saldo: " + str(self.saldo) + " " + self.moneda
    
    def datos_saldo(self):
        return self.saldo

    def _reset_saldo(self):
        self.saldo = 0 

    def datos_movimientos(self):
        return list(self.movimientos)  