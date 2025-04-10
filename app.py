from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculadora():
    resultado = None
    error = None

    if request.method == "POST":
        try:
            numero1 = float(request.form["numero1"])
            numero2 = float(request.form["numero2"])
            operacion = request.form["operacion"]

            if operacion == "sumar":
                resultado = numero1 + numero2
            elif operacion == "restar":
                resultado = numero1 - numero2
            elif operacion == "multiplicar":
                resultado = numero1 * numero2
            elif operacion == "dividir":
                if numero2 == 0:
                    error = "No se puede dividir por cero."
                else:
                    resultado = numero1 / numero2
        except ValueError:
            error = "Por favor ingresa solo números."

    return render_template("index.html", resultado=resultado, error=error)

if __name__ == "__main__":
    app.run(debug=True)