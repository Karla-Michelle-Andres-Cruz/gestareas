from models.tareas import Tarea

class TareaController:
    def __init__(self):
        self.model = Tarea()
        
    def obtener_lista(self, id_usuario):
        return self.model.listar_por_usuario(id_usuario)
    
    def guardar_nueva(self, id_usuario, titulo, descripcion, prioridad, clasificacion, fecha_limite=None, hora_limite=None):
        if not titulo:
            return False, "El titulo es obligatorio"
        self.model.crear(id_usuario, titulo, descripcion, prioridad, clasificacion, fecha_limite, hora_limite)
        return True, "Tarea guardada"
    
    def eliminar(self, id_tarea):
        self.model.eliminar(id_tarea)
        return True, "Tarea eliminada"
    
    def completar(self, id_tarea):
        self.model.completar(id_tarea)
        return True, "Tarea completada"