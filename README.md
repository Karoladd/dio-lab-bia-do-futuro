# 🌍 NoMundo — Agente Jornalístico com IA Generativa

## Contexto

O acesso à informação de qualidade é um desafio crescente. Com dezenas de portais, redes sociais e notificações disputando atenção, **filtrar o que realmente importa consome tempo demais**.

O **NoMundo** é um agente jornalístico inteligente que utiliza IA Generativa para:

- **Buscar em tempo real** as principais notícias do mundo em fontes confiáveis
- **Resumir e categorizar** os acontecimentos de forma clara e objetiva
- **Personalizar** o briefing por tema ou região conforme o interesse do usuário
- **Garantir confiabilidade** citando sempre a fonte de cada notícia (anti-alucinação)

> 💡 Na pasta [`examples/`](./examples) você encontra referências de implementação para cada etapa deste projeto.

---

## O Que Foi Entregue

### 1. Documentação do Agente

Define **o que** o NoMundo faz e **como** ele funciona:

- **Caso de Uso:** Briefing jornalístico em tempo real com as 10 principais notícias do mundo
- **Persona e Tom de Voz:** Correspondente internacional — neutro, objetivo e confiável
- **Arquitetura:** Fluxo de busca web → sumarização → entrega categorizada com fontes
- **Segurança:** Regras anti-alucinação, citação obrigatória de fontes e recusa de opinião

📄 **Documentação:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

O NoMundo não utiliza arquivos estáticos — sua base de conhecimento é **dinâmica e em tempo real**, alimentada via `web_search tool` a cada sessão.

| Fonte | Tipo | Descrição |
|-------|------|-----------|
| Reuters, BBC, AP News | Web (tempo real) | Notícias internacionais |
| G1, Agência Brasil | Web (tempo real) | Notícias nacionais |
| Bloomberg, Financial Times | Web (tempo real) | Economia e mercados |
| Al Jazeera, The Guardian | Web (tempo real) | Geopolítica e perspectiva global |
| MIT Technology Review | Web (tempo real) | Tecnologia e ciência |

📄 **Documentação:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

Documenta os prompts que definem o comportamento do NoMundo:

- **System Prompt:** Persona jornalística, regras de neutralidade, formato de briefing e fontes prioritárias
- **Few-Shot Examples:** Cenários de uso com entrada e saída esperada embutidos no prompt
- **Edge Cases:** Fora do escopo, pedido de opinião política, tema sem cobertura

📄 **Documentação:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

Protótipo funcional do NoMundo construído com Streamlit + API Anthropic:

```
src/
├── app.py           # Interface Streamlit com chat e streaming
├── agente.py        # Lógica do agente e integração com a API
├── config.py        # System prompt, modelo e configurações
└── requirements.txt # Dependências do projeto
```

**Como rodar:**

```bash
# 1. Instale as dependências
pip install -r requirements.txt

# 2. Configure sua API Key
cp .env.example .env
# Edite o .env com sua ANTHROPIC_API_KEY

# 3. Rode a aplicação
streamlit run app.py
```

📁 **Código:** [`src/`](./src)

---

### 5. Avaliação e Métricas

Descreve como avaliar a qualidade do NoMundo:

**Métricas principais:**

| Métrica | O que avalia |
|---------|--------------|
| Atualidade | As notícias são das últimas 24h? |
| Assertividade | O agente respondeu o que foi perguntado? |
| Confiabilidade da Fonte | As fontes citadas são reconhecidas? |
| Segurança | O agente evitou inventar informações? |
| Cobertura | O briefing trouxe variedade de categorias? |

📄 **Documentação:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

Roteiro completo de apresentação de 3 minutos do NoMundo:

- **Problema:** Excesso de informação → dificuldade de se manter informado
- **Solução:** Correspondente pessoal com IA que entrega o essencial em segundos
- **Demo:** Roteiro cronometrado com os melhores cenários para apresentar
- **Diferencial:** Tempo real + fontes verificáveis + neutralidade jornalística

📄 **Documentação:** [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Ferramentas Utilizadas

| Categoria | Ferramenta |
|-----------|-----------|
| **LLM** | [Claude Sonnet](https://claude.ai/) (Anthropic) |
| **Web Search** | Anthropic Web Search Tool (tempo real) |
| **Interface** | [Streamlit](https://streamlit.io/) |
| **Diagramas** | [Mermaid](https://mermaid.js.org/) |
| **Observabilidade** | [LangWatch](https://langwatch.ai/) / [LangFuse](https://langfuse.com/) |

---

## Estrutura do Repositório

```
📁 dio-lab-bia-do-futuro/
│
├── 📄 README.md
│
├── 📁 docs/                        # Documentação completa do projeto
│   ├── 01-documentacao-agente.md   # Caso de uso, persona e arquitetura
│   ├── 02-base-conhecimento.md     # Estratégia de dados em tempo real
│   ├── 03-prompts.md               # System prompt e exemplos de interação
│   ├── 04-metricas.md              # Avaliação, testes e métricas técnicas
│   └── 05-pitch.md                 # Roteiro do pitch de 3 minutos
│
├── 📁 src/                         # Código da aplicação
│   ├── app.py                      # Interface Streamlit
│   ├── agente.py                   # Lógica do agente
│   ├── config.py                   # Configurações e system prompt
│   ├── requirements.txt            # Dependências
│   └── .env.example                # Template de variáveis de ambiente
│
├── 📁 assets/                      # Imagens e diagramas
│
└── 📁 examples/                    # Referências e exemplos
```

---

## Dicas Finais

1. **O system prompt é tudo:** A persona jornalística e as regras anti-alucinação nascem dele
2. **Web search em tempo real:** Nenhum arquivo local — a internet é a base de conhecimento
3. **Cite sempre a fonte:** No jornalismo, credibilidade é inegociável
4. **Teste edge cases:** Pedidos de opinião política e temas fora do escopo revelam fragilidades
5. **Neutralidade é um diferencial:** Sem algoritmo de engajamento, sem bolha de opinião

---

## Sobre o Projeto

Desenvolvido como parte do desafio **BIA do Futuro** da [DIO](https://www.dio.me/) — laboratório de criação de agentes inteligentes com IA Generativa.
