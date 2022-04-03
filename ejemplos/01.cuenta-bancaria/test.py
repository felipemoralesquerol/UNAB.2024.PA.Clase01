from cuentaBancaria import CuentaBancaria

# Creación de objeto
felipe_morales = CuentaBancaria(0, 'Felipe', 'Morales')

# Invocación de métodos
print(felipe_morales.datos_titular())


# Operación de deposito
felipe_morales.depositar(100000)
print(felipe_morales.datos_saldo())


# Operación de extracción
felipe_morales.extraer(100000)
print(felipe_morales.datos_saldo())

