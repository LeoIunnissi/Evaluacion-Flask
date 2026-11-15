
from flask import Flask, render_template, request
import math

# Crear la aplicación Flask
app = Flask(__name__)


# ==========================================
# RUTA PRINCIPAL: MENÚ DE INICIO
# ==========================================
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# ==========================================
# EJERCICIO 1
# ==========================================
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():

    # Comprobar si el formulario fue enviado
    if request.method == "POST":

        try:
            # Recibir los datos enviados desde el formulario
            nota1 = float(request.form.get("nota1", ""))
            nota2 = float(request.form.get("nota2", ""))
            nota3 = float(request.form.get("nota3", ""))
            asistencia = float(request.form.get("asistencia", ""))

        except ValueError:
            return render_template(
                "ejercicio1.html",
                error="Debes ingresar valores numéricos válidos."
            )

        # Validar que las notas estén entre 10 y 70
        notas = [nota1, nota2, nota3]

        if not all(math.isfinite(nota) and 10 <= nota <= 70 for nota in notas):
            return render_template(
                "ejercicio1.html",
                error="Las notas deben estar entre 10 y 70."
            )

        # Validar que la asistencia esté entre 0 y 100
        if not math.isfinite(asistencia) or not 0 <= asistencia <= 100:
            return render_template(
                "ejercicio1.html",
                error="La asistencia debe estar entre 0 y 100."
            )

        # Calcular el promedio de las tres notas
        promedio = sum(notas) / 3

        # Determinar si el estudiante aprueba o reprueba
        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        # Enviar los resultados a la página HTML
        return render_template(
            "resultado.html",
            ejercicio=1,
            promedio=promedio,
            asistencia=asistencia,
            estado=estado
        )

    # Si se ingresa mediante GET, mostrar el formulario
    return render_template("ejercicio1.html")


# ==========================================
# EJERCICIO 2
# ==========================================
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():

    # Comprobar si el formulario fue enviado
    if request.method == "POST":

        # Recibir los tres nombres desde el formulario
        nombre1 = request.form.get("nombre1", "").strip()
        nombre2 = request.form.get("nombre2", "").strip()
        nombre3 = request.form.get("nombre3", "").strip()

        # Almacenar los nombres en una lista
        nombres = [nombre1, nombre2, nombre3]

        # Comprobar que no existan campos vacíos
        if not all(nombres):
            return render_template(
                "ejercicio2.html",
                error="Debes ingresar los tres nombres."
            )

        # Comprobar que los tres nombres sean diferentes
        if len(set(nombre.casefold() for nombre in nombres)) != 3:
            return render_template(
                "ejercicio2.html",
                error="Debes ingresar tres nombres diferentes."
            )

        # Obtener el nombre con mayor cantidad de caracteres
        nombre_mayor = max(nombres, key=len)

        # Contar los caracteres del nombre seleccionado
        cantidad_caracteres = len(nombre_mayor)

        # Enviar los resultados a la página HTML
        return render_template(
            "resultado.html",
            ejercicio=2,
            nombre_mayor=nombre_mayor,
            cantidad_caracteres=cantidad_caracteres
        )

    # Si se ingresa mediante GET, mostrar el formulario
    return render_template("ejercicio2.html")


# ==========================================
# EJECUTAR LA APLICACIÓN
# ==========================================
if __name__ == "__main__":
    app.run(debug=True)
