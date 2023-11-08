import psycopg2
conn = psycopg2.connect(database="movie",host="localhost",user="postgres",password="Narra",port="5432")
cur=conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS films(id serial PRIMARY KEY,title varchar(100),director varchar(200),description varchar(500),genre varchar(100));''')
cur.execute('''INSERT INTO films(title,director,description,genre) VALUES ('Sir','Venu','Education Based Movie','Drama'),('Dada','Srinu','Emotional Story Of Dad','Drama');''')

conn.commit()
cur.close()
conn.close()