from flask import Flask, render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'agenda'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

app.secret_key = 'mysecretkey'

conn = mysql.connect()
cursor = conn.cursor()

@app.route("/")
def index():
    """
    Pagina Principal
    """
    cursor.execute("SELECT * FROM usuarios")
    data = cursor.fetchall()
    return render_template("usuarios.html", usuarios = data)

@app.route("/agregar_usuario", methods=['GET', 'POST'])
def agregar_usuario():
    """
    Agregar usuario a la base de datos, Sin sus conctactos
    """
    if request.method == "POST":
        usr_nick = request.form.get("usr_nick")
        usr_nombre = request.form.get("usr_nombre")
        usr_apellido = request.form.get("usr_apellido")
        usr_email = request.form.get("usr_email")
        usr_pass = request.form.get("usr_pass")
        cursor.execute("""
            INSERT INTO `usuarios`(`usr_nick`, `usr_nombre`, `usr_apellido`, `usr_email`, `usr_pass`) 
            VALUES ('{}','{}','{}','{}','{}')        
        """.format(usr_nick, usr_nombre, usr_apellido, usr_email, usr_pass))
        conn.commit()
        flash("Usuario Añadido!")
        return redirect(url_for("index"))
    else:
        return render_template("agregar_usuario.html")

@app.route("/editar_usuario/<string:id>", methods=['GET', 'POST'])
def editar_usuario(id):
    """
    Editar Usuario, Sin editar sus contactos
    """
    if request.method == "POST":
        usr_nick = request.form.get("usr_nick")
        usr_nombre = request.form.get("usr_nombre")
        usr_apellido = request.form.get("usr_apellido")
        usr_email = request.form.get("usr_email")
        usr_pass = request.form.get("usr_pass")
        if id != "1":
            cursor.execute("""
                UPDATE `usuarios` 
                SET `usr_nick`='{}',`usr_nombre`='{}',
                `usr_apellido`='{}',`usr_email`='{}',`usr_pass`='{}' 
                WHERE `usr_id` = '{}'
            """.format(usr_nick, usr_nombre, usr_apellido, usr_email, usr_pass, id))
            conn.commit()
            flash("Usuario Actualizado!")
        else:
            flash("NO SE PUEDE MODIFICAR EL ADMIN!")
        return redirect(url_for('index'))
    else:
        cursor.execute("""
            SELECT * FROM `usuarios` WHERE `usuarios`.`usr_id` = '{}'
        """.format(id))
        data = cursor.fetchone()
        return render_template("editar_usuario.html", usuario = data)

@app.route("/eliminar_usuario/<string:id>")
def eliminar_usuario(id):
    """
    Eliminar usuario y cambiar sus contactos al usuario admin
    """
    if id == "1":
        flash("NO SE PUEDE ELIMINAR EL ADMIN!")
        return redirect(url_for('index'))
    else:
        cursor.execute("""
            UPDATE `contactos` 
            SET `usr_id`='{}' 
            WHERE `usr_id` = '{}'
        """.format(1, id))
        conn.commit()
        cursor.execute("""
            DELETE FROM `usuarios` WHERE `usr_id` = '{}'
        """.format(id))
        conn.commit()
        flash("Usuario Eliminado!")
        return redirect(url_for('index'))

@app.route("/contactos")
def contactos():
    """
    Mostrar contactos
    """
    cursor.execute("""
        SELECT `con_id`, `usr_nick`, `con_nombre`, `con_apellido`, `con_direccion`, `con_telefono`, `con_email`
        FROM `usuarios`
        JOIN `contactos`
        ON `usuarios`.`usr_id` = `contactos`.`usr_id`
    """)
    data = cursor.fetchall()
    return render_template("contactos.html", contactos = data)

@app.route("/agregar_contacto/<string:id>", methods=['GET', 'POST'])
def agregar_contacto(id):
    """
    Agregar contacto tanto en la tabla usuario, como en la de contactos
    teniendo en cuenta esta a partir si se encia un id o no
    """
    if request.method == "POST":
        con_nombre = request.form.get("con_nombre")
        con_apellido = request.form.get("con_apellido")
        con_direccion = request.form.get("con_direccion")
        con_telefono = request.form.get("con_telefono")
        con_email = request.form.get("con_email")
        if id == "no_id":
            id = request.form.get("usr_id")
            no_hubo_id = True
        else:
            no_hubo_id = False
        cursor.execute("""
            INSERT INTO `contactos`(`usr_id`, `con_nombre`, `con_apellido`,
                                `con_direccion`, `con_telefono`, `con_email`) 
            VALUES ('{}','{}','{}','{}','{}','{}')
        """.format(id, con_nombre, con_apellido, con_direccion, con_telefono, con_email))
        conn.commit()
        flash("Contacto Agregado!")
        if no_hubo_id:
            return redirect(url_for('contactos'))
        else:
            return redirect(url_for('index'))
    else:
        cursor.execute("""
            SELECT * FROM `usuarios`
        """)
        data = cursor.fetchall()
        return render_template("agregar_contacto.html", usuarios=data, id=id)

