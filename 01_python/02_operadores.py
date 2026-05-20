# ============================================================
# Bootcamp TOTVS — Fundamentos de Engenharia de Dados e ML
# Módulo 02 — Tipos de Operadores com Python
# Autora: Renata Citelli
# ============================================================

# ── Operadores Aritméticos ───────────────────────────────────
# Usados para realizar cálculos matemáticos

a = 10
b = 3

print("--- Operadores Aritméticos ---")
print(f"a = {a}, b = {b}")
print(f"Adição:        a + b = {a + b}")
print(f"Subtração:     a - b = {a - b}")
print(f"Multiplicação: a * b = {a * b}")
print(f"Divisão:       a / b = {a / b}")       # retorna float
print(f"Divisão inteira: a // b = {a // b}")   # retorna int
print(f"Módulo (resto): a % b = {a % b}")      # resto da divisão
print(f"Potência:      a ** b = {a ** b}")      # 10 elevado a 3

# Exemplo prático — calculando desconto
preco = 150.00
desconto = 0.10
preco_final = preco - (preco * desconto)
print(f"\nPreço original: R$ {preco:.2f}")
print(f"Desconto (10%): R$ {preco * desconto:.2f}")
print(f"Preço final:    R$ {preco_final:.2f}")

# ── Operadores Relacionais ───────────────────────────────────
# Comparam dois valores e retornam True ou False

x = 8
y = 5

print("\n--- Operadores Relacionais ---")
print(f"x = {x}, y = {y}")
print(f"x == y  (igual):          {x == y}")
print(f"x != y  (diferente):      {x != y}")
print(f"x > y   (maior):          {x > y}")
print(f"x < y   (menor):          {x < y}")
print(f"x >= y  (maior ou igual): {x >= y}")
print(f"x <= y  (menor ou igual): {x <= y}")

# Exemplo prático — verificando meta de atendimento
chamados_resolvidos = 42
meta = 40

print(f"\nMeta atingida? {chamados_resolvidos >= meta}")

# ── Operadores Lógicos ───────────────────────────────────────
# Combinam expressões booleanas

print("\n--- Operadores Lógicos ---")

tem_experiencia = True
tem_formacao = True
tem_ingles = False

# and — retorna True se AMBAS as condições forem verdadeiras
print(f"Tem experiência AND formação: {tem_experiencia and tem_formacao}")

# or — retorna True se PELO MENOS UMA condição for verdadeira
print(f"Tem experiência OR inglês:    {tem_experiencia or tem_ingles}")

# not — inverte o valor booleano
print(f"NOT tem inglês:               {not tem_ingles}")

# Exemplo prático — triagem de candidato
print("\n--- Triagem de candidato ---")
if tem_experiencia and tem_formacao:
    print("Candidato aprovado para a próxima etapa!")
else:
    print("Candidato não atende aos requisitos mínimos.")

# ── Operadores de Atribuição ─────────────────────────────────
# Atribuem e atualizam valores em variáveis

print("\n--- Operadores de Atribuição ---")
total = 100
print(f"Valor inicial: {total}")

total += 50   # total = total + 50
print(f"Após += 50:    {total}")

total -= 30   # total = total - 30
print(f"Após -= 30:    {total}")

total *= 2    # total = total * 2
print(f"Após *= 2:     {total}")

total //= 3   # total = total // 3
print(f"Após //= 3:    {total}")

# ── Resumo do módulo ─────────────────────────────────────────
print("\n--- Resumo do que aprendi ---")
print("✔ Operadores aritméticos: +, -, *, /, //, %, **")
print("✔ Operadores relacionais: ==, !=, >, <, >=, <=")
print("✔ Operadores lógicos: and, or, not")
print("✔ Operadores de atribuição: =, +=, -=, *=, //=")
