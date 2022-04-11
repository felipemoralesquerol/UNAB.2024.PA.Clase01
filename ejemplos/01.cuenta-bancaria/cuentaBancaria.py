class CuentaBancaria():
    ''' Clase que nos permite la gestión de una Cuenta Bancaria genérica
    '''
    
    def __init__(self, saldo_inicial, nombre, apellido):
        # TODO: Guardar en un lista todo los movimientos de saldo con su fecha
        # TODO: Agregar un atributo de moneda
        # TODO: Ver la forma de soportar cajas de ahorro y/o cuentas corrientes
        self.saldo = saldo_inicial
        self.nombre = nombre
        self.apellido = apellido

    def depositar(self, monto):
        '''Método que nos permite realizar un depósito bancario'''
        self.saldo = self.saldo + monto


    def extraer(self, monto):
        # TODO: Agregar documentación inline (https://www.youtube.com/watch?v=SJqANWdRG4I)
        # TODO: Considerar el caso de saldo negativo
        self.saldo = self.saldo - monto
        

    def datos_titular(self):
        return self.apellido + ', ' + self.nombre
    
    def datos_saldo(self):
        return self.saldo

    def _reset_saldo(self):
        self.saldo = 0 