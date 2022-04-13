from cuentaBancaria import CuentaBancaria

# Creación de objeto
x = CuentaBancaria(10, 'Felipe', 'Morales')

# Invocación de métodos
print(x.datos_titular())


# Operación de deposito
x.depositar(100000)
print(x.datos_saldo())



# Operación de extracción
x.extraer(900000)
print(x.datos_saldo())

#felipe_morales.reset_saldo()
#print(dir(x))

# Imprimo el listado de movimientos de la cuenta
print(x.datos_movimientos())
