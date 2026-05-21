# ============================================================
# Bootcamp TOTVS — Fundamentos de Engenharia de Dados e ML
# Módulo 02 — Introdução aos Bancos de Dados Relacionais
# Autora: Renata Citelli
# ============================================================

## 📚 O que é um Banco de Dados?

Banco de Dados é um conjunto organizado de dados armazenados e acessados eletronicamente em um computador.

### Tipos principais:
- **Relacional**: tabelas com linhas e colunas (SQL)
- **NoSQL**: documentos, chave-valor, grafos
- **Série temporal**: dados com timestamp
- **Espacial**: dados geográficos

---

## 🗂️ Banco de Dados Relacional

Estruturado em **TABELAS** (relações) com:
- **LINHAS** (registros): cada linha é um dado único
- **COLUNAS** (atributos): propriedades dos dados
- **CHAVES**: identificadores únicos

### Exemplo de tabela CLIENTES:

```
┌─────┬──────────────┬────────────┬───────────┐
│ id  │ nome         │ email      │ telefone  │
├─────┼──────────────┼────────────┼───────────┤
│ 1   │ Renata       │ r@email... │ 11999... │ ← Tupla
│ 2   │ Ana Paula    │ a@email... │ 21988... │ ← Tupla
│ 3   │ Carlos Silva │ c@email... │ 31977... │ ← Tupla
└─────┴──────────────┴────────────┴───────────┘
```

### 🔹 Tupla (Linha/Registro)
**Tupla** é cada linha da tabela, representando um registro único de dados.

**Exemplo:** A linha com id=1, nome="Renata", email="r@email..." é uma tupla.

---

## 🔗 Relacionamento

**Relacionamento** é a conexão entre tabelas através de chaves primárias e estrangeiras.

**Exemplo:**
```
CLIENTE (1) ──── (N) PEDIDO
```

Um cliente pode ter vários pedidos, e cada pedido pertence a um único cliente.

---

## 🔑 Conceitos-chave

### 1. TABELA (RELAÇÃO)
Estrutura principal — conjunto de dados relacionados
- Exemplo: CLIENTES, PRODUTOS, PEDIDOS

### 2. LINHA (REGISTRO/TUPLA)
Cada linha representa uma entidade única
- Exemplo: Um cliente específico

### 3. COLUNA (ATRIBUTO/CAMPO)
Define as propriedades dos dados
- Exemplo: nome, email, telefone

### 4. CHAVE PRIMÁRIA (PRIMARY KEY)
Identifica unicamente cada linha
- Não pode ser nula ou duplicada
- Exemplo: id (1, 2, 3...)

### 5. CHAVE ESTRANGEIRA (FOREIGN KEY)
Estabelece relacionamento entre tabelas
- Referencia a chave primária de outra tabela
- Exemplo: id_cliente em PEDIDOS refere-se a CLIENTES

### 6. INTEGRIDADE REFERENCIAL
Garante que dados relacionados sejam válidos
- Não permite deletar um cliente com pedidos associados

---

## 🎨 MER e DER

### MER (Modelo Entidade-Relacionamento)
- Representação conceitual do banco
- Define entidades e seus relacionamentos
- Independente de tecnologia

**Exemplo MER simplificado:**
```
CLIENTE (1) ──── (N) PEDIDO
└─ Cada cliente pode ter vários pedidos
└─ Cada pedido pertence a um único cliente
```

### DER (Diagrama Entidade-Relacionamento)
- Representação gráfica do MER
- Usa símbolos para entidades, atributos e relacionamentos
- Facilita visualização da estrutura

---

## 🏗️ Exemplo: Estrutura de um Banco de Dados Simples

Banco de Dados: **LOJA**

```
├── Tabela: CLIENTES
│   ├── id (PK)
│   ├── nome
│   ├── email
│   └── telefone
│
├── Tabela: PRODUTOS
│   ├── id (PK)
│   ├── nome
│   ├── descricao
│   ├── preco
│   └── estoque
│
└── Tabela: PEDIDOS
    ├── id (PK)
    ├── id_cliente (FK → CLIENTES)
    ├── id_produto (FK → PRODUTOS)
    ├── quantidade
    ├── data_pedido
    └── status
```

