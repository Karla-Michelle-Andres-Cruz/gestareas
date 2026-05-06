import flet as ft

def LoginView(page, auth_controller):
    email_input = ft.TextField(label="Correo electrónico", width=350, border_radius=10)
    pass_input = ft.TextField(label="Contraseña", width=350, border_radius=10, password=True, can_reveal_password=True)

    def login_click(e):
        if not email_input.value or not pass_input.value:
            page.open(ft.SnackBar(ft.Text("Por favor, complete todos los campos")))
            return

        user, msg = auth_controller.login(email_input.value, pass_input.value)

        if user:
            page.data = {"user": user}
            page.go("/dashboard")
        else:
            page.open(ft.SnackBar(ft.Text(msg)))

    return ft.View(
        route="/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("SIGE - Login"),
            bgcolor=ft.Colors.BLUE_GREY_900
        ),
        controls=[
            ft.Icon(ft.Icons.LOCK, size=48, color=ft.Colors.BLUE),
            ft.Text("Acceso al sistema", size=24, weight="bold"),
            email_input,
            pass_input,
            ft.ElevatedButton("Entrar", on_click=login_click, width=350),
            ft.TextButton("Crear una cuenta nueva", on_click=lambda _: page.go("/registro"))
        ]
    )