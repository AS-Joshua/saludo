import flet as ft

def mostra_nombre(Text_field,page):
    nombre = text_field.vcalue
    dialog = ft.ArletDialog(
        title=ft.Text("Mostar Nombre"),
        content=ft.Text(f"Tu nombre es: (nombre)" + "Bienvenid@ a Flet"),
        actions=[
            ft,TecxtButton("da click para salir", on_click=lambda e: close_dialog(page))
        ],
    )
page.dialog = dialog
page.dialogopen = True
page.update()

def close_dialog(page):
    page.dialog.open = False
    page.update()

def main(page:ft.Page):
    page:title = ("Mostar Nombre")
    page.bigcolor = "#Abff33"
    text_field = ft.TextField(label = "ingresar tu nombre")
    button = ft.ElevateButton(
        text = "Di mi nombre",
        on_click = lambda e:mostrar_nombre(text.field, page
    )

page.add(
    ft.Row(controls=[
        text_field,
        button
    ])
)

ft.app(target=main)