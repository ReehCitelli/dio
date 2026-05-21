# ============================================================
# Bootcamp TOTVS — Fundamentos de Engenharia de Dados e ML
# Módulo — Modelagem de Dados Relacionais
# Autora: Renata Citelli
# ============================================================

## 📊 Tabelas, Colunas e Registros

### O que é uma Tabela?

**Tabela** é a estrutura principal de um banco de dados relacional. É como uma **planilha** com linhas e colunas.

### Componentes de uma Tabela:

#### 1. Coluna (Campo/Atributo)
Define o **tipo de dados** que será armazenado.

```
┌─────────────────────────────────────────┐
│ COLUNA: id   COLUNA: nome  COLUNA: email│
├─────────────────────────────────────────┤
│    1          Renata      r@email.com   │
│    2          Ana Paula   a@email.com   │
└─────────────────────────────────────────┘
```

Características de uma coluna:
- **Nome** descritivo
- **Tipo de dado** (INT, VARCHAR, DATE, etc)
- **Restrições** (NOT NULL, UNIQUE, etc)
- **Valor padrão** (opcional)

#### 2. Registro (Linha/Tupla)
Cada linha representa um **dado único** na tabela.

```
┌──────┬──────────────┬────────────────┐
│ id   │ nome         │ email          │
├──────┼──────────────┼────────────────┤
│ 1    │ Renata       │ r@email.com    │ ← Registro
│ 2    │ Ana Paula    │ a@email.com    │ ← Registro
│ 3    │ Carlos Silva │ c@email.com    │ ← Registro
└──────┴──────────────┴────────────────┘
```

Um registro contém **um valor para cada coluna**.

#### 3. Célula
Interseção de uma **coluna com um registro**.

```
┌──────┬──────────────┬────────────────┐
│ id   │ nome         │ email          │
├──────┼──────────────┼────────────────┤
│ 1    │ Renata       │ r@email.com    │
│      │              │ ↑ Célula       │
└──────┴──────────────┴────────────────┘
```

### Tipos de Dados Comuns

| Tipo | Uso | Exemplo |
|------|-----|---------|
| **INT** | Números inteiros | 1, 100, -5 |
| **DECIMAL / NUMERIC** | Números com decimais | 19.99, 3.14 |
| **VARCHAR(n)** | Texto de até n caracteres | "Renata" |
| **CHAR(n)** | Texto fixo de n caracteres | "SP" |
| **TEXT** | Texto longo | descrição completa |
| **DATE** | Data | 2024-01-15 |
| **DATETIME / TIMESTAMP** | Data e hora | 2024-01-15 08:30:00 |
| **BOOLEAN** | Verdadeiro ou Falso | TRUE, FALSE |
| **BLOB** | Dados binários | imagens, arquivos |

### Exemplo de Tabela Bem Estruturada

```sql
CREATE TABLE clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,          -- Coluna: id
    nome VARCHAR(100) NOT NULL,                  -- Coluna: nome
    email VARCHAR(100) UNIQUE,                   -- Coluna: email
    telefone VARCHAR(15),                        -- Coluna: telefone
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Coluna: data
);
```

---

## ✏️ Operações CRUD: INSERT e SELECT

### CRUD
São as **4 operações fundamentais** em bancos de dados:

| Operação | Comando | Ação |
|----------|---------|------|
| **C**reate | INSERT | Adicionar dados |
| **R**ead | SELECT | Consultar dados |
| **U**pdate | UPDATE | Modificar dados |
| **D**elete | DELETE | Remover dados |

---

## 📝 INSERT — Criar/Adicionar Registros

### Sintaxe Básica

```sql
INSERT INTO nome_tabela (coluna1, coluna2, coluna3)
VALUES (valor1, valor2, valor3);
```

### Exemplo 1: Inserir um registro

```sql
INSERT INTO clientes (nome, email, telefone)
VALUES ('Renata Citelli', 'renata@email.com', '11999999999');
```

**Resultado:** Um novo cliente é adicionado à tabela.

### Exemplo 2: Inserir múltiplos registros

```sql
INSERT INTO clientes (nome, email, telefone) VALUES
('Renata Citelli', 'renata@email.com', '11999999999'),
('Ana Paula', 'ana@email.com', '21988888888'),
('Carlos Silva', 'carlos@email.com', '31977777777'),
('Diana Lima', 'diana@email.com', '41966666666');
```

### Exemplo 3: Inserir sem especificar colunas

Se você não especificar as colunas, deve fornecer valores para TODAS:

```sql
INSERT INTO clientes
VALUES (1, 'Renata', 'renata@email.com', '11999999999', '2024-01-15');
```

