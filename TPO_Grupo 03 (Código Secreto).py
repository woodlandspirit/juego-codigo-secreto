from random import randint
import os
from datetime import datetime


# *******************************
# Generación UI
# *******************************      

def generar_ui_limpia():
    filas = 28
    ui = [['░'] * 126] + [['░'] + [' '] * 124 + ['░'] for i in range(filas)] + [['░'] * 126 + [' '] * 126 ] # <<<<<<<<<<<<<<<< MATRICES >>>>>>>>>>>>>>>>
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
    dibujar_texto(ui, 20, 5, "IMPORTANTE: Cuenta un máximo de 15 intentos!")
    dibujar_texto(ui, 22, 68, "¡ Mucha suerte !")
    dibujar_texto(ui, 24, 5, "⇨    ")  
    dibujar_texto(ui, 7, 98, "R e g i s t r o  d e")
    dibujar_texto(ui, 8, 98, "  i n t e n t o s :")
    
    return ui


def imprimir_ui(matriz_ui):
    os.system("cls||clear")
    print('\n'.join(''.join(fila) for fila in matriz_ui)) # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CADENAS DE CARACTERES >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 


# Impresión de texto en la UI en fila y columna dada

def dibujar_texto(matriz_ui, fila, columna, texto):
    if len(texto)>1:
        textoBis=texto[:-1] 
        dibujar_texto(matriz_ui, fila, columna, textoBis) # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<< RECURSIVIDAD >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    matriz_ui[fila][columna + (len(texto)-1)] = texto[len(texto)-1:len(texto)]


# Añadido de número y resultado en tabla y formateo de la impresión en la UI

def agregar_registro_usuario(matriz_ui, tabla, contador=0):
    if len(tabla)>1:
        agregar_registro_usuario(matriz_ui, tabla[1:],contador+1) # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<< RECURSIVIDAD >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    ingreso, resultado = tabla[0][0], tabla[0][1]
    dibujar_texto(matriz_ui, 10+contador, 102, f"{ingreso}   {resultado}")


# ************************************************
# Generación del código y bienvenida al usuario
# ************************************************

def generar_codigo_secreto():
    codigo_secreto = "0"
    
    while len(set(codigo_secreto)) != 4:
        codigo_secreto = str(randint(1000, 9999))

    return codigo_secreto


def pedir_nombre(matriz_ui):
    dibujar_texto(matriz_ui, 24, 9,'Bienvenido jugador! Ingrese a continuación su nombre.')
    imprimir_ui(matriz_ui)
    nombre_jugador = input("Nombre: ").title()
    print()
    
    dibujar_texto(matriz_ui, 24, 9, f"Hola {nombre_jugador}! Ingrese a continuación un n° entero de 4 dígitos SIN REPETICIONES")
    dibujar_texto(matriz_ui, 25, 9, "para comenzar. Si desea finalizar el juego antes de terminar, ingrese -1.")
    imprimir_ui(matriz_ui)
    
    return nombre_jugador


# *****************************************************************
# Pedido del número al usuario y validación del número ingresado
# *****************************************************************

def solicitar_numero():
    numero_ingresado=input("Su número elegido: ")
    print()
    return numero_ingresado


# Mensaje al jugador ante petición de finalizar el juego

def salir_juego():
    dibujar_texto(matriz_ui, 24, 9, "Ha salido del juego."+" "*65)
    dibujar_texto(matriz_ui, 25, 0, '░' + ' ' * 124 + '░')
    imprimir_ui(matriz_ui)

    
# Mensaje al jugador ante número incorrecto

def mensaje_incorrecto(verificacion, matriz_ui, tabla): 
    dibujar_texto(matriz_ui, 24, 9, f"El valor ingresado contiene {verificacion}"+" "*30) 
    dibujar_texto(matriz_ui, 25, 9, "Intente nuevamente."+" "*80)
    imprimir_ui(matriz_ui)
    
    
# 1° Etapa de validación (números naturales del 0 al 9)

