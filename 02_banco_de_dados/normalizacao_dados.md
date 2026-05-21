# ============================================================
# Bootcamp TOTVS — Fundamentos de Engenharia de Dados e ML
# Módulo — Normalização de Dados
# Autora: Renata Citelli
# ============================================================

## 📊 Normalização de Dados

### O que é Normalização?

**Normalização** é o processo de organizar as tabelas de um banco de dados para:

- Eliminar **redundância** de dados (informação repetida desnecessariamente)
- Evitar **anomalias** de inserção, atualização e exclusão
- Garantir **integridade** e **consistência** dos dados
- Facilitar a **manutenção** do banco

O processo é dividido em etapas chamadas **Formas Normais (FN)**.

---

## 🔴 Sem Normalização — Problema Inicial

Imagine uma tabela única com tudo misturado:

```
┌────────────┬──────────────┬───────────────────────────┬──────────────────────────────────┬──────────────┐
│ id_usuario │ nome_usuario │ destinos                  │ reservas                         │ telefones    │
├────────────┼──────────────┼───────────────────────────┼──────────────────────────────────┼──────────────┤
│ 1          │ Renata       │ Paris, Roma               │ R001 - 10/01, R002 - 15/02       │ 99999, 88888 │
│ 2          │ Ana Paula    │ Tokyo                     │ R003 - 20/03                     │ 77777        │
└────────────┴──────────────┴───────────────────────────┴──────────────────────────────────┴──────────────┘
```

**Problemas:**
- ❌ Múltiplos valores em uma célula (destinos, reservas, telefones)
- ❌ Difícil de buscar e filtrar
- ❌ Difícil de atualizar sem erros
- ❌ Dados redundantes

---

## 1️⃣ Primeira Forma Normal (1FN)

### Regra:
> Cada célula deve conter **apenas um valor** (valor atômico).  
> Não pode haver grupos repetidos ou múltiplos valores em uma coluna.

### Problema (Antes da 1FN):

```sql
-- ❌ ERRADO: múltiplos valores em uma célula
┌────────────┬──────────────┬───────────────┬──────────────┐
│ id_usuario │ nome_usuario │ destinos      │ telefones    │
├────────────┼──────────────┼───────────────┼──────────────┤
│ 1          │ Renata       │ Paris, Roma   │ 99999, 88888 │
│ 2          │ Ana Paula    │ Tokyo         │ 77777        │
└────────────┴──────────────┴───────────────┴──────────────┘
```

### Solução (Aplicando 1FN):

Separar cada valor em sua própria linha:

```sql
-- ✅ CORRETO: um valor por célula
┌────────────┬──────────────┬──────────┬──────────┐
│ id_usuario │ nome_usuario │ destino  │ telefone │
├────────────┼──────────────┼──────────┼──────────┤
│ 1          │ Renata       │ Paris    │ 99999    │
│ 1          │ Renata       │ Paris    │ 88888    │
│ 1          │ Renata       │ Roma     │ 99999    │
│ 1          │ Renata       │ Roma     │ 88888    │
│ 2          │ Ana Paula    │ Tokyo    │ 77777    │
└────────────┴──────────────┴──────────┴──────────┘
```

### Em SQL:

```sql
CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nome_usuario VARCHAR(100) NOT NULL,
    telefone VARCHAR(15),
    destino VARCHAR(100)
);
```

### ✅ Checklist 1FN:
- ✔ Cada coluna tem um único valor por linha
- ✔ Cada linha é única (tem chave primária)
- ✔ Não há listas ou conjuntos em células

---

## 2️⃣ Segunda Forma Normal (2FN)

### Regra:
> Deve estar na **1FN** +  
> Todos os atributos não-chave devem depender da **chave primária inteira** (sem dependências parciais).

> ⚠️ Só se aplica quando a chave primária é **composta** (formada por mais de uma coluna).

### Problema (Antes da 2FN):

```sql
-- ❌ ERRADO: dependência parcial
-- Chave primária composta: (id_usuario, id_destino)
┌────────────┬─────────────┬──────────────┬───────────────┬────────────────┐
│ id_usuario │ id_destino  │ nome_usuario │ nome_destino  │ data_reserva   │
├────────────┼─────────────┼──────────────┼───────────────┼────────────────┤
│ 1          │ 10          │ Renata       │ Paris         │ 2024-01-10     │
│ 1          │ 20          │ Renata       │ Roma          │ 2024-02-15     │
│ 2          │ 10          │ Ana Paula    │ Paris         │ 2024-03-20     │
└────────────┴─────────────┴──────────────┴───────────────┴────────────────┘
```

**Problema:**
- `nome_usuario` depende só de `id_usuario` (dependência parcial ❌)
- `nome_destino` depende só de `id_destino` (dependência parcial ❌)
- `data_reserva` depende dos dois juntos (dependência total ✅)

### Solução (Aplicando 2FN):

Separar em tabelas independentes:

