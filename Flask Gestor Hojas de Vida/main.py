from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from base64 import b64encode

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class hsVida(db.Model):
    __tablename__ = "hsvida"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    nombre_b = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    apellido_b = db.Column(db.String(100))
    l_nacimiento = db.Column(db.String(100))
    f_nacimiento = db.Column(db.String(100))
    direccion = db.Column(db.String(100))
    barrio = db.Column(db.String(100))
    telefono_fijo = db.Column(db.String(100))
    telefono_celu = db.Column(db.String(100))
    correo = db.Column(db.String(100))
    edad = db.Column(db.String(100))
    genero = db.Column(db.String(100))
    ciudad = db.Column(db.String(100))
    academica = db.relationship('Academica', backref='hsvida', cascade="all, delete-orphan")# el cascade es para que cuando se borre el objeto padre borre tambien en las tablas de las clases hijas los registros con ese id
    """
    se crea una relacion, un atributo de esta clase que dara los atributos de la clase a la cual hace referencia en este caso
    Academica, se hace un backref este sera el ATRIBUTO en la clase hija en el cual se le asignara un PADRE a la hora
    de instanciar
    """
    tecnologias = db.relationship('Tecnologias', backref='hsvida', cascade="all, delete-orphan")
    photo = db.Column(db.Text, unique=False)

    def __init__(self, nombre, nombre_b, apellido, apellido_b, l_nacimiento, f_nacimiento, direccion, barrio,
                 telefono_fijo, telefono_celu, correo, edad, genero, ciudad, photo):
        self.nombre = nombre
        self.nombre_b = nombre_b
        self.apellido = apellido
        self.apellido_b = apellido_b
        self.l_nacimiento = l_nacimiento
        self.f_nacimiento = f_nacimiento
        self.direccion = direccion
        self.barrio = barrio
        self.telefono_fijo = telefono_fijo
        self.telefono_celu = telefono_celu
        self.correo = correo
        self.edad = edad
        self.genero = genero
        self.ciudad = ciudad
        self.photo = photo

class Academica(db.Model):
    __tablename__ = "Academica"
    id = db.Column(db.Integer, primary_key= True)
    tipo = db.Column(db.String(100))
    titulo = db.Column(db.String(100))
    institucion = db.Column(db.String(100))
    ciudad = db.Column(db.String(100))
    year = db.Column(db.String(100))
    hsvida_id = db.Column(db.Integer, db.ForeignKey('hsvida.id'))
    """
    se crea una columna en esta tabla para dar el numero id de la clase padre, un elemento o grupo de elementos
    aca, perteneceran a un OBJETO de la clase PADRE y ese objeto tiene un ID que se mostrara en esta columna
    Para llamar los atribuos de esta clase desde el objeto de la clase padre se hace primero el llamado a el
    atributo de relacion, este sera una LISTA por tanto hay que llamar la posicion de ese arreglo y luego se
    pondra el atributo de la clase hija ej:
    
    objeto_padre.academica[0].titulo = ;
    """

    def __init__(self, tipo, titulo, institucion, ciudad, year, hsvida):
        self.tipo = tipo
        self.titulo = titulo
        self.institucion = institucion
        self.ciudad = ciudad
        self.year = year
        self.hsvida = hsvida

class Tecnologias(db.Model):
    __tablename__= "Tecnologias"
    id = db.Column(db.Integer, primary_key= True)
    tipo=db.Column(db.String(100))
    nombre_tecno=db.Column(db.String(100))
    hsvida_id = db.Column(db.Integer, db.ForeignKey('hsvida.id'))

    def __init__(self, tipo, nombre_tecno, hsvida):
        self.tipo=tipo
        self.nombre_tecno = nombre_tecno
        self.hsvida=hsvida

@app.route("/")
def index():
    return render_template("home.html", hojasdevida = hsVida.query.all() )

