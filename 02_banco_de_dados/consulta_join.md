# ============================================================
# Bootcamp TOTVS — Fundamentos de Engenharia de Dados e ML
# Módulo — Consultas Avançadas: JOINs
# Autora: Renata Citelli
# ============================================================

## 🔗 Junções (JOINs)

### O que é um JOIN?

**JOIN** é uma operação que combina registros de **duas ou mais tabelas** com base em uma coluna relacionada entre elas.

Usado quando os dados estão distribuídos em tabelas diferentes e precisamos consultá-los juntos.

---

## 📦 Tabelas de Exemplo

```sql
-- Tabela usuarios
CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nome_usuario VARCHAR(100) NOT NULL,
    telefone VARCHAR(15)
);

-- Tabela destinos
CREATE TABLE destinos (
    id_destino INT PRIMARY KEY AUTO_INCREMENT,
    nome_destino VARCHAR(100) NOT NULL,
    pais VARCHAR(100)
);

-- Tabela reservas
CREATE TABLE reservas (
    id_reserva INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    id_destino INT,
    data_reserva DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'pendente',
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_destino) REFERENCES destinos(id_destino)
);
```

### Dados de Exemplo:

```
usuarios                        destinos
──────────────────────────      ──────────────────────────
id  │ nome        │ telefone    id  │ nome_destino │ pais
1   │ Renata      │ 99999       10  │ Paris        │ França
2   │ Ana Paula   │ 88888       20  │ Roma         │ Itália
3   │ Carlos      │ 77777       30  │ Tokyo        │ Japão
4   │ Diana       │ 66666

reservas
──────────────────────────────────────────────
id  │ id_usuario │ id_destino │ data_reserva
1   │ 1          │ 10         │ 2024-01-10
2   │ 1          │ 20         │ 2024-02-15
3   │ 2          │ 30         │ 2024-03-20
4   │ 3          │ 10         │ 2024-04-01
```

> ⚠️ Diana (id=4) não tem reservas. Tokyo (id=30) só tem reserva da Ana Paula.

---

## 1️⃣ INNER JOIN

### O que faz:
Retorna apenas os registros que têm **correspondência nas duas tabelas**.
Registros sem correspondência são excluídos.

```
   usuarios        reservas
  ┌────────┐      ┌────────┐
  │        │▓▓▓▓▓▓│        │
  │        │▓▓▓▓▓▓│        │
  └────────┘      └────────┘
              ↑
         só isso
```

### Sintaxe:

```sql
SELECT colunas
FROM tabela1
INNER JOIN tabela2 ON tabela1.coluna = tabela2.coluna;
```

### Exemplo 1: Usuarios com suas reservas

```sql
SELECT 
    u.nome_usuario,
    r.data_reserva,
    r.status
FROM usuarios u
INNER JOIN reservas r ON u.id_usuario = r.id_usuario;
```

**Resultado:**
```
nome_usuario │ data_reserva │ status
Renata       │ 2024-01-10   │ pendente
Renata       │ 2024-02-15   │ pendente
Ana Paula    │ 2024-03-20   │ pendente
Carlos       │ 2024-04-01   │ pendente
```
> ⚠️ Diana não aparece — ela não tem reservas.

### Exemplo 2: Usuarios, reservas e destinos (3 tabelas)

```sql
SELECT 
    u.nome_usuario,
    d.nome_destino,
    d.pais,
    r.data_reserva
FROM usuarios u
INNER JOIN reservas r ON u.id_usuario = r.id_usuario
INNER JOIN destinos d ON r.id_destino = d.id_destino;
```

**Resultado:**
```
nome_usuario │ nome_destino │ pais    │ data_reserva
Renata       │ Paris        │ França  │ 2024-01-10
Renata       │ Roma         │ Itália  │ 2024-02-15
Ana Paula    │ Tokyo        │ Japão   │ 2024-03-20
Carlos       │ Paris        │ França  │ 2024-04-01
```

### ✅ Quando usar INNER JOIN:
- Quando só quer registros com correspondência nas duas tabelas
- É o JOIN mais comum e mais performático

---

## 2️⃣ LEFT JOIN (LEFT OUTER JOIN)

### O que faz:
Retorna **todos os registros da tabela da esquerda** e os correspondentes da direita.
Onde não há correspondência, preenche com **NULL**.

```
   usuarios        reservas
  ┌────────┐      ┌────────┐
  │▓▓▓▓▓▓▓▓│▓▓▓▓▓▓│        │
  │▓▓▓▓▓▓▓▓│▓▓▓▓▓▓│        │
  └────────┘      └────────┘
       ↑
  tudo isso
```

### Sintaxe:

```sql
SELECT colunas
FROM tabela1
LEFT JOIN tabela2 ON tabela1.coluna = tabela2.coluna;
```

### Exemplo 1: Todos os usuarios, com ou sem reservas

```sql
SELECT 
    u.nome_usuario,
    r.data_reserva,
    r.status
FROM usuarios u
LEFT JOIN reservas r ON u.id_usuario = r.id_usuario;
```

