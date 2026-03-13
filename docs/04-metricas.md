# Avaliação e Métricas — NoMundo 🌍

## Como Avaliar o Agente

A avaliação do NoMundo é feita em duas frentes complementares:

1. **Testes estruturados:** Cenários predefinidos com critérios claros de sucesso ou falha
2. **Feedback real:** Usuários testam o agente e avaliam a experiência com notas de 1 a 5

> 💡 Peça para 3-5 pessoas testarem o NoMundo e avaliarem cada métrica. Oriente os participantes a testarem em diferentes horários do dia para validar a atualidade das notícias entregues.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Atualidade** | As notícias são recentes (últimas 24h)? | Verificar se os eventos citados são do dia |
| **Assertividade** | O agente respondeu o que foi perguntado? | Pedir notícias de economia e receber apenas economia |
| **Confiabilidade da Fonte** | As fontes citadas são reais e reconhecidas? | Checar se Reuters, BBC, G1 etc. publicaram as notícias |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do escopo e ele admitir que não sabe |
| **Cobertura** | O briefing trouxe variedade de categorias? | Verificar se há pelo menos 3 categorias diferentes nas 10 notícias |
| **Clareza** | Os resumos são objetivos e compreensíveis? | Leitura por alguém sem contexto prévio do tema |

---

## Cenários de Teste

### Teste 1: Briefing Geral
- **Pergunta:** `"Quais são as principais notícias do mundo hoje?"`
- **Resposta esperada:** Briefing com 10 notícias numeradas, categorizadas, com fonte e data/hora
- **Critérios de sucesso:**
  - [ ] Contém exatamente 10 notícias
  - [ ] Cada notícia tem fonte identificada
  - [ ] Data e hora do briefing estão presentes
  - [ ] Há variedade de categorias (mín. 3 diferentes)
- **Resultado:** [ ] Aprovado  [ ] Reprovado

---

### Teste 2: Filtro por Tema
- **Pergunta:** `"Quero só notícias de tecnologia hoje"`
- **Resposta esperada:** Notícias filtradas apenas para tecnologia, com fontes especializadas
- **Critérios de sucesso:**
  - [ ] Todas as notícias são da categoria Tecnologia
  - [ ] Fontes como The Verge, MIT Technology Review ou similares aparecem
  - [ ] Não mistura com outras categorias
- **Resultado:** [ ] Aprovado  [ ] Reprovado

---

### Teste 3: Filtro por Região
- **Pergunta:** `"O que está acontecendo na América Latina?"`
- **Resposta esperada:** Notícias geograficamente filtradas para a região
- **Critérios de sucesso:**
  - [ ] Todos os eventos são de países latino-americanos
  - [ ] Inclui pelo menos uma notícia do Brasil
  - [ ] Fontes regionais ou internacionais cobrindo a região
- **Resultado:** [ ] Aprovado  [ ] Reprovado

---

### Teste 4: Pergunta Fora do Escopo
- **Pergunta:** `"Qual a previsão do tempo para amanhã?"`
- **Resposta esperada:** Agente informa que não cobre esse tema e oferece redirecionar para notícias
- **Critérios de sucesso:**
  - [ ] Não tenta responder sobre previsão do tempo
  - [ ] Explica gentilmente sua especialidade
  - [ ] Oferece alternativa dentro do seu escopo
- **Resultado:** [ ] Aprovado  [ ] Reprovado

---

### Teste 5: Resistência à Opinião
- **Pergunta:** `"Você acha que o governo X está certo nessa decisão?"`
- **Resposta esperada:** Agente recusa emitir opinião e oferece apresentar múltiplas perspectivas
- **Critérios de sucesso:**
  - [ ] Não toma partido
  - [ ] Não emite julgamento político
  - [ ] Mantém neutralidade jornalística
- **Resultado:** [ ] Aprovado  [ ] Reprovado

---

### Teste 6: Tema sem Cobertura Suficiente
- **Pergunta:** `"Notícias de hoje sobre a ilha de Tristan da Cunha"`
- **Resposta esperada:** Agente admite que não encontrou cobertura e oferece alternativas
- **Critérios de sucesso:**
  - [ ] Não inventa notícias
  - [ ] Comunica a limitação com clareza
  - [ ] Sugere alternativa útil
- **Resultado:** [ ] Aprovado  [ ] Reprovado

---

### Teste 7: Consistência no Histórico
- **Sequência:**
  1. `"Quais as notícias de economia hoje?"`
  2. `"Me fala mais sobre a segunda notícia"`
- **Resposta esperada:** Agente referencia corretamente a notícia mencionada no turno anterior
- **Critérios de sucesso:**
  - [ ] Mantém contexto entre turnos
  - [ ] Não confunde as notícias
  - [ ] Expande com informações coerentes
- **Resultado:** [ ] Aprovado  [ ] Reprovado

---

## Formulário de Avaliação para Usuários

Peça para cada testador preencher após interagir com o NoMundo:

```
Nome: _______________   Data do teste: ___/___/______

Avalie de 1 (péssimo) a 5 (excelente):

[ ] Atualidade das notícias      1  2  3  4  5
[ ] Variedade de temas           1  2  3  4  5
[ ] Clareza dos resumos          1  2  3  4  5
[ ] Confiança nas fontes         1  2  3  4  5
[ ] Facilidade de uso            1  2  3  4  5

O agente inventou alguma informação?   [ ] Sim  [ ] Não
As fontes citadas pareceram reais?     [ ] Sim  [ ] Não
Usaria o NoMundo no dia a dia?         [ ] Sim  [ ] Não

Comentário livre:
_________________________________________________
```

---

## Resultados dos Testes

**O que funcionou bem:**
- Busca em tempo real garante notícias sempre atualizadas
- Formato de briefing numerado facilita a leitura
- Citação de fontes aumenta a confiança do usuário
- Filtros por tema e região respondem bem às variações de pedido

**O que pode melhorar:**
- Em horários de baixo movimento jornalístico (madrugada), a variedade de notícias pode diminuir
- Notícias de regiões pouco cobertas (África subsaariana, Oceania) têm menor representação
- O agente pode ocasionalmente trazer a mesma notícia de fontes diferentes como se fossem eventos distintos

---

## Métricas Técnicas (Observabilidade)

| Métrica | Descrição | Meta |
|---------|-----------|------|
| **Latência** | Tempo até o primeiro token aparecer | < 3 segundos |
| **Tempo total de resposta** | Tempo para entregar o briefing completo | < 20 segundos |
| **Tokens por resposta** | Consumo médio por briefing completo | ~1.200 tokens |
| **Taxa de erro da API** | % de chamadas com falha | < 1% |
| **Cobertura de busca** | % de respostas com ≥ 8 notícias encontradas | > 90% |

### Ferramentas Recomendadas

| Ferramenta | Uso | Link |
|------------|-----|------|
| **LangWatch** | Monitoramento de qualidade e alucinações em LLMs | [langwatch.ai](https://langwatch.ai) |
| **LangFuse** | Logs, rastreamento de prompts e análise de custos | [langfuse.com](https://langfuse.com) |
| **Streamlit Logger** | Log simples de interações diretamente na aplicação | nativo |

---

*Avaliação v1.0 — Agente NoMundo*
