[README.md](https://github.com/user-attachments/files/27732137/README.md)
# 🧮 Calc App

> Calculadora de escritorio construida con **Python + Flet**, con paleta de colores marrón/café y soporte para variables personalizadas.

---

## ✨ Características

- Operaciones básicas: suma, resta, multiplicación y división
- Soporte para decimales y porcentajes
- Cambio de signo (`+/-`)
- Historial de operación en pantalla
- **Teclado físico** compatible (incluyendo teclado numérico)
- Variables personalizadas **A** y **B** definibles por el usuario
- Diseño oscuro con paleta marrón elegante
- Ventana fija y compacta

---

## 🖥️ Requisitos

- Python 3.10 o superior
- Flet 0.80 o superior

---

## 🚀 Instalación

```bash
# 1. Clonar o descargar el proyecto
cd "scada flet"

# 2. Crear entorno virtual
py -m venv venv

# 3. Activar entorno virtual
.\venv\Scripts\Activate.ps1

# 4. Instalar dependencias
pip install flet
```

---

## ▶️ Uso

```bash
python calcu.py
```

---

## ⌨️ Atajos de teclado

| Tecla | Acción |
|---|---|
| `0` — `9` | Ingresar dígitos |
| `.` `,` | Punto decimal |
| `+` `-` `*` `/` | Operaciones |
| `Enter` | Igual `=` |
| `Escape` / `Backspace` | Limpiar (AC) |
| `%` | Porcentaje |
| Teclado numérico | Compatible completo |

---

## 🎨 Paleta de colores

| Elemento | Hex | Vista |
|---|---|---|
| Fondo ventana | `#1a0f0a` | ███ |
| Container | `#2c1810` | ███ |
| Display | `#1a0f0a` | ███ |
| Texto resultado | `#e8c49a` | ███ |
| Botones numéricos | `#4a2c1a` | ███ |
| Botones operadores | `#8b4513` | ███ |
| Botones AC/+/-/% | `#6b4226` | ███ |

> Todos los colores y tamaños están centralizados al inicio del archivo `calcu.py` para fácil personalización.

---

## 📁 Estructura del proyecto

```
scada flet/
│
├── calcu.py        # Código principal de la app
├── README.md       # Este archivo
└── venv/           # Entorno virtual (no subir a git)
```

---

## 🔧 Personalización

Al inicio de `calcu.py` encontrás todas las variables de estilo:

```python
COLOR_FONDO_VENTANA   = "#1a0f0a"
COLOR_BTN_OP          = "#8b4513"
SIZE_RESULT           = 36
BORDER_RADIUS         = 24
# ... y más
```

Cambiá los valores hex por cualquier color que quieras sin tocar el resto del código.

---

## 📌 Notas

- El entorno virtual `venv/` no debe subirse a Git. Agregalo al `.gitignore`.
- Probado en Windows 11 con Python 3.13 y Flet 0.85.

---

<p align="center">Hecho con ☕ y Python</p>
