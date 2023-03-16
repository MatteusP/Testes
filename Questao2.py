
def fibonacci(num):
    a, b = 0, 1
    c = 0
    
    while c < num:
        c = a + b
        a = b
        b = c
    
    if c == num:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

print(fibonacci(int(input("Digite um Número: "))))
