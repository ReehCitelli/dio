# ============================================================
# Bootcamp TOTVS — Fundamentos de Engenharia de Dados e ML
# Módulo — Consultas Avançadas: Índices
# Autora: Renata Citelli
# ============================================================

## 📇 Índices (Indexes)

### O que é um Índice?

**Índice** é uma estrutura de dados que acelera a busca de registros em uma tabela.

Funciona como o **índice de um livro** — em vez de ler página por página para encontrar um assunto, você vai direto ao índice e pula para a página certa.

```
Sem índice:                    Com índice:
──────────────                 ──────────────
Lê registro 1                  Vai direto ao
Lê registro 2                  registro correto
Lê registro 3        vs        ↓
Lê registro 4                  Registro 4 ✅
Lê registro 5
...
```

### Quando usar:
- Colunas usadas frequentemente em **WHERE**
- Colunas usadas em **JOIN**
- Colunas usadas em **ORDER BY**
- Tabelas com **muitos registros**

---

## 📦 Tabelas de Exemplo

```
usuarios                        destinos
──────────────────────────      ──────────────────────────
id  │ nome        │ telefone    id  │ nome_destino │ pais
1   │ Renata      │ 99999       10  │ Paris        │ França
2   │ Ana Paula   │ 88888       20  │ Roma         │ Itália
3   │ Carlos      │ 77777       30  │ Tokyo        │ Japão
4   │ Diana       │ 66666

reservas
────────────────────────────────────────────────────
id  │ id_usuario │ id_destino │ data_reserva │ valor
1   │ 1          │ 10         │ 2024-01-10   │ 1500.00
2   │ 1          │ 20         │ 2024-02-15   │ 2200.00
3   │ 2          │ 30         │ 2024-03-20   │ 3100.00
4   │ 3          │ 10         │ 2024-04-01   │ 1500.00
```

---

## 1️⃣ Tipos de Índice

### Índice Primário (PRIMARY KEY)
Criado **automaticamente** quando você define uma chave primária.

```sql
CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,  -- índice criado automaticamente
    nome_usuario VARCHAR(100)
);
```

---

### Índice Único (UNIQUE)
Garante que não há valores duplicados na coluna. Criado automaticamente com `UNIQUE`.

```sql
CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(100) UNIQUE  -- índice único criado automaticamente
);
```

---

### Índice Simples
Criado manualmente em uma coluna para acelerar buscas.

```sql
-- Criar índice na coluna nome_usuario
CREATE INDEX idx_nome_usuario
ON usuarios(nome_usuario);
```

Agora buscas por nome ficam muito mais rápidas:
```sql
SELECT * FROM usuarios WHERE nome_usuario = 'Renata';  -- usa o índice ✅
```

---

### Índice Composto
Criado em **mais de uma coluna** — útil quando você filtra por múltiplas colunas juntas.

```sql
-- Índice composto em id_usuario e id_destino
CREATE INDEX idx_usuario_destino
ON reservas(id_usuario, id_destino);
```

Acelera queries como:
```sql
SELECT * FROM reservas
WHERE id_usuario = 1 AND id_destino = 10;  -- usa o índice composto ✅
```

> ⚠️ A ordem das colunas importa! O índice `(id_usuario, id_destino)` acelera buscas por `id_usuario` ou por `id_usuario + id_destino`, mas **não** por `id_destino` sozinho.

---

### Índice Full-Text
Para buscas em textos longos.

```sql
CREATE FULLTEXT INDEX idx_descricao
ON destinos(nome_destino);

-- Busca full-text
SELECT * FROM destinos
WHERE MATCH(nome_destino) AGAINST('Paris');
```

---

## 2️⃣ Criando e Removendo Índices

### Criar índice

```sql
-- Sintaxe básica
CREATE INDEX nome_indice ON tabela(coluna);

-- Exemplos
CREATE INDEX idx_data_reserva ON reservas(data_reserva);
CREATE INDEX idx_pais ON destinos(pais);
CREATE INDEX idx_usuario_data ON reservas(id_usuario, data_reserva);
```

### Criar índice junto com a tabela