### Exemplo 4: Inserir com valor padrão

Se a coluna tem um valor padrão, pode omitir:

```sql
-- data_cadastro terá o valor padrão (CURRENT_TIMESTAMP)
INSERT INTO clientes (nome, email, telefone)
VALUES ('Renata', 'renata@email.com', '11999999999');
```

### ✅ Boas Práticas com INSERT

- ✔ Sempre especifique as colunas
- ✔ Respeite os tipos de dados
- ✔ Valide dados antes de inserir
- ✔ Use transações para múltiplas inserções críticas

---

## 🔍 SELECT — Consultar Registros

### Sintaxe Básica

```sql
SELECT coluna1, coluna2, ...
FROM nome_tabela
WHERE condição
ORDER BY coluna
LIMIT quantidade;
```

### Exemplo 1: Selecionar todas as colunas

```sql
SELECT * FROM clientes;
```

**Resultado:**
```
id | nome           | email              | telefone      | data_cadastro
1  | Renata Citelli | renata@email.com   | 11999999999   | 2024-01-15
2  | Ana Paula      | ana@email.com      | 21988888888   | 2024-01-15
3  | Carlos Silva   | carlos@email.com   | 31977777777   | 2024-01-15
```

### Exemplo 2: Selecionar colunas específicas

```sql
SELECT nome, email FROM clientes;
```

**Resultado:**
```
nome           | email
Renata Citelli | renata@email.com
Ana Paula      | ana@email.com
Carlos Silva   | carlos@email.com
```

### Exemplo 3: SELECT com WHERE (filtro)

```sql
SELECT * FROM clientes WHERE id = 1;
```

**Resultado:** Apenas o cliente com id = 1.

### Exemplo 4: SELECT com filtros múltiplos

```sql
SELECT * FROM clientes 
WHERE nome = 'Renata' AND email = 'renata@email.com';
```

Operadores lógicos:
- **AND** → ambas as condições devem ser verdadeiras
- **OR** → pelo menos uma condição deve ser verdadeira
- **NOT** → inverte a condição

### Exemplo 5: SELECT com LIKE (busca parcial)

```sql
SELECT * FROM clientes WHERE nome LIKE 'R%';
```

Retorna todos os clientes cujo nome começa com 'R'.

**Padrões:**
- `'R%'` → começa com R
- `'%a'` → termina com a
- `'%na%'` → contém "na"

### Exemplo 6: SELECT com ORDER BY (ordenação)

```sql
SELECT * FROM clientes ORDER BY nome ASC;
```

**ASC** = Crescente (padrão)  
**DESC** = Decrescente

```sql
SELECT * FROM clientes ORDER BY data_cadastro DESC;
```

Ordena por data mais recente primeiro.

### Exemplo 7: SELECT com LIMIT (limitar resultados)

```sql
SELECT * FROM clientes LIMIT 5;
```

Retorna apenas os 5 primeiros registros.

```sql
SELECT * FROM clientes LIMIT 5 OFFSET 10;
```

Retorna 5 registros começando do 11º registro (pula os primeiros 10).

### Exemplo 8: SELECT com funções de agregação

```sql
SELECT COUNT(*) FROM clientes;
```

Conta quantos clientes existem.

```sql
SELECT COUNT(*), COUNT(email) FROM clientes;
```

Conta clientes e clientes com email preenchido.

---

## 🔄 Operações CRUD: UPDATE e DELETE

---

## 📝 UPDATE — Modificar Registros

### Sintaxe Básica

```sql
UPDATE nome_tabela
SET coluna1 = valor1, coluna2 = valor2
WHERE condição;
```

### Exemplo 1: Atualizar um registro

```sql
UPDATE clientes
SET email = 'novo@email.com'
WHERE id = 1;
```

Muda o email do cliente com id = 1.

### Exemplo 2: Atualizar múltiplas colunas

```sql
UPDATE clientes
SET email = 'novo@email.com', telefone = '11988888888'
WHERE id = 1;
```

### Exemplo 3: Atualizar com cálculo

```sql
UPDATE pedidos
SET valor = valor * 1.10
WHERE id = 5;
```

Aumenta o valor em 10%.

### Exemplo 4: UPDATE sem WHERE (⚠️ CUIDADO!)

```sql
UPDATE clientes SET ativo = FALSE;
```

❌ **PERIGO:** Desativa TODOS os clientes!

Sempre use WHERE para ser específico:

```sql
UPDATE clientes SET ativo = FALSE WHERE id = 1;
```

### ✅ Boas Práticas com UPDATE