def verif_alpha(numero_ingresado, matriz_ui, tabla): 
    verif_bandera = True
    listado_digitos_validos = {"0", "1", "2", "3","4", "5", "6", "7", "8", "9"}  # <<<<<<<<<<<<<<<<<<<<<<<<<< CONJUNTOS >>>>>>>>>>>>>>>>>>>>>>>>>> 

    for digito in numero_ingresado:
        if digito not in listado_digitos_validos:
            verif_bandera = False
            break

    if not verif_bandera:
        mensaje_incorrecto("caracteres NO NUMÉRICOS."+" "*30, matriz_ui, tabla) 
    
    return verif_bandera


# 2° Etapa de validación (número de 4 dígitos, sin repeticiones)

def verif_long(numero_ingresado, matriz_ui, tabla):
    verif_bandera = True
    numero_ingresado_Bis = numero_ingresado
    contador_ingresos = 0

    for digito in numero_ingresado:  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CADENAS DE CARACTERES >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
        for digitoBis in numero_ingresado_Bis:
            if digitoBis == digito:
                contador_ingresos += 1

    if contador_ingresos != 4:
        verif_bandera = False
        mensaje_incorrecto("digitos REPETIDOS o una LONGITUD incorrecta.", matriz_ui, tabla)

    return verif_bandera


# *******************************************************************************
# Comparación del código secreto con el número ingresado y generación de salida
# *******************************************************************************

def comparacion(numero,codigo_secreto):   
    salida_intermedia = ""
    salida_final=""

    for i in range(4): # 1° Etapa de comparación (generación de salida_intermedia)
        bandera = True
        for j in range(4):
            if numero[i] == codigo_secreto[j]: # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CADENAS DE CARACTERES >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  
                if i == j:
                    salida_intermedia += "B"
                else:
                    salida_intermedia += "R"
                bandera = False
        if bandera:
            salida_intermedia += "M"
    
    for letra in salida_intermedia: # 2° Etapa de comparación (generación de salida_final)
        if letra == "B":
            salida_final += letra

    for letra in salida_intermedia:
        if letra == "R":
            salida_final += letra

    for letra in salida_intermedia:
        if letra == "M":
            salida_final += letra

    return salida_final


# *******************************
# Almacenado de data del juego
# *******************************

# Almacenado de intentos válidos

def guardar_ingreso_usuario_y_resultado(ingreso_usuario, resultado):
    registros_usuario = [ingreso_usuario, resultado] # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< LISTAS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    tabla.append(registros_usuario)

    return tabla


# Almacenado del resumen de la partida

def guardar_resumen_del_juego(nombre_jugador, codigo_secreto, registro_intentos, intentos):
    resumen_juego = [nombre_jugador, codigo_secreto, registro_intentos, intentos] # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<< LISTAS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    return resumen_juego


# Generación del directorio y el archivo de resumen cada la partida

def archivar_juego(resumen):
    try: # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< EXCEPCIONES >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
        directorioActual=os.getcwd()+"\Partidas Guardadas"
        
        if not os.path.exists(directorioActual):
            os.makedirs(directorioActual)
            
        directorioArchivo=directorioActual+f"\{resumen[0]} - Sesion {datetime.now().strftime(r'%d-%m-%Y %H%M')}.txt"
        
        archivo = open(directorioArchivo, "wt") # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ARCHIVOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        archivo.write("*".center(50,"*") + "\n")
        archivo.write(f"Nombre del Jugador => {resumen[0]}".center(50) + "\n")
        archivo.write(f"Codigo Secreto => {resumen[1]}".center(50) + "\n")
        archivo.write(f"Cantidad de Intentos => {resumen[3]}".center(50) + "\n")
        archivo.write("*".center(50,"*") + "\n")
        archivo.write(" ".center(50," ") + "\n")

        i = 1
        for data in resumen[2]:
            if i<=9:
                archivo.write(f"Intento 0{i}: {data}".center(50) + "\n")
            else:
                archivo.write(f"Intento {i}: {data}".center(50) + "\n")
            i+=1

        archivo.write(" ".center(50," ") + "\n")
        archivo.write("*".center(50,"*") + "\n")

    except FileNotFoundError:
        resumen[0]="Usuario"
        archivar_juego(resumen)
    except TypeError:
        pass
    except OSError as mensaje:
        for caracter in resumen[0]:
            if not caracter.isalpha():
                resumen[0]="Usuario"
                archivar_juego(resumen)
                
        if resumen[0]!="Usuario":
            print("Error al intentar leer el archivo",mensaje)
        
    finally:
        try:
            archivo.close()
        except NameError:
            pass


