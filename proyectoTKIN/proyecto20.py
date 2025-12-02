from openai import OpenAI
import os
import getpass as gp

key=''

cliente = OpenAI(api_key = key)


modelo = 'gpt-4'
prompt = "Necesito un promt en ingles para crear una foto realista en dall-e de un ferrari andando por colombia"

mensajes = [
    {'role':'system', 'content':'Experto en generacion de prompt para ia'},
    {'role':'user', 'content':prompt}
]

respuesta = cliente.chat.completions.create(
    model = modelo,
    messages = mensajes,
    temperature = 1.3,
    max_tokens = 1000
)

print(respuesta.choices[0].message.content)

promptImagen = respuesta.choices[0].message.content

response = cliente.images.generate(
    model="gpt-image-1",
    prompt=promptImagen,
    size="1024x1024"
)

print(response)