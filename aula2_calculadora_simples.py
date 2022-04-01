print("Calculadora Simples")

print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = int(input("Digite a operação desejada: "))

if op<=0 or op>=5:
    print("Operação inválida")
else:
    #valida o n1
    n1 = int(input("Número 1: "))

    #valida o n2
    n2 = int(input("Número 2: "))

    if op == 1:
        res = n1+n2
    elif op == 2:
        res = n1-n2
    elif op == 3:
        res = n1*n2
    elif op == 4:
        res = n1/n2
    print(f"Resultado é: {res}")


