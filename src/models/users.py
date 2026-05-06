import bcrypt
from .dataBase import DataBase

class Usuario:
    def registrar(self, nombre, apellido, email, password, telefono=None):
        conn = DataBase.get_connection()
        cursor = conn.cursor()
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')  # ✅ guarda str, no bytes
        query = """INSERT INTO usuario (nombre, apellido, email, password, telefono) 
                    VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(query, (nombre, apellido, email, password_hash, telefono))
        conn.commit()
        cursor.close()  # ✅ cierra cursor antes que la conexión
        conn.close()

    def login(self, email, password):
        conn = DataBase.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario WHERE email = %s AND activo = 1", (email,))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()
        if usuario and bcrypt.checkpw(password.encode('utf-8'), usuario['password'].encode('utf-8')):
            return usuario
        return None

    def buscar_por_id(self, id_usuario):
        conn = DataBase.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario WHERE id_usuario = %s", (id_usuario,))
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()
        return resultado