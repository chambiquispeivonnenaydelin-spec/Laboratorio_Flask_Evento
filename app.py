from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Página para el evento ficticio (Carnet termina en 8) [cite: 5, 6]
    return render_template('index.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    nombre = request.form.get('nombre')
    return f"<h1>¡Registro Exitoso!</h1><p>Bienvenido al evento, {nombre}.</p><a href='/'>Volver</a>"

if __name__ == '__main__':
    app.run(debug=True)