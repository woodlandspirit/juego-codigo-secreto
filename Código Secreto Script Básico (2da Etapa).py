from random import randint
import os

tabla = []
resumen_juego = None
cantidad_intentos = 0

def guardar_resumen_del_juego(nombre_jugador, codigo_secreto, registro_intentos, cantidad_intentos):
    """Esta función guarda un resumen general del juego en una tupla, incluida la matriz de intentos válidos."""
    resumen_juego = tuple([nombre_jugador, codigo_secreto, registro_intentos, cantidad_intentos])
    return resumen_juego

def guardar_ingreso_usuario_y_resultado(ingreso_usuario, resultado):
    """ Esta función guarda todos aquellos intentos válidos ingresados por el usuario en una matriz."""
    registros_usuario = tuple([ingreso_usuario, resultado])
    tabla.append(registros_usuario)
    return tabla

def imprimir_registro_usuario(matriz_ui, tabla):
    """ Esta función recorre los últimos quince registros de la matriz de intentos para mostrarlos en la ui."""
    tabla_corta = tabla[-15:]
    for i, registro in enumerate(tabla_corta):
            ingreso, resultado = registro
            dibujar_texto(matriz_ui, 10+i, 102, f"{ingreso}   {resultado}")

def generar_ui_limpia():
    """Esta función genera la plantilla general que ES FIJA en cada momento del juego y la devuelve al programa.
       Incluye el recuadro y todos los textos."""
    filas = 28
    ui = [['░'] * 126] + [['░'] + [' '] * 124 + ['░'] for i in range(filas)] + [['░'] * 126 + [' '] * 126 ]
    dibujar_texto(ui, 3, 46, 'C Ó D I G O  S E C R E T O')
    dibujar_texto(ui, 7, 5, "O b j e t i v o  g e n e r a l  d e l  j u e g o :")
    dibujar_texto(ui, 9, 5, "La computadora generará un código al azar de cuatro números que van del 1 al 9,")
    dibujar_texto(ui, 10, 5, "que no se repiten entre sí. El objetivo es que el jugador adivine el número,")
    dibujar_texto(ui, 11, 5, "ingresando en cada intento un número diferente, mientras la computadora controla,")
    dibujar_texto(ui, 12, 5, "dígito a dígito, si existe coincidencia del número y la posición. Sin embargo,")
    dibujar_texto(ui, 13, 5, "quedará en manos del jugador elaborar una estrategia que le permita adivinar el")
    dibujar_texto(ui, 14, 5, "CÓDIGO SECRETO en el menor número de intentos posible, ya que no se le revelará")
    dibujar_texto(ui, 15, 5, "en qué dígitos ha acertado:sólo verá letras que:")
    dibujar_texto(ui, 16, 10, " *   indiquen que los dígitos coinciden en número y posición = B")
    dibujar_texto(ui, 17, 10, " *   que coinciden sólo en número pero están en la posición incorrecta = R")
    dibujar_texto(ui, 18, 10, " *   o que no coinciden en número ni posición = M")
    dibujar_texto(ui, 20, 68, "¡ Mucha suerte !")
    dibujar_texto(ui, 24, 5, "⇨    ")  
    dibujar_texto(ui, 7, 98, "R e g i s t r o  d e")
    dibujar_texto(ui, 8, 98, "  i n t e n t o s :")
    return ui


def imprimir_ui(matriz_ui):
    """Esta función limpia la consola y transforma cada elemento de la matriz en texto, para luego imprimirlo."""
    os.system("cls||clear")  # limpia la consola
    print('\n'.join([''.join(fila) for fila in matriz_ui]))


def dibujar_texto(matriz_ui, fila, columna, texto):
    """Esta función reasigna los elementos ubicados en la matriz_ui que indiquemos mediante el segundo y tercer parámetro (fila, columna),
       reemplazándolos por los caracteres que indiquemos en el cuarto parámetro."""
    for e, letra in enumerate(texto):
        matriz_ui[fila][columna + e] = letra


# *******************************
# PROGRAMA PRINCIPAL
# *******************************

# Generación del código secreto

codigo_secreto = "0"

while len(set(codigo_secreto)) != 4:
    codigo_secreto = str(randint(1000, 9999))


# Pedido del nombre al jugador

matriz_ui = generar_ui_limpia()
dibujar_texto(matriz_ui, 24, 9,'Bienvenido jugador! Ingrese a continuación su nombre.')
imprimir_ui(matriz_ui)
nombre_jugador = input("Nombre: ").title()



# Pedido del número al jugador

dibujar_texto(matriz_ui, 24, 9, f"Hola {nombre_jugador}! Ingrese a continuación un n° entero de 4 dígitos SIN REPETICIONES")
dibujar_texto(matriz_ui, 25, 9, "para comenzar. Si desea finalizar el juego antes de terminar, ingrese -1.")
imprimir_ui(matriz_ui)

