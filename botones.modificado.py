import flet as ft

def main(page: ft.Page):

    page.title = "Sistema Escolar"
    page.window_width = 900
    page.window_height = 700
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    def mostrar_materia_ejemplo(nombre, descripcion):
        """Versión original para el ejemplo de matemáticas"""
        page.clean()
        page.add(
            ft.Column(
                [
                    ft.Text(nombre, size=30, weight="bold", text_align=ft.TextAlign.CENTER),
                    ft.Text(descripcion, size=18, text_align=ft.TextAlign.CENTER),
                    ft.ElevatedButton(
                        "Volver al menú",
                        on_click=lambda e: menu_principal()
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )

    def mostrar_infografia_movimiento(e):
        """Infografía para Movimiento y estabilidad (ANC)"""
        page.clean()
        
        # Definir los pasos del proceso ANC
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
        
        # Crear tarjetas para cada paso
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
                                            weight="bold",
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
                                weight="bold",
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
        
        # Organizar tarjetas en filas (2 columnas)
        fila1 = ft.Row(tarjetas[:2], alignment=ft.MainAxisAlignment.CENTER, spacing=30)
        fila2 = ft.Row(tarjetas[2:], alignment=ft.MainAxisAlignment.CENTER, spacing=30)
        
        # Decoración de ondas
        ondas = ft.Container(
            content=ft.Text(
                "〰️ 〰️ 〰️ ONDAS SONORAS 〰️ 〰️ 〰️",
                size=18,
                weight="bold",
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
                        weight="bold",
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.INDIGO_700
                    ),
                    
                    ft.Text(
                        "CANCELACIÓN ACTIVA DE RUIDO (ANC) EN AUDÍFONOS",
                        size=20,
                        weight="bold",
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.INDIGO_500
                    ),
                    
                    ft.Divider(height=20, color=ft.Colors.INDIGO_200),
                    
                    ondas,
                    
                    ft.Text(
                        "PROCESO EXPLICADO PASO A PASO:",
                        size=22,
                        weight="bold",
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
                                    weight="bold",
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
                        on_click=lambda e: menu_principal(),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.INDIGO_500,
                            color=ft.Colors.WHITE
                        )
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=25
            )
        )

    def mostrar_infografia_organismos(e):
        """Infografía para Organismos, Estructuras y Procesos (Digestión)"""
        page.clean()
        
        # Datos del proceso digestivo
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
        
        # Crear timeline visual
        elementos_timeline = []
        for i, etapa in enumerate(etapas):
            es_ultimo = i == len(etapas) - 1
            
            # Tarjeta de la etapa
            tarjeta = ft.Container(
                content=ft.Row(
                    [
                        # Círculo con número (más pequeño)
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Text(
                                        etapa["numero"],
                                        size=16,
                                        weight="bold",
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
                        
                        # Contenido de la etapa
                        ft.Column(
                            [
                                ft.Text(etapa["nombre"], size=22, weight="bold", color=etapa["color"], text_align=ft.TextAlign.CENTER),
                                ft.Text(etapa["descripcion"], size=14, text_align=ft.TextAlign.CENTER),
                                ft.Row(
                                    [
                                        ft.Text(f"⏱️ {etapa['duracion']}", size=12, italic=True, text_align=ft.TextAlign.CENTER),
                                        ft.Text(f"📍 {etapa['organo']}", size=12, italic=True, text_align=ft.TextAlign.CENTER),
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
                shadow=ft.BoxShadow(spread_radius=1, blur_radius=5, color=ft.Colors.GREY_300),
            )
            
            elementos_timeline.append(tarjeta)
            
            # Flecha conectora (excepto en el último)
            if not es_ultimo:
                flecha = ft.Container(
                    content=ft.Text("▼", size=30, color=ft.Colors.GREY_400),
                    padding=5
                )
                elementos_timeline.append(flecha)
        
        # Resumen nutricional
        resumen = ft.Container(
            content=ft.Column(
                [
                    ft.Text("DATOS INTERESANTES:", size=20, weight="bold", text_align=ft.TextAlign.CENTER),
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
                        weight="bold",
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.GREEN_700
                    ),
                    
                    ft.Text(
                        "EL PROCESO DE ALIMENTACIÓN Y NUTRICIÓN",
                        size=20,
                        weight="bold",
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.GREEN_600
                    ),
                    
                    ft.Divider(height=20, color=ft.Colors.GREEN_200),
                    
                    ft.Text(
                        "TIMELINE DEL PROCESO DIGESTIVO:",
                        size=22,
                        weight="bold",
                        text_align=ft.TextAlign.CENTER
                    ),
                    
                    ft.Column(elementos_timeline, spacing=5, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    
                    ft.Divider(height=20),
                    
                    resumen,
                    
                    ft.ElevatedButton(
                        "Volver al menú",
                        on_click=lambda e: menu_principal(),
                        style=ft.ButtonStyle(
                            padding=15,
                            bgcolor=ft.Colors.GREEN_600,
                            color=ft.Colors.WHITE
                        )
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=25,
                scroll=ft.ScrollMode.AUTO
            )
        )

    def mostrar_opciones_matematicas(e):
        """Muestra opciones: ver ejemplo existente o ingresar datos propios"""
        page.clean()
        
        page.add(
            ft.Column(
                [
                    ft.Text("Temas selectos de Matemáticas", size=30, weight="bold", text_align=ft.TextAlign.CENTER),
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
                    
                    ft.Text("O", size=16, weight="bold", text_align=ft.TextAlign.CENTER),
                    
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
        """Muestra formulario para que el usuario ingrese su propia función y límites"""
        page.clean()
        
        campo_funcion = ft.TextField(label="Función f(x)", hint_text="Ejemplo: x**2+2, x^2+2, 2*x+1", width=400, text_align=ft.TextAlign.CENTER)
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
                    error=f"Error en los datos: {str(err)}\nVerifica que los límites sean números válidos."
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
                    ft.Text("Ingresa tu propia función", size=30, weight="bold", text_align=ft.TextAlign.CENTER),
                    ft.Text("Ingresa una función polinómica en términos de x", size=16, text_align=ft.TextAlign.CENTER),
                    campo_funcion,
                    ft.Row(
                        [campo_limite_inferior, campo_limite_superior],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20
                    ),
                    ft.ElevatedButton(
                        "Calcular integral",
                        on_click=calcular_con_datos_usuario,
                        width=200,
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
        """Calcula la integral definida de una función polinómica simple."""
        try:
            funcion_str = funcion_str.replace('^', '**')
            import re
            
            def integrar_termino(termino):
                termino = termino.strip()
                if termino == '':
                    return ''
                
                if 'x' in termino:
                    match = re.match(r'([+-]?\d*\.?\d*)\*?x(?:\*\*(\d+))?', termino)
                    if match:
                        coef = match.group(1)
                        exp = match.group(2)
                        
                        if coef == '' or coef == '+':
                            coef = 1
                        elif coef == '-':
                            coef = -1
                        else:
                            coef = float(coef)
                        
                        if exp is None:
                            exp = 1
                        else:
                            exp = int(exp)
                        
                        nuevo_coef = coef / (exp + 1)
                        nuevo_exp = exp + 1
                        
                        if nuevo_coef == 1:
                            return f"x**{nuevo_exp}"
                        elif nuevo_coef == -1:
                            return f"-x**{nuevo_exp}"
                        else:
                            return f"{nuevo_coef}*x**{nuevo_exp}"
                else:
                    coef = float(termino) if termino else 0
                    if coef == 1:
                        return "x"
                    elif coef == -1:
                        return "-x"
                    else:
                        return f"{coef}*x"
                return termino
            
            terminos = re.findall(r'([+-]?[^+-]+)', funcion_str)
            antiderivada_str = ''
            for term in terminos:
                term_integrado = integrar_termino(term)
                if term_integrado:
                    antiderivada_str += '+' + term_integrado
            
            antiderivada_str = antiderivada_str.lstrip('+')
            
            def evaluar_antiderivada(x_val):
                return eval(antiderivada_str, {"x": x_val, "__builtins__": {}}, {})
            
            valor_superior = evaluar_antiderivada(limite_sup)
            valor_inferior = evaluar_antiderivada(limite_inf)
            resultado = valor_superior - valor_inferior
            
            mostrar_resultado_matematicas(
                funcion_str.replace('**', '^'),
                limite_inf,
                limite_sup,
                antiderivada_str.replace('**', '^'),
                valor_superior,
                valor_inferior,
                resultado
            )
            
        except Exception as err:
            mostrar_resultado_matematicas(
                funcion_str,
                limite_inf,
                limite_sup,
                error=f"Error al calcular: {str(err)}\nAsegúrate de usar formato como: x**2, 2*x, x**2+3*x+1"
            )

    def mostrar_resultado_matematicas(funcion, lim_inf, lim_sup, antiderivada=None, val_sup=None, val_inf=None, resultado=None, error=None):
        page.clean()
        
        contenido = [
            ft.Text("Temas selectos de Matemáticas", size=30, weight="bold", text_align=ft.TextAlign.CENTER),
            ft.Text(f"Función: f(x) = {funcion}", size=18, text_align=ft.TextAlign.CENTER),
            ft.Text(f"Límite inferior: {lim_inf}", size=16, text_align=ft.TextAlign.CENTER),
            ft.Text(f"Límite superior: {lim_sup}", size=16, text_align=ft.TextAlign.CENTER),
            ft.Divider(),
        ]
        
        if error:
            contenido.append(ft.Text(error, size=16, color="red", text_align=ft.TextAlign.CENTER))
        else:
            contenido.extend([
                ft.Text("Proceso de integración:", size=20, weight="bold", text_align=ft.TextAlign.CENTER),
                ft.Text(f"1. Planteamiento:", size=16, weight="bold", text_align=ft.TextAlign.CENTER),
                ft.Text(f"   ∫ ({funcion}) dx desde {lim_inf} hasta {lim_sup}", size=14, text_align=ft.TextAlign.CENTER),
                ft.Text(f"2. Antiderivada:", size=16, weight="bold", text_align=ft.TextAlign.CENTER),
                ft.Text(f"   F(x) = {antiderivada}", size=14, text_align=ft.TextAlign.CENTER),
                ft.Text(f"3. Evaluación en límite superior ({lim_sup}):", size=16, weight="bold", text_align=ft.TextAlign.CENTER),
                ft.Text(f"   F({lim_sup}) = {val_sup}", size=14, text_align=ft.TextAlign.CENTER),
                ft.Text(f"4. Evaluación en límite inferior ({lim_inf}):", size=16, weight="bold", text_align=ft.TextAlign.CENTER),
                ft.Text(f"   F({lim_inf}) = {val_inf}", size=14, text_align=ft.TextAlign.CENTER),
                ft.Text(f"5. Resultado (Teorema Fundamental):", size=16, weight="bold", text_align=ft.TextAlign.CENTER),
                ft.Text(f"   {val_sup} - {val_inf} = {resultado}", size=14, text_align=ft.TextAlign.CENTER),
                ft.Divider(),
                ft.Text(f"Área bajo la curva: {resultado} unidades cuadradas", size=18, weight="bold", color="green", text_align=ft.TextAlign.CENTER),
            ])
        
        contenido.append(
            ft.ElevatedButton(
                "Volver al menú",
                on_click=lambda e: menu_principal(),
                width=200,
            )
        )
        
        page.add(ft.Column(contenido, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15))

    def menu_principal():
        page.clean()

        page.add(
            ft.Column(
                [
                    ft.Image(
                        src="images.jpg",
                        width=150,
                        height=150,
                        fit="contain",
                    ),
                    
                    ft.Text(
                        "Bienvenido al Sistema Escolar",
                        size=30,
                        weight="bold",
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
                                width=250,
                            ),

                            ft.ElevatedButton(
                                "Movimiento y estabilidad",
                                on_click=mostrar_infografia_movimiento,
                                width=250,
                            ),

                            ft.ElevatedButton(
                                "Organismos Estructuras y Procesos",
                                on_click=mostrar_infografia_organismos,
                                width=250,
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