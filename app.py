from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = "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"

def crear_imagen(descripcion, cantidad):
    respuesta = openai.Image.create(
        prompt=descripcion,
        n=cantidad,
        size="512x512"
    )
    return respuesta["data"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar_imagen', methods=['POST'])
def generar_imagen():
    descripcion = request.form['descripcion']
    cantidad = int(request.form['cantidad'])  # Convertir el número del input
    res = crear_imagen(descripcion, cantidad)
    urls = [url['url'] for url in res]
    return render_template('index.html', urls=urls)

if __name__ == "__main__":
    app.run(debug=True)
