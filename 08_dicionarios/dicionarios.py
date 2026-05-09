# ============================================================
# Bootcamp TOTVS — Fundamentos de Engenharia de Dados e ML
# Módulo 08 — Aprendendo a Utilizar Dicionários
# Autora: Renata Citelli
# ============================================================

# ── O que é um Dicionário? ───────────────────────────────────
# Dicionário é uma coleção de pares chave:valor.
# Mutável, não permite chaves duplicadas.
# Muito usado para representar objetos e estruturar dados.

cliente = {
    "nome": "Renata Citelli",
    "cidade": "Campinas",
    "area": "Ciência de Dados",
    "ativo": True
}

print(cliente)

# ── Acessando valores ────────────────────────────────────────
print("\n--- Acessando valores ---")

print(f"Nome:   {cliente['nome']}")
print(f"Cidade: {cliente['cidade']}")

# get() — mais seguro, retorna None se a chave não existir
print(f"Área:   {cliente.get('area')}")
print(f"Idade:  {cliente.get('idade', 'não informado')}")  # valor padrão

# ── Adicionando e modificando ────────────────────────────────
print("\n--- Adicionando e modificando ---")

print(f"Antes: {cliente}")

cliente["idade"] = 29               # adiciona nova chave
cliente["cidade"] = "Campinas/SP"   # modifica valor existente

print(f"Depois: {cliente}")

# ── Removendo ────────────────────────────────────────────────
print("\n--- Removendo ---")

chamado = {"id": 1, "titulo": "Erro no totem", "status": "aberto", "temp": "lixo"}

del chamado["temp"]                  # remove a chave
resolvido = chamado.pop("status")   # remove e retorna o valor

print(f"Chamado: {chamado}")
print(f"Status removido: {resolvido}")

# ── Métodos essenciais ───────────────────────────────────────
print("\n--- Métodos ---")

sistema = {
    "nome": "TouchPay",
    "versao": "2.5.1",
    "ambiente": "producao",
    "porta": 5432
}

print(f"keys():   {list(sistema.keys())}")
print(f"values(): {list(sistema.values())}")
print(f"items():  {list(sistema.items())}")
print(f"len():    {len(sistema)}")
print(f"'nome' in sistema? {'nome' in sistema}")

# ── Iterando sobre dicionários ───────────────────────────────
print("\n--- Iteração ---")

for chave, valor in sistema.items():
    print(f"  {chave}: {valor}")

# ── Dicionários aninhados ────────────────────────────────────
print("\n--- Dicionários aninhados ---")

chamados = {
    "#001": {"titulo": "Totem offline",        "prioridade": "alta",  "tempo": 48},
    "#002": {"titulo": "Erro no pagamento Pix", "prioridade": "alta",  "tempo": 12},
    "#003": {"titulo": "Dúvida de uso",         "prioridade": "baixa", "tempo": 5},
}

for id_chamado, dados in chamados.items():
    print(f"  {id_chamado} | {dados['titulo']} | {dados['prioridade']} | {dados['tempo']}h")

# Acessando dado específico
print(f"\nTítulo do #002: {chamados['#002']['titulo']}")

# ── Dict Comprehension ───────────────────────────────────────
print("\n--- Dict Comprehension ---")

# Criando dicionário de quadrados
quadrados = {n: n ** 2 for n in range(1, 6)}
print(f"Quadrados: {quadrados}")

# Filtrando chamados de alta prioridade
alta_prioridade = {
    id: dados for id, dados in chamados.items()
    if dados["prioridade"] == "alta"
}
print(f"Alta prioridade: {list(alta_prioridade.keys())}")

# ── Exemplo prático — painel de atendimento ──────────────────
print("\n--- Painel de atendimento ---")

atendimentos = [
    {"analista": "Ana",    "chamados": 15, "resolvidos": 14},
    {"analista": "Bruno",  "chamados": 12, "resolvidos": 10},
    {"analista": "Carlos", "chamados": 18, "resolvidos": 18},
    {"analista": "Diana",  "chamados": 10, "resolvidos": 8},
]

print(f"{'Analista':<10} {'Chamados':>9} {'Resolvidos':>11} {'Taxa':>6}")
print("-" * 40)

for a in atendimentos:
    taxa = (a["resolvidos"] / a["chamados"]) * 100
    print(f"{a['analista']:<10} {a['chamados']:>9} {a['resolvidos']:>11} {taxa:>5.0f}%")

total_chamados  = sum(a["chamados"]   for a in atendimentos)
total_resolvidos = sum(a["resolvidos"] for a in atendimentos)
taxa_geral = (total_resolvidos / total_chamados) * 100

print("-" * 40)
print(f"{'TOTAL':<10} {total_chamados:>9} {total_resolvidos:>11} {taxa_geral:>5.0f}%")

# ── Resumo do módulo ─────────────────────────────────────────
print("\n--- Resumo do que aprendi ---")
print("OK Dicionário armazena pares chave:valor")
print("OK Acesso por chave direta ou get() com valor padrão")
print("OK keys(), values(), items() para iterar")
print("OK del e pop() para remover entradas")
print("OK Dicionários aninhados para estruturas complexas")
print("OK Dict comprehension para criação compacta")