salida_final = ""
bandera = True  # bandera que, al cambiar a False, determina el final abrupto del juego a pedido del jugador

while bandera and salida_final != "BBBB":

    salida_final = ""
    bandera2 = False  # bandera que, al cambiar a True, indica que el número ingresado por el jugador es válido

    numero_ingresado = input("Su número elegido: ")

    if numero_ingresado == "-1":
        matriz_ui = generar_ui_limpia()
        dibujar_texto(matriz_ui, 24, 9, "Ha salido del juego.")
        imprimir_registro_usuario(matriz_ui, tabla)
        imprimir_ui(matriz_ui)
        bandera = False

# 1° Etapa de validación del ingreso del jugador (todos números naturales del 0 al 9)

    while bandera and not bandera2:
        listado_digitos_validos = {"0", "1", "2", "3","4", "5", "6", "7", "8", "9"}  # Conjuntos

        while True:
            bandera2 = True

            for digito in numero_ingresado:
                if digito not in listado_digitos_validos:
                    bandera2 = False
                    break
            
            if bandera2:
                break
            
            matriz_ui = generar_ui_limpia()
            dibujar_texto(matriz_ui, 24, 9, "El valor ingresado NO ES VÁLIDO por contener caracteres NO NUMÉRICOS.")
            dibujar_texto(matriz_ui, 25, 9, "Intente nuevamente.")
            imprimir_registro_usuario(matriz_ui, tabla)
            imprimir_ui(matriz_ui)
            numero_ingresado = input("Su número elegido: ")

            if numero_ingresado == "-1":
                matriz_ui = generar_ui_limpia()
                dibujar_texto(matriz_ui, 24, 9, "Ha salido del juego.")
                imprimir_registro_usuario(matriz_ui, tabla)
                imprimir_ui(matriz_ui)
                bandera = False
                break

# 2° Etapa de validación del ingreso del jugador (número de 4 dígitos y sin repeticiones)

        if bandera:
            numero_ingresado_Bis = numero_ingresado
            contador_ingresos = 0

            for digito in numero_ingresado:  # Cadenas de caracteres
                for digitoBis in numero_ingresado_Bis:
                    if digitoBis == digito:
                        contador_ingresos += 1

            if contador_ingresos != 4:
                matriz_ui = generar_ui_limpia()
                dibujar_texto(matriz_ui, 24, 9, "El n°ingresado NO ES VÁLIDO. Puede deberse a que contenga DÍGITOS REPETIDOS o una")
                dibujar_texto(matriz_ui, 25, 9, "CANTIDAD INCORRECTA DE DÍGITOS. Intente nuevamente.")
                imprimir_registro_usuario(matriz_ui, tabla)
                imprimir_ui(matriz_ui)
                numero_ingresado = input("Su número elegido: ")
                bandera2 = False

            if numero_ingresado == "-1":
                matriz_ui = generar_ui_limpia()
                dibujar_texto(matriz_ui, 24, 9, "Ha salido del juego.")
                imprimir_registro_usuario(matriz_ui, tabla)
                imprimir_ui(matriz_ui)
                bandera = False



# Evaluación del número ingresado por el jugador


# 1° Etapa (comparación con códigoSecreto, caracter a caracter, y generación de salida_intermedia)

    if bandera:
        salida_intermedia = ""

        for i in range(4):
            bandera3 = True
            for j in range(4):
                if numero_ingresado[i] == codigo_secreto[j]:
                    if i == j:
                        salida_intermedia += "B"
                    else:
                        salida_intermedia += "R"
                    bandera3 = False
            if bandera3:
                salida_intermedia += "M"

# 2° Etapa (generación de salida_final a partir del reordenamiento de salida_intermedia)

        for letra in salida_intermedia:
            if letra == "B":
                salida_final += letra

        for letra in salida_intermedia:
            if letra == "R":
                salida_final += letra

        for letra in salida_intermedia:
            if letra == "M":
                salida_final += letra


# Entrega de salida al jugador y vuelta al ciclo en caso de no haber acertado

        cantidad_intentos += 1
        matriz_ui = generar_ui_limpia()
        dibujar_texto(matriz_ui, 24, 9, f"El resultado para su número ingresado es: {salida_final}")
        imprimir_ui(matriz_ui)

        tabla = guardar_ingreso_usuario_y_resultado(numero_ingresado, salida_final)
        imprimir_registro_usuario(matriz_ui, tabla)
        resumen_juego = guardar_resumen_del_juego(nombre_jugador, codigo_secreto, tabla, cantidad_intentos)

        if salida_final != "BBBB":
            dibujar_texto(matriz_ui, 25, 9, "Vuelva a intentarlo!")
            imprimir_ui(matriz_ui)
        else:
            dibujar_texto(matriz_ui, 25, 9, f"Felicidades!! Ha ganado el juego {nombre_jugador}!!")
            imprimir_registro_usuario(matriz_ui, tabla)
            imprimir_ui(matriz_ui)
        print(resumen_juego)