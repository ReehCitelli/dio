# 📚 MER e DER — Modelagem de Banco de Dados

---

## 🧠 O que é Modelagem?

**Modelagem** é o processo de organizar e planejar como os dados serão estruturados no banco de dados.

**Antes de criar tabelas em SQL**, normalmente fazemos um modelo para visualizar e planejar a estrutura.

### Por que modelar?
- ✔ Planejar antes de implementar
- ✔ Evitar erros de estrutura
- ✔ Comunicar com stakeholders
- ✔ Entender relacionamentos entre dados
- ✔ Documentar o projeto

---

## 🔷 MER — Modelo Entidade Relacionamento

### O que é:
**Representação CONCEITUAL** do banco de dados.

É um **diagrama lógico** que mostra como os dados se relacionam, **independente de qual SGBD será usado**.

### Serve para:
- ✔ **Planejar** a estrutura do banco
- ✔ **Entender** os dados e regras de negócio
- ✔ **Visualizar** relacionamentos entre entidades
- ✔ **Documentar** o projeto

### MER mostra:
- **Entidades** → Objetos do mundo real
- **Atributos** → Propriedades das entidades
- **Relacionamentos** → Ligações entre entidades

---

## 🧱 Entidades

### O que é:
**Entidade** representa um **objeto do mundo real** que armazena dados.

Normalmente viram **tabelas no banco de dados**.

### Exemplos de entidades:
- **CLIENTE** → pessoas que compram
- **PEDIDO** → compras realizadas
- **PRODUTO** → itens à venda
- **FUNCIONÁRIO** → pessoas que trabalham
- **CATEGORIA** → classificação de produtos
- **FORNECEDOR** → empresas que vendem para nós

### Representação em MER:
```
┌─────────────┐
│   CLIENTE   │
└─────────────┘
```

### Exemplo de Entidade com contexto:
```
CLIENTE → Torna-se → Tabela: clientes
PRODUTO → Torna-se → Tabela: produtos
PEDIDO → Torna-se → Tabela: pedidos
```

---

## 🏷️ Atributos

### O que é:
**Atributo** é uma **característica ou propriedade de uma entidade**.

Normalmente viram **colunas da tabela**.

### Exemplos de atributos para CLIENTE:
```
id_cliente      (identificador único)
nome            (nome do cliente)
email           (endereço de email)
telefone        (número de telefone)
data_cadastro   (quando foi cadastrado)
endereco        (endereço de residência)
```

### Representação em MER:
```
        CLIENTE
    ┌────────────────┐
    │  Atributos:    │
    ├────────────────┤
    │ id_cliente     │
    │ nome           │
    │ email          │
    │ telefone       │
    │ data_cadastro  │
    └────────────────┘
```

### Tipos de Atributos:

#### Simples
Um único valor indivisível.
```
nome = "Renata"
```

#### Composto
Pode ser dividido em partes.
```
endereco = rua + numero + cidade + estado
```

#### Derivado
Calculado a partir de outro atributo.
```
idade = calculada de data_nascimento
```

#### Multivalorado
Pode ter múltiplos valores.
```
telefones = ["11999999999", "11988888888"]
```

---

## 🔗 Relacionamento

### O que é:
**Relacionamento** é a **ligação ou associação** entre duas ou mais entidades.

Os relacionamentos mostram **como os dados se conectam**.

### Exemplo simples:
```
CLIENTE  faz  PEDIDO
```

Um cliente faz pedidos.

### Exemplo com mais contexto:
```
CLIENTE  contém  PEDIDO
PEDIDO   contém  ITEM_PEDIDO
ITEM_PEDIDO  refere-se a  PRODUTO
```

---

## 📌 Cardinalidade

### O que é:
**Cardinalidade** define **QUANTAS ocorrências de uma entidade** podem se relacionar com outra entidade.

É representada por **números** como (1:1), (1:N), (N:N).

### Como ler:
```
CLIENTE (1) ──── (N) PEDIDO

Lê-se:
"Um cliente pode ter MUITOS pedidos"
"Um pedido pertence a UM cliente"
```

---

## 🔹 Tipo 1: Um para Um (1:1)

### O que é:
Um registro de uma entidade se relaciona com **exatamente um registro** de outra entidade.

### Exemplo:
```
PESSOA ──── (1:1) ──── CPF

✔ Uma pessoa possui UM CPF
✔ Um CPF pertence a UMA pessoa
```

### Representação gráfica:
```
    PESSOA
    ───────
    id
    nome
    email
        |
        | (1:1)
        |
    CPF
    ───
    numero
    id_pessoa
```

