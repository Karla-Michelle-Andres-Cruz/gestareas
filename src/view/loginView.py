import flet as ft

def LoginView(page, auth_controller):
    email_imput = ft.TextField(label="Correo electronico", width=350, border_radius=10)
    pass_imput = ft.TextField(label="Contraseña", width=350, border_radius=10, password=True, can_reveal_password=True)
    
    def login_click(e):
        user, nsg = auth_controller.login(email_imput.value, pass_imput.value)
        if user:
            page.session.set("user", user)
            page.go("/dashboard")
        else:
            page.snack_bar = ft.SnackBar(ft.Text(nsg))
            page.snack_bar.open = True
            page.update()
            
    return ft.View(
        route="/",
        controls=[
            ft.AppBar(title=ft.Text("SIGE - Login"), bgcolor=ft.Colors.BLUE_GREY_900),
            ft.Container(
                content=ft.Column([
                    ft.Icon("lock", size=48, color=ft.Colors.BLUE),
                    ft.Text("Acceso al sistema", size=24, weight="bold"),
                    email_imput,
                    pass_imput,
                    ft.ElevatedButton("Entrar", on_click=login_click, width=350),
                    ft.TextButton("Crear una cuenta nueva", on_click=lambda _: page.go("/registro"))
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER),
                expand=True,
                alignment=ft.Alignment(0, 0)
            )
        ]
    )