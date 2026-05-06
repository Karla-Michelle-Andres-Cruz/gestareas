import flet as ft

def RegistroView(page, auth_controller):
    nombre_input = ft.TextField(label="Nombre", width=350, border_radius=10)
    apellido_input = ft.TextField(label="Apellido", width=350, border_radius=10)
    email_input = ft.TextField(label="Correo electrónico", width=350, border_radius=10)
    pass_input = ft.TextField(label="Contraseña", width=350, border_radius=10, password=True, can_reveal_password=True)

    def registrar_click(e):
        success, msg = auth_controller.registrar_usuario(
            nombre_input.value,
            apellido_input.value,
            email_input.value,
            pass_input.value
        )
        page.snack_bar = ft.SnackBar(ft.Text(msg))
        page.snack_bar.open = True
        if success:
            page.go("/")
        page.update()

    return ft.View(
        route="/registro",
        controls=[
            ft.AppBar(title=ft.Text("SIGE - Registro"), bgcolor=ft.Colors.BLUE_GREY_900),
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.PERSON_ADD, size=48, color=ft.Colors.BLUE),
                    ft.Text("Crear cuenta nueva", size=24, weight="bold"),
                    nombre_input,
                    apellido_input,
                    email_input,
                    pass_input,
                    ft.ElevatedButton("Registrarse", on_click=registrar_click, width=350),
                    ft.TextButton("Ya tengo cuenta", on_click=lambda _: page.go("/"))
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER),
                expand=True,
                alignment=ft.Alignment(0, 0)
            )
        ]
    )