@app.route("/contactos_admin/<string:id>", methods=['GET', 'POST'])
def contactos_admin(id):
    """
    Esta opcion se habilita a usuarios que deseen recuperar contactos almacenados en la cuenta admin
    """
    if request.method == "POST":
        IDs_Para_Usuario = request.form.getlist("IDs_Para_Agregar")
        for ID_Actualizado in IDs_Para_Usuario:
            if ID_Actualizado != "1":
                cursor.execute("""
                    UPDATE `contactos` 
                    SET `usr_id`= '{}'
                    WHERE `con_id` = '{}'
                """.format(id, ID_Actualizado))
                conn.commit()
        flash("Contactos Agregados!")
        return redirect(url_for('index'))
    else:
        cursor.execute("""
            SELECT * 
            FROM `contactos`
            WHERE `contactos`.`usr_id`= '1'
        """)
        data = cursor.fetchall()
        return render_template("contactos_admin.html", contactos = data)

@app.route("/editar_contacto/<string:id>", methods=['GET', 'POST'])
def editar_contacto(id):
    """
    Editar el contactos
    """
    if request.method == "POST":
        usr_id = request.form.get("usr_id")
        con_nombre = request.form.get("con_nombre")
        con_apellido = request.form.get("con_apellido")
        con_direccion = request.form.get("con_direccion")
        con_telefono = request.form.get("con_telefono")
        con_email = request.form.get("con_email")
        if id != "1":
            cursor.execute("""
                UPDATE `contactos` 
                SET `usr_id`='{}',`con_nombre`='{}',
                `con_apellido`='{}',`con_direccion`='{}',`con_telefono`='{}',
                `con_email`='{}' 
                WHERE `contactos`.`con_id` = '{}'
            """.format(usr_id, con_nombre, con_apellido, con_direccion, con_telefono, con_email, id))
            conn.commit()
            flash("Contacto Actualizado!")
        else:
            flash("NO SE PUEDE MODIFICAR EL ADMIN!")
        return redirect(url_for('contactos'))
    else:
        cursor.execute("""
            SELECT * FROM `contactos` WHERE `contactos`.`con_id` = '{}'
        """.format(id))
        data = cursor.fetchone()
        cursor.execute("""
            SELECT * FROM `usuarios`
        """)
        data2 = cursor.fetchall()
        return render_template("editar_contacto.html", contacto = data, usuarios = data2)

@app.route("/eliminar_contacto/<string:id>")
def eliminar_contacto(id):
    """
    Elimina el contacto y trasnlada sus citas al contacto admin
    """
    if id == '1':
        flash("NO SE PUEDE BORRAR EL ADMIN")
        return redirect(url_for('contactos'))
    else:
        cursor.execute("""
            UPDATE `citas` 
            SET `con_id`='1'
            WHERE `citas`.`con_id` = '{}'
        """.format(id))
        conn.commit()
        cursor.execute("""
            DELETE FROM `contactos` 
            WHERE `contactos`.`con_id` = '{}'
        """.format(id))
        conn.commit()
        flash("Contacto Eliminado!")
        return redirect(url_for('contactos'))

@app.route("/citas")
def citas():
    """
    Muestra la tabla de citas
    """
    cursor.execute("""
        SELECT `cit_id`, `contactos`.`usr_id`, `con_nombre`, `con_apellido`, `con_email`, `cit_lugar`, `cit_fecha`, `cit_hora`, `cit_descripcion`
        FROM `contactos`
        RIGHT JOIN `citas`
        ON `citas`.`con_id` = `contactos`.`con_id`
    """)
    data = cursor.fetchall()
    cursor.execute("""
        SELECT * FROM `usuarios`
    """)
    data2 = cursor.fetchall()
    return render_template("citas.html", citas = data, usuarios = data2)

