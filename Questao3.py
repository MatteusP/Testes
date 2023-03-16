import json

# Carrega os dados do arquivo dados.json
with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

# Inicializa as variáveis
menor_valor = float('inf')
maior_valor = float('-inf')
soma_valores = 0
dias_com_faturamento_acima_da_media = 0
quantidade_dias_com_faturamento = 0

# Percorre o objeto para calcular o menor valor de faturamento, o maior valor de faturamento e a média mensal
for dia in dados:
    if dia['valor'] > 0:
        menor_valor = min(menor_valor, dia['valor'])
        maior_valor = max(maior_valor, dia['valor'])
        soma_valores += dia['valor']
        quantidade_dias_com_faturamento += 1

media_mensal = soma_valores / quantidade_dias_com_faturamento

# Percorre o objeto novamente para contar o número de dias em que o valor de faturamento diário foi superior à média mensal
for dia in dados:
    if dia['valor'] > media_mensal:
        dias_com_faturamento_acima_da_media += 1

# Imprime os resultados
print(media_mensal)
print(f'Menor valor de faturamento: R${menor_valor:.2f}')
print(f'Maior valor de faturamento: R${maior_valor:.2f}')
print(f'Número de dias com faturamento acima da média: {dias_com_faturamento_acima_da_media}')
