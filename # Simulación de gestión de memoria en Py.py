# Simulación de gestión de memoria en Python

# Definimos la memoria disponible (en bloques)
memoria_total = 100
memoria_disponible = memoria_total

# Lista para registrar procesos y su memoria asignada
procesos = []

# Función para asignar memoria
def asignar_memoria(nombre, memoria):
    global memoria_disponible
    if memoria <= memoria_disponible:
        procesos.append({'nombre': nombre, 'memoria': memoria})
        memoria_disponible -= memoria
        print(f"Proceso {nombre} asignado con {memoria} unidades de memoria.")
    else:
        print(f"No hay suficiente memoria para el proceso {nombre}.")

# Función para liberar memoria
def liberar_memoria(nombre):
    global memoria_disponible
    for proceso in procesos:
        if proceso['nombre'] == nombre:
            memoria_disponible += proceso['memoria']
            procesos.remove(proceso)
            print(f"Proceso {nombre} finalizado. Memoria liberada.")
            break

# Ejecución de ejemplo
asignar_memoria('P1', 30)
asignar_memoria('P2', 50)
asignar_memoria('P3', 40)  # No se asigna, memoria insuficiente
liberar_memoria('P1')
asignar_memoria('P3', 40)  # Ahora sí se asigna
print(f"Memoria disponible: {memoria_disponible}")