@app.route("/agregar_cita/<string:id>", methods=['GET', 'POST'])
def agregar_cita(id):
    """
    Agregar la cita teniendo en cuenta de donde provino la solicitud teniendo en cuenta
    el id que se manda por el url
    """
    if request.method == "POST":
        cit_lugar = request.form.get("cit_lugar")
        cit_fecha = request.form.get("cit_fecha")
        cit_hora = request.form.get("cit_hora")
        cit_descripcion = request.form.get("cit_descripcion")
        if id == "no_id":
            id = request.form.get("con_id")
            no_id = True
        else:
            no_id = False
        cursor.execute("""
            INSERT INTO `citas`(`con_id`, `cit_lugar`, 
            `cit_fecha`, `cit_hora`, `cit_descripcion`) 
            VALUES ('{}','{}','{}','{}','{}')
        """.format(id, cit_lugar, cit_fecha, cit_hora, cit_descripcion))
        conn.commit()
        flash("Cita Añadida!")
        if no_id:
            return redirect(url_for('citas'))
        else:
            return redirect(url_for('contactos'))
    else:
        cursor.execute("""
            SELECT * FROM `contactos`
        """)
        data = cursor.fetchall()
        return render_template("agregar_cita.html", contactos = data, id=id)

@app.route("/editar_cita/<string:id>", methods=['GET','POST'])
def editar_cita(id):
    """
    Edita la cita habilitando la posibilidad de cambiar de contacto DEL USUARIO!
    """
    if request.method == "POST":
        con_id = request.form.get("con_id")
        cit_lugar = request.form.get("cit_lugar")
        cit_fecha = request.form.get("cit_fecha")
        cit_hora = request.form.get("cit_hora")
        cit_descripcion = request.form.get("cit_descripcion")
        cursor.execute("""
            UPDATE `citas` 
            SET `con_id`='{}',`cit_lugar`='{}',
            `cit_fecha`='{}',`cit_hora`='{}',`cit_descripcion`='{}' 
            WHERE `citas`.`cit_id` = '{}'
        """.format(con_id, cit_lugar, cit_fecha, cit_hora, cit_descripcion, id))
        conn.commit()
        flash("Cita Actualizada!")
        return redirect(url_for('citas'))
    else:
        """
        Se hacen 3 consultas la primera para mandar la cita a modificar
        las otras dos para mandar los contactos del USUARIO al que tiene registrada esa cita y 
        no todos los contactos al tiempo
        """
        cursor.execute("""
            SELECT * FROM `citas` 
            WHERE `citas`.`cit_id` = '{}'
        """.format(id))
        data = cursor.fetchone()

        cursor.execute("""
            SELECT `usr_id` 
            FROM `contactos` 
            WHERE `contactos`.`con_id` = '{}'
        """.format(data[1]))
        data2 = cursor.fetchone()

        cursor.execute("""
            SELECT * 
            FROM `contactos` 
            WHERE `contactos`.`usr_id` = '{}' 
        """.format(data2[0]))

        data3 = cursor.fetchall()

        return render_template("editar_cita.html", cita = data, contactos = data3)


@app.route("/eliminar_cita/<string:id>")
def eliminar_cita(id):
    """
    Elimina la cita a diferencia de las otras dos aqui no se asigna la cita a ninguna cuenta
    porque, si se borra aqui es porque ya se quiere eliminar definitivamente
    """
    cursor.execute("""
        DELETE FROM `citas` WHERE `citas`.`cit_id` = '{}' 
    """.format(id))
    conn.commit()
    flash("Cita Eliminada!")
    return redirect(url_for('citas'))

@app.route("/citas_admin/<string:id>", methods=['GET', 'POST'])
def citas_admin(id):
    """
    Da la posibilidad a contactos de agregar citas de contactos eliminados anteriormente almacenadas en
    el contacto admin
    """
    if request.method == "POST":
        IDs_Para_Agregar = request.form.getlist("IDs_Para_Agregar")
        for ID_de_cita in IDs_Para_Agregar:
            cursor.execute("""
                UPDATE `citas` 
                SET `con_id`='{}'
                WHERE `citas`.`cit_id` = '{}'
            """.format(id, ID_de_cita))
            conn.commit()
        flash("Citas Agregadas!")
        return redirect(url_for('contactos'))
    else:
        cursor.execute("""
            SELECT *
            FROM `citas`
            WHERE `citas`.`con_id` = '1'
        """)
        data = cursor.fetchall()
        return render_template("citas_admin.html", citas = data)

@app.route("/wip", methods=['POST'])
def wip():
    """
    Funcion de prueba para los formularios
    """
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)