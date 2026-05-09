# ============================================================
# Bootcamp TOTVS — Fundamentos de Engenharia de Dados e ML
# Módulo 03 — Estruturas Condicionais e de Repetição
# Autora: Renata Citelli
# ============================================================

# ── Estruturas Condicionais ──────────────────────────────────
# Permitem que o programa tome decisões com base em condições.
# if → se | elif → senão se | else → senão

print("--- if / elif / else ---")

nota = 75

if nota >= 90:
    print("Aprovado com distinção!")
elif nota >= 70:
    print("Aprovado!")
elif nota >= 50:
    print("Recuperação.")
else:
    print("Reprovado.")

# Exemplo prático — classificando prioridade de chamado
print("\n--- Classificação de chamado ---")

tempo_aberto = 48  # horas

if tempo_aberto >= 72:
    prioridade = "Crítica"
elif tempo_aberto >= 24:
    prioridade = "Alta"
else:
    prioridade = "Normal"

print(f"Chamado aberto há {tempo_aberto}h → Prioridade: {prioridade}")

# ── Condicional em uma linha (ternário) ──────────────────────
idade = 20
status = "maior de idade" if idade >= 18 else "menor de idade"
print(f"\nIdade: {idade} → {status}")

# ── Estrutura de Repetição — for ─────────────────────────────
print("\n--- Loop for ---")

areas = ["Suporte", "Comercial", "Dados", "TI"]

for area in areas:
    print(f"Área: {area}")

print("\nContando de 1 a 5:")
for i in range(1, 6):
    print(i)

# Exemplo prático — processando chamados
print("\n--- Processando chamados ---")

chamados = ["Chamado #001", "Chamado #002", "Chamado #003"]

for chamado in chamados:
    print(f"OK: {chamado} processado com sucesso.")

# ── Estrutura de Repetição — while ───────────────────────────
print("\n--- Loop while ---")

tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    tentativas += 1
    print(f"Tentativa {tentativas} de {max_tentativas}")

print("Número máximo de tentativas atingido.")

# ── break e continue ─────────────────────────────────────────
print("\n--- break ---")
for numero in range(1, 10):
    if numero == 5:
        print("Encontrou o 5 — parando o loop.")
        break
    print(numero)

print("\n--- continue ---")
for numero in range(1, 8):
    if numero % 2 == 0:
        continue
    print(f"Número ímpar: {numero}")

# ── Exemplo completo — sistema de tickets ────────────────────
print("\n--- Sistema de tickets ---")

tickets = [
    {"id": 1, "status": "aberto",  "tempo": 10},
    {"id": 2, "status": "fechado", "tempo": 48},
    {"id": 3, "status": "aberto",  "tempo": 80},
    {"id": 4, "status": "aberto",  "tempo": 5},
]

print("Tickets em aberto:")

for ticket in tickets:
    if ticket["status"] == "fechado":
        continue
    if ticket["tempo"] >= 24:
        print(f"  Ticket #{ticket['id']} — aberto há {ticket['tempo']}h — ATENCAO!")
    else:
        print(f"  Ticket #{ticket['id']} — aberto há {ticket['tempo']}h — OK")

# ── Resumo do módulo ─────────────────────────────────────────
print("\n--- Resumo do que aprendi ---")
print("OK if, elif, else — tomada de decisão")
print("OK Operador ternário — if/else em uma linha")
print("OK for — iteração sobre sequências")
print("OK while — repetição com condição")
print("OK break — interrompe o loop")
print("OK continue — pula para a próxima iteração")
