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
    to_email = data.get("email")
    pedido = data.get("pedido")

    if not to_email or not pedido:
        return jsonify({"error": "Faltan campos requeridos"}), 400

    # Crear el mensaje
    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = to_email
    msg["Subject"] = "Resumen de tu pedido - Panadería Future"

    cuerpo = f"""
    ¡Gracias por tu compra!

    Este es el resumen de tu pedido:
    {pedido}

    ¡Esperamos verte pronto!

    Panadería Future
    """

    msg.attach(MIMEText(cuerpo, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL, APP_PASSWORD)
            server.sendmail(EMAIL, to_email, msg.as_string())
        return jsonify({"mensaje": "Correo enviado con éxito"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)