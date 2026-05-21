# 📚 SQL — Organização da Linguagem

**SQL** (**Structured Query Language**) é a linguagem usada para:
- ✔ **Criar** bancos de dados e tabelas
- ✔ **Consultar** informações
- ✔ **Manipular** dados (inserir, atualizar, deletar)
- ✔ **Controlar** acesso e transações

---

## 🗂️ Categorias da SQL

A linguagem SQL é dividida em **5 grupos de comandos**, cada um com uma função específica.

---

## 🔍 DQL — Data Query Language

**Linguagem de Consulta de Dados**

### Função:
Buscar e recuperar informações do banco de dados sem modificar dados.

### Principal comando:
```sql
SELECT
```

### Exemplo:
```sql
SELECT * FROM clientes;
```
👉 Retorna todos os clientes da tabela

### Mais exemplos:
```sql
-- Selecionar colunas específicas
SELECT id, nome, email FROM clientes;

-- Com filtro
SELECT * FROM clientes WHERE id = 1;

-- Com ordenação
SELECT * FROM clientes ORDER BY nome;
```

---

## ✏️ DML — Data Manipulation Language

**Linguagem de Manipulação de Dados**

### Função:
Inserir, atualizar e excluir dados nas tabelas.

### Principais comandos:
```sql
INSERT    -- Adicionar novos registros
UPDATE    -- Modificar registros existentes
DELETE    -- Remover registros
```

### INSERT — Adicionar Dados
```sql
INSERT INTO clientes (nome, email, telefone)
VALUES ('Renata Citelli', 'renata@email.com', '11999999999');
```

Ou inserir múltiplos registros:
```sql
INSERT INTO clientes (nome, email) VALUES
('Ana Paula', 'ana@email.com'),
('Carlos Silva', 'carlos@email.com'),
('Diana Lima', 'diana@email.com');
```

### UPDATE — Modificar Dados
```sql
UPDATE clientes
SET nome = 'Renata Citelli'
WHERE id = 1;
```

Atualizando múltiplas colunas:
```sql
UPDATE clientes
SET email = 'novo@email.com', telefone = '11988888888'
WHERE id = 1;
```

### DELETE — Remover Dados
```sql
DELETE FROM clientes
WHERE id = 1;
```

⚠️ **Cuidado:** Delete sem WHERE remove **todos os registros**!

```sql
-- ❌ PERIGOSO — Remove todos!
DELETE FROM clientes;

-- ✅ SEGURO — Remove apenas um
DELETE FROM clientes WHERE id = 1;
```

---

## 🏗️ DDL — Data Definition Language

**Linguagem de Definição de Dados**

### Função:
Criar, alterar e remover estruturas (tabelas, índices, etc.) do banco.

### Principais comandos:
```sql
CREATE    -- Criar nova estrutura
ALTER     -- Modificar estrutura existente
DROP      -- Remover estrutura
TRUNCATE  -- Limpar dados (mantém estrutura)
```

### CREATE — Criar Tabela
```sql
CREATE TABLE clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    telefone VARCHAR(15),
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### ALTER — Modificar Tabela

Adicionar coluna:
```sql
ALTER TABLE clientes
ADD email VARCHAR(100);
```

Remover coluna:
```sql
ALTER TABLE clientes
DROP COLUMN telefone;
```

Modificar tipo de coluna:
```sql
ALTER TABLE clientes
MODIFY COLUMN nome VARCHAR(150);
```

Renomear coluna:
```sql
ALTER TABLE clientes
CHANGE COLUMN email email_cliente VARCHAR(100);
```

### DROP — Deletar Tabela
```sql
DROP TABLE clientes;
```

⚠️ **Cuidado:** Deleta a tabela inteira, não apenas os dados!

### TRUNCATE — Limpar Dados
```sql
TRUNCATE TABLE clientes;
```

Diferenças:
- `DELETE`: Remove dados um por um, mais lento
- `TRUNCATE`: Remove todos os dados rapidamente, reseta auto-increment
- `DROP`: Remove estrutura e dados

---

## 🔒 DCL — Data Control Language

**Linguagem de Controle de Dados**

### Função:
Controlar permissões e acesso ao banco de dados.

### Principais comandos:
```sql
GRANT     -- Conceder permissões
REVOKE    -- Remover permissões
```

### GRANT — Conceder Permissão
```sql
-- Dar acesso SELECT a um usuário
GRANT SELECT ON clientes TO usuario;

-- Múltiplas permissões
GRANT SELECT, INSERT, UPDATE ON clientes TO usuario;

-- Todas as permissões
GRANT ALL ON clientes TO usuario;

-- Em todas as tabelas
GRANT SELECT ON * TO usuario;
```

### REVOKE — Remover Permissão
```sql
-- Remover acesso SELECT
REVOKE SELECT ON clientes FROM usuario;

-- Remover múltiplas permissões
REVOKE INSERT, UPDATE ON clientes FROM usuario;

