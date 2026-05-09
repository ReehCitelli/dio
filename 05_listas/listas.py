# ============================================================
# Bootcamp TOTVS — Fundamentos de Engenharia de Dados e ML
# Módulo 05 — Trabalhando com Listas
# Autora: Renata Citelli
# ============================================================

# ── O que é uma Lista? ───────────────────────────────────────
# Lista é uma coleção ordenada e mutável de elementos.
# Pode conter tipos diferentes e permite duplicatas.

frutas = ["maçã", "banana", "uva", "laranja"]
numeros = [1, 2, 3, 4, 5]
misto = ["Renata", 29, True, 1.65]

print(frutas)
print(numeros)
print(misto)

# ── Acessando elementos ──────────────────────────────────────
print("\n--- Indexação ---")

ferramentas = ["Python", "SQL", "Power BI", "Excel", "Git"]

print(f"Primeira: {ferramentas[0]}")    # Python
print(f"Última:   {ferramentas[-1]}")   # Git
print(f"Índice 1 a 3: {ferramentas[1:3]}")  # SQL, Power BI

# ── Modificando listas ───────────────────────────────────────
print("\n--- Adicionando e removendo ---")

chamados = ["Chamado #001", "Chamado #002", "Chamado #003"]
print(f"Original: {chamados}")

chamados.append("Chamado #004")         # adiciona no final
print(f"append(): {chamados}")

chamados.insert(1, "Chamado #URGENTE")  # adiciona na posição 1
print(f"insert(): {chamados}")

chamados.remove("Chamado #002")         # remove pelo valor
print(f"remove(): {chamados}")

removido = chamados.pop()               # remove e retorna o último
print(f"pop():    {chamados}")
print(f"Removido: {removido}")

# ── Informações sobre a lista ────────────────────────────────
print("\n--- Informações ---")

notas = [8.5, 9.0, 7.5, 10.0, 6.0, 9.5]

print(f"Tamanho:  {len(notas)}")
print(f"Maior:    {max(notas)}")
print(f"Menor:    {min(notas)}")
print(f"Soma:     {sum(notas)}")
print(f"Média:    {sum(notas) / len(notas):.2f}")
print(f"Tem 10.0? {10.0 in notas}")

# ── Ordenando listas ─────────────────────────────────────────
print("\n--- Ordenação ---")

numeros = [5, 2, 8, 1, 9, 3]
print(f"Original:       {numeros}")

numeros.sort()
print(f"sort():         {numeros}")

numeros.sort(reverse=True)
print(f"sort(reverse):  {numeros}")

print(f"sorted():       {sorted([5, 2, 8, 1])}")  # não altera a original

# ── Iterando sobre listas ────────────────────────────────────
print("\n--- Iteração ---")

areas = ["Suporte", "Comercial", "Dados", "TI"]

for area in areas:
    print(f"  - {area}")

# Com índice usando enumerate()
print()
for indice, area in enumerate(areas):
    print(f"  {indice + 1}. {area}")

# ── List Comprehension ───────────────────────────────────────
# Forma compacta e elegante de criar listas

print("\n--- List Comprehension ---")

# Forma tradicional
quadrados = []
for n in range(1, 6):
    quadrados.append(n ** 2)
print(f"Tradicional:       {quadrados}")

# Com list comprehension
quadrados = [n ** 2 for n in range(1, 6)]
print(f"Comprehension:     {quadrados}")

# Com condição
pares = [n for n in range(1, 11) if n % 2 == 0]
print(f"Só pares (1-10):   {pares}")

# ── Exemplo prático — painel de chamados ─────────────────────
print("\n--- Painel de chamados ---")

chamados = [
    {"id": 1, "status": "aberto",   "tempo": 10},
    {"id": 2, "status": "fechado",  "tempo": 48},
    {"id": 3, "status": "aberto",   "tempo": 80},
    {"id": 4, "status": "fechado",  "tempo": 5},
    {"id": 5, "status": "aberto",   "tempo": 30},
]

abertos = [c for c in chamados if c["status"] == "aberto"]
tempos = [c["tempo"] for c in abertos]

print(f"Total de chamados: {len(chamados)}")
print(f"Chamados abertos:  {len(abertos)}")
print(f"Tempo médio (abertos): {sum(tempos) / len(tempos):.1f}h")
print(f"Chamado mais antigo:   #{max(abertos, key=lambda c: c['tempo'])['id']}")

# ── Resumo do módulo ─────────────────────────────────────────
print("\n--- Resumo do que aprendi ---")
print("OK Criação e acesso a elementos de listas")
print("OK append, insert, remove, pop")
print("OK len, max, min, sum, in")
print("OK sort() e sorted() para ordenação")
print("OK Iteração com for e enumerate()")
print("OK List comprehension para listas compactas")