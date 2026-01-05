from openai import OpenAI
import os
import time

client = OpenAI(api_key = "")

preguntas = list()
respuestasGpt = list()
mensajes = list()

contexto = input("Sistema: Escribe un contecto: ")

if contexto == "":
    contexto = "Actua como el mas experimentado de los ingenieros de datos del mundo"

mensajes.append({"role": "system", "content":contexto})

while True:
    preguntaActual = input("Yo: ")
    if preguntaActual.lower() in ['exit', 'quit', 'parar', 'stop', 'salir']:
        print("chatBot: Fue un placer ayudarte!!")
        time.sleep(3)
        break
    if preguntaActual == "":
        continue

    mensajes.append({"role": "user", "content":preguntaActual})
    respuesta = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = mensajes,
    temperature = 0.7,
    max_tokens = 500
    )
    
    respuestaActual = respuesta.choices[0].message.content
    print(f"\nChatBot: {respuestaActual}")
    respuestasGpt.append(respuestaActual)
    mensajes.append({"role": "assistant", "content":respuestaActual})
    print()
    print("*" * 150)
    print()



""" p1 = "¿Como ser un ingenierode datos junior?"
p2 = "¿Como ser un ingenierode datos semi-senior?"
p3 = "¿Como ser un ingenierode datos senior?"

contexto = "Responde como todo un ingeniero de datos experto"

menjase = [
    {"role": "system", "content":contexto},
    {"role":"user", "content":p1}
]

respuesta = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = menjase,
    temperature = 0.7
)

respuesta_chat = respuesta.choices[0].message.content

print(respuesta_chat)
print()
print("*" * 150)
print()

#respuesta 2
menjase = [
    {"role": "system", "content":contexto},
    {"role":"user", "content":p1},
    {"role": "assistant", "content":respuesta_chat},
    {"role":"user", "content":p2}
]

respuesta = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = menjase,
    temperature = 0.7
)

respuesta_chat2 = respuesta.choices[0].message.content

print(respuesta_chat2)
print()
print("*" * 150)
print()

#respuesta3
menjase = [
    {"role": "system", "content":contexto},
    {"role":"user", "content":p1},
    {"role": "assistant", "content":respuesta_chat},
    {"role":"user", "content":p2},
    {"role": "assistant", "content":respuesta_chat2},
    {"role":"user", "content":p3}
]

respuesta = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = menjase,
    temperature = 0.7
)

respuesta_chat3 = respuesta.choices[0].message.content

print(respuesta_chat3)
print()
print("*" * 150)
print() """