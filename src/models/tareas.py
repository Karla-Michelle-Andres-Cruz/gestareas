from .dataBase import DataBase

class Tarea:
    def listar_por_usuario(self, id_usuario):
        conn = DataBase.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM tareas WHERE id_usuario = %s ORDER BY fecha_limite ASC"
        cursor.execute(query, (id_usuario,))
        resultado = cursor.fetchall()
        conn.close()
        return resultado

    def crear(self, id_usuario, titulo, descripcion, prioridad, clasificacion, fecha_limite=None, hora_limite=None):
        conn = DataBase.get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO tareas (id_usuario, titulo, descripcion, prioridad, clasificacion, fecha_limite, hora_limite) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (id_usuario, titulo, descripcion, prioridad, clasificacion, fecha_limite, hora_limite))
        conn.commit()
        conn.close()

    def completar(self, id_tarea):
        conn = DataBase.get_connection()
        cursor = conn.cursor()
        query = """UPDATE tareas SET completada = 1, estado = 'completada', 
                    fecha_completada = CURRENT_TIMESTAMP WHERE id_tarea = %s"""
        cursor.execute(query, (id_tarea,))
        conn.commit()
        conn.close()

    def eliminar(self, id_tarea):
        conn = DataBase.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tareas WHERE id_tarea = %s", (id_tarea,))
        conn.commit()
        conn.close()