from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("menus.html")

@app.route("/wpc")
def wpc_principal():
    return render_template("wpc/principal.html")

@app.route("/datos")
def wpc_datos():
    return render_template("wpc/datos.html")

@app.route("/infoe")
def wpc_infoe():
    return render_template("wpc/infoe.html")

@app.route("/tecno")
def wpc_tecno():
    return render_template("wpc/tecno.html")

@app.route("/fav")
def fav_principal():
    return 'Pendiente'

if __name__ == "__main__":
    app.run(debug=True)