# Enrique Gutiérrez - A00827430
# Reflexión individual
# Con esta actividad, aprendí sobre juegos en los que se toman los inputs del usuario por medio de clicks. En los juegos que 
# habíamos visto anteriormente se utilizaban más las teclas para interactuar con el programa. En lo personal, siento que fue un 
# juego sencillo y no muy retador, en comparación con los otros que habíamos visto, pero fue un muy buen cierre. La explicación
# durante la clase me hizo comprender cómo funciona el juego y cómo realizar los cambios adecuados para cumplir la actividad.
# Siento que hice un buen trabajo con el código y estoy satisfecho con mi resultado. En lo personal decidí hacer el memorama de
# carácteres especiales del teclado, ya que con símbolos que todos hemos visto y son pequeños y fáciles de acomodar en los 
# recuadros, una opción con mucho texto hubiera complicado mucho el memorama y no se hubiera visto bien, por lo que estoy conforme
# con mi selección. En general, la semana tec fue de aprendizajes muy valiosos y me ayudó a incrementar mi interés en la pregramación.
# En mi carrera no se ven mucho estos temas pero creo que hacen un gran complemento con cualquier carrerra y programar es una
# habilidad muy útil en la vida profesional, y me gustaría mucho aprenderlo mejor y saber cómo aplicarlo en cualquier área en la
# que trabaje.
# 7 - Mayo - 2021

# LINK DEL VIDEO: https://youtu.be/5qT4zrjr4cU

# Se importan las librerías
from random import *
from turtle import *
from freegames import path

# Utiliza la imagen de path (el carro)
car = path('car.gif')
# genera una lista de lo que habrá en el memorama y forma los 2 pares
tiles = [
    '@','#','=','$','&','%','?','¿','!','¡','|','°','¬','*','+','-','¨',
    '{','}','[',']','_','^','`',';','<','>',':','(',')','/','"'
    ]*2

# Estado inicial del juego
state = {'mark': None}
hide = [True] * 64
taps = 0

# Define la función que dibuja los cuadros que cubren la imagen
def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    # va a la posicion donde dibujará el cuadro
    goto(x, y)
    down()
    # Seleccionar el color de los recuadros
    color('black', 'light blue')
    begin_fill()
    # hace el cuadro y lo rellena
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

# calcula la posición en la lista al hacer click
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# Convierte una posición a coordenadas en el tablero
def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Cambia los tiles al hacer click en ellas
def tap(x, y):
    "Update mark and hidden tiles based on tap."
    global taps
    # regresa el índice de la casilla en la que se hizo click
    spot = index(x, y)
    # Saca el valor de state - al inicio es None
    mark = state['mark']
    # Contador de taps
    taps = taps + 1

    # Si se da click en un recuadro válido, en el mismo recuadro o es un número diferente
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        # El estado cambia al cuandro donde el usuario dio click
        state['mark'] = spot
    else:
        # Cuando son pares, elimina los recuadros
        hide[spot] = False
        hide[mark] = False
        # Vuelve a hacer mark none para poder seleccionar otra carta
        state['mark'] = None

def draw():
    "Draw image and tiles."
    # Limapia la ventana
    clear()
    # Va al medio de la ventana
    goto(0, 0)
    # Carga la imagen en turtle shape
    shape(car)
    # Hace una copia de la shape en la ventana actual
    stamp()

    # Dibuja las 64 cartas sobre la imagen
    for count in range(64):
        # Verifica que la carta no está descubierta
        if hide[count]:
            # Calcula las coordenadas a la que esta
            x, y = xy(count)
            # Llama a la función para dibujar el cuadrado
            square(x, y)

    mark = state['mark']

    # Muestra los números cuando se hace click sobre un recuadro que no es par y no estaba visible
    if mark is not None and hide[mark]:
        # Calcula la posición de la carta
        x, y = xy(mark)
        # Levanta el lapiz
        up()
        # mueve el turtle a la posición x+2, y
        goto(x + 10, y+2)
        # Despliega el número de la carta
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))
    
    # Cuenta cuantas cartas faltan
    escondidas = hide.count(True)
    
    # Cuando se revelan todos los cuadros despliega el mensaje
    if escondidas == 0:
        up()
        goto(-185, 120)
        color('green')
        # Escribe que ganaste el auto en la posición seleccionada
        write('GANASTE UN AUTO!!',font=('Arial',28,'normal'))
        goto(-120, 80)
        color('white')
        # Despliega el número de taps que se realizaron
        write(f'Número de taps: {taps}',font=('Arial',20,'normal'))
        up()
        goto(-150, -150)
        color('white')
        # Despliega mi nombre y matrícula
        write('Enrique Gutiérrez    A00827430',font=('Arial',15,'normal'))
        
    
    
    # Actualiza la ventana y muestra lo dibujado
    update()
    # vuelve a llamar la función draw en 1 seg
    ontimer(draw, 100)

# Revuelve los valores de la lista del memorama
shuffle(tiles)
setup(420, 420, 370, 0)
# Agrega la imagen del carro
addshape(car)
# Esconde la tortuga
hideturtle()
# hace que se dibuje instantáneamente
tracer(False)
# Detecta los eventos del mouse y llama a la función tap
onscreenclick(tap)
draw()
done()