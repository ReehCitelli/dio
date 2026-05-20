# Módulo 09 — Git e GitHub: Primeiros Passos

**Bootcamp TOTVS — Fundamentos de Engenharia de Dados e ML**  
**Autora:** Renata Citelli

---

## O que é Git?

Git é um sistema de **controle de versões** — ele registra todas as alterações feitas nos arquivos ao longo do tempo, permitindo:

- Voltar a versões anteriores do código
- Trabalhar em equipe sem sobrescrever o trabalho dos outros
- Manter um histórico completo de todas as mudanças
- Criar ramificações (branches) para desenvolver funcionalidades isoladas

---

## O que é GitHub?

GitHub é uma plataforma online que hospeda repositórios Git na nuvem. Com ele é possível:

- Armazenar e compartilhar projetos
- Colaborar com outras pessoas
- Exibir portfólio de projetos públicos
- Integrar com ferramentas de CI/CD e deploy

---

## Configuração inicial

```bash
# Configura nome e e-mail (feito uma vez só)
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"

# Verifica as configurações
git config --list
```

---

## Fluxo básico do Git

```
Área de trabalho  →  Staging Area  →  Repositório Local  →  GitHub
  (edita arquivos)    (git add)        (git commit)          (git push)
```

---

## Comandos essenciais

### Iniciando um repositório

```bash
git init                    # inicia repositório na pasta atual
git clone <url>             # clona repositório existente do GitHub
```

### Verificando o estado

```bash
git status                  # mostra arquivos modificados
git log                     # histórico de commits
git log --oneline           # histórico resumido
```

### Salvando alterações

```bash
git add .                   # adiciona todos os arquivos ao staging
git add arquivo.py          # adiciona um arquivo específico
git commit -m "mensagem"    # salva as alterações com descrição
```

### Enviando para o GitHub

```bash
git push                    # envia commits para o repositório remoto
git push origin main        # envia para a branch main
git pull                    # baixa e integra atualizações do remoto
```

### Trabalhando com branches

```bash
git branch                  # lista branches
git branch nova-feature     # cria nova branch
git checkout nova-feature   # muda para a branch
git checkout -b nova-branch # cria e já muda para a branch
git merge nova-feature      # une a branch na branch atual
```

---

## Boas práticas para mensagens de commit

Use verbos no imperativo e seja descritivo:

```bash
git commit -m "feat: adiciona módulo de dicionários"
git commit -m "fix: corrige cálculo de média"
git commit -m "docs: atualiza README com novos módulos"
git commit -m "refactor: reorganiza estrutura de pastas"
```

| Prefixo    | Uso |
|------------|-----|
| `feat:`    | Nova funcionalidade |
| `fix:`     | Correção de bug |
| `docs:`    | Documentação |
| `refactor:`| Refatoração de código |
| `test:`    | Testes |
| `chore:`   | Tarefas gerais |

---

## Arquivo .gitignore

Arquivo que lista o que o Git deve **ignorar** (não versionar):

```
# Exemplo de .gitignore para Python
__pycache__/
*.pyc
.env
.vscode/
*.log
```

---

## Resumo do que aprendi

- ✅ Git controla versões do código localmente
- ✅ GitHub hospeda repositórios na nuvem
- ✅ `git add` → `git commit` → `git push` é o fluxo básico
- ✅ Branches permitem desenvolver sem afetar o código principal
- ✅ Mensagens de commit descritivas facilitam o histórico
- ✅ `.gitignore` evita versionar arquivos desnecessários