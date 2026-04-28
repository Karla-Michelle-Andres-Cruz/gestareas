import flet as ft

def LoginView(page, auth_controller):
    email_imput = ft.TextField(label="Correo electronico", width=350, border_radius=10)
    pass_imput = ft.TextField(label="Contraseña", width=350, border_radius=10, password=True, can_reveal_password=True)
    
    def login_click(e):
        if not email_imput.value or not pass_imput.value:
            page.show_dialog(ft.SnackBar(ft.Text("Por favor, complete todos los campos")))
            
            return
        
        user, msg = auth_controller.login(email_imput.value, pass_imput.value)
        
        if user:
            page.user_data = user
            page.go("/dashboard")
        else:
            page.show_dialog(ft.SnackBar(ft.Text(msg)))



    return ft.View(
        route="/",
        vertical_alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar = ft.AppBar(
            title=ft.Text("SIGE - Login"),
            bgcolor=ft.Colors.BLUE_GREY_900
        ),
        controls=[
            ft.Icon(ft.Icons.LOCK, size=48, color=ft.Colors.BLUE),
            ft.Text("Acceso al sistema", size=24, weight="bold"),
            email_imput,
            pass_imput,
            ft.ElevatedButton("Entrar", on_click=login_click, width=350),
            ft.TextButton("Crear una cuenta nueva", on_click=lambda _: page.go("/registro"))
        ]
    )