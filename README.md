# Bot de Instagram con Python

Este proyecto es un bot de Instagram desarrollado en Python que automatiza ciertas acciones en la plataforma.

## Descripción

El bot utiliza la librería de Selenium para interactuar con la plataforma. Puede realizar diversas tareas, como seguir usuarios, dar "me gusta" a publicaciones...

## Instalación

1. Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/valantoni/instagram-bot.git
cd instagram-bot
```

2. Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

## Configuración

Antes de ejecutar el bot, debes configurar tus credenciales de Instagram en el archivo `.env`. Asegúrate de incluir tu nombre de usuario y contraseña de Instagram.

```python
# .env

USERNAME = 'tu_nombre_de_usuario'
PASSWORD = 'tu_contraseña'
```

## Ejecución

```bash
python main.py
```
