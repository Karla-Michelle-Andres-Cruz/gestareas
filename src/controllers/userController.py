from models.users import Usuario
from models.schemas import UserSchema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = Usuario()
        
    def registrar_usuario(self, nombre, apellido, email, password):
        try:
            nuevo_usuario = UserSchema(
                nombre=nombre,
                apellido=apellido,
                email=email,
                password=password
            )
            self.model.registrar(
                nombre=nuevo_usuario.nombre,
                apellido=nuevo_usuario.apellido,
                email=nuevo_usuario.email,
                password=nuevo_usuario.password
            )
            return True, "Usuario creado correctamente"
        except ValidationError as e:
            return False, e.errors()[0]['msg']
        
    def login(self, email, password):
        try:
            usuario = self.model.login(email, password)
            if usuario:
                return usuario, "Bienvenido"
            return None, "Correo o contraseña incorrectos"
        except Exception as e:
                return None, str(e)