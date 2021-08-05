from flask import Flask, render_template, request, redirect, sessions, url_for, flash
from flask_mysqldb import MySQL
from tkinter import *


app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'us-cdbr-east-04.cleardb.com'
app.config['MYSQL_USER'] = 'bb70a0130dbc04'
app.config['MYSQL_PASSWORD'] = 'f3140c45'
app.config['MYSQL_DB'] = 'heroku_b8e8dcc210fc9f8'



mysql = MySQL(app)


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM condutor")
    data = cur.fetchall()
    cur.execute("SELECT id_veiculo, ano, ano_modelo, fabricante, modelo, renavan, id_condutor FROM veiculo;")
    data1 = cur.fetchall()
    cur.close()
    return render_template('index2.html', veiculo=data1,condutor=data )
  
    
   


@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Condutor cadastrado com Sucesso!!") # quando adciona corretamente no banco 
        id_condutor = request.form['id_condutor']
        name = request.form['nome']
        telefone = request.form['telefone']
        cnh = request.form['cnh']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO condutor (id_condutor, nome, telefone, cnh, email) VALUES (%s, %s, %s, %s, %s)", (id_condutor, name, telefone, cnh, email))
        mysql.connection.commit()
        return redirect(url_for('Index'))


@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Condutor Deletado com Sucesso!!")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM condutor WHERE id_condutor=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))


@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_condutor = request.form['id_condutor']
        nome = request.form['nome']
        telefone = request.form['telefone']
        cnh = request.form['cnh']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE condutor
               SET id_condutor=%s, nome=%s, telefone=%s, cnh=%s, email=%s, 
               WHERE id_condutor=%s
            """, (id_condutor, nome, telefone, cnh, email))
        flash("Condutor atualizado com Sucesso!!")
        mysql.connection.commit()
        return redirect(url_for('Index'))

##if __name__ == "__main__":
##    app.run(debug=True)
#################################veiculo


@app.route('/veiculoinsert', methods = ['POST',])
def veiculoinsert():

    if request.method == "POST":
        flash("Veiculo cadastrado com Sucesso!!") # quando adciona corretamente no banco 
        id_veiculo = request.form['id_veiculo']
        ano = request.form['ano']
        ano_modelo = request.form['ano_modelo']
        fabricante = request.form['fabricante']
        modelo = request.form['modelo']
        renavan = request.form['renavan']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO veiculo (id_veiculo, ano, ano_modelo, fabricante, modelo, renavan) VALUES (%s, %s, %s, %s, %s, %s)", (id_veiculo, ano, ano_modelo, fabricante, modelo, renavan))
        mysql.connection.commit()
        return redirect(url_for('Index'))


@app.route('/deletev/<string:id_data>', methods = ['GET'])
def deletev(id_data):
    flash("Veiculo deletado com Sucesso!!")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM veiculo WHERE id_veiculo=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))


@app.route('/updatev',methods=['POST','GET'])
def updatev():

    if request.method == 'POST':
        id_veiculo = request.form['id_veiculo']
        ano = request.form['ano']
        ano_modelo = request.form['ano_modelo']
        fabricante = request.form['fabricante']
        modelo = request.form['modelo']
        renavan = request.form['renavan']
        id_condutor = request.form['id_condutor']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE veiculo
               SET id_veiculo=%s, ano=%s, ano_modelo=%s, fabricante=%s, modelo=%s, renavan=%s, id_condutor=%s 
               WHERE id_veiculo=%s
            """, (id_veiculo, ano, ano_modelo, fabricante, modelo, renavan, id_condutor))
        flash("Veiculo atualizado com Sucesso!!")
        mysql.connection.commit()
        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)