---

## ✨ Vantagens dos Bancos Relacionais

✓ Estrutura bem organizada  
✓ Integridade dos dados garantida  
✓ Consultas poderosas com SQL  
✓ Escalabilidade  
✓ Segurança com controle de acesso  
✓ Recuperação de falhas (backups)

---

## 🛠️ SGBD (Sistema Gerenciador de Banco de Dados)

SGBD é o software responsável por:
- ✔ **Criar** bancos de dados
- ✔ **Armazenar** dados de forma segura
- ✔ **Organizar** dados estruturados
- ✔ **Consultar** dados eficientemente

### Exemplos de SGBD:
- **MySQL**: simples, popular, open-source
- **PostgreSQL**: robusto, features avançadas
- **Oracle Database**: enterprise, escalável
- **SQL Server**: Microsoft, integração Windows
- **SQLite**: leve, sem servidor

---

## 🔄 CRUD — Operações Básicas

CRUD são as 4 operações fundamentais em bancos de dados:

| Letra | Significado | Comando SQL |
|-------|-------------|-------------|
| **C** | **Create** (criar) | INSERT |
| **R** | **Read** (ler) | SELECT |
| **U** | **Update** (atualizar) | UPDATE |
| **D** | **Delete** (excluir) | DELETE |

### Exemplos CRUD:

**Create (INSERT):**
```sql
INSERT INTO clientes (nome, email) 
VALUES ('Renata', 'renata@email.com');
```

**Read (SELECT):**
```sql
SELECT * FROM clientes WHERE id = 1;
```

**Update (UPDATE):**
```sql
UPDATE clientes 
SET email = 'novo@email.com' 
WHERE id = 1;
```

**Delete (DELETE):**
```sql
DELETE FROM clientes WHERE id = 1;
```

---

## 🔍 SQL — Linguagem de Consulta Estruturada

SQL é a linguagem padrão para trabalhar com bancos relacionais, permitindo criar, manipular e consultar dados.

### Principais comandos:
- `SELECT` → buscar dados (Read)
- `INSERT` → adicionar dados (Create)
- `UPDATE` → modificar dados (Update)
- `DELETE` → remover dados (Delete)
- `CREATE` → criar tabelas
- `ALTER` → modificar estrutura
- `DROP` → deletar tabelas

### Exemplo básico:
```sql
SELECT nome, email 
FROM CLIENTES 
WHERE id = 1;
```

**Resultado esperado:**
```
nome      | email
--------  | -----------
Renata    | r@email...
```

---

## 🛠️ Ambiente de Desenvolvimento

Para trabalhar com Bancos de Dados Relacionais:

### Opções gratuitas:
- **SQLite**: banco simples, sem servidor (ótimo para aprender)
- **PostgreSQL**: robusto e open-source
- **MySQL**: simples e popular
- **MariaDB**: alternativa ao MySQL

### IDEs e ferramentas:
- **DBeaver**: interface gráfica para múltiplos bancos
- **pgAdmin**: específico para PostgreSQL
- **MySQL Workbench**: específico para MySQL
- **VS Code**: com extensões SQL

---

## 💻 Exemplo Prático: Criando Tabelas (SQL)

```sql
CREATE TABLE clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    telefone VARCHAR(15),
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pedidos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    valor DECIMAL(10, 2),
    data_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'pendente',
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);
```

---

## 📝 Exemplo Prático: Inserindo Dados

```sql
INSERT INTO clientes (nome, email, telefone) VALUES
('Renata Citelli', 'renata@email.com', '11999999999'),
('Ana Paula', 'ana@email.com', '21988888888'),
('Carlos Silva', 'carlos@email.com', '31977777777');

INSERT INTO pedidos (id_cliente, valor, status) VALUES
(1, 150.00, 'concluído'),
(1, 250.50, 'pendente'),
(2, 89.99, 'concluído');
```

---

## 🔎 Exemplo Prático: Consultando Dados

### Consulta simples:
```sql
SELECT * FROM clientes;
```
→ Retorna todos os clientes

### Consulta com filtro:
```sql
SELECT nome, email 
FROM clientes 
WHERE id = 1;
```
→ Retorna nome e email do cliente com id = 1

