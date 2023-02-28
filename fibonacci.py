# Escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci 
# e retorne uma mensagem avisando se o número informado pertence ou não a sequência

def checa_fibonacci (valor):
    x = 1
    y = 1
    prox = 0
    while prox <= valor:
        x = y
        y = prox
        if prox == valor:
            return 1
        prox = x + y


valor = int(input("Informe um valor: "))

resultado = checa_fibonacci(valor) # não chamei a função durante o input na variável "valor" para a utilizar no output

if resultado == 1:
    print(f"O valor {valor} pertence a sequência de Fibonacci!")
else:
    print(f"O valor {valor} não pertence a sequência de Fibonacci!")