```sql
-- ✅ Tabela usuarios
CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nome_usuario VARCHAR(100) NOT NULL,
    telefone VARCHAR(15)
);

-- ✅ Tabela destinos
CREATE TABLE destinos (
    id_destino INT PRIMARY KEY AUTO_INCREMENT,
    nome_destino VARCHAR(100) NOT NULL,
    pais VARCHAR(100)
);

-- ✅ Tabela reservas (chave composta — dependência total)
CREATE TABLE reservas (
    id_usuario INT,
    id_destino INT,
    data_reserva DATE NOT NULL,
    PRIMARY KEY (id_usuario, id_destino),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_destino) REFERENCES destinos(id_destino)
);
```

### ✅ Checklist 2FN:
- ✔ Está na 1FN
- ✔ Nenhum atributo não-chave depende parcialmente da chave primária
- ✔ Cada tabela representa uma única entidade

---

## 3️⃣ Terceira Forma Normal (3FN)

### Regra:
> Deve estar na **2FN** +  
> Não pode haver **dependências transitivas** — atributos não-chave não podem depender de outros atributos não-chave.

### Problema (Antes da 3FN):

```sql
-- ❌ ERRADO: dependência transitiva
┌────────────┬──────────────┬──────────┬──────────────────┐
│ id_usuario │ nome_usuario │ id_cidade│ nome_cidade      │
├────────────┼──────────────┼──────────┼──────────────────┤
│ 1          │ Renata       │ 5        │ Campinas         │
│ 2          │ Ana Paula    │ 1        │ São Paulo        │
│ 3          │ Carlos       │ 5        │ Campinas         │
└────────────┴──────────────┴──────────┴──────────────────┘
```

**Problema:**
- `nome_cidade` depende de `id_cidade`, não de `id_usuario`
- `id_cidade` → `nome_cidade` é uma dependência transitiva ❌
- "Campinas" repetido desnecessariamente

### Solução (Aplicando 3FN):

```sql
-- ✅ Tabela cidades separada
CREATE TABLE cidades (
    id_cidade INT PRIMARY KEY AUTO_INCREMENT,
    nome_cidade VARCHAR(100) NOT NULL
);

-- ✅ Tabela usuarios sem dependência transitiva
CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nome_usuario VARCHAR(100) NOT NULL,
    telefone VARCHAR(15),
    id_cidade INT,
    FOREIGN KEY (id_cidade) REFERENCES cidades(id_cidade)
);

-- ✅ Tabela destinos
CREATE TABLE destinos (
    id_destino INT PRIMARY KEY AUTO_INCREMENT,
    nome_destino VARCHAR(100) NOT NULL,
    pais VARCHAR(100)
);

-- ✅ Tabela reservas
CREATE TABLE reservas (
    id_reserva INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    id_destino INT NOT NULL,
    data_reserva DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'pendente',
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_destino) REFERENCES destinos(id_destino)
);
```

### ✅ Checklist 3FN:
- ✔ Está na 2FN
- ✔ Nenhum atributo não-chave depende de outro atributo não-chave
- ✔ Toda dependência é diretamente com a chave primária

---

## 🗺️ Estrutura Final Normalizada

```
usuarios                 reservas               destinos
─────────────────        ────────────────────   ──────────────────
id_usuario (PK)  ←──── id_usuario (FK)         id_destino (PK)
nome_usuario             id_reserva (PK)   ────→ nome_destino
telefone                 id_destino (FK)         pais
id_cidade (FK)           data_reserva
     │                   status
     ↓
cidades
──────────────
id_cidade (PK)
nome_cidade
```

---

## 📊 Comparativo das Formas Normais

| Forma Normal | Regra Principal | Problema Resolvido |
|---|---|---|
| **1FN** | Um valor por célula | Valores múltiplos em uma coluna |
| **2FN** | Sem dependências parciais | Atributo depende só de parte da chave |
| **3FN** | Sem dependências transitivas | Atributo depende de outro não-chave |

---

## ⚖️ Normalização vs Desnormalização

| | Normalização | Desnormalização |
|---|---|---|
| **Objetivo** | Eliminar redundância | Melhorar performance de leitura |
| **Quando usar** | Sistemas transacionais (OLTP) | Sistemas analíticos (OLAP) |
| **Resultado** | Mais tabelas, menos redundância | Menos tabelas, mais redundância |
| **Exemplo** | Sistema de reservas | Dashboard de relatórios |

---

## 📌 Resumo do Módulo

- ✅ **Normalização** organiza tabelas para eliminar redundância
- ✅ **1FN** — um valor por célula, sem grupos repetidos
- ✅ **2FN** — sem dependências parciais da chave primária
- ✅ **3FN** — sem dependências transitivas entre não-chaves
- ✅ Cada forma normal **inclui** as anteriores
- ✅ O resultado é um banco mais **consistente** e **fácil de manter**
- ✅ **Desnormalização** pode ser usada para performance em leituras analíticas

---

## 🎯 Próximos Passos

- Consultas Avançadas (JOINs)
- Funções de Agregação (GROUP BY, HAVING)
- Índices e Performance
- Segurança em Banco de Dados