- ✔ Sempre use WHERE para ser específico
- ✔ Teste a condição com SELECT antes
- ✔ Faça backup antes de updates em massa
- ✔ Use transações para operações críticas

---

## 🗑️ DELETE — Remover Registros

### Sintaxe Básica

```sql
DELETE FROM nome_tabela
WHERE condição;
```

### Exemplo 1: Deletar um registro

```sql
DELETE FROM clientes
WHERE id = 1;
```

Remove o cliente com id = 1.

### Exemplo 2: Deletar múltiplos registros

```sql
DELETE FROM clientes
WHERE data_cadastro < '2023-01-01';
```

Remove clientes cadastrados antes de 2023.

### Exemplo 3: DELETE sem WHERE (⚠️ CUIDADO!)

```sql
DELETE FROM clientes;
```

❌ **PERIGO:** Deleta TODOS os clientes!

Sempre use WHERE:

```sql
DELETE FROM clientes WHERE id = 1;
```

### ✅ Boas Práticas com DELETE

- ✔ Sempre use WHERE para ser específico
- ✔ Teste com SELECT antes de deletar
- ✔ Faça backup antes
- ✔ Use transações
- ✔ Considere usar soft delete (coluna ativo = false) ao invés de hard delete

### Soft Delete vs Hard Delete

**Hard Delete (Perigoso):**
```sql
DELETE FROM clientes WHERE id = 1;
-- Registro é removido completamente
```

**Soft Delete (Recomendado):**
```sql
UPDATE clientes SET ativo = FALSE WHERE id = 1;
-- Registro permanece, mas marcado como inativo
-- Pode ser restaurado depois
```

---

## 🔧 Alterando e Excluindo Tabelas

---

## 📝 ALTER TABLE — Modificar Estrutura

### Adicionar Coluna

```sql
ALTER TABLE clientes
ADD email VARCHAR(100);
```

Adiciona uma nova coluna "email" à tabela.

### Adicionar Coluna com Restrições

```sql
ALTER TABLE clientes
ADD email VARCHAR(100) NOT NULL UNIQUE;
```

### Remover Coluna

```sql
ALTER TABLE clientes
DROP COLUMN telefone;
```

Remove a coluna "telefone".

### Modificar Tipo de Coluna

```sql
ALTER TABLE clientes
MODIFY COLUMN nome VARCHAR(150);
```

Aumenta o tamanho máximo de "nome" de 100 para 150.

### Renomear Coluna

```sql
ALTER TABLE clientes
CHANGE COLUMN telefone telefone_principal VARCHAR(15);
```

Renomeia "telefone" para "telefone_principal".

### Adicionar Valor Padrão

```sql
ALTER TABLE clientes
ALTER COLUMN ativo SET DEFAULT TRUE;
```

### Renomear Tabela

```sql
ALTER TABLE clientes
RENAME TO customers;
```

Renomeia a tabela de "clientes" para "customers".

### Exemplo Completo

```sql
-- Criar tabela simples
CREATE TABLE usuarios (
    id INT PRIMARY KEY,
    nome VARCHAR(50)
);

-- Adicionar coluna
ALTER TABLE usuarios ADD email VARCHAR(100);

-- Adicionar restrição
ALTER TABLE usuarios ADD UNIQUE(email);

-- Modificar tipo
ALTER TABLE usuarios MODIFY COLUMN nome VARCHAR(100) NOT NULL;

-- Remover coluna
ALTER TABLE usuarios DROP COLUMN email;

-- Renomear tabela
ALTER TABLE usuarios RENAME TO accounts;
```

---

## 🗑️ DROP TABLE — Deletar Tabela

### Sintaxe

```sql
DROP TABLE nome_tabela;
```

### Exemplo

```sql
DROP TABLE clientes;
```

❌ **CUIDADO:** Deleta a tabela **inteira** (estrutura e dados)!

### DROP com verificação

```sql
DROP TABLE IF EXISTS clientes;
```

Só deleta se a tabela existir (não gera erro se não existir).

### Diferenças

| Comando | O que faz | Recuperável |
|---------|-----------|-------------|
| **DELETE** | Remove dados | ✔ Sim (com ROLLBACK) |
| **TRUNCATE** | Remove todos os dados | ⚠️ Depende |
| **DROP** | Remove tabela inteira | ❌ Difícil |

---

## 🔑 Chaves Primárias e Estrangeiras

### Chave Primária (PK — Primary Key)

#### O que é:
**Chave Primária** identifica **unicamente cada linha** da tabela.

#### Características:
- ✔ Não pode ser NULL
- ✔ Não pode ter valores duplicados
- ✔ Uma tabela tem apenas UMA chave primária
- ✔ Melhora performance de buscas

