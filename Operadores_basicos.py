def operadores_basicos(a, b):
    # Operaciones matemáticas
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"

    # Operadores comparativos
    mayor_que = a > b
    menor_que = a < b
    igual_a = a == b

    # Operadores lógicos
    and_logico = (a > 0) and (b > 0)
    or_logico = (a > 0) or (b > 0)
    not_logico = not (a == b)

    #Resultados de operadores
    print(f"Operaciones matemáticas:")
    print(f"La suma de {a} + {b} es = {suma}")
    print(f"La resta de {a} - {b} es = {resta}")
    print(f"La multiplicación de {a} * {b} es = {multiplicacion}")
    print(f"La división de {a} / {b} es = {division}")

    print(f"\nOperadores comparativos:")
    print(f"{a} > {b} es {mayor_que}")
    print(f"{a} < {b} es {menor_que}")
    print(f"{a} == {b} es {igual_a}")

    print(f"\nOperadores lógicos:")
    print(f"({a} > 0) AND ({b} > 0) es {and_logico}")
    print(f"({a} > 0) OR ({b} > 0) es {or_logico}")
    print(f"NOT ({a} == {b}) es {not_logico}")

# Ejemplo de uso
operadores_basicos(5, 3)