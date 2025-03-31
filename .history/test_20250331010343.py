import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Cargar las variables del entorno
load_dotenv()

EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

# Crear el mensaje
destinatario = "nachoayerbe2003@gmail.com"
asunto = "Test de envío de correo desde Python"
cuerpo = """
Hola Nacho,

Este es un test exitoso de envío de correo usando Python + Gmail App Password.

🚀 Todo funciona perfecto.

Saludos,  
Future’s Bakery Bot
"""

msg = MIMEText(cuerpo)
msg["Subject"] = asunto
msg["From"] = EMAIL
msg["To"] = destinatario

# Enviar el correo
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, APP_PASSWORD)
        server.sendmail(EMAIL, destinatario, msg.as_string())
        print("✅ Correo enviado con éxito")
except Exception as e:
    print("❌ Error:", e)
