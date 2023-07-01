#Librerias usadas para la ejecucion del bot
import discord
from discord import app_commands
from discord.ext import commands
import openai
import random
import asyncio

#Librerias usadas para la ejecucion del bot
import discord
import discord.embeds

import random
import requests
import asyncio
import json

# Configura tu token de API de OpenAI y de discord
OPENAI_API_KEY = "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"
DISCORD_TOKEN = "MTEyMzY2NzQ1NzUzODgwNTg1MA.GYcu2z.uzU7hejC_Ze9g9cylP-OeIc94isrx7ACdb9K5A"

openai.api_key = OPENAI_API_KEY

# Crea el cliente con los intents definidos
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# prompt de traducción para un lenguaje mas normal
translation_prompt = "You're a direct, concrete, no pleasantries professional translator. You wait for the user to ask you to translate from one language to the other. You respect slang and local cultural words and phrases and translate to the appropiate cultural context in the other language. You have to present always the message in spanish, an you don't have to explain al the local slangs, just write the slangs in the message if is necessary"
#------------------------------------------------------------------------------------------------
@bot.event
async def on_ready():
    print("Bot is Up and Ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
#-----------------------------------------------------------------------------------------------
#Comandos que presentan todos los comandos disponibles en el bot
#---------------------Listo---------------------
@bot.tree.command(name="info", description="Obten informacion sobre los contenidos a aprender")
async def info(ctx):
    embed = discord.Embed(title="Temas a aprender")
    embed.add_field(name="Estos son los temas que tengo para que aprendas Python:",value=".............................................................................................................................................", inline=False)
    embed.add_field(name="Usa estos comandos para obtener mas información de las clase de cada tema",  value=" ", inline=False)
    embed.add_field(name="/configuracion_del_entorno", value="Visualiza los comandos para las clases de este tema", inline=False)
    embed.add_field(name="/fundamentos_de_programacion", value="Visualiza los comandos para las clases de este tema", inline=False)
    embed.add_field(name="/trabajando_con_modulos", value="Visualiza los comandos para las clases de este tema", inline=False)
    embed.add_field(name="/bibliotecas_y_desarrollo", value="Visualiza los comandos para las clases de este tema", inline=False)
    embed.add_field(name="/proyecto_y_evaluacion_final", value="Visualiza los comandos para las clases de este tema", inline=False)
    await ctx.response.send_message(embed=embed)

@bot.tree.command(name="configuracion_del_entorno", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def configuracion_del_entorno(ctx):
    embed = discord.Embed(title="Configuracion del entorno", description="Preparate para iniciar en Python!!!")
    embed.add_field(name="Estas son las clases que tengo del primer tema configuracion del entorno:",value=".............................................................................................................................................", inline=False)
    embed.add_field(name="Usa estos comandos para obtener acceder a la clase",  value=" ",inline=False)
    embed.add_field(name="/que_es_la_programacion", value="Descubre qué es la programación, su historia y cómo ha evolucionado para convertirse en una habilidad esencial en el mundo moderno.", inline=False)
    embed.add_field(name="/introduccion_a_python", value="Conoce Python, un lenguaje de programación popular y versátil. Aprende por qué es una excelente opción para principiantes y profesionales por igual.", inline=False)
    embed.add_field(name="/instalacion_de_python", value="Aprende cómo instalar Python en tu computadora y prepárate para escribir tu primer programa.", inline=False)
    embed.add_field(name="/configuracion_de_variables", value="Configura las variables de entorno para Python y entiende por qué son importantes para ejecutar tus programas.", inline=False)
    embed.add_field(name="/uso_de_pip", value="Familiarízate con pip, la herramienta que te permitirá instalar y administrar librerías adicionales en Python.", inline=False)
    embed.add_field(name="/instalacion_de_librerias_comunes", value="Aprende a instalar librerías comunes y útiles en Python, como numpy y pandas, para mejorar tus capacidades de programación.", inline=False)
    embed.add_field(name="/instalacion_de_node_js", value="Descubre cómo instalar Node.js, una plataforma para ejecutar código JavaScript fuera del navegador.", inline=False)
    embed.add_field(name="/instalacion_y_uso_de_npm", value="Aprende a instalar y utilizar npm, el manejador de paquetes de Node.js, que te permitirá instalar librerías y herramientas para JavaScript.", inline=False)
    embed.add_field(name="/instalacion_de_vs_code", value="Configura tu entorno de desarrollo con Visual Studio Code, un editor de código versátil y poderoso que te ayudará a escribir y organizar tu código de manera eficiente.", inline=False)
    embed.add_field(name="/examen_configuracion_del_entorno", value="Pon a prueba tus conocimientossobre la configuración del entorno de desarrollo con este examen que cubre todos los temas que hemos aprendido.", inline=False)
    await ctx.response.send_message(embed=embed)


@bot.tree.command(name="fundamentos_de_programacion", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def fundamentos_de_programacion(ctx):
    embed = discord.Embed(title="Temas a aprender", description="Estoy listo para la acción!!!")
    embed.add_field(name="Estos son los temas que tengo para que aprendas Python:",value=".............................................................................................................................................", inline=False)
    embed.add_field(name="Usa estos comandos para obtener mas información de las clase de cada tema",  value=" ",inline=False)
    embed.add_field(name="/tipos_de_datos_y_variables", value="Aprende sobre los diferentes tipos de datos en Python, como números y cadenas, y cómo almacenarlos en variables.", inline=False)
    embed.add_field(name="/estructuras_de_datos", value="Descubre las estructuras de datos en Python, como listas y diccionarios, y cómo pueden ayudarte a organizar y manipular información de manera eficiente.", inline=False)
    embed.add_field(name="/declaraciones_if_else_elif", value="Domina el uso de declaraciones condicionales como if, else y elif para controlar el flujo de tus programas en Python.", inline=False)
    embed.add_field(name="/bucles_for_y_while", value="Aprende cómo usar bucles for y while en Python para repetir acciones y procesar colecciones de datos.", inline=False)
    embed.add_field(name="/definicion_de_funciones", value="Descubre cómo definir tus propias funciones en Python para crear código reutilizable y bien organizado.", inline=False)
    embed.add_field(name="/parametros_y_argumentos", value="Aprende sobre parámetros y argumentos en Python, y cómo usarlos para pasar información a tus funciones.", inline=False)
    embed.add_field(name="/funciones_incorporadas", value="Explora las funciones incorporadas en Python que puedes usar para realizar tareas comunes sin tener que escribir código adicional.", inline=False)
    embed.add_field(name="/proyecto_del_bloque_2", value="Aplica lo que has aprendido en un proyecto práctico que te ayudará a consolidar tus habilidades en Python.", inline=False)
    embed.add_field(name="/examen_del_bloque_2", value="Evalúa tu comprensión de los conceptos aprendidos en este bloque con un examen desafiante.", inline=False)
    await ctx.response.send_message(embed=embed)


@bot.tree.command(name="trabajando_con_modulos", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def trabajando_con_modulos(ctx):
    embed = discord.Embed(title="Temas a aprender", description="Estoy listo para la acción!!!")
    embed.add_field(name="Estos son los temas que tengo para que aprendas Python:",value=".............................................................................................................................................", inline=False)
    embed.add_field(name="Usa estos comandos para obtener mas información de las clase de cada tema",  value=" ", inline=False)
    embed.add_field(name="/importacion_de_modulos", value="Aprende a importar módulos en Python para reutilizar código y acceder a funciones adicionales.", inline=False)
    embed.add_field(name="/uso_de_modulos_incorporados", value="Explora los módulos incorporados en Python que te permiten realizar tareas comunes de manera eficiente sin tener que escribir código adicional.", inline=False)
    embed.add_field(name="/creacion_de_paquetes", value="Aprende cómo crear paquetes en Python para organizar y estructurar tu código de manera efectiva.", inline=False)
    embed.add_field(name="/importacion_de_paquetes", value="Descubre cómo importar paquetes en Python y cómo pueden ayudarte a estructurar tus proyectos de manera más eficiente.", inline=False)
    embed.add_field(name="/manejo_de_errores_try_except", value="Domina el manejo de errores en Python utilizando bloques try y except para prevenir que tu programa se caiga debido a errores inesperados.", inline=False)
    embed.add_field(name="/excepciones_personalizadas", value="Aprende a crear excepciones personalizadas en Python para manejar situaciones específicas en tu código.", inline=False)
    embed.add_field(name="/leer_archivos_de_texto", value="Aprende cómo leer archivos de texto en Python, una habilidad fundamental para trabajar con datos y archivos en tus proyectos.", inline=False)
    embed.add_field(name="/escribir_en_archivos_de_texto", value="Descubre cómo escribir en archivos de texto utilizando Python, permitiéndote almacenar información y datos de manera persistente.", inline=False)
    embed.add_field(name="/proyecto_del_bloque_3", value="plica los conceptos aprendidos en un proyecto práctico. Este proyecto te ayudará a consolidar tus habilidades en Python y entender cómo aplicarlas en situaciones reales.", inline=False)
    embed.add_field(name="/examen_del_bloque_3", value="Evalúa tu comprensión de los conceptos aprendidos en este bloque con un examen desafiante.", inline=False)
    await ctx.response.send_message(embed=embed)

@bot.tree.command(name="bibliotecas_y_desarrollo", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def bibliotecas_y_desarrollo(ctx):
    embed = discord.Embed(title="Temas a aprender", description="Estoy listo para la acción!!!")
    embed.add_field(name="Estos son los temas que tengo para que aprendas Python:",value=".............................................................................................................................................", inline=False)
    embed.add_field(name="Usa estos comandos para obtener mas información de las clase de cada tema",  value=" ", inline=False)
    embed.add_field(name="/introduccion_a_numpy", value="Descubre NumPy, una librería esencial para la computación científica en Python que facilita el trabajo con arreglos de datos.", inline=False)
    embed.add_field(name="/creacion_y_uso_de_arrays", value="Aprende cómo crear y manipular arreglos con NumPy, una habilidad fundamental para el análisis de datos y la ciencia en Python.", inline=False)
    embed.add_field(name="/introduccion_a_pandas", value="Explora Pandas, una poderosa librería de Python para el análisis de datos que permite trabajar con estructuras de datos tabulares de manera eficiente.", inline=False)
    embed.add_field(name="/trabajo_con_data_frames", value="Domina los DataFrames en Pandas, que son estructuras de datos bidimensionales, y aprende cómo manipularlos para analizar datos de manera efectiva.", inline=False)
    embed.add_field(name="/libreria_de_openai", value="Conoce la librería de OpenAI y cómo puedes utilizarla para interactuar con modelos de inteligencia artificial potentes y versátiles.", inline=False)
    embed.add_field(name="/programa_con_la_api_de_openai", value="Aprende a programar con la API de OpenAI y cómo puedes utilizarla para incorporar capacidades de IA en tus propias aplicaciones y proyectos.", inline=False)
    embed.add_field(name="/proyecto_del_bloque_4", value="Pon en práctica lo que has aprendido en este bloque a través de un proyecto. Este proyecto te ayudará a aplicar conceptos prácticos y consolidar tu conocimiento.", inline=False)
    embed.add_field(name="/examen_del_bloque_4", value="Evalúa tu comprensión de los conceptos aprendidos en este bloque a través de un examen desafiante.", inline=False)
    await ctx.response.send_message(embed=embed)

@bot.tree.command(name="proyecto_y_evaluacion_final", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def proyecto_y_evaluacion_final(ctx):
    embed = discord.Embed(title="Temas a aprender", description="Estoy listo para la acción!!!")
    embed.add_field(name="Estos son los temas que tengo para que aprendas Python:",value=".............................................................................................................................................", inline=False)
    embed.add_field(name="Usa estos comandos para obtener mas información de las clase de cada tema",  value=" ", inline=False)
    embed.add_field(name="/proyecto_final", value="Demuestra tus habilidades y conocimientos adquiridos en Python a través de un proyecto final integral que englobe todos los conceptos aprendidos durante el curso.", inline=False)
    embed.add_field(name="/examen_final", value="Evalúa tu dominio de Python y los conceptos de programación abordados en el curso con un examen final completo. Es hora de poner a prueba todo lo que has aprendido.", inline=False)
    
    await ctx.response.send_message(embed=embed)



@bot.tree.command(name="que_es_la_programacion", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def que_es_la_programacion(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Explain what programming is in a simple and friendly way for beginners."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )
    
    # Enviar la respuesta real una vez que esté disponible
    await ctx.followup.send(f"**¿Qué es la programación?** \n{response['choices'][0]['message']['content']}")


@bot.tree.command(name="introduccion_a_python", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def introduccion_a_python(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Introduce Python as a programming language and explain why it is popular among beginners and professionals."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )
    
    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Introducción a Python**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje

@bot.tree.command(name="instalacion_de_python", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def instalacion_de_python(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Guide a user through installing Python on their computer in an easy-to-understand manner."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )
    
    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Instalación a Python**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje

@bot.tree.command(name="configuracion_de_variables", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def configuracion_de_variables(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Explain the importance of setting environment variables for Python and guide through the configuration process."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )
    
    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Configuración de variables de entorno**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje

@bot.tree.command(name="uso_de_pip", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def uso_de_pip(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Introduce pip as a tool for managing Python libraries, and explain how to use it in simple terms."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )
    
    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Uso de pip para instalar librerias**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje

@bot.tree.command(name="instalacion_de_librerias_comunes", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def instalacion_de_librerias_comunes(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Explain the importance of Python libraries like numpy and pandas, and guide the user on how to install them using pip."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )
    
    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Instalacion de librerias comunes (numpy,pandas)**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje

@bot.tree.command(name="instalacion_de_node_js", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def instalacion_de_node_js(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Explain what Node.js is and guide the user through the installation process in a beginner-friendly way."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )
    
    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Instalación de Node.js**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje
        
@bot.tree.command(name="instalacion_y_uso_de_npm", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def instalacion_y_uso_de_npm(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Introduce npm as Node.js's package manager and explain how to install and use it in simple terms."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )
    
    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Instalación y uso de npm**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje

@bot.tree.command(name="instalacion_de_vs_code", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def instalacion_de_vs_code(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Introduce Visual Studio Code as a code editor and guide the user through the installation and basic setup for Python development."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )
    
    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Instalación de VSCode y configuracion basica**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje

#Examen bloque 1
with open('trivia1.txt', 'r', encoding='utf-8') as f:#se añadio la codificación utf-8 para que interprete de forma correcta los caracteres del lenguaje español
    lines = f.readlines()

trivias = []
for line in lines:
    parts = line.strip().split(';')
    question = parts[0]
    answers = parts[1:]
    correct = answers.index([a for a in answers if a.endswith('*')][0])
    answers = [a.replace('*', '') for a in answers]
    trivias.append({'question': question, 'answers': answers, 'correct': correct})


@bot.tree.command(name="examen_configuracion_del_entorno", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def start_examen_configuracion_del_entorno(ctx):
    score = 0
    for _ in range(10):
        trivia = random.choice(trivias)
        print(f"{trivia['correct']}")  # check
        question_message = f"Pregunta: {trivia['question']}\nOpciones:\n"
        for i, answer in enumerate(trivia['answers']):
            question_message += f"{i + 1}. {answer}\n"
        
        # Use follow-up messages for sending questions
        if _ == 0:
            # For the first message, use ctx.response.send_message
            await ctx.response.send_message(question_message)
        else:
            # For subsequent messages, use follow-up messages
            await ctx.followup.send(content=question_message)
        
        def check(m):
            return m.author.id == ctx.user.id and m.content.isdigit() and int(m.content) in range(1, len(trivia['answers']) + 1)

        try:
            answer = await bot.wait_for('message', check=check, timeout=30.0)
        except asyncio.TimeoutError:
            embed = discord.Embed(title="Ni modo :(", description="Lo siento, se acabó el tiempo!", color=0x00ff00)
            await ctx.followup.send(embed=embed)
        else:
            if int(answer.content) == trivia['correct'] + 1:
                embed = discord.Embed(title="Asi se hace!", description="¡Bien hecho! La respuesta es correcta")
                score += 1
                await ctx.followup.send(embed=embed)
            else:
                embed = discord.Embed(title="Lo siento :(", description="Parece que tendrás que estudiar un poco más. Respuesta incorrecta!")
                await ctx.followup.send(embed=embed)

    # Send final score
    final_message = f"¡Examen completado! Tu puntuación final es: {score} / 10"
    await ctx.followup.send(content=final_message)




#-----------------------------------Comandos segundo tema------------------------------------
@bot.tree.command(name="tipos_de_datos_y_variables", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def tipos_de_datos_y_variables(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Explain the different types of data in Python, such as numbers and strings, and how to store them in variables in a beginner-friendly way."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )

    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Tipos de Datos y Variables**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje


@bot.tree.command(name="estructuras_de_datos", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def estructuras_de_datos(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Introduce data structures in Python, such as lists and dictionaries, and explain how they are used to organize and manipulate data in simple terms."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )

    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Estructuras de Datos**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje


@bot.tree.command(name="declaraciones_if_else_elif", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def declaraciones_if_else_elif(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Explain how to use conditional statements like if, else, and elif in Python to control the flow of a program in an easy-to-understand manner."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )

    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Declaraciones if, elif, else**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje


@bot.tree.command(name="bucles_for_y_while", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def bucles_for_y_while(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Introduce for and while loops in Python and explain how they can be used to repeat actions and process collections of data in simple terms."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )

    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Bucles for y while**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje


@bot.tree.command(name="definicion_de_funciones", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def definicion_de_funciones(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Explain how to define custom functions in Python and why they are important for creating reusable and well-organized code."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )
    
    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Definición de funciones**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje


@bot.tree.command(name="parametros_y_argumentos", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def parametros_y_argumentos(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Introduce parameters and arguments in Python functions and explain how to use them to pass information to functions in a user-friendly way."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )

    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Parámetros y argumentos**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje


@bot.tree.command(name="funciones_incorporadas", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def funciones_incorporadas(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Introduce built-in functions in Python and explain how they can be used to perform common tasks without writing extra code."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )

    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Funciones incorporadas**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje


#-----------------------------------------------------
#Verificar
#-----------------------------------------------------
@bot.tree.command(name="proyecto_del_bloque_2", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def proyecto_del_bloque_2(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Explain what programming is in a simple and friendly way for beginners."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )
    
    # Enviar la respuesta real una vez que esté disponible
    await ctx.followup.send(f"**Proyecto del bloque 2** \n{response['choices'][0]['message']['content']}")

#-----------------------------------------------------
#Verificar
#-----------------------------------------------------
with open('trivia2.txt', 'r', encoding='utf-8') as f:#se añadio la codificación utf-8 para que interprete de forma correcta los caracteres del lenguaje español
    lines = f.readlines()

trivias2 = []
for line in lines:
    parts = line.strip().split(';')
    question = parts[0]
    answers = parts[1:]
    correct = answers.index([a for a in answers if a.endswith('*')][0])
    answers = [a.replace('*', '') for a in answers]
    trivias2.append({'question': question, 'answers': answers, 'correct': correct})


@bot.tree.command(name="examen_del_bloque_2", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def examen_del_bloque_2(ctx):
    score = 0
    for _ in range(10):
        trivia = random.choice(trivias2)
        print(f"{trivia['correct']}")  # check
        question_message = f"Pregunta: {trivia['question']}\nOpciones:\n"
        for i, answer in enumerate(trivia['answers']):
            question_message += f"{i + 1}. {answer}\n"
        
        # Use follow-up messages for sending questions
        if _ == 0:
            # For the first message, use ctx.response.send_message
            await ctx.response.send_message(question_message)
        else:
            # For subsequent messages, use follow-up messages
            await ctx.followup.send(content=question_message)
        
        def check(m):
            return m.author.id == ctx.user.id and m.content.isdigit() and int(m.content) in range(1, len(trivia['answers']) + 1)

        try:
            answer = await bot.wait_for('message', check=check, timeout=30.0)
        except asyncio.TimeoutError:
            embed = discord.Embed(title="Ni modo :(", description="Lo siento, se acabó el tiempo!", color=0x00ff00)
            await ctx.followup.send(embed=embed)
        else:
            if int(answer.content) == trivia['correct'] + 1:
                embed = discord.Embed(title="Asi se hace!", description="¡Bien hecho! La respuesta es correcta")
                score += 1
                await ctx.followup.send(embed=embed)
            else:
                embed = discord.Embed(title="Lo siento :(", description="Parece que tendrás que estudiar un poco más. Respuesta incorrecta!")
                await ctx.followup.send(embed=embed)

    # Send final score
    final_message = f"¡Examen completado! Tu puntuación final es: {score} / 10"
    await ctx.followup.send(content=final_message)

 



#------------------------------------Comandos tercer tema------------------------------------
@bot.tree.command(name="importacion_de_modulos", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def importacion_de_modulos(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Explain how to import modules in Python and why it's useful in a simple and beginner-friendly way."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )
    
    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Importación de módulos**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje
    

@bot.tree.command(name="uso_de_modulos_incorporados", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def uso_de_modulos_incorporados(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Introduce built-in modules in Python and explain how they can be used to perform common tasks efficiently."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )

    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Uso de módulos incorporados**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje

    
@bot.tree.command(name="creacion_de_paquetes", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def creacion_de_paquetes(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Explain how to create packages in Python and why they are important for organizing and structuring code effectively."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )

    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Creación de paquetes**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje

    
@bot.tree.command(name="importacion_de_paquetes", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def importacion_de_paquetes(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Explain the process of importing packages in Python and how it helps in structuring projects more efficiently."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )

    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Importación de paquetes**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje


@bot.tree.command(name="manejo_de_errores_try_except", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def manejo_de_errores_try_except(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Explain how to handle errors in Python using try and except blocks, and why this is important for preventing program crashes."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )

    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Manejo de errores try except**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje


@bot.tree.command(name="excepeciones_personalizadas", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def excepciones_personalizadas(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Introduce custom exceptions in Python and explain how to create them for handling specific situations in code."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )

    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Creación de excepciones personalizadas**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje

    
@bot.tree.command(name="leer_archivos_de_texto", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def leer_archivos_de_texto(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Explain how to read text files in Python in a simple and easy-to-understand way."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )

    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Leer archivos de texto**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje

    
@bot.tree.command(name="escribir_en_archivos_de_texto", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def escribir_en_archivos_de_texto(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Introduce writing to text files in Python and explain how this allows for persistently storing information and data, also explain how to write in text documents."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )

    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Escribir en archivos de texto**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje

    
#-----------------------------------------------------
#Verificar
#-----------------------------------------------------
@bot.tree.command(name="proyecto_del_bloque_3", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def proyecto_del_bloque_3(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Explain what programming is in a simple and friendly way for beginners."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )
    
    # Enviar la respuesta real una vez que esté disponible
    await ctx.followup.send(f"**Proyecto del bloque 3** \n{response['choices'][0]['message']['content']}")

#examen bloque 3
with open('trivia3.txt', 'r', encoding='utf-8') as f:#se añadio la codificación utf-8 para que interprete de forma correcta los caracteres del lenguaje español
    lines = f.readlines()

trivias3 = []
for line in lines:
    parts = line.strip().split(';')
    question = parts[0]
    answers = parts[1:]
    correct = answers.index([a for a in answers if a.endswith('*')][0])
    answers = [a.replace('*', '') for a in answers]
    trivias3.append({'question': question, 'answers': answers, 'correct': correct})


@bot.tree.command(name="examen_del_bloque_3", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def examen_del_bloque_3(ctx):
    score = 0
    for _ in range(10):
        trivia = random.choice(trivias3)
        print(f"{trivia['correct']}")  # check
        question_message = f"Pregunta: {trivia['question']}\nOpciones:\n"
        for i, answer in enumerate(trivia['answers']):
            question_message += f"{i + 1}. {answer}\n"
        
        # Use follow-up messages for sending questions
        if _ == 0:
            # For the first message, use ctx.response.send_message
            await ctx.response.send_message(question_message)
        else:
            # For subsequent messages, use follow-up messages
            await ctx.followup.send(content=question_message)
        
        def check(m):
            return m.author.id == ctx.user.id and m.content.isdigit() and int(m.content) in range(1, len(trivia['answers']) + 1)

        try:
            answer = await bot.wait_for('message', check=check, timeout=30.0)
        except asyncio.TimeoutError:
            embed = discord.Embed(title="Ni modo :(", description="Lo siento, se acabó el tiempo!", color=0x00ff00)
            await ctx.followup.send(embed=embed)
        else:
            if int(answer.content) == trivia['correct'] + 1:
                embed = discord.Embed(title="Asi se hace!", description="¡Bien hecho! La respuesta es correcta")
                score += 1
                await ctx.followup.send(embed=embed)
            else:
                embed = discord.Embed(title="Lo siento :(", description="Parece que tendrás que estudiar un poco más. Respuesta incorrecta!")
                await ctx.followup.send(embed=embed)

    # Send final score
    final_message = f"¡Examen completado! Tu puntuación final es: {score} / 10"
    await ctx.followup.send(content=final_message)


#------------------------------------Comandos cuarto tema------------------------------------
@bot.tree.command(name="introduccion_a_numpy", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def introduccion_a_numpy(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Introduce NumPy and explain its importance in scientific computing and data manipulation in Python in a beginner-friendly way."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )
    
    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Introducción a NumPy**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje

    
@bot.tree.command(name="creacion_y_uso_de_arrays", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def creacion_y_uso_de_arrays(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Explain how to create and manipulate arrays in NumPy and why arrays are important for data analysis and science in Python."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )

    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Creación y manipulación de arrays**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje

    
@bot.tree.command(name="introduccion_a_pandas", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def introduccion_a_pandas(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Introduce Pandas and explain its role in data analysis by efficiently working with tabular data structures in Python."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )

    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Introducción a Pandas**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje

    
@bot.tree.command(name="trabajo_con_data_frames", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def trabajo_con_data_frames(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Explain what DataFrames are in Pandas and how they can be manipulated for effective data analysis in Python."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )

    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Trabajo con DataFrames**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje

    
@bot.tree.command(name="libreria_de_openai", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def libreria_de_openai(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Introduce the OpenAI library and explain how it can be installed,and used to interact with powerful and versatile artificial intelligence models."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )

    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Instalación de la librería de OpenAI**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje

    
@bot.tree.command(name="programa_con_la_api_de_openai", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def programa_con_la_api_de_openai(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Explain how to program with the OpenAI API and how it can be used to incorporate AI capabilities into one's own applications and projects. Also give an example of code which the openai api"

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )

    # Enviar la respuesta real una vez que esté disponible
    content = response['choices'][0]['message']['content']
    intro_text = "**Creación de un programa simple utilizando la API de OpenAI**\n"

    # Divide el contenido en fragmentos de menos de 2000 caracteres
    max_length = 2000 - len(intro_text)
    chunks = [content[i:i+max_length] for i in range(0, len(content), max_length)]

    # Envía cada fragmento como un mensaje separado
    for chunk in chunks:
        await ctx.followup.send(f"{intro_text}{chunk}")
        intro_text = ""  # Solo añadir "**Introducción a Python**\n" al primer mensaje

#-----------------------------------------------------
#Verificar
#-----------------------------------------------------
@bot.tree.command(name="proyecto_del_bloque_4", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def proyecto_del_bloque_4(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Explain what programming is in a simple and friendly way for beginners."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2000
    )
    
    # Enviar la respuesta real una vez que esté disponible
    await ctx.followup.send(f"**Proyecto del bloque 4** \n{response['choices'][0]['message']['content']}")

#examen bloque 4
#     
with open('trivia4.txt', 'r', encoding='utf-8') as f:#se añadio la codificación utf-8 para que interprete de forma correcta los caracteres del lenguaje español
    lines = f.readlines()

trivias4 = []
for line in lines:
    parts = line.strip().split(';')
    question = parts[0]
    answers = parts[1:]
    correct = answers.index([a for a in answers if a.endswith('*')][0])
    answers = [a.replace('*', '') for a in answers]
    trivias4.append({'question': question, 'answers': answers, 'correct': correct})


@bot.tree.command(name="examen_del_bloque_4", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def examen_del_bloque_4(ctx):
    score = 0
    for _ in range(10):
        trivia = random.choice(trivias4)
        print(f"{trivia['correct']}")  # check
        question_message = f"Pregunta: {trivia['question']}\nOpciones:\n"
        for i, answer in enumerate(trivia['answers']):
            question_message += f"{i + 1}. {answer}\n"
        
        # Use follow-up messages for sending questions
        if _ == 0:
            # For the first message, use ctx.response.send_message
            await ctx.response.send_message(question_message)
        else:
            # For subsequent messages, use follow-up messages
            await ctx.followup.send(content=question_message)
        
        def check(m):
            return m.author.id == ctx.user.id and m.content.isdigit() and int(m.content) in range(1, len(trivia['answers']) + 1)

        try:
            answer = await bot.wait_for('message', check=check, timeout=30.0)
        except asyncio.TimeoutError:
            embed = discord.Embed(title="Ni modo :(", description="Lo siento, se acabó el tiempo!", color=0x00ff00)
            await ctx.followup.send(embed=embed)
        else:
            if int(answer.content) == trivia['correct'] + 1:
                embed = discord.Embed(title="Asi se hace!", description="¡Bien hecho! La respuesta es correcta")
                score += 1
                await ctx.followup.send(embed=embed)
            else:
                embed = discord.Embed(title="Lo siento :(", description="Parece que tendrás que estudiar un poco más. Respuesta incorrecta!")
                await ctx.followup.send(embed=embed)

    # Send final score
    final_message = f"¡Examen completado! Tu puntuación final es: {score} / 10"
    await ctx.followup.send(content=final_message)


#------------------------------------Comandos quinto tema------------------------------------

#-----------------------------------------------------
#Verificar
#-----------------------------------------------------
@bot.tree.command(name="proyecto_final", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def proyecto_final(ctx):
    # Enviar una respuesta inicial inmediatamente
    await ctx.response.send_message("Procesando tu solicitud...", ephemeral=True)
    
    # Prompt de la clase
    prompt = "Explain what programming is in a simple and friendly way for beginners."

    # Añade el prompt de traducción para una mejor ejecución
    user_message = f"{translation_prompt}\nUser: {prompt}"

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=300
    )
    
    # Enviar la respuesta real una vez que esté disponible
    await ctx.followup.send(f"**Proyecto final** \n{response['choices'][0]['message']['content']}")

#Examen final

with open('trivia5.txt', 'r', encoding='utf-8') as f:#se añadio la codificación utf-8 para que interprete de forma correcta los caracteres del lenguaje español
    lines = f.readlines()

trivias5 = []
for line in lines:
    parts = line.strip().split(';')
    question = parts[0]
    answers = parts[1:]
    correct = answers.index([a for a in answers if a.endswith('*')][0])
    answers = [a.replace('*', '') for a in answers]
    trivias5.append({'question': question, 'answers': answers, 'correct': correct})


@bot.tree.command(name="examen_final", description="Obten informacion sobre los contenidos a aprender de este bloque de contenido")
async def examen_final(ctx):
    score = 0
    for _ in range(10):
        trivia = random.choice(trivias5)
        print(f"{trivia['correct']}")  # check
        question_message = f"Pregunta: {trivia['question']}\nOpciones:\n"
        for i, answer in enumerate(trivia['answers']):
            question_message += f"{i + 1}. {answer}\n"
        
        # Use follow-up messages for sending questions
        if _ == 0:
            # For the first message, use ctx.response.send_message
            await ctx.response.send_message(question_message)
        else:
            # For subsequent messages, use follow-up messages
            await ctx.followup.send(content=question_message)
        
        def check(m):
            return m.author.id == ctx.user.id and m.content.isdigit() and int(m.content) in range(1, len(trivia['answers']) + 1)

        try:
            answer = await bot.wait_for('message', check=check, timeout=30.0)
        except asyncio.TimeoutError:
            embed = discord.Embed(title="Ni modo :(", description="Lo siento, se acabó el tiempo!", color=0x00ff00)
            await ctx.followup.send(embed=embed)
        else:
            if int(answer.content) == trivia['correct'] + 1:
                embed = discord.Embed(title="Asi se hace!", description="¡Bien hecho! La respuesta es correcta")
                score += 1
                await ctx.followup.send(embed=embed)
            else:
                embed = discord.Embed(title="Lo siento :(", description="Parece que tendrás que estudiar un poco más. Respuesta incorrecta!")
                await ctx.followup.send(embed=embed)

    # Send final score   #Actualizado 1/07/2023 (Si el usuario resulta graduado se escribira su nombre en el documento txt graduados seguido de un salto de linea)
    if score >= 6:
      final_message = embed.Discord(title= "Felicidades", description=f"Felicidades, has completado el examen correctamente. Ya estas listo para escribir tud primeras lineas de codigo. \n\nTu puntuacion fue: {score}")
      embed.set_image("https://jimdo-storage.freetls.fastly.net/image/392552801/58ebd500-4915-47fb-a28e-cb55170cfa80.png?quality=80,90&auto=webp&disable=upscale&width=800&height=617&trim=0,0,0,0")
      with open("graduados.txt", "a") as f:
        f.write(ctx.author.name + "\n")
    else:
       final_message = embed.Discord(title= "Lo siento :(", description=f"Lo siento, parece que tendras que estudiar un poco mas. \n\nTu puntuacio final fue: {score}")
    await ctx.send(embed=final_message)


#--------------Funcion para checar a los graduados----------------------------------------------------------------------------
def check_graduado(username):     
    with open("graduados.txt", "r") as f:
        graduados = f.read().splitlines() 
    if username in graduados:
        return True
    else:
        return False
#------------------------------------------------------------------------------------------------------------------


#--------------Comando checa si estas graduado----------------------------------------------------------------------------
@bot.command(name="check", help="Verifica si estás graduado")
async def check(ctx):
    if check_graduado(ctx.author.name):
        embed = discord.Embed(title="¡Felicidades!", description="Tu nombre de usuario ya se encuentra en la base de datos. ¡Estás graduado!")
    else:
        embed = discord.Embed(title="Aún no estás graduado", description="Tu usuario no se encuentra en la base de datos. Sigue estudiando y realiza el examen final para graduarte.")
    await ctx.send(embed=embed)
#------------------------------------------------------------------------------------------------------------------


#--------------Checa todos los estudiantes graduados + El total de graduados-----------------------------------------------------------------
@bot.command(name="graduados", help="Muestra la lista de graduados")
async def graduados(ctx):
    with open("graduados.txt", "r") as f:
        graduados = f.read().splitlines()
    total_graduados = len(graduados)
    graduados_message = "Lista de graduados:\n"
    for graduado in graduados:
        graduados_message += f"- {graduado}\n"
    graduados_message += f"\nTotal de graduados: {total_graduados}"
    embed = discord.Embed(title="Graduados", description=graduados_message)
    await ctx.send(embed=embed)
#------------------------------------------------------------------------------------------------------------------


bot.run(DISCORD_TOKEN)
