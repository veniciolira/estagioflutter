def pertence_a_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

numero = int(input("Informe um número: "))

if pertence_a_fibonacci(numero):
    print(f"O número {numero} está na sequência de Fibonacci.")
else:
    print(f"O número {numero} não está na sequência de Fibonacci.")
