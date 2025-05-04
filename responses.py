from datetime import datetime, timedelta
import feedparser

INTENTS = {
    "proximo_jogo": ["quando", "próximo", "jogo", "partida", "confronto"],
    "ultimos_resultados": ["últimos", "resultados", "jogos", "placares"],
    "elenco": ["jogadores", "elenco", "time", "equipe"],
    "torcida": ["torcida", "vamo", "furia", "mensagem", "vai"],
    "ranking": ["ranking", "posição", "colocação", "tabela"],
    "noticias": ["notícias", "novidades", "news", "última"]
}

RESPONSES = {
    "ultimos_resultados": "🏆 Últimos resultados:<br>FURIA 0x2 The MongolZ<br>FURIA 0x2 Virtus.pro<br>FURIA 1x2 Complexity",
    "elenco": "🐾 Jogadores atuais: KSCERATO, yuurih, YEKINDAR, molodoy e FalleN.",
    "torcida": "🔥 VAMOOO FURIAAAA! Vai pra cima! 👊💥",
    "ranking": "📊 A FURIA está atualmente no top 17 do ranking mundial da HLTV."
}

def detectar_intent(texto):
    texto = texto.lower()
    for intent, palavras in INTENTS.items():
        if any(p in texto for p in palavras):
            return intent
    return None

def obter_ultima_noticia_furia():
    try:
        # Feed com notícias de CS:GO (HLTV não tem feed oficial da FURIA, então pegamos geral)
        feed_url = "https://www.hltv.org/rss/news"
        feed = feedparser.parse(feed_url)

        for entry in feed.entries:
            if "FURIA" in entry.title or "FURIA" in entry.summary:
                titulo = entry.title
                link = entry.link
                data_pub = entry.published
                return f"📰 Última notícia sobre a FURIA:<br><strong>{titulo}</strong><br>🗓️ {data_pub}<br>🔗 <a href='{link}' target='_blank'>Ler mais</a>"

        return "🔍 Nenhuma notícia recente sobre a FURIA encontrada no momento."
    except Exception as e:
        print("[ERRO FEED]:", e)
        return "⚠️ Erro ao buscar notícias no momento. Tente novamente mais tarde."

def gerar_resposta(intent):
    if intent == "proximo_jogo":
        # Mock de data para exemplo
        data_jogo = datetime(2025, 5, 10, 5, 0, 0)
        agora = datetime.now()
        if data_jogo > agora:
            diferenca = data_jogo - agora
            dias = diferenca.days
            horas = diferenca.seconds // 3600
            minutos = (diferenca.seconds % 3600) // 60
            return (
                f"📅 O próximo jogo da FURIA será contra a The MongolZ no dia 10/05 às 5h! ⚔️<br>"
                f"⏳ Faltam {dias} dias, {horas} horas e {minutos} minutos!"
            )
        else:
            return "⚔️ O próximo jogo da FURIA contra a The MongolZ já aconteceu."
    
    elif intent == "noticias":
        return obter_ultima_noticia_furia()

    else:
        return RESPONSES.get(intent, "Desculpe, não entendi 😓.")