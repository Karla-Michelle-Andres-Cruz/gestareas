from models.tareas import Tarea

class TareaController:
    def __init__(self):
        self.model = Tarea()
        
    def obtener_lista(self, id_usuario):
        return self.model.listar_por_usuario(id_usuario)
    
    def guardar_nueva(self, id_usuario, titulo, descripcion, prioridad, clasificacion):
        if not titulo:
            return False, "El titulo es obligatorio"
        
        self.model.crear(id_usuario, titulo, descripcion, prioridad, clasificacion)  # ← quitamos 'self'
        return True, "Tarea guardada"