# importar el archivo de la conexión a la BD
from configdb import get_connection

def add_user(email, name, passwd ):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("INSERT INTO user (email, name, passwd) VALUES (%s,%s,%s)",(email, name, passwd))
    cnn.commit()
    cnn.close()
    
def update_user( email, name, passwd):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("UPDATE user SET name = %s, passwod = %s WHERE email = %s",(name, passwd, email))
    cnn.commit()
    cnn.close()

