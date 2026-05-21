# ============================================================
# Bootcamp TOTVS — Fundamentos de Engenharia de Dados e ML
# Módulo — Consultas Avançadas: Funções Agregadas e Agrupamento
# Autora: Renata Citelli
# ============================================================

## 📊 Funções Agregadas e Agrupamento de Resultados

### O que são Funções Agregadas?

**Funções Agregadas** realizam cálculos sobre um conjunto de valores e retornam um único resultado.

Muito usadas para:
- Contar registros
- Somar valores
- Calcular médias
- Encontrar mínimos e máximos

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

## 1️⃣ Funções Agregadas Principais

### COUNT — Contar registros

```sql
-- Total de reservas
SELECT COUNT(*) AS total_reservas
FROM reservas;
```
**Resultado:** `4`

```sql
-- Conta só registros com valor preenchido (ignora NULL)
SELECT COUNT(valor) AS reservas_com_valor
FROM reservas;
```

```sql
-- Conta valores únicos
SELECT COUNT(DISTINCT id_destino) AS destinos_distintos
FROM reservas;
```
**Resultado:** `3`

---

### SUM — Somar valores

```sql
-- Soma total de todos os valores das reservas
SELECT SUM(valor) AS receita_total
FROM reservas;
```
**Resultado:** `R$ 8300.00`

```sql
-- Soma das reservas de um usuario específico
SELECT SUM(valor) AS total_renata
FROM reservas
WHERE id_usuario = 1;
```
**Resultado:** `R$ 3700.00`

---

### AVG — Média

```sql
-- Valor médio das reservas
SELECT AVG(valor) AS valor_medio
FROM reservas;
```
**Resultado:** `R$ 2075.00`

---

### MIN e MAX — Mínimo e Máximo

```sql
-- Reserva mais barata e mais cara
SELECT 
    MIN(valor) AS reserva_mais_barata,
    MAX(valor) AS reserva_mais_cara
FROM reservas;
```

**Resultado:**
```
reserva_mais_barata │ reserva_mais_cara
1500.00             │ 3100.00
```

```sql
-- Data da primeira e última reserva
SELECT 
    MIN(data_reserva) AS primeira_reserva,
    MAX(data_reserva) AS ultima_reserva
FROM reservas;
```

---

## 2️⃣ GROUP BY — Agrupando Resultados

### O que é:
**GROUP BY** agrupa registros com o mesmo valor em uma coluna e aplica funções agregadas em cada grupo.

### Sintaxe:

```sql
SELECT coluna, FUNÇÃO_AGREGADA(coluna)
FROM tabela
GROUP BY coluna;
```

### Exemplo 1: Total de reservas por usuario

```sql
SELECT 
    id_usuario,
    COUNT(*) AS total_reservas
FROM reservas
GROUP BY id_usuario;
```

**Resultado:**
```
id_usuario │ total_reservas
1          │ 2
2          │ 1
3          │ 1
```

### Exemplo 2: Com JOIN para mostrar o nome

```sql
SELECT 
    u.nome_usuario,
    COUNT(r.id_reserva) AS total_reservas,
    SUM(r.valor) AS valor_total
FROM usuarios u
LEFT JOIN reservas r ON u.id_usuario = r.id_usuario
GROUP BY u.id_usuario, u.nome_usuario;
```

**Resultado:**
```
nome_usuario │ total_reservas │ valor_total
Renata       │ 2              │ 3700.00
Ana Paula    │ 1              │ 3100.00
Carlos       │ 1              │ 1500.00
Diana        │ 0              │ NULL
```

### Exemplo 3: Total de reservas por destino

```sql
SELECT 
    d.nome_destino,
    d.pais,
    COUNT(r.id_reserva) AS total_reservas,
    SUM(r.valor) AS receita_destino
FROM destinos d
LEFT JOIN reservas r ON d.id_destino = r.id_destino
GROUP BY d.id_destino, d.nome_destino, d.pais;
```

**Resultado:**
```
nome_destino │ pais    │ total_reservas │ receita_destino
Paris        │ França  │ 2              │ 3000.00
Roma         │ Itália  │ 1              │ 2200.00
Tokyo        │ Japão   │ 1              │ 3100.00
```

---

## 3️⃣ HAVING — Filtrando Grupos

### O que é:
**HAVING** filtra grupos após o GROUP BY.
É o equivalente do WHERE, mas para grupos.

### WHERE vs HAVING

