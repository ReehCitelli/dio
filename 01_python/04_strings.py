# ============================================================
# Bootcamp TOTVS — Fundamentos de Engenharia de Dados e ML
# Módulo 04 — Manipulando Strings com Python
# Autora: Renata Citelli
# ============================================================

# ── O que é uma String? ──────────────────────────────────────
# String é uma sequência de caracteres (texto).
# Pode ser criada com aspas simples, duplas ou triplas.

nome = "Renata Citelli"
cidade = 'Campinas'
descricao = """Estudante de Ciência de Dados,
apaixonada por tecnologia."""

print(nome)
print(cidade)
print(descricao)

# ── Acessando caracteres ─────────────────────────────────────
# Strings são indexadas — cada caractere tem uma posição.
# Índice começa em 0.

print("\n--- Indexação ---")
print(f"Primeiro caractere: {nome[0]}")   # R
print(f"Último caractere:   {nome[-1]}")  # i
print(f"Caracteres 0 a 5:   {nome[0:6]}") # Renata

# ── Métodos essenciais ───────────────────────────────────────
print("\n--- Métodos de String ---")

texto = "  suporte técnico amlabs  "

print(f"Original:    '{texto}'")
print(f"strip():     '{texto.strip()}'")        # remove espaços nas bordas
print(f"upper():     '{texto.strip().upper()}'") # tudo maiúsculo
print(f"lower():     '{texto.strip().lower()}'") # tudo minúsculo
print(f"title():     '{texto.strip().title()}'") # primeira letra maiúscula
print(f"replace():   '{texto.strip().replace('amlabs', 'AMLabs')}'")
print(f"len():       {len(texto.strip())}")      # quantidade de caracteres

# ── Verificações ─────────────────────────────────────────────
print("\n--- Verificações ---")

email = "renata@email.com"
numero = "12345"

print(f"'{email}' contém '@'?      {('@' in email)}")
print(f"'{numero}' é numérico?     {numero.isnumeric()}")
print(f"'{email}' começa com 're'? {email.startswith('re')}")
print(f"'{email}' termina com 'com'? {email.endswith('com')}")

# ── Separando e juntando ─────────────────────────────────────
print("\n--- split() e join() ---")

# split() — divide a string em uma lista
frase = "Python,SQL,Power BI,Excel"
ferramentas = frase.split(",")
print(f"split: {ferramentas}")

# join() — junta uma lista em string
unido = " | ".join(ferramentas)
print(f"join:  {unido}")

# ── f-strings ────────────────────────────────────────────────
print("\n--- f-strings ---")

nome = "Renata"
modulo = 4
bootcamp = "TOTVS"

print(f"Olá, {nome}! Você está no módulo {modulo} do bootcamp {bootcamp}.")
print(f"Módulo formatado: {modulo:02d}")  # exibe com 2 dígitos: 04
print(f"Valor: R$ {1500.5:.2f}")          # formata casas decimais

# ── Exemplo prático — tratando dados de chamado ──────────────
print("\n--- Tratando dados de chamado ---")

chamado_bruto = "  PROBLEMA NO TOUCHPAY - PAGAMENTO NÃO PROCESSADO  "

titulo = chamado_bruto.strip().title()
contem_pagamento = "pagamento" in chamado_bruto.lower()
palavras = len(titulo.split())

print(f"Título tratado:        {titulo}")
print(f"Envolve pagamento?     {contem_pagamento}")
print(f"Número de palavras:    {palavras}")
print(f"Caracteres (sem espaços extras): {len(chamado_bruto.strip())}")

# ── Resumo do módulo ─────────────────────────────────────────
print("\n--- Resumo do que aprendi ---")
print("OK Criação de strings com aspas simples, duplas e triplas")
print("OK Indexação e fatiamento de strings")
print("OK Métodos: strip, upper, lower, title, replace, len")
print("OK Verificações: in, startswith, endswith, isnumeric")
print("OK split() e join() para separar e juntar strings")
print("OK f-strings para formatar textos de forma eficiente")