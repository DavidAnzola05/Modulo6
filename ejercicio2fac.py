n = int(input("Ingrese un número: "))

resultado = 1
while n > 0:
    resultado *= n
    n -= 1

print("El factorial es:", resultado)
