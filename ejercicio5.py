print("Tabla de multiplicar del 1 al 10:")
print("-" * 40)

for i in range(1, 11):  # Filas (número base)
    for j in range(1, 11):  # Columnas (multiplicadores)
        # Formateamos para alinear en columnas
        print(f"{i * j:4}", end="")  
    print()  # Salto de línea al terminar cada fila