### Quando usar:
- Dados exclusivos de uma pessoa
- Informações que não podem se repetir
- Exemplo: FUNCIONÁRIO ↔ CARTÃO_ACESSO

---

## 🔹 Tipo 2: Um para Muitos (1:N)

### O que é:
Um registro de uma entidade pode se relacionar com **vários registros** de outra entidade.

### Exemplo:
```
CLIENTE ──── (1:N) ──── PEDIDO

✔ Um cliente pode ter VÁRIOS pedidos
✔ Cada pedido pertence a UM cliente
```

### Representação gráfica:
```
    CLIENTE
    ───────
    id
    nome
    email
        |
        | (1:N)
        |
    PEDIDO
    ──────
    id
    id_cliente (FK)
    valor
    data
```

### 👉 **ESTE É O RELACIONAMENTO MAIS COMUM!**

### Outros exemplos:
- CATEGORIA (1:N) PRODUTO
- DEPARTAMENTO (1:N) FUNCIONÁRIO
- AUTOR (1:N) LIVRO
- FORNECEDOR (1:N) PRODUTO

---

## 🔹 Tipo 3: Muitos para Muitos (N:N)

### O que é:
Vários registros de uma entidade se relacionam com **vários registros** de outra entidade.

### Exemplo:
```
ALUNO ──── (N:N) ──── CURSO

✔ Um aluno pode fazer VÁRIOS cursos
✔ Um curso pode ter VÁRIOS alunos
```

### Representação gráfica:
```
    ALUNO
    ────────
    id
    nome
    email
        |
        | (N:N)
        |
    CURSO
    ────────
    id
    nome
    descricao
```

### ⚠️ IMPORTANTE: Tabela Intermediária

Relacionamento N:N **normalmente precisa de uma tabela intermediária** (tabela de junção).

**Por quê?** Bancos relacionais não suportam diretamente N:N.

### Solução:
```
    ALUNO (N) ──── ALUNO_CURSO ──── (N) CURSO
    
    
ALUNO_CURSO (tabela de junção):
┌──────────┬──────────┬────────────────┐
│ id_aluno │ id_curso │ data_inscricao │
├──────────┼──────────┼────────────────┤
│ 1        │ 101      │ 2024-01-15     │
│ 1        │ 102      │ 2024-01-20     │
│ 2        │ 101      │ 2024-01-15     │
└──────────┴──────────┴────────────────┘
```

### Outros exemplos N:N:
- ESTUDANTE (N:N) MATERIA (via MATRICULA)
- PRODUTO (N:N) PEDIDO (via ITEM_PEDIDO)
- ATOR (N:N) FILME (via ELENCO)
- USUARIO (N:N) PERMISSAO (via USUARIO_PERMISSAO)

---

## 🖼️ DER — Diagrama Entidade Relacionamento

### O que é:
**Representação GRÁFICA** do MER.

É o **desenho visual** da estrutura do banco de dados, mostrando entidades, atributos e relacionamentos com símbolos padronizados.

### DER usa símbolos:
- **Retângulo** = Entidade
- **Óvalo/Elipse** = Atributo
- **Linha** = Relacionamento
- **Números/letras** = Cardinalidade

### Exemplo simples de DER:
```
┌──────────────────┐         ┌──────────────────┐
│     CLIENTE      │         │     PEDIDO       │
├──────────────────┤(1)──(N)─├──────────────────┤
│ id_cliente (PK)  │         │ id_pedido (PK)   │
│ nome             │         │ id_cliente (FK)  │
│ email            │         │ valor            │
│ telefone         │         │ data_pedido      │
└──────────────────┘         └──────────────────┘
```

### Exemplo mais detalhado:
```
                    ┌─────────────────┐
                    │   CATEGORIA     │
                    ├─────────────────┤
                    │ id (PK)         │
                    │ nome            │
                    └─────────────────┘
                           ▲
                           │ (1:N)
                           │
                    ┌─────────────────┐         ┌─────────────────┐
                    │    PRODUTO      │◄────────│  ITEM_PEDIDO    │
                    ├─────────────────┤ (1:N)   ├─────────────────┤
                    │ id (PK)         │         │ id_pedido (FK)  │
                    │ nome            │         │ id_produto (FK) │
                    │ preco           │         │ quantidade      │
                    │ id_categoria(FK)│         └─────────────────┘
                    └─────────────────┘                   ▲
                                                          │ (N:1)
                                                          │
                           ┌──────────────────┐────────────┘
                           │      PEDIDO      │
                           ├──────────────────┤
                           │ id (PK)          │
                           │ id_cliente (FK)  │
                           │ data_pedido      │
                           │ valor_total      │
                           └──────────────────┘
                                   ▲
                                   │ (N:1)
                                   │
                           ┌──────────────────┐
                           │     CLIENTE      │
                           ├──────────────────┤
                           │ id (PK)          │
                           │ nome             │
                           │ email            │
                           │ telefone         │
                           └──────────────────┘
```