| | WHERE | HAVING |
|---|---|---|
| **Quando filtra** | Antes do agrupamento | Depois do agrupamento |
| **Filtra** | Linhas individuais | Grupos |
| **Usa** | Colunas normais | Funções agregadas |

### Sintaxe:

```sql
SELECT coluna, FUNÇÃO_AGREGADA(coluna)
FROM tabela
GROUP BY coluna
HAVING condição_com_agregação;
```

### Exemplo 1: Usuarios com mais de 1 reserva

```sql
SELECT 
    u.nome_usuario,
    COUNT(r.id_reserva) AS total_reservas
FROM usuarios u
INNER JOIN reservas r ON u.id_usuario = r.id_usuario
GROUP BY u.id_usuario, u.nome_usuario
HAVING COUNT(r.id_reserva) > 1;
```

**Resultado:**
```
nome_usuario │ total_reservas
Renata       │ 2
```

### Exemplo 2: Destinos com receita acima de 2000

```sql
SELECT 
    d.nome_destino,
    SUM(r.valor) AS receita_total
FROM destinos d
INNER JOIN reservas r ON d.id_destino = r.id_destino
GROUP BY d.id_destino, d.nome_destino
HAVING SUM(r.valor) > 2000;
```

**Resultado:**
```
nome_destino │ receita_total
Roma         │ 2200.00
Tokyo        │ 3100.00
```

### Exemplo 3: WHERE e HAVING juntos

```sql
-- Usuarios com mais de 1 reserva feita em 2024
SELECT 
    u.nome_usuario,
    COUNT(r.id_reserva) AS total_reservas
FROM usuarios u
INNER JOIN reservas r ON u.id_usuario = r.id_usuario
WHERE YEAR(r.data_reserva) = 2024          -- filtra linhas antes
GROUP BY u.id_usuario, u.nome_usuario
HAVING COUNT(r.id_reserva) > 1;            -- filtra grupos depois
```

---

## 4️⃣ ORDER BY com Agregações

```sql
-- Usuarios ordenados pelo total gasto (maior para menor)
SELECT 
    u.nome_usuario,
    SUM(r.valor) AS total_gasto
FROM usuarios u
INNER JOIN reservas r ON u.id_usuario = r.id_usuario
GROUP BY u.id_usuario, u.nome_usuario
ORDER BY total_gasto DESC;
```

**Resultado:**
```
nome_usuario │ total_gasto
Renata       │ 3700.00
Ana Paula    │ 3100.00
Carlos       │ 1500.00
```

---

## 5️⃣ Ordem de Execução do SQL

É importante entender a ordem em que o SQL executa cada cláusula:

```
1. FROM        → de onde vêm os dados
2. JOIN        → combina tabelas
3. WHERE       → filtra linhas
4. GROUP BY    → agrupa
5. HAVING      → filtra grupos
6. SELECT      → seleciona colunas
7. ORDER BY    → ordena
8. LIMIT       → limita resultados
```

> 💡 Por isso WHERE não pode usar funções agregadas — ele é executado ANTES do GROUP BY!

---

## 📊 Resumo das Funções Agregadas

| Função | O que faz | Exemplo |
|--------|-----------|---------|
| `COUNT(*)` | Conta todos os registros | `COUNT(*)` → 4 |
| `COUNT(coluna)` | Conta valores não nulos | `COUNT(valor)` → 4 |
| `COUNT(DISTINCT col)` | Conta valores únicos | `COUNT(DISTINCT id_destino)` → 3 |
| `SUM(coluna)` | Soma os valores | `SUM(valor)` → 8300.00 |
| `AVG(coluna)` | Calcula a média | `AVG(valor)` → 2075.00 |
| `MIN(coluna)` | Menor valor | `MIN(valor)` → 1500.00 |
| `MAX(coluna)` | Maior valor | `MAX(valor)` → 3100.00 |

---

## 📌 Resumo

- ✅ **Funções agregadas** calculam sobre conjuntos de valores
- ✅ **COUNT** conta registros, **SUM** soma, **AVG** calcula média, **MIN/MAX** encontram extremos
- ✅ **GROUP BY** agrupa registros pelo mesmo valor de uma coluna
- ✅ **HAVING** filtra grupos — equivalente ao WHERE para agregações
- ✅ **WHERE** filtra antes do agrupamento, **HAVING** filtra depois
- ✅ A ordem de execução do SQL determina o que pode ser usado em cada cláusula

---

## 🎯 Próximos Passos

- Índices e Performance
- Segurança em Banco de Dados