-- Remover todas as permissões
REVOKE ALL ON clientes FROM usuario;
```

---

## 🔄 TCL — Transaction Control Language

**Linguagem de Controle de Transações**

(Alguns materiais chamam de DTL — Data Transaction Language)

### Função:
Controlar confirmação e desfazimento de operações (transações).

### Principais comandos:
```sql
COMMIT      -- Confirmar/salvar alterações
ROLLBACK    -- Desfazer alterações
SAVEPOINT   -- Criar ponto de restauração
```

### Conceito: Transação
Uma transação é um **conjunto de operações** que devem ser tratadas como uma unidade indivisível.

**Exemplo:** Transferência bancária
- Tirar dinheiro de uma conta
- Colocar dinheiro em outra conta

Se falhar no meio, ambas devem voltar ao estado original.

### COMMIT — Confirmar Alterações
```sql
BEGIN TRANSACTION;
  UPDATE contas SET saldo = saldo - 100 WHERE id = 1;
  UPDATE contas SET saldo = saldo + 100 WHERE id = 2;
COMMIT;
```
👉 Salva as alterações no banco permanentemente

### ROLLBACK — Desfazer Alterações
```sql
BEGIN TRANSACTION;
  UPDATE clientes SET email = 'novo@email.com' WHERE id = 1;
  -- Mudei de ideia!
ROLLBACK;
```
👉 Desfaz todas as alterações da transação

### SAVEPOINT — Criar Ponto de Restauração
```sql
BEGIN TRANSACTION;
  INSERT INTO pedidos VALUES (1, 100.00);
  SAVEPOINT ponto1;
  
  INSERT INTO pedidos VALUES (2, 200.00);
  -- Erro aqui!
  ROLLBACK TO ponto1;
  -- Volta apenas ao ponto1, não cancela tudo
COMMIT;
```

---

## 🏷️ Nomenclatura em Banco de Dados

### Boas Práticas:
- ✔ **Nomes claros e descritivos**
- ✔ **Sem espaços** (use underscore)
- ✔ **Padronizados** (escolha um padrão e mantenha)
- ✔ **Fáceis de entender**
- ✔ **Evite abreviações confusas**

### ✅ Exemplos Bons:
```text
clientes
pedidos
id_cliente
data_pedido
valor_total
email_principal
telefone_celular
```

### ❌ Evitar:
```text
Tabela1          ← genérico
dados123         ← confuso
x, y, z          ← muito vago
tbl_cli_ped      ← abreviação desnecessária
"Cliente Id"     ← espaço em branco
```

---

## 🧠 Padrões Comuns de Nomenclatura

### snake_case (Mais usado em banco de dados)
Palavras separadas por underscore, tudo minúsculo.

```text
id_cliente
data_pedido
valor_total
email_principal
data_nascimento
```

**Vantagem:** Funciona em todos os SGBDs, fácil de ler

### camelCase (Menos comum em SQL)
Primeira palavra minúscula, próximas com inicial maiúscula.

```text
idCliente
dataPedido
valorTotal
```

**Desvantagem:** Alguns SGBDs diferenciam maiúscula de minúscula

### PascalCase (Raro em SQL)
Todas as palavras com inicial maiúscula.

```text
IdCliente
DataPedido
ValorTotal
```

---

## 📋 Resumo Comparativo

| Categoria | O que faz | Comandos principais | Afeta dados? |
|-----------|-----------|-------|------|
| **DQL** | Consultar dados | SELECT | Não |
| **DML** | Manipular dados | INSERT, UPDATE, DELETE | Sim |
| **DDL** | Estrutura do banco | CREATE, ALTER, DROP, TRUNCATE | Sim (estrutura) |
| **DCL** | Controlar acesso | GRANT, REVOKE | Não (dados) |
| **TCL** | Controlar transações | COMMIT, ROLLBACK, SAVEPOINT | Sim (confirmação) |

---

## 💜 Resumão para Fixar

| Categoria | Função | Quando usar |
|-----------|--------|-------------|
| **DQL** | Consultar | Quando precisa ler dados |
| **DML** | Manipular dados | Quando precisa inserir, atualizar ou deletar |
| **DDL** | Criar estrutura | Quando precisa criar/modificar tabelas |
| **DCL** | Controle e permissões | Quando precisa controlar acesso |
| **TCL** | Controle de transações | Quando precisa confirmar/desfazer operações |

---

## 🎯 Fluxo Típico

```
1. DDL   → CREATE TABLE clientes (criar estrutura)
2. DML   → INSERT INTO clientes (adicionar dados)
3. DQL   → SELECT * FROM clientes (consultar dados)
4. DML   → UPDATE clientes (atualizar dados)
5. TCL   → COMMIT (confirmar alterações)
```

---

## 💡 Dicas Importantes

✅ Sempre use nomes descritivos  
✅ Mantenha um padrão de nomenclatura  
✅ Use COMMIT e ROLLBACK para segurança  
✅ Teste DELETE e UPDATE com WHERE antes de executar  
✅ Sempre faça backup antes de operações grandes  
✅ Use transações para operações críticas  

---

**Próximo:** Usar esses comandos em consultas avançadas!