---

## 🧠 Diferença entre MER e DER

### MER (Modelo Entidade Relacionamento)
- **Tipo:** Conceitual
- **Forma:** Textual ou simples
- **Foco:** Entender o que existe
- **Uso:** Planejamento inicial
- **Linguagem:** Português/descrição
- **Exemplo:** "Cliente faz Pedido"

### DER (Diagrama Entidade Relacionamento)
- **Tipo:** Visual/Gráfico
- **Forma:** Desenho com símbolos
- **Foco:** Visualizar estrutura
- **Uso:** Implementação
- **Linguagem:** Símbolos e notação
- **Exemplo:** Retângulos conectados com linhas

### Resumo:
```
MER  →  É a IDEIA
DER  →  É o DESENHO da ideia
```

---

## 🔄 Como Identificar Cardinalidade

### Pergunta-chave:
Para cada entidade, faça a pergunta:

**"Quantos [ENTIDADE B] podem ter [ENTIDADE A]?"**

### Exemplos:

#### Exemplo 1:
```
Pergunta: Quantos pedidos um cliente pode ter?
Resposta: Vários (muitos)
Cardinalidade: 1:N
Desenho: CLIENTE (1) ──── (N) PEDIDO
```

#### Exemplo 2:
```
Pergunta: Quantos cursos um aluno pode fazer?
Resposta: Vários (muitos)
Pergunta reversa: Quantos alunos um curso pode ter?
Resposta: Vários (muitos)
Cardinalidade: N:N
Desenho: ALUNO (N) ──── (N) CURSO
```

#### Exemplo 3:
```
Pergunta: Quantos CPFs uma pessoa pode ter?
Resposta: Um (apenas um)
Pergunta reversa: Quantas pessoas um CPF pode ter?
Resposta: Uma (apenas uma)
Cardinalidade: 1:1
Desenho: PESSOA (1) ──── (1) CPF
```

---

## 💜 Resumão para Fixar

### Conceitos Básicos:
- 👉 **Entidade** → Objeto do mundo real (vira tabela)
- 👉 **Atributo** → Propriedade da entidade (vira coluna)
- 👉 **Tupla** → Linha/registro de dados
- 👉 **Relacionamento** → Ligação entre entidades
- 👉 **Cardinalidade** → Quantidade do relacionamento

### MER vs DER:
- 👉 **MER** → Modelo conceitual (ideia)
- 👉 **DER** → Diagrama visual (desenho)

### Cardinalidades:
| Tipo | Significado | Exemplo |
|------|-------------|---------|
| **1:1** | Um para Um | PESSOA ↔ CPF |
| **1:N** | Um para Muitos | CLIENTE → PEDIDOS |
| **N:N** | Muitos para Muitos | ALUNO ↔ CURSOS |

### N:N Precisa:
- 👉 Tabela intermediária para implementação

---

## 🎯 Fluxo de Modelagem

```
1. Entender o negócio
   ↓
2. Identificar entidades
   ↓
3. Listar atributos de cada entidade
   ↓
4. Identificar relacionamentos
   ↓
5. Definir cardinalidades
   ↓
6. Criar MER (textual)
   ↓
7. Criar DER (visual)
   ↓
8. Normalizar (se necessário)
   ↓
9. Implementar em SQL
```

---

## 📝 Exercício Prático

### Cenário: Sistema de Biblioteca

**Identifique:**
1. Entidades
2. Atributos
3. Relacionamentos
4. Cardinalidades

**Resposta sugerida:**

**Entidades:**
- LIVRO
- AUTOR
- LEITOR
- EMPRESTIMO

**Atributos:**
- LIVRO: id, titulo, isbn, data_publicacao
- AUTOR: id, nome, data_nascimento
- LEITOR: id, nome, email, telefone
- EMPRESTIMO: id, id_leitor, id_livro, data_emprestimo, data_devolucao

**Relacionamentos e Cardinalidades:**
- AUTOR (1) ──── (N) LIVRO (um autor escreve vários livros)
- LEITOR (1) ──── (N) EMPRESTIMO (um leitor faz vários empréstimos)
- LIVRO (1) ──── (N) EMPRESTIMO (um livro é emprestado várias vezes)
- LIVRO (N) ──── (N) AUTOR (um livro pode ter vários autores, um autor escreve vários livros)

---

**Próximo:** Normalizar dados para evitar redundâncias!