```sql
CREATE TABLE reservas (
    id_reserva INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    id_destino INT,
    data_reserva DATE NOT NULL,
    valor DECIMAL(10,2),
    INDEX idx_data_reserva (data_reserva),        -- índice simples
    INDEX idx_usuario_destino (id_usuario, id_destino),  -- índice composto
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_destino) REFERENCES destinos(id_destino)
);
```

### Ver índices de uma tabela

```sql
SHOW INDEX FROM reservas;
SHOW INDEX FROM usuarios;
```

### Remover índice

```sql
DROP INDEX idx_data_reserva ON reservas;
ALTER TABLE reservas DROP INDEX idx_data_reserva;
```

---

## 3️⃣ Como o Índice Funciona na Prática

### Sem índice — Full Table Scan

```sql
-- Sem índice em data_reserva
SELECT * FROM reservas WHERE data_reserva = '2024-01-10';
```

O banco lê **todos os registros** da tabela até encontrar os correspondentes.
Em uma tabela com milhões de registros, isso é lento. ❌

---

### Com índice — Index Scan

```sql
-- Criando o índice
CREATE INDEX idx_data_reserva ON reservas(data_reserva);

-- Mesma query agora usa o índice
SELECT * FROM reservas WHERE data_reserva = '2024-01-10';
```

O banco vai **diretamente** aos registros de 2024-01-10. ✅

---

### EXPLAIN — Verificando se o índice está sendo usado

```sql
EXPLAIN SELECT * FROM reservas WHERE data_reserva = '2024-01-10';
```

**Resultado sem índice:**
```
type: ALL  ← Full Table Scan (ruim)
key: NULL  ← nenhum índice usado
rows: 4    ← leu todos os registros
```

**Resultado com índice:**
```
type: ref          ← usou índice (bom)
key: idx_data      ← nome do índice usado
rows: 1            ← leu só o necessário
```

---

## 4️⃣ Vantagens e Desvantagens

| | Com Índice | Sem Índice |
|---|---|---|
| **SELECT (leitura)** | ✅ Muito mais rápido | ❌ Mais lento |
| **INSERT** | ❌ Mais lento (atualiza índice) | ✅ Mais rápido |
| **UPDATE** | ❌ Mais lento (atualiza índice) | ✅ Mais rápido |
| **DELETE** | ❌ Mais lento (atualiza índice) | ✅ Mais rápido |
| **Espaço em disco** | ❌ Usa mais espaço | ✅ Usa menos espaço |

> 💡 Índice é uma troca — ganha velocidade na leitura, perde um pouco na escrita.

---

## 5️⃣ Boas Práticas

```sql
-- ✔ Criar índice em colunas usadas frequentemente no WHERE
CREATE INDEX idx_status ON reservas(status);

-- ✔ Criar índice em colunas usadas em JOIN
CREATE INDEX idx_id_usuario ON reservas(id_usuario);
CREATE INDEX idx_id_destino ON reservas(id_destino);

-- ✔ Criar índice composto quando filtra por duas colunas juntas
CREATE INDEX idx_usuario_data ON reservas(id_usuario, data_reserva);

-- ❌ Não criar índice em colunas com poucos valores únicos
-- (ex: coluna "ativo" com só TRUE/FALSE — não vale a pena)

-- ❌ Não criar índices desnecessários
-- Cada índice extra ocupa espaço e deixa INSERT/UPDATE mais lentos
```

---

## 📌 Resumo

- ✅ **Índice** acelera buscas como o índice de um livro
- ✅ **PRIMARY KEY** e **UNIQUE** criam índices automaticamente
- ✅ **CREATE INDEX** cria índices manuais em colunas específicas
- ✅ **Índice composto** acelera filtros com múltiplas colunas
- ✅ **EXPLAIN** mostra se a query está usando o índice
- ✅ Índice melhora leitura mas pode deixar escrita mais lenta
- ✅ Crie índices nas colunas usadas em **WHERE**, **JOIN** e **ORDER BY**
- ✅ Evite índices desnecessários — menos é mais

---

## 🎯 Próximos Passos

- Segurança em Banco de Dados
- Transações e Controle de Concorrência
- Banco de Dados na Nuvem
