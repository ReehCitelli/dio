# Desafio 02 — Aprovação de Pedido por Valor e Prioridade
# Bootcamp TOTVS — Fundamentos de Engenharia de Dados e Machine Learning
#
# Descrição: Recebe o valor e a prioridade de um pedido e decide se ele
# deve ser aprovado, encaminhado para revisão ou rejeitado.
#
# Regras:
#   - valor <= 1000 e prioridade "alta" ou "media" → aprovado
#   - valor > 1000 e prioridade "alta"             → revisao
#   - demais casos                                 → rejeitado
#
# Entrada: uma linha com dois valores separados por espaço
#          ex: 800 alta
# Saída:   "aprovado", "revisao" ou "rejeitado"

# Lê a linha de entrada e separa os valores
entrada = input().strip()
valor_str, prioridade = entrada.split()
valor = int(valor_str)

# Lógica condicional de aprovação
if valor <= 1000 and prioridade in ["alta", "media"]:
    print("aprovado")
elif valor > 1000 and prioridade == "alta":
    print("revisao")
else:
    print("rejeitado")