# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

def Percentual (tot, estado):
    return estado * 100 / tot

def Total(x):
    total = 0
    for i in range(0,5):
        total = total + x[i]
    return total

valores = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
estados = ["SP", "RJ", "MG", "ES", "Outros"]

for i in range(0,5):
    print(f"O percentual de {estados[i]} foi: ", Percentual(Total(valores), valores[i]))