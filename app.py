from flask import Flask, render_template, request, jsonify
from responses import detectar_intent, gerar_resposta  # ✅ Importação das funções e dados

from datetime import datetime  

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["GET", "POST"])
def chat():
    user_message = request.get_json()["msg"]
    print(f"[LOG] Mensagem do usuário: {user_message}")

    intent_detectada = detectar_intent(user_message)
    resposta = gerar_resposta(intent_detectada) if intent_detectada else "Desculpe, não entendi 😓. Tente perguntar de outro jeito (ex: 'qual o próximo jogo?')."

    return jsonify({"answer": resposta})

if __name__ == "__main__":
    app.run()
