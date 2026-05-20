# ============================================================
# Bootcamp TOTVS — Fundamentos de Engenharia de Dados e ML
# Módulo 06 — Conhecendo Tuplas
# Autora: Renata Citelli
# ============================================================

# ── O que é uma Tupla? ───────────────────────────────────────
# Tupla é uma coleção ordenada e IMUTÁVEL de elementos.
# Imutável = depois de criada, não pode ser alterada.
# Usa parênteses () ao invés de colchetes []

coordenadas = (23.5, 46.6)
cores_rgb = (255, 128, 0)
dados_usuario = ("Renata", 29, "Campinas")

print(coordenadas)
print(cores_rgb)
print(dados_usuario)

# ── Diferença entre Lista e Tupla ────────────────────────────
print("\n--- Lista vs Tupla ---")

lista = [1, 2, 3]
tupla = (1, 2, 3)

lista[0] = 99       # funciona — lista é mutável
print(f"Lista alterada: {lista}")

# tupla[0] = 99     # erro! tupla é imutável
print("Tupla não pode ser alterada após criação.")

# ── Quando usar Tupla? ───────────────────────────────────────
# - Dados que não devem ser alterados (coordenadas, configs)
# - Mais rápida que lista em leitura
# - Pode ser usada como chave de dicionário (lista não pode)

# ── Acessando elementos ──────────────────────────────────────
print("\n--- Acessando elementos ---")

pessoa = ("Renata", "Citelli", 29, "Campinas", "Ciência de Dados")

print(f"Nome:      {pessoa[0]}")
print(f"Sobrenome: {pessoa[1]}")
print(f"Idade:     {pessoa[2]}")
print(f"Cidade:    {pessoa[3]}")
print(f"Área:      {pessoa[4]}")
print(f"Últimos 2: {pessoa[-2:]}")

# ── Desempacotamento ─────────────────────────────────────────
# Forma elegante de extrair valores de uma tupla

print("\n--- Desempacotamento ---")

nome, sobrenome, idade, cidade, area = pessoa

print(f"Nome completo: {nome} {sobrenome}")
print(f"Tem {idade} anos e mora em {cidade}")
print(f"Estuda {area}")

# Desempacotamento parcial com *
primeiro, *meio, ultimo = (10, 20, 30, 40, 50)
print(f"\nPrimeiro: {primeiro}")
print(f"Meio:     {meio}")
print(f"Último:   {ultimo}")

# ── Métodos disponíveis ──────────────────────────────────────
print("\n--- Métodos ---")

notas = (8.5, 9.0, 7.5, 9.0, 10.0, 8.5)

print(f"Tupla:           {notas}")
print(f"Tamanho:         {len(notas)}")
print(f"Maior nota:      {max(notas)}")
print(f"Menor nota:      {min(notas)}")
print(f"Soma:            {sum(notas)}")
print(f"Conta 9.0:       {notas.count(9.0)}")   # quantas vezes aparece
print(f"Índice do 10.0:  {notas.index(10.0)}")  # posição do valor

# ── Tupla com um elemento ────────────────────────────────────
print("\n--- Tupla com um elemento ---")

# Precisa da vírgula! Sem ela, é só um valor entre parênteses
nao_e_tupla = (42)
e_tupla = (42,)

print(f"Sem vírgula: {type(nao_e_tupla)}")  # int
print(f"Com vírgula: {type(e_tupla)}")       # tuple

# ── Exemplo prático — configurações do sistema ───────────────
print("\n--- Configurações do sistema ---")

# Tuplas são ideais para dados fixos de configuração
CONFIG = (
    "sistema_touchpay",   # nome do sistema
    "v2.5.1",            # versão
    "producao",          # ambiente
    5432,                # porta do banco
)

sistema, versao, ambiente, porta = CONFIG

print(f"Sistema:   {sistema}")
print(f"Versão:    {versao}")
print(f"Ambiente:  {ambiente}")
print(f"Porta:     {porta}")

# ── Convertendo entre lista e tupla ─────────────────────────
print("\n--- Conversão ---")

lista = ["Python", "SQL", "Power BI"]
tupla = tuple(lista)          # lista → tupla
lista_nova = list(tupla)      # tupla → lista

print(f"Lista:     {lista}")
print(f"Tupla:     {tupla}")
print(f"De volta:  {lista_nova}")

# ── Resumo do módulo ─────────────────────────────────────────
print("\n--- Resumo do que aprendi ---")
print("OK Tupla é imutável — não pode ser alterada após criação")
print("OK Acesso por índice igual à lista")
print("OK Desempacotamento para extrair valores com elegância")
print("OK count() e index() como métodos disponíveis")
print("OK Ideal para dados fixos como configurações")
print("OK Conversão entre lista e tupla com tuple() e list()")