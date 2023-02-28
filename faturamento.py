# Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# O menor valor de faturamento ocorrido em um dia do mês;
# O maior valor de faturamento ocorrido em um dia do mês;
# Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

def Menor_valor(x):
    y = x[0]
    for i in range(0, 30):
        if x[i] < y:
            y = x[i]
    return y

def Maior_valor(x):
    y = x[0]
    for i in range(0, 30):
        if x[i] > y:
            y = x[i]
    return y

def Acima_media(x):
    y = 0
    for i in range(0,30):
        y = y + x[i]
    resultado = y / 30
    cont = 0
    for i in range(0,30):
        if x[i] > resultado:
            cont += 1
    return cont

valores = [4334,4345,27834,5906,3456,1453,5644,2534,5064,2934,3345,6147,6378,1234,1623,4856,6978,3405,7645,1234,5674,8667,2534,5678,3145,5678,3745,2354,4567,2334]

menor_valor = Menor_valor(valores)
maior_valor = Maior_valor(valores)
acima_media = Acima_media(valores)

print(f"O menor rendimento diário mensal foi: {menor_valor}")
print(f"O menor rendimento diário mensal foi: {maior_valor}")
print(f"Total de dias em que o rendimento foi maior que a média mensal: {acima_media}")