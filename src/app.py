from flask import Flask, render_template, request,redirect ,url_for, flash
# from flask import MySQL
from .db import mysql

app = Flask(__name__)
# Settings
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/PaginaI')
def login():
    return render_template('PaginaI.html')

@app.route('/Crear-Notas')
def CNota():    
    return render_template('Crear-Notas.html')

@app.route('/Crear-Notas')
def CN():
    return render_template('Crear-Notas.html')

@app.route('/crearnota/')
def CrearN():
    return render_template('Crear-Notas.html')

@app.route('/Crear-TipoNota/')
def CTipoNot():
    return render_template('Crear-TipoNota.html')

@app.route('/Crear-TipoNota')
def CTipoNota():
    return render_template('Crear-TipoNota.html')


@app.route('/NotasUsuarios/')
def NotasUsuarios():
    cur = mysql.connection.cursor()
    cur.execute("""
    SELECT IdTipoUsuario,NOMBRE,IdTipoNota, Titulo, Contenido, IdNota 
        FROM Usuario INNER JOIN NotaU 
            INNER JOIN Notas INNER JOIN TipoNota 
            INNER JOIN TipoUsuario
            ON Usuario.IdUsuario = NotaU.IdUsuarioU 
            AND Notas.IdNotas = NotaU.IdNotaU 
            AND TipoNota.IdTipoNota = Notas.IdTipoNotaN 
            AND TipoUsuario.IdTipoUsuario = Usuario.IdTipoUsuarioU;
    """)
    data = cur.fetchall()
    return render_template('NotasUsuarios.html', usuar = data)

#Ingresar a la aplicacion
@app.route('/Ingresar', methods=['POST'])
def Ingresar():
        correo = request.form['correo']
        contrasena = request.form['contrasena'] 
        cur = mysql.connection.cursor()
        cur.execute("SELECT IdUsuario FROM Usuario WHERE EMAIL ='"+ correo +"' AND CONTRASENA = '"+ contrasena +"'")
        data = cur.fetchall()
        if len(data) == 1:
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM TipoNota')
            tipno = cur.fetchall()
            cur.execute('SELECT * FROM Notas')
            data = cur.fetchall()
            cur.execute('SELECT * FROM Usuario')
            usuar = cur.fetchall()
            return render_template('MisNotas.html', nos = data, usua = usuar, no = tipno )
        else:
            return render_template('index.html')

#Crear Usuario
@app.route('/CrearUsuario', methods=['POST'])
def CrearUsuario():
    tipo = request.form['tipo']
    nombre = request.form['nombre']
    correo = request.form['correo']
    contrasena = request.form['contrasena'] 
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO Usuario (IdTipoUsuarioU,NOMBRE, EMAIL, CONTRASENA) VALUES (%s, %s, %s, %s)', (tipo,nombre, correo, contrasena))
    mysql.connection.commit()
    flash('Usuario Añadido')
    return render_template('index.html')
#Crear Tipo Usuario
@app.route('/CrearTipoUsuario', methods=['POST'])
def CrearTipoUsuario():
    tipo = request.form['tip']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO TipoUsuario (IdTipoUsuario) VALUES ('"+ tipo +"')")
    mysql.connection.commit()
    flash('Tipo de Usuario Añadido')
    return render_template('index.html')
#Pagina Principal
@app.route('/MisNotas')
def MisNotas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM TipoNota')
    tipno = cur.fetchall()
    cur.execute('SELECT * FROM Notas')
    data = cur.fetchall()
    cur.execute('SELECT * FROM Usuario')
    usuar = cur.fetchall()
    return render_template('MisNotas.html', nos = data, usua = usuar, no = tipno )
#Agregar Notas
@app.route('/add_notas', methods=['POST'])
def add_notas():
    if request.method == 'POST':
        tipo = request.form['tipo']
        titulo = request.form['titulo']
        texton = request.form['texton']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Notas (IdTipoNotaN,Titulo, Contenido) VALUES ('"+ tipo +"','"+ titulo +"', '"+ texton +"')")
        mysql.connection.commit()
        flash('Elemento Añadido')
        return redirect(url_for('MisNotas'))
#Agregar Tipo de Nota
@app.route('/add_tiponota', methods=['POST'])
def add_tiponota():
    if request.method == 'POST':
        tipo = request.form['tipo']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO TipoNota (IdTipoNota) VALUES ('"+ tipo +"')")
        mysql.connection.commit()
        flash('Elemento Añadido')
        return redirect(url_for('MisNotas'))

add_tiponota

#Agregar Notas con Usuarios
@app.route('/add_notasu', methods=['POST'])
def add_notasu():
    if request.method == 'POST':
        nombreu = request.form['nombreu']
        titulo = request.form['titulo']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO NotaU (IdNotaU, IdUsuarioU) VALUES ('" + nombreu +"','" + titulo +"')")
        mysql.connection.commit()
        return redirect(url_for('MisNotas'))

#Editar Notas
@app.route('/edit/<string:id>')
def get_notas(id):
    #Solucionar error de
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Notas WHERE IdNotas = {0}'.format(id))
    data = cur.fetchall()
    return render_template('edit-notas.html', no = data[0])

#Editar Notas
@app.route('/update/<id>', methods = ['POST'])
def update_notas(id):
    if request.method == 'POST':
        tipo = request.form['tipo']
        titulo = request.form['titulo']
        texton = request.form['texton'] 
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE Notas 
        SET IdTipoNotaN = %s,
            Titulo = %s, 
            Contenido = %s
        WHERE IdNotas = %s
        """, (tipo,titulo, texton, id))
        mysql.connection.commit()
        flash('Actualización Exitosa')
        return redirect(url_for('MisNotas'))

#Eliminar Nota
@app.route('/delete/<string:id>')
def delete_notas(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Notas WHERE IdNotas = {0}'.format(id))
    mysql.connection.commit()
    flash('Elemento Eliminado')
    return redirect(url_for('MisNotas'))

#Eliminar NotaU
@app.route('/deleteu/<string:id>')
def delete_notau(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM NotaU WHERE IdNota = {0}'.format(id))
    mysql.connection.commit()
    flash('Elemento Eliminado')
    return redirect(url_for('NotasUsuarios'))


@app.route('/MisNotas')
def misn():
    return render_template('MisNotas.html')
