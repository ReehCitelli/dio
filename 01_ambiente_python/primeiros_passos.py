# ============================================================
# Bootcamp TOTVS — Fundamentos de Engenharia de Dados e ML
# Módulo 01 — Ambiente e Primeiros Passos com Python
# Autora: Renata Citelli
# ============================================================

# ── O que é Python? ──────────────────────────────────────────
# Python é uma linguagem de programação de alto nível,
# interpretada e de propósito geral. É muito usada em:
# - Ciência de Dados e Machine Learning
# - Automação de processos
# - Desenvolvimento web e sistemas
# - Engenharia de Dados

# ── Paradigmas do Python ─────────────────────────────────────
# Python suporta múltiplos paradigmas de programação:
# - Imperativo: instruções executadas linha a linha
# - Orientado a Objetos: organiza código em classes e objetos
# - Funcional: trata funções como valores

# ── Primeiro programa ────────────────────────────────────────
print("Olá, mundo!")
print("Iniciando minha jornada em Python! 🚀")

# ── Tipos de dados básicos ───────────────────────────────────

# int — números inteiros
idade = 29
ano = 2025
print(type(idade))   # <class 'int'>

# float — números decimais
altura = 1.65
salario = 3500.50
print(type(altura))  # <class 'float'>

# str — texto (string)
nome = "Renata Citelli"
cidade = "Campinas"
print(type(nome))    # <class 'str'>

# bool — verdadeiro ou falso
estudando = True
formada = False
print(type(estudando))  # <class 'bool'>

# ── Variáveis ────────────────────────────────────────────────
# Variáveis armazenam valores na memória do programa.
# Em Python, não precisamos declarar o tipo — ele é inferido.

nome = "Renata"
area = "Ciência de Dados"
modulos_concluidos = 1

print(nome)
print(area)
print(modulos_concluidos)

# ── Boas práticas de nomenclatura ────────────────────────────
# - Use snake_case para variáveis e funções (ex: minha_variavel)
# - Nomes descritivos (ex: total_vendas, não tv)
# - Não use palavras reservadas do Python (if, for, while...)

# ── Exibindo valores com print() ─────────────────────────────

# Concatenação simples
print("Meu nome é " + nome)

# Usando f-string (forma moderna e recomendada)
print(f"Olá! Sou {nome} e estudo {area}.")
print(f"Módulos concluídos até agora: {modulos_concluidos}")

# ── Entrada de dados com input() ─────────────────────────────
# A função input() recebe dados digitados pelo usuário.
# Descomente as linhas abaixo para testar no terminal:

# usuario = input("Qual é o seu nome? ")
# print(f"Seja bem-vindo(a), {usuario}!")

# ── Conversão de tipos (casting) ─────────────────────────────
# Às vezes precisamos converter um tipo em outro.

numero_texto = "42"          # string
numero_inteiro = int(numero_texto)   # converte para int
numero_decimal = float(numero_texto) # converte para float

print(type(numero_texto))    # <class 'str'>
print(type(numero_inteiro))  # <class 'int'>
print(type(numero_decimal))  # <class 'float'>

# ── Comentários ──────────────────────────────────────────────
# Use # para comentários de uma linha
# Comentários explicam o código para quem for ler depois

"""
Use três aspas para comentários de múltiplas linhas.
Útil para documentar funções e módulos.
Também chamado de docstring.
"""

# ── Resumo do módulo ─────────────────────────────────────────
print("\n--- Resumo do que aprendi ---")
print("✔ O que é Python e seus paradigmas")
print("✔ Tipos de dados: int, float, str, bool")
print("✔ Como criar e nomear variáveis")
print("✔ Como usar print() e f-strings")
print("✔ Como converter tipos com int(), float(), str()")
