import bcrypt
from .dataBase import DataBase

class UsuarioModel:
    def __init__(self):
        self.db = DataBase()

    def registrar(self, usuario_data):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(usuario_data.password.encode('utf-8'), salt)
        
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO usuario (nombre, email, password) VALUES (%s, %s, %s)",
                (usuario_data.nombre, usuario_data.email, hashed_password.decode('utf-8'))
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
            
            
    def validar_login(self, email, password):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT password FROM usuario WHERE email = %s", (email,))
            result = cursor.fetchone()
            
            if result:
                stored_password = result[0].encode('utf-8')
                return bcrypt.checkpw(password.encode('utf-8'), stored_password)
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()