### Consulta com agregação:
```sql
SELECT c.nome, COUNT(p.id) as total_pedidos
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.id_cliente
GROUP BY c.id, c.nome;
```
→ Conta quantos pedidos cada cliente fez

---

## 🔗 Relacionamentos

### 1 : 1 (Um para Um)
Um cliente tem um endereço principal

### 1 : N (Um para Muitos)
Um cliente tem vários pedidos

### N : N (Muitos para Muitos)
Vários estudantes têm várias matérias  
Necessita tabela de junção (ALUNOS_MATÉRIAS)

---

## 🛡️ Integridade dos Dados

Integridade é a garantia de que os dados estejam:
- ✔ **Corretos**: dentro dos padrões esperados
- ✔ **Válidos**: respeitam as regras do negócio
- ✔ **Consistentes**: sem contradições entre tabelas

**Exemplo:** Se um cliente é deletado, seus pedidos também devem ser, evitando referências órfãs.

---

## 📚 Normalização

**Normalização** é a técnica para organizar dados evitando:
- ❌ **Duplicidade**: dados repetidos desnecessariamente
- ❌ **Inconsistência**: informações conflitantes
- ❌ **Anomalias**: problemas ao inserir, atualizar ou deletar

> Veremos normalização em detalhes no Módulo 04

---

## 🔒 Segurança

Bancos relacionais oferecem controle de:
- ✔ **Acesso**: quem pode acessar os dados
- ✔ **Permissões**: qual operação cada usuário pode fazer
- ✔ **Proteção**: criptografia e backup dos dados

---

## 🔄 Flexibilidade

Bancos relacionais permitem:
- ✔ **Alterar tabelas**: adicionar/remover colunas
- ✔ **Adicionar dados**: crescer sem limitações
- ✔ **Expandir estrutura**: ajustar conforme necessário

---

## ⚡ Suporte ACID — Garantia de Transações Seguras

ACID é um conjunto de propriedades que garantem a **segurança e confiabilidade** das transações em um banco de dados.

### 🔹 A — Atomicidade
"Ou faz tudo ou não faz nada"

**Exemplo:** Uma transferência bancária move dinheiro de uma conta para outra. Se falhar no meio, ambas as contas retornam ao estado original.

```sql
BEGIN TRANSACTION;
  UPDATE contas SET saldo = saldo - 100 WHERE id = 1;
  UPDATE contas SET saldo = saldo + 100 WHERE id = 2;
COMMIT;
```
Se qualquer comando falhar, toda a transação é revertida.

### 🔹 C — Consistência
"Mantém dados válidos"

**Exemplo:** Se a regra diz que saldo não pode ser negativo, o banco garante isso sempre.

```sql
ALTER TABLE contas 
ADD CONSTRAINT saldo_valido CHECK (saldo >= 0);
```

### 🔹 I — Isolamento
"Transações não interferem umas nas outras"

**Exemplo:** Se dois usuários fazem transferências ao mesmo tempo, uma não afeta a outra.

Níveis de isolamento:
- READ UNCOMMITTED
- READ COMMITTED
- REPEATABLE READ
- SERIALIZABLE

### 🔹 D — Durabilidade
"Dados salvos permanecem mesmo após falhas"

**Exemplo:** Se a eletricidade cair logo após um commit, os dados não são perdidos.

O banco escreve em disco (não apenas memória) para garantir persistência.

---

## 💜 Resumão para Fixar

- 👉 **SGBD** → Software que gerencia o banco
- 👉 **CRUD** → Operações: Create, Read, Update, Delete
- 👉 **Tupla** → Linha da tabela (um registro)
- 👉 **SQL** → Linguagem padrão do banco
- 👉 **Relacionamento** → Conexão entre tabelas via chaves
- 👉 **ACID** → Segurança e confiabilidade das transações
- 👉 **Integridade** → Dados corretos, válidos e consistentes
- 👉 **Normalização** → Organizar dados evitando redundâncias
- 👉 **Segurança** → Controle de acesso e permissões
- 👉 **Flexibilidade** → Capacidade de crescimento e adaptação