# *******************************
# Impresión de salida
# *******************************

# Selección de mensaje al usuario según el número ingresado

def imprimir_resultados(salida, numero, nombre, matriz_ui, intentos):
    tabla = guardar_ingreso_usuario_y_resultado(numero, salida)

    if salida != "BBBB":              
        agregar_registro_usuario(matriz_ui, tabla)
        if len(tabla)<15:
            dibujar_texto(matriz_ui, 24, 9, f"El resultado para su número ingresado es: {salida}"+" "*70)
            dibujar_texto(matriz_ui, 25, 9, "Vuelva a intentarlo!"+" "*65)
            imprimir_ui(matriz_ui)

            juego_principal(codigo_secreto, nombre, matriz_ui, tabla, partida, len(tabla))
            resumen_juego=guardar_resumen_del_juego(nombre_jugador, codigo_secreto, tabla, len(tabla))
        else:
            dibujar_texto(matriz_ui, 24, 9, "Juego finalizado! Ha llegado a los 15 intentos."+" "*30)
            dibujar_texto(matriz_ui, 25, 0, '░' + ' ' * 124 + '░')
            imprimir_ui(matriz_ui)

            resumen_juego=guardar_resumen_del_juego(nombre_jugador, codigo_secreto, tabla, len(tabla))
            
    else:
        dibujar_texto(matriz_ui, 24, 9, f"Felicidades!! Ha ganado el juego {nombre}!!"+" "*30)
        agregar_registro_usuario(matriz_ui, tabla)
        
        imprimir_ui(matriz_ui)

        resumen_juego=guardar_resumen_del_juego(nombre_jugador, codigo_secreto, tabla, len(tabla))

    return resumen_juego


# *******************************
# Función MAIN
# *******************************

def juego_principal(codigo_secreto, nombre, matriz_ui, tabla, partida, cant_intentos=0):
    try: # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< EXCEPCIONES >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if len(tabla)<15:    
            numero=solicitar_numero()
        
            if numero!="-1": # ¿El usuario pidió finalizar el juego?
                bandera=verif_alpha(numero, matriz_ui, tabla)
                if bandera:
                    bandera=verif_long(numero, matriz_ui, tabla)
                
                if bandera: 
                    verif_bandera=True
                else: 
                    verif_bandera=False
                
                if verif_bandera: # ¿El número ingresado el válido?
                    salida=comparacion(numero,codigo_secreto)
                    partida=imprimir_resultados(salida,numero,nombre, matriz_ui, len(tabla))
                else:
                    partida=juego_principal(codigo_secreto, nombre, matriz_ui, tabla, partida) # <<<<<<<<<<<<<<<<<< RECURSIVIDAD >>>>>>>>>>>>>>>>>>                    

                return partida

            else:
                salir_juego()
                return 
        else:
            return partida
        
    except KeyboardInterrupt:
        print()
        salir_juego()   
        return
        
    except OSError:
        print("Ha habido un error. Por favor, reintente.")
                     

# *******************************
# PROGRAMA PRINCIPAL
# *******************************

# Inicialización de variables globales

tabla=[]
resumen_juego=None
salida_final=""
bandera=True  # Bandera que, al cambiar a False, determina el final abrupto del juego a pedido del jugador
matriz_ui=generar_ui_limpia()
partida=None


# Generación del código secreto

codigo_secreto=generar_codigo_secreto()


# Bienvenida al jugador

nombre_jugador=pedir_nombre(matriz_ui)


# Comienza el juego

partida=juego_principal(codigo_secreto, nombre_jugador, matriz_ui, tabla, partida)


# Generar archivo de la partida

archivar_juego(partida)
