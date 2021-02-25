from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from flask import Flask, render_template, url_for, redirect, request
import os

app = Flask(__name__)

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

"""
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
    print("gauth.credentials is None")
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
    print("gauth.access_token_expired")
else:
    # Initialize the saved creds
    gauth.Authorize()
    print("gauth.credentials is {} and gauth.access_token_expired {}".format(gauth.credentials, gauth.access_token_expired))
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")
""" #Guardar Credenciales

drive = GoogleDrive(gauth)

idCarpeta = "1Kdjd8kJMsta3D33VHeVHP-8ZwS-2ADQb"

@app.route("/")
def index():
    file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(idCarpeta)}).GetList()
    return render_template("index.html", archivos=file_list)

@app.route("/addCarpeta", methods=['GET', 'POST'])
def addCarpeta():
    if request.method == "POST":
        nombreCarpeta = request.form.get('nombreCarpeta')
        carpeta = drive.CreateFile({
            "title": nombreCarpeta,
            "mimeType": "application/vnd.google-apps.folder",
            "parents": [{'kind': 'drive#parentReference',
                     'id': idCarpeta
            }]
        })
        carpeta.Upload()
        return redirect(url_for("index"))
    else:
        return render_template("addCarpeta.html")

@app.route("/subirArchivo", methods=['GET', 'POST'])
def subirArchivo():
    if request.method == "POST":
        archivo = request.files['archivo']
        archivo.save(os.path.join("Archivos/", archivo.filename))
        #archivo.save(os.path.join(archivo.filename))
        archivoDrive = drive.CreateFile({
            "title": archivo.filename,
            "parents": [{'kind': 'drive#parentReference',
                         'id': idCarpeta}]
        })
        archivoDrive.SetContentFile("Archivos/{}".format(archivo.filename))
        archivoDrive.Upload()
        return redirect(url_for("index"))
    else:
        return render_template("subirArchivo.html")



if __name__ == "__main__":
    #app.run(debug=True)
    app.run(debug=True, use_reloader=False) #Evitar Que se ejecute dos veces