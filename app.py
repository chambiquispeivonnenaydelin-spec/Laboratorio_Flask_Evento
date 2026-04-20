from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Esta ruta DEBE llamarse /registro porque así lo pusimos en el HTML
@app.route('/registro', methods=['POST'])
def registro():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    taller = request.form.get('taller')
    
    # Esto es lo que verá el usuario al terminar
    return f"""
    <body style="background:#121212; color:white; font-family:sans-serif; display:flex; justify-content:center; align-items:center; height:100vh; text-align:center;">
        <div>
            <h1 style="color:#00f2fe;">¡Registro Exitoso!</h1>
            <p>Hola <strong>{nombre}</strong>, ya estás en el taller de {taller}.</p>
            <p>Confirmación enviada a: {email}</p>
            <br>
            <a href="/" style="color:#4facfe; text-decoration:none;">Volver al inicio</a>
        </div>
    </body>
    """

if __name__ == '__main__':
    app.run(debug=True)
