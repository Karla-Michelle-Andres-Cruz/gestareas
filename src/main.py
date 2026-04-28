import flet as ft
from controllers.userController import AuthController
from controllers.tareaController import TareaController 
from view.loginView import LoginView
from view.registroView import RegistroView
from view.dashboard import DashboardView

def start(page: ft.Page):
    auth_ctrl = AuthController()
    tarea_ctrl = TareaController()

    def route_change(e):
        print(f" route_change llamado: {page.route}")
        page.views.clear()
        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        elif page.route == "/registro":
            page.views.append(RegistroView(page, auth_ctrl))
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, auth_ctrl, tarea_ctrl))
        page.update()

    page.on_route_change = route_change

    page.views.append(LoginView(page, auth_ctrl))
    page.update()
    
    page.go("/")

def main():
    ft.app(target=start)