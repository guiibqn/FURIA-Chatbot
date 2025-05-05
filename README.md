# 🐺 FURIA Chatbot – Desafio Técnico FURIA Tech

🎯 O objetivo foi criar uma **interface conversacional temática voltada aos fãs da FURIA**, oferecendo informações úteis sobre o time de CS em um ambiente interativo com visual gamer.

🔗 Acesse a versão online: [https://furia-chatbot-7jwo.onrender.com](https://furia-chatbot-7jwo.onrender.com)


---

## 💡 Funcionalidades

- 🤖 Interface conversacional simulando um chat com a FURIA
- 🧠 Intents personalizadas para:
  - Próximos jogos
  - Últimos resultados
  - Elenco atual
  - Ranking
  - Torcida
  - Notícias (via RSS Feed)
- 💬 Botões com perguntas rápidas
- 👾 Avatares personalizados e visual gamer

---

## 📸 Captura de Tela

![screenshot](static/Screenshot-furia.png)

---

## 🚀 Como executar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/chatbot-furia.git
cd chatbot-furia
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

Se não houver no `requirements.txt`, instale manualmente:

```bash
pip install flask feedparser
```

### 3. Execute o servidor Flask

```bash
python app.py
```

### 5. Acesse o navegador

Abra: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🛠 Estrutura do Projeto

```
.
├── app.py                 # Lógica principal do backend Flask
├── responses.py          # Intents e respostas personalizadas
├── templates/
│   └── chat.html         # Interface do chat (frontend)
├── static/
│   ├── style-furia.css         # Estilos visuais personalizados
│   └── images/           # Logos, avatars, background
```

---

## 📚 Tecnologias Utilizadas

- Python 3.10
- Flask
- HTML + CSS + JavaScript
- Feedparser (leitura de RSS)
- Design customizado com imagens da FURIA

---

## 🤝 Agradecimentos

Projeto desenvolvido por **Guilherme Augusto Boquimpani**.  
Obrigado pela oportunidade! 👊
