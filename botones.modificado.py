import flet as ft
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import tempfile
import os
import re

def main(page: ft.Page):

    page.title = "Sistema Escolar"
    page.window_width = 1000
    page.window_height = 800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    def crear_grafica(funcion_str, limite_inf, limite_sup, resultado):
        """Crea una gráfica de la función y el área bajo la curva"""
        try:
            funcion_eval = funcion_str.replace('^', '**')
            x = np.linspace(limite_inf - 1, limite_sup + 1, 1000)
            
            def f(x_val):
                return eval(funcion_eval, {"x": x_val, "np": np, "sin": np.sin, "cos": np.cos, 
                                         "exp": np.exp, "log": np.log, "sqrt": np.sqrt,
                                         "__builtins__": {}}, {})
            
            y = []
            for xi in x:
                try:
                    yi = f(xi)
                    if np.isinf(yi) or np.isnan(yi) or abs(yi) > 1e6:
                        yi = 0
                    y.append(yi)
                except:
                    y.append(0)
            y = np.array(y)
            
            fig, ax = plt.subplots(figsize=(10, 6))
            fig.patch.set_facecolor('#f5f5f5')
            ax.set_facecolor('#ffffff')
            
            ax.plot(x, y, 'b-', linewidth=2.5, label=f'f(x) = {funcion_str}', zorder=3)
            
            try:
                x_fill = np.linspace(limite_inf, limite_sup, 500)
                y_fill = []
                for xi in x_fill:
                    try:
                        yi = f(xi)
                        if np.isinf(yi) or np.isnan(yi) or abs(yi) > 1e6:
                            yi = 0
                        y_fill.append(yi)
                    except:
                        y_fill.append(0)
                y_fill = np.array(y_fill)
                if np.max(np.abs(y_fill)) < 1e6:
                    ax.fill_between(x_fill, 0, y_fill, alpha=0.3, color='green', 
                                   label=f'Área = {resultado:.4f}', zorder=2)
            except:
                pass
            
            ax.axvline(x=limite_inf, color='red', linestyle='--', alpha=0.7, linewidth=2)
            ax.axvline(x=limite_sup, color='orange', linestyle='--', alpha=0.7, linewidth=2)
            
            ax.grid(True, alpha=0.3, linestyle='--')
            ax.set_xlabel('x', fontsize=12, fontweight='bold')
            ax.set_ylabel('f(x)', fontsize=12, fontweight='bold')
            ax.set_title(f'Área bajo la curva f(x) = {funcion_str}', fontsize=14, fontweight='bold', pad=20)
            ax.legend(loc='upper right', framealpha=0.9)
            ax.axhline(y=0, color='black', linestyle='-', linewidth=0.8, zorder=1)
            ax.axvline(x=0, color='black', linestyle='-', linewidth=0.8, zorder=1)
            
            y_finite = y[np.isfinite(y)]
            if len(y_finite) > 0:
                y_min = min(np.min(y_finite), 0) - 1
                y_max = np.max(y_finite) + 1
                if y_max - y_min > 100:
                    y_max = min(y_max, 50)
                    y_min = max(y_min, -50)
                ax.set_ylim(y_min, y_max)
            
            plt.tight_layout()
            
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
            plt.savefig(temp_file.name, format='png', dpi=100, bbox_inches='tight', facecolor='#f5f5f5')
            temp_file.close()
            plt.close(fig)
            
            imagen = ft.Image(src=temp_file.name, width=800, height=500)
            
            import threading
            def eliminar_temp():
                try:
                    if os.path.exists(temp_file.name):
                        os.unlink(temp_file.name)
                except:
                    pass
            
            threading.Timer(5.0, eliminar_temp).start()
            return imagen
        
        except Exception as e:
            print(f"Error en gráfica: {str(e)}")
            return ft.Text(f"No se pudo generar la gráfica: {str(e)[:100]}", color="red", size=14)

    def mostrar_materia_ejemplo(nombre, descripcion):
        page.clean()
        grafica = crear_grafica("x^2 + 2", 1, 3, 38/3)
        
        page.add(
            ft.Column(
                [
                    ft.Text(nombre, size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    ft.Text(descripcion, size=18, text_align=ft.TextAlign.CENTER),
                    ft.Divider(height=20),
                    ft.Text("Gráfica del área bajo la curva:", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    grafica,
                    ft.Divider(height=20),
                    ft.ElevatedButton(
                        "Volver al menú",
                        on_click=lambda e: menu_principal()
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                scroll=ft.ScrollMode.AUTO
            )
        )

    def mostrar_infografia_movimiento(e):
        """Infografía original para Movimiento y estabilidad (ANC)"""
        page.clean()
        
        pasos = [
            {
                "numero": "1",
                "titulo": "Captura del sonido",
                "descripcion": "Los micrófonos externos del audífono detectan el ruido ambiental (onda original).",
                "color": ft.Colors.BLUE_400
            },
            {
                "numero": "2",
                "titulo": "Procesamiento",
                "descripcion": "El chip interno calcula la frecuencia y amplitud de la onda contaminante.",
                "color": ft.Colors.INDIGO_400
            },
            {
                "numero": "3",
                "titulo": "Interferencia Destructiva",
                "descripcion": "El audífono genera una onda idéntica pero con la fase invertida (desfase de 180°).",
                "color": ft.Colors.PURPLE_400
            },
            {
                "numero": "4",
                "titulo": "Resultado",
                "descripcion": "Al colisionar la cresta con el valle, se anulan mutuamente, logrando silencio.",
                "color": ft.Colors.GREEN_400
            }
        ]
        
        tarjetas = []
        for paso in pasos:
            tarjeta = ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Text(
                                            paso["numero"],
                                            size=18,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.Colors.WHITE
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                                ),
                                width=40,
                                height=40,
                                bgcolor=paso["color"],
                                border_radius=20,
                            ),
                            ft.Text(
                                paso["titulo"],
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.CENTER
                            ),
                            ft.Text(
                                paso["descripcion"],
                                size=16,
                                text_align=ft.TextAlign.CENTER
                            ),
                        ],
                        spacing=10,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    padding=20,
                    width=350,
                ),
                elevation=5,
            )
            tarjetas.append(tarjeta)
        
        fila1 = ft.Row(tarjetas[:2], alignment=ft.MainAxisAlignment.CENTER, spacing=30)
        fila2 = ft.Row(tarjetas[2:], alignment=ft.MainAxisAlignment.CENTER, spacing=30)
        
        ondas = ft.Container(
            content=ft.Text(
                "〰️ 〰️ 〰️ ONDAS SONORAS 〰️ 〰️ 〰️",
                size=18,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_600
            ),
            padding=20,
            bgcolor=ft.Colors.BLUE_50,
            border_radius=20,
        )
        
        page.add(
            ft.Column(
                [
                    ft.Text(
                        "Movimiento y estabilidad",
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.INDIGO_700
                    ),
                    ft.Text(
                        "CANCELACIÓN ACTIVA DE RUIDO (ANC) EN AUDÍFONOS",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.INDIGO_500
                    ),
                    ft.Divider(height=20, color=ft.Colors.INDIGO_200),
                    ondas,
                    ft.Text(
                        "PROCESO EXPLICADO PASO A PASO:",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER
                    ),
                    fila1,
                    fila2,
                    ft.Divider(height=30),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(
                                    "¿CÓMO FUNCIONA FÍSICAMENTE?",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    text_align=ft.TextAlign.CENTER
                                ),
                                ft.Text(
                                    "La cancelación activa de ruido se basa en el principio de SUPERPOSICIÓN DE ONDAS. "
                                    "Cuando dos ondas sonoras de igual amplitud pero fase opuesta se encuentran, "
                                    "se anulan mutuamente (interferencia destructiva), resultando en una reducción significativa del ruido percibido.",
                                    size=16,
                                    text_align=ft.TextAlign.CENTER
                                ),
                            ],
                            spacing=10,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        padding=20,
                        bgcolor=ft.Colors.GREY_100,
                        border_radius=15,
                        width=700,
                    ),
                    ft.ElevatedButton(
                        "Volver al menú",
                        on_click=lambda e: menu_principal()
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=25,
                scroll=ft.ScrollMode.AUTO
            )
        )

    def mostrar_infografia_organismos(e):
        """Infografía original para Organismos, Estructuras y Procesos (Digestión)"""
        page.clean()
        
        etapas = [
            {
                "nombre": "INGESTIÓN",
                "descripcion": "Entrada de comida. Comienza la digestión mecánica (dientes) y química (enzimas salivares).",
                "duracion": "5-10 segundos",
                "organo": "Boca",
                "color": ft.Colors.ORANGE_400,
                "numero": "1"
            },
            {
                "nombre": "DIGESTIÓN",
                "descripcion": "Degradación de alimentos en el estómago mediante jugos gástricos ácidos para romper proteínas.",
                "duracion": "2-4 horas",
                "organo": "Estómago",
                "color": ft.Colors.RED_400,
                "numero": "2"
            },
            {
                "nombre": "ABSORCIÓN",
                "descripcion": "Ocurre en el intestino delgado. Las vellosidades absorben nutrientes (glucosa, aminoácidos) hacia la sangre.",
                "duracion": "4-6 horas",
                "organo": "Intestino delgado",
                "color": ft.Colors.GREEN_400,
                "numero": "3"
            },
            {
                "nombre": "EGESTIÓN",
                "descripcion": "El intestino grueso compacta los desechos no utilizables para su posterior eliminación.",
                "duracion": "12-48 horas",
                "organo": "Intestino grueso",
                "color": ft.Colors.BROWN_400,
                "numero": "4"
            }
        ]
        
        elementos_timeline = []
        for i, etapa in enumerate(etapas):
            es_ultimo = i == len(etapas) - 1
            
            tarjeta = ft.Container(
                content=ft.Row(
                    [
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Text(
                                        etapa["numero"],
                                        size=16,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.WHITE
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            width=40,
                            height=40,
                            bgcolor=etapa["color"],
                            border_radius=20,
                        ),
                        ft.Column(
                            [
                                ft.Text(etapa["nombre"], size=22, weight=ft.FontWeight.BOLD, color=etapa["color"], text_align=ft.TextAlign.CENTER),
                                ft.Text(etapa["descripcion"], size=14, text_align=ft.TextAlign.CENTER),
                                ft.Row(
                                    [
                                        ft.Text(f"⏱️ {etapa['duracion']}", size=12, italic=True),
                                        ft.Text(f"📍 {etapa['organo']}", size=12, italic=True),
                                    ],
                                    spacing=20,
                                    alignment=ft.MainAxisAlignment.CENTER
                                )
                            ],
                            spacing=8,
                            expand=True,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        )
                    ],
                    spacing=20,
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                padding=15,
                bgcolor=ft.Colors.WHITE,
                border_radius=15,
            )
            
            elementos_timeline.append(tarjeta)
            
            if not es_ultimo:
                flecha = ft.Container(
                    content=ft.Text("▼", size=30, color=ft.Colors.GREY_400),
                    padding=5
                )
                elementos_timeline.append(flecha)
        
        resumen = ft.Container(
            content=ft.Column(
                [
                    ft.Text("DATOS INTERESANTES:", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    ft.Text("• El intestino delgado mide aproximadamente 6-7 metros", size=14, text_align=ft.TextAlign.CENTER),
                    ft.Text("• El estómago puede expandirse hasta 1.5 litros", size=14, text_align=ft.TextAlign.CENTER),
                    ft.Text("• La digestión total puede tomar entre 24 y 72 horas", size=14, text_align=ft.TextAlign.CENTER),
                    ft.Text("• Las vellosidades intestinales aumentan 10 veces la superficie de absorción", size=14, text_align=ft.TextAlign.CENTER),
                ],
                spacing=8,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=20,
            bgcolor=ft.Colors.GREEN_50,
            border_radius=15,
            width=600,
        )
        
        page.add(
            ft.Column(
                [
                    ft.Text(
                        "Organismos, Estructuras y Procesos",
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.GREEN_700
                    ),
                    ft.Text(
                        "EL PROCESO DE ALIMENTACIÓN Y NUTRICIÓN",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.GREEN_600
                    ),
                    ft.Divider(height=20, color=ft.Colors.GREEN_200),
                    ft.Text(
                        "TIMELINE DEL PROCESO DIGESTIVO:",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Column(elementos_timeline, spacing=5, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    ft.Divider(height=20),
                    resumen,
                    ft.ElevatedButton(
                        "Volver al menú",
                        on_click=lambda e: menu_principal()
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=25,
                scroll=ft.ScrollMode.AUTO
            )
        )

    def mostrar_opciones_matematicas(e):
        page.clean()
        
        page.add(
            ft.Column(
                [
                    ft.Text("Temas selectos de Matemáticas", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    ft.Text("¿Cómo deseas calcular el área bajo la curva?", size=18, text_align=ft.TextAlign.CENTER),
                    ft.ElevatedButton(
                        "Ver ejemplo (Integral definida: x² + 2 desde 1 a 3)",
                        on_click=lambda e: mostrar_materia_ejemplo(
                            "Temas selectos de Matemáticas",
                            "CÁLCULO DE UNA INTEGRAL DEFINIDA\n\n"
                            "Problema: Calcular el área bajo la curva f(x) = x² + 2 desde x=1 hasta x=3.\n\n"
                            "1. Planteamiento: ∫ (x² + 2) dx desde 1 hasta 3.\n"
                            "2. Integración: F(x) = (x³ / 3) + 2x\n"
                            "3. Evaluación Límite Superior (3): (3³ / 3) + 2(3) = 9 + 6 = 15\n"
                            "4. Evaluación Límite Inferior (1): (1³ / 3) + 2(1) = 1/3 + 2 = 7/3\n"
                            "5. Resta (Teorema Fundamental): 15 - 7/3 = 38/3 ≈ 12.67 unidades cuadradas."
                        ),
                        width=400,
                    ),
                    ft.Text("O", size=16, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    ft.ElevatedButton(
                        "Ingresar mis propios datos",
                        on_click=mostrar_formulario_matematicas,
                        width=400,
                    ),
                    ft.ElevatedButton(
                        "Volver al menú",
                        on_click=lambda e: menu_principal(),
                        width=200,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
    
    def mostrar_formulario_matematicas(e):
        page.clean()
        
        campo_funcion = ft.TextField(label="Función f(x)", hint_text="Ejemplo: x**2+2, x^2+2, 2*x+1, sin(x), exp(x)", width=400, text_align=ft.TextAlign.CENTER)
        campo_limite_inferior = ft.TextField(label="Límite inferior", hint_text="Ejemplo: 1", width=200, text_align=ft.TextAlign.CENTER)
        campo_limite_superior = ft.TextField(label="Límite superior", hint_text="Ejemplo: 3", width=200, text_align=ft.TextAlign.CENTER)
        
        def calcular_con_datos_usuario(e):
            try:
                funcion = campo_funcion.value.strip()
                lim_inf = float(campo_limite_inferior.value)
                lim_sup = float(campo_limite_superior.value)
                if not funcion:
                    raise ValueError("Debes ingresar una función")
                calcular_integral(e, funcion, lim_inf, lim_sup)
            except ValueError as err:
                mostrar_resultado_matematicas(
                    campo_funcion.value if campo_funcion.value else "?",
                    campo_limite_inferior.value if campo_limite_inferior.value else "?",
                    campo_limite_superior.value if campo_limite_superior.value else "?",
                    error=f"Error en los datos: {str(err)}"
                )
            except Exception as err:
                mostrar_resultado_matematicas(
                    campo_funcion.value if campo_funcion.value else "?",
                    campo_limite_inferior.value if campo_limite_inferior.value else "?",
                    campo_limite_superior.value if campo_limite_superior.value else "?",
                    error=f"Error inesperado: {str(err)}"
                )
        
        page.add(
            ft.Column(
                [
                    ft.Text("Ingresa tu propia función", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    ft.Text("Ingresa una función en términos de x (ejemplos: x**2, sin(x), exp(x), log(x))", size=14, text_align=ft.TextAlign.CENTER),
                    campo_funcion,
                    ft.Row(
                        [campo_limite_inferior, campo_limite_superior],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20
                    ),
                    ft.ElevatedButton(
                        "Calcular integral y graficar",
                        on_click=calcular_con_datos_usuario,
                        width=250,
                    ),
                    ft.ElevatedButton(
                        "Volver",
                        on_click=mostrar_opciones_matematicas,
                        width=200,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )

    def calcular_integral(e, funcion_str, limite_inf, limite_sup):
        try:
            funcion_str_original = funcion_str
            funcion_str = funcion_str.replace('^', '**')
            
            def f(x_val):
                return eval(funcion_str, {"x": x_val, "np": np, "sin": np.sin, "cos": np.cos, 
                                         "exp": np.exp, "log": np.log, "sqrt": np.sqrt,
                                         "__builtins__": {}}, {})
            
            f(limite_inf)
            f(limite_sup)
            
            n = 1000
            h = (limite_sup - limite_inf) / n
            resultado = f(limite_inf) + f(limite_sup)
            
            for i in range(1, n):
                x_val = limite_inf + i * h
                try:
                    fx = f(x_val)
                    if np.isinf(fx) or np.isnan(fx):
                        fx = 0
                    if i % 2 == 0:
                        resultado += 2 * fx
                    else:
                        resultado += 4 * fx
                except:
                    pass
            
            resultado *= h / 3
            
            mostrar_resultado_matematicas(funcion_str_original, limite_inf, limite_sup, resultado=resultado)
            
        except Exception as err:
            mostrar_resultado_matematicas(funcion_str, limite_inf, limite_sup, error=f"Error: {str(err)}")

    def mostrar_resultado_matematicas(funcion, lim_inf, lim_sup, resultado=None, error=None):
        page.clean()
        
        contenido = [
            ft.Text("Temas selectos de Matemáticas", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            ft.Text(f"Función: f(x) = {funcion}", size=18, text_align=ft.TextAlign.CENTER),
            ft.Text(f"Límite inferior: {lim_inf}", size=16, text_align=ft.TextAlign.CENTER),
            ft.Text(f"Límite superior: {lim_sup}", size=16, text_align=ft.TextAlign.CENTER),
            ft.Divider(),
        ]
        
        if error:
            contenido.append(ft.Text(error, size=16, color=ft.Colors.RED, text_align=ft.TextAlign.CENTER))
        else:
            grafica = crear_grafica(funcion, lim_inf, lim_sup, resultado)
            contenido.extend([
                ft.Text("Resultado de la integral definida:", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ft.Text(f"∫ f(x) dx desde {lim_inf} hasta {lim_sup} = {resultado:.6f} unidades cuadradas", 
                       size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN, text_align=ft.TextAlign.CENTER),
                ft.Divider(),
                ft.Text("Representación gráfica:", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                grafica,
                ft.Divider(),
                ft.Text("La gráfica muestra el área sombreada que representa el valor de la integral.", size=14, italic=True, text_align=ft.TextAlign.CENTER),
            ])
        
        contenido.append(
            ft.Row(
                [
                    ft.ElevatedButton("Calcular otra", on_click=mostrar_formulario_matematicas, width=150),
                    ft.ElevatedButton("Volver al menú", on_click=lambda e: menu_principal(), width=150),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            )
        )
        
        page.add(ft.Column(contenido, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15, scroll=ft.ScrollMode.AUTO))

    def menu_principal():
        page.clean()

        page.add(
            ft.Column(
                [
                    ft.Image(
                        src="images.jpeg",
                        width=150,
                        height=150,
                        fit="contain",
                    ),
                    ft.Text(
                        "Bienvenido al Sistema Escolar",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Text(
                        "Seleccione una asignatura",
                        size=20,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                "Temas selectos de Matemáticas",
                                on_click=mostrar_opciones_matematicas,
                                width=280,
                            ),
                            ft.ElevatedButton(
                                "Movimiento y estabilidad",
                                on_click=mostrar_infografia_movimiento,
                                width=280,
                            ),
                            ft.ElevatedButton(
                                "Organismos Estructuras y Procesos",
                                on_click=mostrar_infografia_organismos,
                                width=280,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                        wrap=True
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )

    menu_principal()

ft.app(target=main)