import flet as ft

## COLORES - Paleta marrón / café
COLOR_FONDO_VENTANA   = "#1a0f0a"   # fondo de la ventana (marrón muy oscuro)
COLOR_FONDO_CONTAINER = "#2c1810"   # fondo del container principal
COLOR_FONDO_DISPLAY   = "#1a0f0a"   # fondo del área de display
COLOR_TEXTO_RESULT    = "#e8c49a"   # número grande (crema dorado)
COLOR_TEXTO_OP        = "#8b6347"   # operación chica arriba (marrón medio)
COLOR_BTN_NUM         = "#4a2c1a"   # botones numéricos (marrón oscuro)
COLOR_BTN_OP          = "#8b4513"   # botones de operación (marrón silla de montar)
COLOR_BTN_EXTRA       = "#6b4226"   # botones AC +/- % (marrón medio)
COLOR_BTN_TEXT        = "#e8c49a"   # texto de todos los botones (crema)
COLOR_BTN_TEXT_EX     = "#f5deb3"   # texto botones extra (trigo)

## TAMAÑOS
SIZE_RESULT    = 36
SIZE_OP        = 14
BORDER_RADIUS  = 24
PADDING        = 20

def main(page: ft.Page):
    page.title = "Calc App"
    page.window.width = 400
    page.window.height = 520
    page.window.resizable = False
    page.padding = 10
    page.bgcolor = COLOR_FONDO_VENTANA

    operand1 = 0
    operand2 = 0
    operator = ""
    new_operand = True

    operation_display = ft.Text(
        value="",
        color=COLOR_TEXTO_OP,
        size=SIZE_OP,
        font_family="monospace",
        italic=True,
    )
    result = ft.Text(
        value="0",
        color=COLOR_TEXTO_RESULT,
        size=SIZE_RESULT,
        weight=ft.FontWeight.BOLD,
        font_family="monospace",
    )

    def button_clicked(e):
        nonlocal operand1, operand2, operator, new_operand
        data = e.control.content.value

        if data.isdigit() or data == ".":
            if result.value == "0" or new_operand:
                result.value = data
                new_operand = False
            else:
                result.value = result.value + data

        elif data in ["+", "-", "*", "/"]:
            operand1 = float(result.value)
            operator = data
            operation_display.value = f"{operand1} {operator}"
            new_operand = True

        elif data == "=":
            operand2 = float(result.value)
            operation_display.value = f"{operand1} {operator} {operand2} ="
            if operator == "+":
                result.value = str(operand1 + operand2)
            elif operator == "-":
                result.value = str(operand1 - operand2)
            elif operator == "*":
                result.value = str(operand1 * operand2)
            elif operator == "/":
                result.value = str(operand1 / operand2) if operand2 != 0 else "Error"
            new_operand = True

        elif data == "AC":
            result.value = "0"
            operation_display.value = ""
            operand1 = 0
            operand2 = 0
            operator = ""
            new_operand = True

        elif data == "+/-":
            try:
                if float(result.value) > 0:
                    result.value = "-" + result.value
                elif float(result.value) < 0:
                    result.value = result.value[1:]
            except ValueError:
                pass

        elif data == "%":
            result.value = str(float(result.value) / 100)

        page.update()

    def on_keyboard(e: ft.KeyboardEvent):
        nonlocal operand1, operand2, operator, new_operand

        key_map = {
            "0": "0", "1": "1", "2": "2", "3": "3", "4": "4",
            "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
            "Numpad 0": "0", "Numpad 1": "1", "Numpad 2": "2",
            "Numpad 3": "3", "Numpad 4": "4", "Numpad 5": "5",
            "Numpad 6": "6", "Numpad 7": "7", "Numpad 8": "8",
            "Numpad 9": "9",
            ".": ".", ",": ".", "Numpad Decimal": ".",
            "+": "+", "-": "-", "*": "*", "/": "/",
            "Numpad Add": "+", "Numpad Subtract": "-",
            "Numpad Multiply": "*", "Numpad Divide": "/",
            "Enter": "=", "Numpad Enter": "=",
            "Escape": "AC", "Backspace": "AC",
            "%": "%",
        }

        key = e.key
        if key not in key_map:
            return
        data = key_map[key]

        if data.isdigit() or data == ".":
            if result.value == "0" or new_operand:
                result.value = data
                new_operand = False
            else:
                result.value = result.value + data

        elif data in ["+", "-", "*", "/"]:
            operand1 = float(result.value)
            operator = data
            operation_display.value = f"{operand1} {operator}"
            new_operand = True

        elif data == "=":
            operand2 = float(result.value)
            operation_display.value = f"{operand1} {operator} {operand2} ="
            if operator == "+":
                result.value = str(operand1 + operand2)
            elif operator == "-":
                result.value = str(operand1 - operand2)
            elif operator == "*":
                result.value = str(operand1 * operand2)
            elif operator == "/":
                result.value = str(operand1 / operand2) if operand2 != 0 else "Error"
            new_operand = True

        elif data == "AC":
            result.value = "0"
            operation_display.value = ""
            operand1 = 0
            operand2 = 0
            operator = ""
            new_operand = True

        elif data == "%":
            result.value = str(float(result.value) / 100)

        page.update()

    page.on_keyboard_event = on_keyboard

    class CalcButton(ft.Button):
        def __init__(self, content, on_click, expand=1, bgcolor=None, color=None):
            super().__init__(
                content=ft.Text(
                    content,
                    weight=ft.FontWeight.W_600,
                    font_family="monospace",
                    size=16,
                ),
                on_click=on_click,
                expand=expand,
                bgcolor=bgcolor,
                color=color,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=14),
                    overlay_color=ft.Colors.with_opacity(0.15, ft.Colors.WHITE),
                ),
            )

    class DigitButton(CalcButton):
        def __init__(self, content, expand=1):
            super().__init__(
                content=content,
                on_click=button_clicked,
                expand=expand,
                bgcolor=COLOR_BTN_NUM,
                color=COLOR_BTN_TEXT,
            )

    class ActionButton(CalcButton):
        def __init__(self, content, expand=1):
            super().__init__(
                content=content,
                on_click=button_clicked,
                expand=expand,
                bgcolor=COLOR_BTN_OP,
                color=COLOR_BTN_TEXT,
            )

    class ExtraActionButton(CalcButton):
        def __init__(self, content, expand=1):
            super().__init__(
                content=content,
                on_click=button_clicked,
                expand=expand,
                bgcolor=COLOR_BTN_EXTRA,
                color=COLOR_BTN_TEXT_EX,
            )

    page.add(
        ft.Container(
            width=370,
            bgcolor=COLOR_FONDO_CONTAINER,
            border_radius=BORDER_RADIUS,
            padding=PADDING,
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=20,
                color=ft.Colors.with_opacity(0.5, ft.Colors.BLACK),
                offset=ft.Offset(0, 6),
            ),
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Container(
                        bgcolor=COLOR_FONDO_DISPLAY,
                        border_radius=16,
                        padding=ft.Padding(left=16, right=16, top=12, bottom=12),
                        content=ft.Column(
                            spacing=2,
                            horizontal_alignment=ft.CrossAxisAlignment.END,
                            controls=[
                                ft.Row(
                                    controls=[operation_display],
                                    alignment=ft.MainAxisAlignment.END,
                                ),
                                ft.Row(
                                    controls=[result],
                                    alignment=ft.MainAxisAlignment.END,
                                ),
                            ],
                        ),
                    ),
                    ft.Row(spacing=8, controls=[
                        ExtraActionButton(content="AC"),
                        ExtraActionButton(content="+/-"),
                        ExtraActionButton(content="%"),
                        ActionButton(content="/"),
                    ]),
                    ft.Row(spacing=8, controls=[
                        DigitButton(content="7"),
                        DigitButton(content="8"),
                        DigitButton(content="9"),
                        ActionButton(content="*"),
                    ]),
                    ft.Row(spacing=8, controls=[
                        DigitButton(content="4"),
                        DigitButton(content="5"),
                        DigitButton(content="6"),
                        ActionButton(content="-"),
                    ]),
                    ft.Row(spacing=8, controls=[
                        DigitButton(content="1"),
                        DigitButton(content="2"),
                        DigitButton(content="3"),
                        ActionButton(content="+"),
                    ]),
                    ft.Row(spacing=8, controls=[
                        DigitButton(content="0", expand=2),
                        DigitButton(content="."),
                        ActionButton(content="="),
                    ]),
                ],
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)
