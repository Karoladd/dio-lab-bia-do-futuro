# Base de Conhecimento
## Dados Utilizados

O agente **NoMundo** não depende de arquivos locais estáticos. Sua base de conhecimento é **dinâmica**, alimentada em tempo real por buscas na web a cada sessão.

| Fonte | Formato | Utilização no Agente |
|-------|---------|----------------------|
| Reuters, BBC, AP News | HTML / RSS | Notícias internacionais em tempo real |
| G1, Folha de S.Paulo, Agência Brasil | HTML / RSS | Notícias nacionais em tempo real |
| Bloomberg, Financial Times | HTML | Notícias de economia e mercados |
| Al Jazeera, The Guardian | HTML | Perspectivas globais e geopolítica |
| MIT Technology Review | HTML | Notícias de ciência e tecnologia |

> **Por que sem arquivos locais?** O domínio do agente é notícias em tempo real — qualquer base estática estaria desatualizada em horas. A web search tool garante que o conteúdo seja sempre atual.

---

## Adaptações nos Dados

Não há dados mockados ou modificados. O agente trabalha exclusivamente com **conteúdo público e atualizado** obtido via busca em tempo real.

Cada resposta é construída a partir de:

- Títulos e resumos de artigos jornalísticos
- Data e hora de publicação das matérias
- Identificação do veículo de origem
- Categoria inferida pelo conteúdo (Política, Economia, Tecnologia, etc.)

---

## Estratégia de Integração

### Como os dados são carregados?

A cada sessão, o agente executa **buscas ativas** via `web_search tool` com queries estruturadas por categoria e relevância global. Não há pré-carregamento — o conteúdo é buscado sob demanda no momento da solicitação.

```
Fluxo de busca:
1. Usuário solicita notícias
2. Agente dispara múltiplas queries paralelas por categoria
3. Resultados são filtrados por fonte confiável e data
4. Conteúdo é sumarizado e formatado
5. Resposta entregue com fonte e timestamp
```

### Como os dados são usados no prompt?

Os dados coletados pela web search são **injetados dinamicamente no contexto** antes da geração da resposta final. O system prompt define:

- Quais fontes priorizar
- Como estruturar o resumo de cada notícia
- O formato de saída (briefing numerado com fonte)
- A instrução de nunca inventar fatos sem respaldo da busca

---

## Exemplo de Contexto Montado

Abaixo um exemplo de como o agente organiza os dados coletados antes de gerar a resposta:

```
BRIEFING NOMUNDO — 11/03/2026 | 09:45

Resultados da busca:

[1] GEOPOLÍTICA
Título: Cúpula da ONU debate crise humanitária no Oriente Médio
Resumo: Líderes de 40 países se reuniram em Genebra para discutir o
aumento do fluxo de refugiados e o financiamento de ajuda humanitária.
Fonte: Reuters | Publicado há 2 horas

[2] ECONOMIA
Título: Fed mantém juros e sinaliza corte para o segundo semestre
Resumo: O Federal Reserve dos EUA decidiu manter a taxa de juros no
patamar atual, indicando possível redução a partir de julho.
Fonte: Bloomberg | Publicado há 1 hora

[3] TECNOLOGIA
Título: União Europeia aprova nova regulação para IAs generativas
Resumo: O Parlamento Europeu ratificou o AI Act com exigências de
transparência e auditoria para modelos de linguagem de grande escala.
Fonte: The Guardian | Publicado há 3 horas

[4] BRASIL
Título: Banco Central anuncia nova rodada do Pix por aproximação
Resumo: O BC divulgou expansão do sistema de pagamentos instantâneos
com suporte a dispositivos wearables a partir do segundo trimestre.
Fonte: G1 | Publicado há 4 horas

...e mais 6 notícias categorizadas.

---
⚠️ Informações obtidas de fontes públicas. Sujeitas a atualização.
```

---

## Queries de Busca Utilizadas

O agente estrutura suas buscas com queries específicas para garantir cobertura ampla e atual:

| Categoria | Query Exemplo |
|-----------|--------------|
| Geral | `top world news today` |
| Geopolítica | `international politics breaking news` |
| Economia | `global economy markets news today` |
| Brasil | `principais notícias brasil hoje` |
| Tecnologia | `technology science news today` |
| Clima/Meio Ambiente | `climate environment news today` |

---

*Base de Conhecimento v1.0 — Agente NoMundo*
