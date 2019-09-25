import psycopg2

#Criando a conexão com o PostgreSQL
conn = psycopg2.connect(host='localhost', database='Users',
user='postgres', password='dnr@2016')

#Abrindo o cursor 
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Usuarios(
    ID Serial PRIMARY KEY,
    Nome VARCHAR(80) NOT NULL,
    Email VARCHAR(50) NOT NULL,
    Usuario VARCHAR(30) NOT NULL,
    Senha VARCHAR(30) NOT NULL
);
""")

conn.commit()

print("Conectado ao PostgreSQL")