#### Exemplo 1: Chave Primária Simples

```sql
CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100)
);
```

#### Exemplo 2: Chave Primária com AUTO_INCREMENT

```sql
CREATE TABLE clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100)
);
```

AUTO_INCREMENT gera id automaticamente: 1, 2, 3, 4...

#### Exemplo 3: Adicionar Chave Primária Depois

```sql
ALTER TABLE clientes
ADD PRIMARY KEY (id);
```

#### Exemplo 4: Chave Primária Composta

Uma chave primária formada por **múltiplas colunas**:

```sql
CREATE TABLE matriculas (
    id_aluno INT,
    id_curso INT,
    data_inscricao DATE,
    PRIMARY KEY (id_aluno, id_curso)
);
```

Garante que um aluno não se inscreva duas vezes no mesmo curso.

---

### Chave Estrangeira (FK — Foreign Key)

#### O que é:
**Chave Estrangeira** estabelece um **relacionamento entre tabelas**.

Refere-se à **chave primária de outra tabela**.

#### Características:
- ✔ Implementa integridade referencial
- ✔ Garante que referências são válidas
- ✔ Pode ser NULL
- ✔ Uma tabela pode ter múltiplas chaves estrangeiras

#### Exemplo 1: Chave Estrangeira Simples

```sql
CREATE TABLE pedidos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT,
    valor DECIMAL(10, 2),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);
```

Diz que "id_cliente" refere-se ao "id" de "clientes".

#### Exemplo 2: Adicionar Chave Estrangeira Depois

```sql
ALTER TABLE pedidos
ADD FOREIGN KEY (id_cliente) REFERENCES clientes(id);
```

#### Exemplo 3: Chave Estrangeira com ON DELETE

```sql
CREATE TABLE pedidos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT,
    valor DECIMAL(10, 2),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id) 
        ON DELETE CASCADE
);
```

**ON DELETE CASCADE:** Se deletar um cliente, seus pedidos também são deletados.

Outras opções:
- **CASCADE** → deleta registros relacionados
- **SET NULL** → define como NULL
- **RESTRICT** → impede deleção (padrão)
- **NO ACTION** → igual a RESTRICT

#### Exemplo 4: Sistema Completo com Chaves

```sql
-- Tabela pai
CREATE TABLE clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE
);

-- Tabela filha
CREATE TABLE pedidos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    valor DECIMAL(10, 2),
    data_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id) ON DELETE CASCADE
);

-- Tabela de junção (N:N)
CREATE TABLE itens_pedido (
    id_pedido INT,
    id_produto INT,
    quantidade INT,
    PRIMARY KEY (id_pedido, id_produto),
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id) ON DELETE CASCADE,
    FOREIGN KEY (id_produto) REFERENCES produtos(id)
);
```

---

## 🛡️ Integridade Referencial

**Integridade Referencial** garante que:
- ✔ Chaves estrangeiras sempre referenciam registros válidos
- ✔ Não há "orfãos" (registros sem relacionamento válido)
- ✔ Dados relacionados permanecem consistentes

### Exemplo de Violação

```sql
-- ❌ ERRO: id_cliente 999 não existe em clientes
INSERT INTO pedidos (id_cliente, valor) 
VALUES (999, 150.00);
```

```
Error: FOREIGN KEY constraint failed
```

### Solução

```sql
-- ✅ CORRETO: id_cliente 1 existe em clientes
INSERT INTO pedidos (id_cliente, valor) 
VALUES (1, 150.00);
```

---

## 📌 Resumo do Módulo

- ✅ **Tabelas** armazenam dados em colunas e registros
- ✅ **Colunas** definem o tipo de dado
- ✅ **Registros** são linhas de dados
- ✅ **INSERT** adiciona novos registros
- ✅ **SELECT** consulta registros
- ✅ **UPDATE** modifica registros existentes
- ✅ **DELETE** remove registros
- ✅ **ALTER TABLE** modifica a estrutura
- ✅ **DROP TABLE** deleta tabelas
- ✅ **Chave Primária** identifica unicamente cada linha
- ✅ **Chave Estrangeira** estabelece relacionamentos
- ✅ **Integridade Referencial** garante consistência
- ✅ Sempre use **WHERE** em UPDATE e DELETE
- ✅ Faça **backup** antes de operações perigosas

---

## 🎯 Próximos Passos

- Normalização de Dados (1FN, 2FN, 3FN)
- Consultas Avançadas (JOINs, Agregações)
- Otimização de Performance
- Segurança em Banco de Dados
