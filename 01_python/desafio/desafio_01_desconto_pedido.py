# Desafio 01 — Cálculo de Desconto em Pedido
# Bootcamp TOTVS — Fundamentos de Engenharia de Dados e Machine Learning
#
# Descrição: Recebe o valor total de um pedido e o percentual de desconto,
# calcula e exibe o valor final com duas casas decimais.
#
# Entrada: uma linha com dois valores separados por espaço
#          ex: 150.00 10
# Saída:   valor final com duas casas decimais
#          ex: 135.00

# Lê a linha de entrada e separa os valores
entrada = input().strip().split()
valor_total = float(entrada[0])
percentual_desconto = int(entrada[1])

# Calcula o valor do desconto e subtrai do total
valor_desconto = valor_total * percentual_desconto / 100
valor_final = valor_total - valor_desconto

# Imprime com duas casas decimais
print(f"{valor_final:.2f}")