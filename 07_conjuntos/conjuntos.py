# ============================================================
# Bootcamp TOTVS — Fundamentos de Engenharia de Dados e ML
# Módulo 07 — Explorando Conjuntos (Sets)
# Autora: Renata Citelli
# ============================================================

# ── O que é um Conjunto? ─────────────────────────────────────
# Set é uma coleção NÃO ordenada, NÃO indexada e SEM duplicatas.
# Muito útil para eliminar valores repetidos e fazer operações
# matemáticas entre grupos de dados.

frutas = {"maçã", "banana", "uva", "maçã", "banana"}
print(f"Set (sem duplicatas): {frutas}")

numeros = {1, 2, 3, 4, 5}
print(f"Números: {numeros}")

# Criando set a partir de uma lista com duplicatas
lista_com_repeticao = [1, 2, 2, 3, 3, 3, 4]
sem_repeticao = set(lista_com_repeticao)
print(f"Lista original:  {lista_com_repeticao}")
print(f"Set resultante:  {sem_repeticao}")

# ── Adicionando e removendo ──────────────────────────────────
print("\n--- Adicionando e removendo ---")

tecnologias = {"Python", "SQL", "Excel"}
print(f"Original: {tecnologias}")

tecnologias.add("Power BI")
print(f"add():    {tecnologias}")

tecnologias.discard("Excel")       # remove sem erro se não existir
print(f"discard(): {tecnologias}")

tecnologias.remove("SQL")          # remove — gera erro se não existir
print(f"remove():  {tecnologias}")

# ── Operações entre conjuntos ────────────────────────────────
print("\n--- Operações entre conjuntos ---")

time_suporte   = {"Ana", "Bruno", "Carlos", "Diana"}
time_comercial = {"Carlos", "Diana", "Eduardo", "Fernanda"}

# União — todos os elementos de ambos os conjuntos
uniao = time_suporte | time_comercial
print(f"União:        {uniao}")

# Interseção — elementos que estão nos dois conjuntos
intersecao = time_suporte & time_comercial
print(f"Interseção:   {intersecao}")

# Diferença — elementos que estão em A mas não em B
diferenca = time_suporte - time_comercial
print(f"Só Suporte:   {diferenca}")

diferenca2 = time_comercial - time_suporte
print(f"Só Comercial: {diferenca2}")

# Diferença simétrica — elementos que estão em um OU outro, mas não nos dois
dif_simetrica = time_suporte ^ time_comercial
print(f"Diferença simétrica: {dif_simetrica}")

# ── Verificações ─────────────────────────────────────────────
print("\n--- Verificações ---")

print(f"'Ana' está no suporte?     {'Ana' in time_suporte}")
print(f"'Ana' está no comercial?   {'Ana' in time_comercial}")

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print(f"\n{a} é subconjunto de {b}?   {a.issubset(b)}")
print(f"{b} é superconjunto de {a}? {b.issuperset(a)}")
print(f"{a} e {b} são disjuntos?    {a.isdisjoint(b)}")

# ── Exemplo prático — analisando chamados ────────────────────
print("\n--- Análise de chamados ---")

chamados_segunda = {"#001", "#002", "#003", "#004", "#005"}
chamados_terca   = {"#003", "#004", "#005", "#006", "#007"}

resolvidos_segunda = {"#001", "#002", "#003"}
resolvidos_terca   = {"#004", "#005", "#006"}

todos_chamados = chamados_segunda | chamados_terca
pendentes = todos_chamados - (resolvidos_segunda | resolvidos_terca)
reabertos = chamados_segunda & chamados_terca

print(f"Total de chamados únicos: {len(todos_chamados)}")
print(f"Chamados pendentes:       {pendentes}")
print(f"Chamados reabertos:       {reabertos}")

# ── Exemplo prático — limpando dados duplicados ──────────────
print("\n--- Limpando dados duplicados ---")

emails_cadastro = [
    "ana@email.com",
    "bruno@email.com",
    "ana@email.com",
    "carlos@email.com",
    "bruno@email.com",
    "diana@email.com"
]

emails_unicos = list(set(emails_cadastro))
print(f"Emails com duplicata: {len(emails_cadastro)}")
print(f"Emails únicos:        {len(emails_unicos)}")
print(f"Duplicatas removidas: {len(emails_cadastro) - len(emails_unicos)}")

# ── Resumo do módulo ─────────────────────────────────────────
print("\n--- Resumo do que aprendi ---")
print("OK Set é não ordenado, não indexado e sem duplicatas")
print("OK add(), discard(), remove() para modificar")
print("OK União (|), Interseção (&), Diferença (-), Simétrica (^)")
print("OK issubset(), issuperset(), isdisjoint() para verificações")
print("OK Muito útil para limpar dados duplicados")