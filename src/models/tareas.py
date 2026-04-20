from .database import Database

class TareaModel:
    def __init__(self):
        self.db = Database()
        
    def listar_por_usuario(self, usuario_id):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM tareas WHERE id_usuarios = %s ORDER BY fecha_limite ASC"
        cursor.execute(query, (usuario_id,))
        resultado = cursor.fetchall()
        conn.close()
        return resultado
    
    def crear(self, id_usuarios, titulo, descripcion, prioridad, clasificacion):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO tareas (id_usuarios, titulo, descripcion, prioridad, clasificacion) VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(query, (id_usuarios, titulo, descripcion, prioridad, clasificacion))
        conn.commit()
        conn.close()