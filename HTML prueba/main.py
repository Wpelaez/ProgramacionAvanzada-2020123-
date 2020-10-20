from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("menus.html")

@app.route("/wpc_principal")
def wpc_principal():
    return render_template("wpc/principal.html")

@app.route("/wpc_datos")
def wpc_datos():
    return render_template("wpc/datos.html")

@app.route("/wpc_infoe")
def wpc_infoe():
    return render_template("wpc/infoe.html")

@app.route("/wpc_tecno")
def wpc_tecno():
    return render_template("wpc/tecno.html")

@app.route("/fav_principal")
def fav_principal():
    return render_template("fav/Hola.html")

@app.route("/fav_Hola2")
def fav_Hola2():
    return render_template("fav/Hola2.html")

@app.route("/fav_Hola3")
def fav_Hola3():
    return render_template("fav/Hola3.html")

if __name__ == "__main__":
    app.run(debug=True)