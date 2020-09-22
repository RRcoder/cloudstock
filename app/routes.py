from flask import render_template, Response, request
from app import app, mysql

@app.route('/')
def index():
    #return ('hello')

    return render_template('index.html')

@app.route('/add_stk')
def add_stk():
    return render_template('add_stk.html')

@app.route('/add_stk', methods=['POST'])
def add_stk_post():
    if request.method=='POST':
        codigo = request.form['codigo']
        descrip= request.form['descrip']
        tipoped= request.form['tipoped']
        saldo  = request.form['saldo']
        aplica = request.form['aplica']
   
        cur = mysql.connection.cursor()
        sql= "insert into rstk (codigo, descrip, tipoped, saldo, aplica, activo) values (%s, %s, %s, %s, %s, %s)"
        cur.execute(sql, (codigo, descrip, tipoped, float(saldo), aplica, 'S'))
        mysql.connection.commit()
    return render_template('list_stk.html')

@app.route('/list_stk')
def list_stk():
    cur = mysql.connection.cursor()
    sql= "select id, codigo, descrip, tipoped, saldo, aplica, activo from rstk;"
    cur.execute(sql)
    datos=cur.fetchall()
    
    return render_template('list_stk.html', datos = datos)

@app.route('/link2')
def link2():
    #return ('hello')

    return render_template('link2.html')

@app.route('/prueba')
def prueba():
    #return ('hello')

    return render_template('prueba.html')

