import streamlit as st
from agente import stream_resposta, formatar_historico
from config import WELCOME_MESSAGE

# ── Configuração da página ────────────────────────────────────────────────────
st.set_page_config(
    page_title="NoMundo — Notícias em Tempo Real",
    page_icon="🌍",
    layout="centered",
)

# ── CSS personalizado ─────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .nomundo-header {
        text-align: center;
        padding: 1.5rem 0 0.5rem;
    }

    .nomundo-header h1 {
        font-family: 'Playfair Display', serif;
        font-size: 2.8rem;
        color: #1a1a2e;
        margin: 0;
        letter-spacing: -1px;
    }

    .nomundo-header p {
        color: #666;
        font-size: 0.95rem;
        margin-top: 0.25rem;
    }

    .stChatMessage {
        border-radius: 12px;
    }

    .badge {
        display: inline-block;
        background: #e8f4fd;
        color: #1a6fb5;
        font-size: 0.75rem;
        font-weight: 500;
        padding: 2px 10px;
        border-radius: 20px;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="nomundo-header">
    <h1>🌍 NoMundo</h1>
    <p>Seu correspondente de notícias globais em tempo real</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── Estado da sessão ──────────────────────────────────────────────────────────
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []
    st.session_state.iniciado = False

# ── Mensagem de boas-vindas (exibida apenas uma vez) ──────────────────────────
if not st.session_state.iniciado:
    with st.chat_message("assistant"):
        st.markdown(WELCOME_MESSAGE)
    st.session_state.iniciado = True

# ── Histórico de mensagens ────────────────────────────────────────────────────
for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ── Input do usuário ──────────────────────────────────────────────────────────
if prompt := st.chat_input("O que está acontecendo no mundo?"):

    # Salva e exibe a mensagem do usuário
    st.session_state.mensagens.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Exibe resposta com streaming
    with st.chat_message("assistant"):
        historico = formatar_historico(st.session_state.mensagens)

        with st.spinner("🔍 Buscando notícias..."):
            resposta_completa = st.write_stream(stream_resposta(historico))

    # Salva a resposta no histórico
    st.session_state.mensagens.append({
        "role": "assistant",
        "content": resposta_completa,
    })

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 📰 NoMundo")
    st.markdown("Notícias em tempo real direto das maiores agências do mundo.")
    st.divider()

    st.markdown("**Sugestões de perguntas:**")
    sugestoes = [
        "📋 Briefing completo de hoje",
        "💰 Economia global agora",
        "🇧🇷 Notícias do Brasil",
        "🌏 O que acontece na Ásia?",
        "🔬 Novidades em tecnologia",
        "🌱 Notícias sobre o clima",
    ]
    for s in sugestoes:
        st.markdown(f"- {s}")

    st.divider()

    if st.button("🗑️ Limpar conversa", use_container_width=True):
        st.session_state.mensagens = []
        st.rerun()

    st.caption("Powered by Claude + Anthropic Web Search")
