import anthropic
from config import ANTHROPIC_API_KEY, MODEL, MAX_TOKENS, SYSTEM_PROMPT

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

WEB_SEARCH_TOOL = {
    "type": "web_search_20250305",
    "name": "web_search",
}


def stream_resposta(historico: list):
    """
    Envia o histórico de mensagens ao agente e retorna um
    gerador que faz streaming token a token da resposta final.
    """
    with client.messages.stream(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=SYSTEM_PROMPT,
        tools=[WEB_SEARCH_TOOL],
        messages=historico,
    ) as stream:
        for text in stream.text_stream:
            yield text


def get_resposta(historico: list) -> str:
    """
    Versão sem streaming — retorna a resposta completa.
    Útil para testes e integrações que não suportam streaming.
    """
    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=SYSTEM_PROMPT,
        tools=[WEB_SEARCH_TOOL],
        messages=historico,
    )

    # Extrai apenas os blocos de texto da resposta
    texto = " ".join(
        bloco.text
        for bloco in response.content
        if hasattr(bloco, "text")
    )
    return texto.strip()


def formatar_historico(mensagens: list[dict]) -> list[dict]:
    """
    Converte o formato interno do Streamlit para o formato
    esperado pela API da Anthropic.
    """
    return [
        {"role": m["role"], "content": m["content"]}
        for m in mensagens
    ]
