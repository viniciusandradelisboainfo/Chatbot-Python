import openai

chave_api = #suachave openai

openai.api_key = chave_api

def enviar_mensagem(mensagem, mensagens=None):
    if mensagens is None:
        mensagens = []
    mensagens.append(
        {"role": "user", "content" : mensagem}
        )

    resposta = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = mensagens,
    )

    return resposta["choices"][0]["message"]

mensagens = []
while True:
    texto = input("escreva aqui sua mensagem:")

    if texto == "sair":
        break
    else:
        resposta = enviar_mensagem(texto, mensagens)
        mensagens.append(resposta)
        print ("Chatbot:", resposta["content"])

