import flet as ft

def DashboardView(page, auth_ctrl, tarea_ctrl):
    user = page.session.get("user")
    
    # ✅ Si no hay sesión, redirige al login
    if not user:
        page.go("/")
        return ft.View("/dashboard", [])

    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
    
    def refresh():
        lista_tareas.controls.clear()
        for t in tarea_ctrl.obtener_lista(user["id_usuario"]):
            lista_tareas.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.ListTile(
                            title=ft.Text(t['titulo'], weight="bold"),       # ✅ minúsculas
                            subtitle=ft.Text(f"{t['descripcion']}\nPrioridad: {t['prioridad']}"),  # ✅ minúsculas
                            trailing=ft.Badge(
                                content=ft.Text(t['estado']),
                                bgcolor=ft.Colors.ORANGE_300               # ✅ mayúsculas
                            )
                        ), padding=10
                    )
                )
            )
        page.update()

    txt_titulo = ft.TextField(label="Título", expand=True)
    
    def add_task(e):
        success, msg = tarea_ctrl.guardar_nueva(
            user["id_usuario"], txt_titulo.value, "", "media", "trabajo"
        )
        if success:
            txt_titulo.value = ""
            refresh()

    refresh()
            
    return ft.View("/dashboard", [
        ft.AppBar(
            title=ft.Text(f"Bienvenido, {user['nombre']}"),
            actions=[ft.IconButton("exit_to_app", on_click=lambda e: page.go("/"))],
        ),
        ft.Column([
            ft.Row([txt_titulo, ft.FloatingActionButton("add", on_click=add_task)]),
            ft.Divider(),
            ft.Text("Mis Tareas pendientes:", size=20, weight="bold"),
            lista_tareas
        ], expand=True, padding=20),
    ], on_resume=lambda _: refresh())