@app.route("/agregar", methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        photo = request.files['photo']
        if not photo:
            print("NO HAY FOTO")
            leer_foto = None
        else:
            print("HAY FOTO")
            leer_foto = photo.read()

        hjvida_objeto = hsVida(request.form['nombre'], request.form['nombre_b'], request.form['apellido'],
                               request.form['apellido_b'], request.form['l_nacimiento'], request.form['f_nacimiento'],
                               request.form['direccion'], request.form['barrio'], request.form['telefono_fijo'],
                               request.form['telefono_celu'], request.form['correo'], request.form['edad'],
                               request.form['genero'], request.form['ciudad'], leer_foto)
        db.session.add(hjvida_objeto)
        db.session.commit()
        return render_template("agregar_exito.html", persona=hjvida_objeto)
    return render_template("agregar.html")

@app.route("/quitar", methods =['POST'])
def quitar():
    codigo_quitar = request.form.get('codigo_borrar')#Aca saca de codigo_borrar el valor que esta en el request es decir unicamente el codigo de la hoja de vida
    persona = hsVida.query.filter_by(id=codigo_quitar).first()#A persona la vuelve un objeto de la clase hsvida con los atributos del el codigo que se le mando a buscar
    db.session.delete(persona)
    db.session.commit()
    return render_template("quitar.html", nombre= persona.nombre, apellido= persona.apellido)

@app.route("/actualizar", methods =['POST'])
def actualizar():
    codigo_actualizar = hsVida.query.filter_by(id=request.form.get('codigo_actualizar')).first()
    return render_template("actualizar.html", persona = codigo_actualizar, codigo_antiguo= codigo_actualizar.id)

@app.route("/accion_actualizar", methods =['POST'])
def accion_actualizar():
    codigo_actualizar = hsVida.query.filter_by(id=request.form.get('codigo_actualizar')).first()
    codigo_actualizar.nombre=request.form.get('nombre')
    codigo_actualizar.nombre_b=request.form.get('nombre_b')
    codigo_actualizar.apellido=request.form.get('apellido')
    codigo_actualizar.apellido_b=request.form.get('apellido_b')
    codigo_actualizar.l_nacimiento=request.form.get('l_nacimiento')
    codigo_actualizar.f_nacimiento=request.form.get('f_nacimiento')
    codigo_actualizar.direccion=request.form.get('direccion')
    codigo_actualizar.barrio=request.form.get('barrio')
    codigo_actualizar.telefono_fijo=request.form.get('telefono_fijo')
    codigo_actualizar.telefono_celu=request.form.get('telefono_celu')
    codigo_actualizar.correo=request.form.get('correo')
    codigo_actualizar.edad=request.form.get('edad')
    codigo_actualizar.genero=request.form.get('genero')
    codigo_actualizar.ciudad=request.form.get('ciudad')
    photo = request.files['photo']
    if photo:
        codigo_actualizar.photo = photo.read()
    borrar_foto = request.form.get('borrar_foto')
    if not borrar_foto:
        borrar_foto = 0
    borrar_foto = int(borrar_foto)
    if borrar_foto == 1:
        codigo_actualizar.photo = None
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/ver", methods =['POST'])
def ver():
    ver_hojavida = hsVida.query.filter_by(id=request.form.get('ver_hojavida')).first()
    if ver_hojavida.photo  == None:
        photo = None
    else:
        photo = b64encode(ver_hojavida.photo).decode("utf-8")
    return render_template("ver.html", persona=ver_hojavida, photo=photo)

@app.route("/agregar_academica", methods =['POST'])
def agregar_academica():
    objeto_padre = hsVida.query.filter_by(id=request.form.get('codigo')).first()
    return render_template("agregar_academica.html", persona=objeto_padre)

@app.route("/accion_agregar_academica", methods=['POST'])
def accion_agregar_academica():
    objeto_padre = hsVida.query.filter_by(id=request.form.get('codigo')).first()
    info_academica = Academica(request.form.get('tipo'), request.form.get('titulo'),
                               request.form.get('institucion'), request.form.get('ciudad'),
                               request.form.get('year'), objeto_padre)
    db.session.add(info_academica)
    db.session.commit()
    return render_template("agregar_infoe_exito.html", persona= objeto_padre)

@app.route("/actualizar_infoe", methods =['POST'])
def actualizar_infoe():
    codigo_actualizar = hsVida.query.filter_by(id=request.form.get('codigo_actualizar')).first()
    return render_template("actualizar_infoe.html", persona = codigo_actualizar, codigo_antiguo= codigo_actualizar.id, len=len(codigo_actualizar.academica))

@app.route("/accion_actualizar_infoe", methods =['POST'])
def accion_actualizar_infoe():
    codigo_actualizar = hsVida.query.filter_by(id=request.form.get('codigo_actualizar')).first()
    for i in range(len(codigo_actualizar.academica)):
        codigo_actualizar.academica[i].tipo = request.form.get('tipo{}'.format(i))
        codigo_actualizar.academica[i].titulo = request.form.get('titulo{}'.format(i))
        codigo_actualizar.academica[i].institucion = request.form.get('institucion{}'.format(i))
        codigo_actualizar.academica[i].ciudad = request.form.get('ciudad{}'.format(i))
        codigo_actualizar.academica[i].year = request.form.get('year{}'.format(i))
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/eliminar_academica", methods =['POST'])
def eliminar_academica():
    objeto_padre = hsVida.query.filter_by(id=request.form.get('codigo')).first()
    return render_template("eliminar_infoe.html", persona = objeto_padre, len=len(objeto_padre.academica))

@app.route("/accion_eliminar_academica", methods= ['POST'])
def accion_eliminar_academica():
    objeto_padre = hsVida.query.filter_by(id=request.form.get('codigo')).first()
    test = request.form.getlist('posicion_borrar')
    for i in range(len(test)):
        test[i]=int(test[i])
    test = sorted(test, reverse=True)
    print(test)
    for i in test:
        (objeto_padre.academica).pop(i)
    db.session.commit()
    return render_template("agregar_infoe_exito.html", persona= objeto_padre)

@app.route("/agregar_tecnologica", methods=['POST'])
def agregar_tecnologica():
    objeto_padre = hsVida.query.filter_by(id=request.form.get('codigo')).first()
    return render_template("agregar_tecnologica.html", persona = objeto_padre)

@app.route("/accion_agregar_tecnologica", methods=['POST'])
def accion_agregar_tecnologica():
    objeto_padre = hsVida.query.filter_by(id=request.form.get('codigo')).first()
    informacion_tecnologia = Tecnologias(request.form.get('tipo'), request.form.get('nombre_tecno'), objeto_padre)
    db.session.add(informacion_tecnologia)
    db.session.commit()
    return render_template("agregar_tecno_exito.html", persona = objeto_padre)

@app.route("/actualizar_tecno", methods=['POST'])
def actualizar_tecno():
    objeto_padre = hsVida.query.filter_by(id=request.form.get('codigo_actualizar')).first()
    return render_template("actualizar_tecno.html", persona=objeto_padre, codigo_antiguo=objeto_padre.id, len=len(objeto_padre.tecnologias))

@app.route("/accion_actualizar_tecno", methods=['POST'])
def accion_actualizar_tecno():
    objeto_padre = hsVida.query.filter_by(id=request.form.get('codigo_actualizar')).first()
    for i in range(len(objeto_padre.tecnologias)):
        objeto_padre.tecnologias[i].tipo = request.form.get('tipo{}'.format(i))
        objeto_padre.tecnologias[i].nombre_tecno = request.form.get('nombre_tecno{}'.format(i))
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/eliminar_tecnologica", methods=['POST'])
def eliminar_tecnologica():
    objeto_padre = hsVida.query.filter_by(id=request.form.get('codigo')).first()
    return render_template("eliminar_tecno.html", persona=objeto_padre, len=len(objeto_padre.tecnologias))

@app.route("/accion_eliminar_tecnologica", methods=['POST'])
def accion_eliminar_tecnologica():
    objeto_padre = hsVida.query.filter_by(id=request.form.get('codigo')).first()
    indices_borrar = request.form.getlist('posicion_borrar')

    for i in range(len(indices_borrar)):
        indices_borrar[i] = int(indices_borrar[i])

    for i in sorted(indices_borrar, reverse=True):
        (objeto_padre.tecnologias).pop(i)

    """
    indices_borrar es una lista que contine los cuadritos que se seleccionaron los devuelve de tipo string por
    tanto se convierte a entero en el primer for, luego en el segundo for se borran los elementos de la lista
    objeto_padre.tecnologias lista que contiene las tecnologias que pertenecen a la hoja de vida, en el segundo for
    se le dice que recorra la lista indices_borrar y que i tome el valor de cada elemento de la lista en cada
    iteracion PERO, debido a que si se borra un elemento de la lista los elementos a la derecha se devolveran una 
    casilla y cambiaran el tamaño de la lista, se hace que la lista de indices, primero se 
    organizen de mayor a menor, para que cuando elimine un elemento de dicho indice este sea el ultimo de los elementos
    a borrar y los demas elementos restantes conservaran su indice(posicion) y no se desborda el for con el tamaño de la lista  
    """
    db.session.commit()
    return render_template("agregar_tecno_exito.html", persona = objeto_padre)



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)