**Resultado:**
```
nome_usuario │ data_reserva │ status
Renata       │ 2024-01-10   │ pendente
Renata       │ 2024-02-15   │ pendente
Ana Paula    │ 2024-03-20   │ pendente
Carlos       │ 2024-04-01   │ pendente
Diana        │ NULL         │ NULL
```
> ✅ Diana aparece, mas com NULL nas colunas de reserva.

### Exemplo 2: Usuarios SEM reservas

```sql
SELECT 
    u.nome_usuario
FROM usuarios u
LEFT JOIN reservas r ON u.id_usuario = r.id_usuario
WHERE r.id_reserva IS NULL;
```

**Resultado:**
```
nome_usuario
Diana
```
> Filtrando só quem não tem reserva — útil para encontrar registros sem correspondência!

### ✅ Quando usar LEFT JOIN:
- Quando quer todos os registros da tabela principal, mesmo sem correspondência
- Para encontrar registros "órfãos" (sem relacionamento)

---

## 3️⃣ RIGHT JOIN (RIGHT OUTER JOIN)

### O que faz:
Retorna **todos os registros da tabela da direita** e os correspondentes da esquerda.
Onde não há correspondência, preenche com **NULL**.

```
   usuarios        reservas
  ┌────────┐      ┌────────┐
  │        │▓▓▓▓▓▓│▓▓▓▓▓▓▓▓│
  │        │▓▓▓▓▓▓│▓▓▓▓▓▓▓▓│
  └────────┘      └────────┘
                       ↑
                  tudo isso
```

### Sintaxe:

```sql
SELECT colunas
FROM tabela1
RIGHT JOIN tabela2 ON tabela1.coluna = tabela2.coluna;
```

### Exemplo 1: Todos os destinos, com ou sem reservas

```sql
SELECT 
    d.nome_destino,
    d.pais,
    r.data_reserva
FROM reservas r
RIGHT JOIN destinos d ON r.id_destino = d.id_destino;
```

**Resultado:**
```
nome_destino │ pais    │ data_reserva
Paris        │ França  │ 2024-01-10
Paris        │ França  │ 2024-04-01
Roma         │ Itália  │ 2024-02-15
Tokyo        │ Japão   │ 2024-03-20
```
> ⚠️ Nesse exemplo todos os destinos têm reserva. Se houvesse um destino sem reserva, apareceria com NULL.

### Exemplo 2: Destinos SEM reservas

```sql
SELECT 
    d.nome_destino
FROM reservas r
RIGHT JOIN destinos d ON r.id_destino = d.id_destino
WHERE r.id_reserva IS NULL;
```

### 💡 Dica:
RIGHT JOIN é menos comum — a maioria dos desenvolvedores prefere inverter a ordem das tabelas e usar LEFT JOIN, que é mais intuitivo.

```sql
-- Estas duas queries têm o mesmo resultado:
SELECT * FROM reservas r RIGHT JOIN destinos d ON r.id_destino = d.id_destino;
SELECT * FROM destinos d LEFT JOIN reservas r ON d.id_destino = r.id_destino;
```

### ✅ Quando usar RIGHT JOIN:
- Quando quer todos os registros da tabela secundária
- Na prática, muitos preferem reescrever como LEFT JOIN

---

## 📊 Comparativo dos JOINs

| JOIN | Retorna | Registros sem correspondência |
|------|---------|-------------------------------|
| **INNER JOIN** | Só correspondências | ❌ Excluídos |
| **LEFT JOIN** | Todos da esquerda | ✅ NULL na direita |
| **RIGHT JOIN** | Todos da direita | ✅ NULL na esquerda |

---

## 🎯 Boas Práticas com JOINs

```sql
-- ✔ Use alias para deixar mais legível
SELECT u.nome_usuario, d.nome_destino
FROM usuarios u
INNER JOIN reservas r ON u.id_usuario = r.id_usuario
INNER JOIN destinos d ON r.id_destino = d.id_destino;

-- ✔ Especifique sempre a tabela antes da coluna em joins
-- ❌ Ambíguo:
SELECT nome_usuario, data_reserva FROM usuarios INNER JOIN reservas ...

-- ✅ Claro:
SELECT u.nome_usuario, r.data_reserva FROM usuarios u INNER JOIN reservas r ...
```

---

## 📌 Resumo

- ✅ **JOIN** combina dados de múltiplas tabelas
- ✅ **INNER JOIN** — só registros com correspondência nas duas tabelas
- ✅ **LEFT JOIN** — todos da esquerda + correspondências da direita (NULL onde não há)
- ✅ **RIGHT JOIN** — todos da direita + correspondências da esquerda (NULL onde não há)
- ✅ Use **alias** (`u`, `r`, `d`) para deixar as queries mais legíveis
- ✅ Sempre especifique a **tabela.coluna** em queries com JOIN
- ✅ RIGHT JOIN pode ser reescrito como LEFT JOIN invertendo a ordem das tabelas

---

## 🎯 Próximos Passos

- Subconsultas (Subqueries)
- Funções Agregadas e GROUP BY
- Índices e Performance
