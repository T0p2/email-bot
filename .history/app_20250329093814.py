from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)

# Configuración del correo
EMAIL = "nachoayerbe2003@gmail.com"
APP_PASSWORD = "alslpihvexxvuvcd"

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.json

    email = data.get("email")
    carrito = data.get("carrito_productos")
    costo = data.get("costo_envio")
    total = data.get("total_pedido")
    nombre = data.get("nombre_cliente_completo")
    direccion = data.get("direccion_cliente")
    nro = data.get("nro_pedido")

    # Validar campos requeridos
    if not all([email, carrito, costo, total, nombre, direccion, nro]):
        return jsonify({"error": "Faltan campos requeridos"}), 400

    # Crear el mensaje
    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = email
    msg["Subject"] = "Resumen de tu pedido - Panadería Future"

    cuerpo = f"""
Estimado/a {nombre},

Muchas gracias por realizar tu pedido en *Panadería Future*. A continuación, te enviamos el resumen detallado:

🛒 Productos solicitados:
{carrito}

🚚 Costo de envío: ${costo}
💰 Total a pagar: ${total}

📍 Punto de entrega:
{direccion}

📦 Número de pedido: {nro}

Si tenés alguna duda o consulta adicional, no dudes en escribirnos a este mismo correo.

¡Gracias por confiar en nosotros!

Atentamente,  
**Panadería Future**
"""

    msg.attach(MIMEText(cuerpo, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL, APP_PASSWORD)
            server.sendmail(EMAIL, email, msg.as_string())
        return jsonify({"mensaje": "Correo enviado con éxito"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
