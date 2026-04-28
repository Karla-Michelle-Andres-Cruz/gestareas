import bcrypt
from .dataBase import DataBase

class Usuario:
    def registrar(self, nombre, apellido, email, password, telefono=None):
        conn = DataBase.get_connection()
        cursor = conn.cursor()
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        query = """INSERT INTO usuario (nombre, apellido, email, password, telefono) 
                    VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(query, (nombre, apellido, email, password_hash, telefono))
        conn.commit()
        conn.close()

    def login(self, email, password):
        conn = DataBase.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM usuario WHERE email = %s AND activo = 1"
        cursor.execute(query, (email,))
        usuario = cursor.fetchone()
        conn.close()
        if usuario and bcrypt.checkpw(password.encode('utf-8'), usuario['password'].encode('utf-8')):
            return usuario
        return None

    def buscar_por_id(self, id_usuario):
        conn = DataBase.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario WHERE id_usuario = %s", (id_usuario,))
        resultado = cursor.fetchone()
        conn.close()
        return resultado