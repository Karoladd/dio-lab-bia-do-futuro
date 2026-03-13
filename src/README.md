# Código da Aplicação — NoMundo 🌍

## Estrutura do Projeto

```
nomundo/
├── app.py              # Interface Streamlit (frontend + chat)
├── agente.py           # Lógica do agente (chamadas à API Anthropic)
├── config.py           # System prompt, configurações e constantes
├── requirements.txt    # Dependências do projeto
└── .env.example        # Modelo do arquivo de variáveis de ambiente
```

---

## Responsabilidade de Cada Arquivo

| Arquivo | Responsabilidade |
|---------|-----------------|
| `app.py` | Interface visual, gerenciamento do histórico de chat e streaming da resposta |
| `agente.py` | Comunicação com a API Anthropic, configuração da web search tool e formatação do histórico |
| `config.py` | System prompt completo, modelo, tokens máximos e mensagem de boas-vindas |
| `requirements.txt` | Dependências necessárias para rodar o projeto |
| `.env.example` | Template para criação do arquivo `.env` com a API key |

---

## Como Rodar

### 1. Clone ou baixe os arquivos

```bash
# Entre na pasta do projeto
cd nomundo
```

### 2. Crie o ambiente virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a API Key

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o .env e insira sua chave da Anthropic
ANTHROPIC_API_KEY=sk-ant-...
```

> Obtenha sua chave em: https://console.anthropic.com

### 5. Rode a aplicação

```bash
streamlit run app.py
```

Acesse no navegador: `http://localhost:8501`

---

## Arquitetura do Código

```
Usuário digita no chat
        ↓
    app.py coleta o input
        ↓
    Adiciona ao histórico de mensagens
        ↓
    agente.py formata o histórico para a API
        ↓
    API Anthropic (Claude Sonnet)
    + Web Search Tool ativa
        ↓
    Claude busca notícias na web em tempo real
        ↓
    Resposta é transmitida via streaming
        ↓
    app.py exibe token a token no chat
        ↓
    Resposta salva no histórico da sessão
```

---

## Dependências

| Pacote | Versão | Uso |
|--------|--------|-----|
| `streamlit` | 1.42.0 | Interface web do chat |
| `anthropic` | 0.49.0 | SDK oficial para a API do Claude |
| `python-dotenv` | 1.0.1 | Carregamento seguro da API key via `.env` |
| `requests` | 2.32.3 | Requisições HTTP auxiliares |

---

## Variáveis de Ambiente

| Variável | Obrigatória | Descrição |
|----------|-------------|-----------|
| `ANTHROPIC_API_KEY` | ✅ Sim | Chave de acesso à API da Anthropic |

---

## Funcionalidades Implementadas

- ✅ Chat com histórico de mensagens na sessão
- ✅ Streaming da resposta token a token
- ✅ Web Search Tool integrada (busca em tempo real)
- ✅ System prompt completo com persona e regras do NoMundo
- ✅ Interface com sidebar de sugestões de perguntas
- ✅ Botão para limpar o histórico da conversa
- ✅ Mensagem de boas-vindas na abertura
- ✅ Design responsivo com tipografia editorial
