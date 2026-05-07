import flet as ft

def DashboardView(page, auth_ctrl, tarea_ctrl):
    user = page.data.get("user") if page.data else None

    if not user:
        page.go("/")
        return ft.Column([])

    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)

    def completar(id_tarea):
        tarea_ctrl.completar(id_tarea)
        refresh()

    def eliminar(id_tarea):
        tarea_ctrl.eliminar(id_tarea)
        refresh()

    def refresh():
        lista_tareas.controls.clear()
        tareas = tarea_ctrl.obtener_lista(user["id_usuario"])
        if not tareas:
            lista_tareas.controls.append(
                ft.Text("No hay tareas pendientes", color=ft.Colors.GREY_400, italic=True)
            )
        else:
            for t in tareas:
                lista_tareas.controls.append(
                    ft.Card(
                        content=ft.Container(
                            content=ft.ListTile(
                                leading=ft.Checkbox(
                                    value=t["completada"] == 1,
                                    disabled=t["completada"] == 1,
                                    on_change=lambda e, id=t["id_tarea"]: completar(id)
                                ),
                                title=ft.Text(t['titulo'], weight="bold"),
                                subtitle=ft.Text(
                                    f"{t['descripcion'] or ''}\n"
                                    f"Prioridad: {t['prioridad']}  |  {t['clasificacion']}  |  {t['estado']}\n"
                                    f"Fecha límite: {t['fecha_limite'] or 'Sin fecha'}"
                                ),
                                trailing=ft.IconButton(
                                    ft.Icons.DELETE_OUTLINE,
                                    on_click=lambda e, id=t["id_tarea"]: eliminar(id)
                                )
                            ), padding=10
                        )
                    )
                )
        page.update()

    txt_titulo      = ft.TextField(label="Título", expand=True)
    txt_descripcion = ft.TextField(label="Descripción", expand=True)
    dd_prioridad    = ft.Dropdown(
        label="Prioridad", width=120,
        options=[ft.dropdown.Option("baja"), ft.dropdown.Option("media"), ft.dropdown.Option("alta")],
        value="media"
    )
    dd_clasificacion = ft.Dropdown(
        label="Categoría", width=140,
        options=[
            ft.dropdown.Option("personal"), ft.dropdown.Option("trabajo"),
            ft.dropdown.Option("estudio"),  ft.dropdown.Option("hogar"),
            ft.dropdown.Option("salud"),    ft.dropdown.Option("otro"),
        ],
        value="personal"
    )

    def add_task(e):
        if not txt_titulo.value.strip():
            page.snack_bar = ft.SnackBar(ft.Text("El título es obligatorio"), open=True)
            page.update()
            return
        success, msg = tarea_ctrl.guardar_nueva(
            user["id_usuario"],
            txt_titulo.value.strip(),
            txt_descripcion.value.strip(),
            dd_prioridad.value,
            dd_clasificacion.value,
        )
        if success:
            txt_titulo.value = ""
            txt_descripcion.value = ""
            refresh()

    refresh()

    return ft.Column(
        [
            ft.AppBar(
                title=ft.Text(f"Bienvenido, {user['nombre']}"),
                actions=[ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=lambda e: page.go("/"))],
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text("Nueva tarea", size=16, weight="bold"),
                    ft.Row([txt_titulo, txt_descripcion]),
                    ft.Row([
                        dd_prioridad,
                        dd_clasificacion,
                        ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task),
                    ]),
                    ft.Divider(),
                    ft.Text("Mis Tareas pendientes:", size=20, weight="bold"),
                    lista_tareas,
                ], expand=True),
                padding=20,
                expand=True,
            ),
        ],
        expand=True,
    )