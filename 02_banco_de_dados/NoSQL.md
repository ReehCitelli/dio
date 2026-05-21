# ============================================================
# Bootcamp TOTVS — Fundamentos de Engenharia de Dados e ML
# Módulo — Banco de Dados NoSQL
# Autora: Renata Citelli
# ============================================================

# 🌌 Introdução aos Bancos de Dados Não Relacionais (NoSQL)

## 📚 O que é NoSQL?

**NoSQL** significa **"Not Only SQL"** — não apenas SQL.

Os bancos NoSQL surgiram para resolver problemas que bancos relacionais tradicionais tinham dificuldade em lidar, principalmente:

- Grande volume de dados
- Escalabilidade
- Flexibilidade
- Alta performance
- Aplicações distribuídas

---

## 🧠 SQL vs NoSQL

| SQL (Relacional) | NoSQL (Não Relacional) |
|---|---|
| Estrutura fixa | Estrutura flexível |
| Usa tabelas | Usa documentos, grafos, chave-valor etc |
| Relacionamentos fortes | Relacionamentos flexíveis |
| Escalabilidade vertical | Escalabilidade horizontal |
| Schema rígido | Schema dinâmico |
| Ideal para transações | Ideal para grandes volumes |

---

## 🗂️ Características do NoSQL

### ✔ Flexibilidade
Os dados não precisam seguir uma estrutura fixa.

```json
{ "nome": "Renata", "idade": 28 }
{ "nome": "Miguel", "cidade": "São Paulo" }
```

### ✔ Escalabilidade Horizontal
Permite distribuir dados entre vários servidores, melhorando performance, disponibilidade e processamento.

### ✔ Alta Performance
Otimizado para leitura e escrita rápidas, ideal para aplicações em tempo real.

### ✔ Alta Disponibilidade
Dados replicados entre servidores para evitar falhas.

---

## 🧩 Tipos de Bancos NoSQL

### 1️⃣ Chave-Valor (Key-Value)

Armazena pares `chave → valor`. Muito rápido e simples.

```
"user:1" → "Renata"
```

**Usos:** cache, sessões, autenticação
**Exemplos:** Redis, DynamoDB

---

### 2️⃣ Documento (Document Database)

Armazena dados em documentos JSON/BSON.

```json
{
  "nome": "Renata",
  "idade": 28,
  "habilidades": ["Python", "SQL"]
}
```

**Vantagens:** flexível, fácil de escalar, ótimo para APIs
**Exemplos:** MongoDB, CouchDB

---

### 3️⃣ Colunar (Column Family)

Organiza dados em colunas ao invés de linhas. Ideal para Big Data e analytics.

**Exemplos:** Cassandra, HBase

---

### 4️⃣ Grafos (Graph Database)

Focado em relacionamentos complexos como redes sociais, sistemas de recomendação e mapas.

**Exemplos:** Neo4j, ArangoDB

---

## 🍃 MongoDB

### O que é?

MongoDB é um banco NoSQL orientado a documentos que armazena dados em **BSON** (Binary JSON).

### Estrutura

| SQL | MongoDB |
|-----|---------|
| Banco de Dados | Database |
| Tabela | Collection |
| Linha | Documento |
| Coluna | Campo |

### Exemplo de Documento

```json
{
  "nome": "Renata",
  "idade": 28,
  "cidade": "São Paulo"
}
```

---

### ☁️ MongoDB Atlas

Versão em nuvem do MongoDB. Permite criar clusters, acessar pela internet e armazenar bancos na cloud.

---

### 🧠 Modelagem de Dados

#### Embedded Documents
Dados relacionados ficam no mesmo documento — consultas mais rápidas.

```json
{
  "cliente": "Renata",
  "endereco": {
    "cidade": "São Paulo",
    "estado": "SP"
  }
}
```

#### Referências
Documentos separados se relacionam por IDs — melhor para dados compartilhados.

```json
{ "id_cliente": 1 }
```

#### Exemplo com dados aninhados

```json
{
  "cliente": "Renata",
  "pedidos": [
    { "produto": "Notebook", "valor": 3500 },
    { "produto": "Mouse", "valor": 150 }
  ]
}
```

---

### 🔧 Operações no MongoDB

#### INSERT — Inserir documento

```javascript
db.clientes.insertOne({
  nome: "Renata",
  idade: 28
})
```

#### FIND — Consultar documentos

```javascript
// Todos os documentos
db.clientes.find()

// Com filtro
db.clientes.find({ nome: "Renata" })

// Com condição
db.clientes.find({ idade: { $gt: 18 } })
```

**Operadores de comparação:**

| Operador | Significado |
|----------|-------------|
| `$gt` | maior que |
| `$lt` | menor que |
| `$gte` | maior ou igual |
| `$lte` | menor ou igual |

#### UPDATE — Atualizar documento

```javascript
db.clientes.updateOne(
  { nome: "Renata" },
  { $set: { idade: 29 } }
)
```

#### DELETE — Remover documento

```javascript
db.clientes.deleteOne({ nome: "Renata" })
```

---

## 🔴 Redis

### O que é?

Redis é um banco NoSQL do tipo **Chave-Valor**, extremamente rápido por trabalhar em **memória RAM**.

### Principais usos

- Cache
- Sessões
- Filas
- Ranking
- Tempo real

### Exemplo

```
"usuario:1" → "Renata"
```

### Vantagens

- Altíssima velocidade
- Baixo tempo de resposta
- Simples de usar
- Ótimo para aplicações em tempo real

---

## 📌 Quando usar SQL vs NoSQL?

| Situação | Melhor escolha |
|----------|----------------|
| Relacionamentos complexos | SQL |
| Grande volume de dados | NoSQL |
| Estrutura rígida | SQL |
| Dados flexíveis | NoSQL |
| Transações financeiras | SQL |
| Escalabilidade massiva | NoSQL |

---

## 📌 Resumo

- ✅ **NoSQL** = "Not Only SQL" — estrutura flexível e escalável
- ✅ **MongoDB** usa documentos JSON/BSON organizados em collections
- ✅ **Redis** é chave-valor e extremamente rápido (memória RAM)
- ✅ **Embedded Documents** — dados juntos para consultas rápidas
- ✅ **Referências** — documentos separados relacionados por ID
- ✅ NoSQL é ideal para Big Data e aplicações distribuídas
- ✅ Redis é muito usado para cache e sessões
- ✅ NoSQL prioriza performance e escalabilidade

---

## 🎯 Próximos Passos

- Aggregation Framework no MongoDB
- Índices e Performance
- Replicação e Sharding
- Integração Python + MongoDB
- Engenharia de Dados com NoSQL
