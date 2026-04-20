from models.tareas import tareas
class TareaController:
    def __init__(self):
        self.model = tareas()
        
    def btener_lista(self, id_usuario):
        return self.model.listar_por_usuario(id_usuario)
    
    def guardar_nueva(self, id_usuario, titulo, descripcion, prioridad, clasificacion):
        if not titulo:
            return False, "El titulo es obligatorio"
        
        self.model.crear(self, id_usuario, titulo, descripcion, prioridad, clasificacion)
        return True, "Tarea guardada"