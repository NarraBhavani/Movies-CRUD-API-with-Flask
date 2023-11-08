import psycopg2
from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)
def db_conn():
    conn = psycopg2.connect(database="movie", host="localhost", user="postgres", password="Narra", port="5432")
    return conn

@app.route('/')
def index():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM films ORDER BY id''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html',data= data)

@app.route('/create',methods=['GET','POST'])
def create():
    conn=db_conn()
    cur=conn.cursor()
    title=request.form['title']
    director=request.form['director']
    description=request.form['description']
    genre = request.form['genre']
    cur.execute('''INSERT INTO films(title,director,description,genre) VALUES(%s,%s,%s,%s)''',(title,director,description,genre))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update',methods=['GET','POST'])
def update():
    conn=db_conn()
    cur=conn.cursor()

    title=request.form['title']
    director = request.form['director']
    description = request.form['description']
    genre=request.form['genre']
    id=request.form['id']

    cur.execute(
        '''UPDATE films SET title=%s,director=%s,description=%s,genre=%s WHERE id=%s''',(title,director,description,genre,id)
    )
    conn.commit()
    return redirect(url_for('index'))
@app.route('/delete',methods=['GET','POST'])
def delete():
    conn=db_conn()
    cur=conn.cursor()
    id=request.form['id']

    cur.execute('''DELETE FROM films WHERE id=%s''',(id,))
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for('index'))
