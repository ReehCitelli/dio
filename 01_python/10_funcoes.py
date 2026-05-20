# ============================================================
# Bootcamp TOTVS — Fundamentos de Engenharia de Dados e ML
# Módulo 10 — Dominando Funções Python
# Autora: Renata Citelli
# ============================================================

# ── O que é uma Função? ──────────────────────────────────────
# Função é um bloco de código identificado por um nome.
# Pode receber parâmetros (com ou sem valores padrão).
# Torna o código mais legível e reutilizável.
# Programar com funções = programação estruturada.

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônimo"):   # parâmetro com valor padrão
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="Renata")
exibir_mensagem_3()
exibir_mensagem_3(nome="Renata")

# ── Retornando valores ───────────────────────────────────────
print("\n--- Retornando valores ---")

# Toda função retorna None por padrão
# Em Python uma função pode retornar mais de um valor

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor   = numero + 1
    return antecessor, sucessor   # retorna uma tupla

print(calcular_total([10, 20, 34]))           # 64
print(retorna_antecessor_e_sucessor(10))      # (9, 11)

ant, suc = retorna_antecessor_e_sucessor(10)  # desempacotamento
print(f"Antecessor: {ant} | Sucessor: {suc}")

# ── Argumentos nomeados ──────────────────────────────────────
print("\n--- Argumentos nomeados ---")

# Funções podem ser chamadas usando chave=valor
# A ordem dos argumentos nomeados não importa

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")                              # posição
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")       # nomeado
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})  # dicionário

# ── *args e **kwargs ─────────────────────────────────────────
print("\n--- *args e **kwargs ---")

# *args   → recebe múltiplos argumentos como TUPLA
# **kwargs → recebe múltiplos argumentos nomeados como DICIONÁRIO

def exibir_poema(data_extenso, *args, **kwargs):
    texto      = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem   = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Zen of Python",
    "Belo é melhor que feio.",
    "Explícito é melhor que implícito.",
    autor="Tim Peters",
    ano=1999
)

# ── Parâmetros especiais ─────────────────────────────────────
print("\n--- Parâmetros especiais ---")

# /  → parâmetros SOMENTE posicionais (antes da barra)
# *  → parâmetros SOMENTE nomeados   (após o asterisco)
# /* → combinação: posicional antes, nomeado depois

# Positional only (/)
def criar_carro_pos(modelo, ano, placa, /, marca, motor, combustivel):
    print(f"{modelo} | {ano} | {placa} | {marca} | {motor} | {combustivel}")

criar_carro_pos("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # válido
# criar_carro_pos(modelo="Palio", ...)  # inválido — lançaria TypeError

# Keyword only (*)
def criar_carro_kw(*, modelo, ano, placa, marca, motor, combustivel):
    print(f"{modelo} | {ano} | {placa} | {marca} | {motor} | {combustivel}")

criar_carro_kw(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # válido
# criar_carro_kw("Palio", 1999, ...)  # inválido — lançaria TypeError

# Keyword and Positional only (/, *)
def criar_carro_misto(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(f"{modelo} | {ano} | {placa} | {marca} | {motor} | {combustivel}")

criar_carro_misto("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # válido

# ── Objetos de primeira classe ───────────────────────────────
print("\n--- Funções como objetos ---")

# Em Python tudo é objeto — funções também!
# Podemos: atribuir a variáveis, passar como parâmetro,
# usar em listas/dicionários e retornar de outras funções.

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"Resultado: {a} op {b} = {resultado}")

exibir_resultado(10, 10, somar)     # → 20
exibir_resultado(10, 5,  subtrair)  # → 5

# Função atribuída a variável
operacao = somar
print(f"operacao(3, 4) = {operacao(3, 4)}")  # → 7

# ── Escopo local e global ────────────────────────────────────
print("\n--- Escopo local e global ---")

# Dentro da função o escopo é LOCAL.
# Alterações em objetos imutáveis são perdidas ao sair da função.
# A palavra-chave global permite acessar variáveis globais
# dentro de uma função — mas NÃO é boa prática!

salario = 2000

def salario_bonus(bonus):
    global salario   # ⚠️ evitar — use return no lugar
    salario += bonus
    return salario

print(f"Salário com bônus: R${salario_bonus(500):.2f}")  # → 2500

# Forma recomendada — sem global:
def calcular_salario_bonus(salario_base, bonus):
    return salario_base + bonus

salario_base = 2000
novo_salario = calcular_salario_bonus(salario_base, 500)
print(f"Salário com bônus (recomendado): R${novo_salario:.2f}")  # → 2500

# ── Exemplo prático — pipeline de dados ─────────────────────
print("\n--- Exemplo prático: pipeline de dados ---")

dados_brutos = [
    {"nome": "  renata citelli ", "salario": 5000.0, "ativo": True},
    {"nome": "ANA PAULA",         "salario": 3800.5, "ativo": False},
    {"nome": "carlos souza",      "salario": 4200.0, "ativo": True},
    {"nome": "  DIANA LIMA  ",    "salario": 6100.0, "ativo": True},
]

def limpar_nome(nome):
    return nome.strip().title()

def aplicar_reajuste(salario, percentual=0.10):
    return salario * (1 + percentual)

def filtrar_ativos(funcionarios):
    return [f for f in funcionarios if f["ativo"]]

def processar_funcionarios(funcionarios, reajuste=0.10):
    ativos = filtrar_ativos(funcionarios)
    return [
        {
            "nome":    limpar_nome(f["nome"]),
            "salario": aplicar_reajuste(f["salario"], reajuste)
        }
        for f in ativos
    ]

resultado = processar_funcionarios(dados_brutos, reajuste=0.10)

print(f"{'Nome':<20} {'Novo Salário':>12}")
print("-" * 34)
for f in resultado:
    print(f"{f['nome']:<20} R${f['salario']:>9.2f}")

# ── Resumo do módulo ─────────────────────────────────────────
print("\n--- Resumo do que aprendi ---")
print("OK Função é um bloco reutilizável definido com def")
print("OK Parâmetros podem ter valores padrão")
print("OK return devolve valor — padrão é None")
print("OK Uma função pode retornar múltiplos valores (tupla)")
print("OK *args recebe múltiplos argumentos como tupla")
print("OK **kwargs recebe argumentos nomeados como dicionário")
print("OK / define parâmetros somente posicionais")
print("OK * define parâmetros somente nomeados")
print("OK Funções são objetos de primeira classe em Python")
print("OK Escopo local x global — evitar uso de global")
