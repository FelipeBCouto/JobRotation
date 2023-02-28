# Escreva um programa que inverta os caracteres de um string.
# Evite usar funções prontas, como, por exemplo, reverse.

palavra = []

qnt = int(input("Informe a quantidade letras da palavra: "))

for i in range(0, qnt):
    palavra.append(input(f"Informe a {i}ª letra: "))

for i in range (qnt - 1,-1, -1):
    print(palavra[i])