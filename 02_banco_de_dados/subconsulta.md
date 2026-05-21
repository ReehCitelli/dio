# ============================================================
# Bootcamp TOTVS — Fundamentos de Engenharia de Dados e ML
# Módulo — Consultas Avançadas: Subconsultas
# Autora: Renata Citelli
# ============================================================

## 🔍 Subconsultas (Subqueries)

### O que é uma Subconsulta?

**Subconsulta** é uma consulta SQL dentro de outra consulta.
A consulta interna é executada primeiro e seu resultado é usado pela consulta externa.

```sql
SELECT colunas
FROM tabela
WHERE coluna = (SELECT coluna FROM tabela WHERE condição);
                └─────────────────────────────────────┘
                            subconsulta
```

### Quando usar:
- Quando precisa filtrar com base em resultados de outra tabela
- Quando o JOIN deixaria a query muito complexa
- Para cálculos que dependem de agregações

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
──────────────────────────────────────────────
id  │ id_usuario │ id_destino │ data_reserva
1   │ 1          │ 10         │ 2024-01-10
2   │ 1          │ 20         │ 2024-02-15
3   │ 2          │ 30         │ 2024-03-20
4   │ 3          │ 10         │ 2024-04-01
```

---

## 1️⃣ Subconsulta no WHERE

### O uso mais comum — filtra resultados com base em outra query.

### Exemplo 1: Usuarios que têm reservas para Paris

```sql
SELECT nome_usuario
FROM usuarios
WHERE id_usuario IN (
    SELECT id_usuario
    FROM reservas
    WHERE id_destino = (
        SELECT id_destino
        FROM destinos
        WHERE nome_destino = 'Paris'
    )
);
```

**Resultado:**
```
nome_usuario
Renata
Carlos
```

**Como funciona passo a passo:**
1. A subconsulta mais interna busca o `id_destino` de Paris → retorna `10`
2. A subconsulta do meio busca `id_usuario` das reservas com `id_destino = 10` → retorna `1, 3`
3. A query externa busca os nomes com `id_usuario IN (1, 3)`

---

### Exemplo 2: Usuarios SEM nenhuma reserva

```sql
SELECT nome_usuario
FROM usuarios
WHERE id_usuario NOT IN (
    SELECT id_usuario
    FROM reservas
);
```

**Resultado:**
```
nome_usuario
Diana
```

---

### Exemplo 3: Reservas feitas depois da primeira reserva da Renata

```sql
SELECT *
FROM reservas
WHERE data_reserva > (
    SELECT MIN(data_reserva)
    FROM reservas
    WHERE id_usuario = 1
);
```

**Resultado:** Todas as reservas após 2024-01-10.

---

## 2️⃣ Subconsulta no FROM

### Trata o resultado da subconsulta como uma tabela temporária.

### Exemplo: Total de reservas por usuario

```sql
SELECT u.nome_usuario, contagem.total
FROM usuarios u
INNER JOIN (
    SELECT id_usuario, COUNT(*) AS total
    FROM reservas
    GROUP BY id_usuario
) AS contagem ON u.id_usuario = contagem.id_usuario;
```

**Resultado:**
```
nome_usuario │ total
Renata       │ 2
Ana Paula    │ 1
Carlos       │ 1
```

> A subconsulta no FROM sempre precisa de um **alias** (`AS contagem`).

---

## 3️⃣ Subconsulta no SELECT

### Calcula um valor para cada linha da query principal.

### Exemplo: Nome do usuario + total de reservas dele

```sql
SELECT 
    nome_usuario,
    (SELECT COUNT(*) 
     FROM reservas r 
     WHERE r.id_usuario = u.id_usuario) AS total_reservas
FROM usuarios u;
```

**Resultado:**
```
nome_usuario │ total_reservas
Renata       │ 2
Ana Paula    │ 1
Carlos       │ 1
Diana        │ 0
```

> ✅ Diana aparece com 0 — diferente do INNER JOIN que a excluiria.

---

## 4️⃣ Operadores com Subconsultas

### IN / NOT IN
Verifica se o valor está (ou não está) na lista retornada:

```sql
-- Usuarios que foram para destinos na Europa
SELECT nome_usuario
FROM usuarios
WHERE id_usuario IN (
    SELECT r.id_usuario
    FROM reservas r
    INNER JOIN destinos d ON r.id_destino = d.id_destino
    WHERE d.pais IN ('França', 'Itália')
);
```

**Resultado:**
```
nome_usuario
Renata
Carlos
```

---

### EXISTS / NOT EXISTS
Verifica se a subconsulta retorna algum resultado:

```sql
-- Usuarios que têm pelo menos uma reserva
SELECT nome_usuario
FROM usuarios u
WHERE EXISTS (
    SELECT 1
    FROM reservas r
    WHERE r.id_usuario = u.id_usuario
);
```

**Resultado:**
```
nome_usuario
Renata
Ana Paula
Carlos
```

```sql
-- Usuarios sem nenhuma reserva
SELECT nome_usuario
FROM usuarios u
WHERE NOT EXISTS (
    SELECT 1
    FROM reservas r
    WHERE r.id_usuario = u.id_usuario
);
```

**Resultado:**
```
nome_usuario
Diana
```

> 💡 **EXISTS vs IN:** EXISTS para quando a subconsulta pode retornar muitos resultados — é mais eficiente.

---

### ALL / ANY
Compara com todos ou qualquer valor da subconsulta:

```sql
-- Destinos com mais reservas que a média
SELECT nome_destino
FROM destinos
WHERE id_destino = ANY (
    SELECT id_destino
    FROM reservas
    GROUP BY id_destino
    HAVING COUNT(*) > 1
);
```

---

## 📊 Subconsulta vs JOIN

| | Subconsulta | JOIN |
|---|---|---|
| **Legibilidade** | Mais fácil de ler | Pode ficar complexo |
| **Performance** | Pode ser mais lenta | Geralmente mais rápido |
| **Quando usar** | Lógica complexa em etapas | Combinar dados de tabelas |
| **Resultado** | Filtra ou calcula | Combina colunas |

> 💡 Na prática: use JOIN para combinar dados e subconsulta para filtrar ou calcular.

---

## ✅ Boas Práticas

```sql
-- ✔ Sempre use alias em subconsultas no FROM
SELECT u.nome_usuario, sub.total
FROM usuarios u
INNER JOIN (SELECT id_usuario, COUNT(*) AS total FROM reservas GROUP BY id_usuario) AS sub
ON u.id_usuario = sub.id_usuario;

-- ✔ Prefira EXISTS a IN quando a subconsulta retorna muitas linhas
-- ✔ Teste a subconsulta separadamente antes de encaixar na query principal
-- ✔ Evite subconsultas muito aninhadas — dificultam a leitura e manutenção
```

---

## 📌 Resumo

- ✅ **Subconsulta** é uma query dentro de outra query
- ✅ A subconsulta **interna** é executada primeiro
- ✅ Pode aparecer no **WHERE**, **FROM** ou **SELECT**
- ✅ **IN / NOT IN** — verifica se valor está na lista
- ✅ **EXISTS / NOT EXISTS** — verifica se há resultado
- ✅ Subconsulta no FROM precisa de **alias**
- ✅ Para combinar dados prefira **JOIN**, para filtrar prefira **subconsulta**

---

## 🎯 Próximos Passos

- Funções Agregadas e GROUP BY
- Índices e Performance
