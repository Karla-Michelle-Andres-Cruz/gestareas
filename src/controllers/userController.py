from models.users import UsuarioModel
from models.schemas import UserSchema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()
        
    def registrar_Usuario(self, nombre, email, contraseña):
        try:
            nuevo_usuario = UsuarioShema(nombre=nombre, email=email, contraseña=contraseña)
            success = self.model.registrar(nuevo_usuario)
            return success, "Usuario creado correctamente"
        except ValidationError as e:
            
            return False, e.errors()[0],{'msg'}