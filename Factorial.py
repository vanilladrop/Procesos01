def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n

num = int(input("Escribe el número del que requieres su factorial: "))

if num < 0:
    print("No hay factorial para números negativos.")
elif num == 0:
    print("El factorial de 0 es 1.")
else:
    print("El factorial de", num, "es", factorial(num))

print("Este es un proyecto en GitHub")