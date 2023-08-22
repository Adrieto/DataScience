from tkinter import *

def pot_recursiva(base,exp):
    if exp == 0:
        return 1
    else:
        return base * pot_recursiva(base, exp-1)

def factorial(n):
    f = n * factorial(n - 1)
    if n == 0:
        return 1
    return f

def menu():
    print('1. Opcion 1')
    print('2. Opcion 2')
    print('3. Salir')
    op = int(input('Ingrese opcion: '))
    if op == 1:
        print('Eligio la opcion 1...')
    elif op == 2:
        print('Eligio la opcion 2...')
    elif op == 3:
        return
    menu()

def producto(a, b):
    if a == 0 or b == 0:
        return 0
    return a + producto(a, b-1)


a=10
e=3
#print(f"potencia comunacha: {pow(a,e)}")
#print(f"potencia recursiva: {pot_recursiva(a,e)}")

#print(producto(12,0))




def function(canvas):
    # los ejes...
    canvas.create_line((90, 400, 400, 400), fill='orange')
    canvas.create_line((100, 410, 100, 200), fill='orange')

    # las curvas...
    canvas.create_line((100, 400, 230, 350), fill='black')
    canvas.create_line((230, 350, 300, 250), fill='black')

    # los puntos...
    canvas.create_oval((95, 395, 105, 405), outline='blue', fill='blue')
    canvas.create_oval((225, 345, 235, 355), outline='blue', fill='blue')
    canvas.create_oval((295, 245, 305, 255), outline='blue', fill='blue')

def button(canvas):
    x, y, ancho, alto = 100, 100, 100, 25

    # el fondo y el texto del botón...
    canvas.create_rectangle((x, y, x + ancho, y + alto), fill='light gray')
    canvas.create_text(x + ancho // 2 - 1, y + alto // 2 + 1, text='Ok', fill='black')

    for f in range(2):
        # los bordes blancos...
        canvas.create_line((x + f, y + f, x + ancho - f, y + f), fill='white')
        canvas.create_line((x + f, y + f, x + f, y + alto - f), fill='white')

        # los bordes oscuros...
        canvas.create_line((x + f, y + alto - f, x + ancho - f, y + alto - f), fill='dark gray')
        canvas.create_line((x + ancho - f, y + alto - f, x + ancho - f, y + f), fill='dark gray')

def edit(canvas):
    x, y, ancho, alto = 100, 100, 100, 25

    # el fondo y el texto del campo de edición...
    canvas.create_rectangle((x, y, x + ancho, y + alto), fill='white')
    canvas.create_text(x - 25, y + alto // 2, text='Valor: ', fill='black')

    for f in range(2):
        # los bordes oscuros...
        canvas.create_line((x + f, y + f, x + ancho - f, y + f), fill='dark gray')
        canvas.create_line((x + f, y + f, x + f, y + alto - f), fill='dark gray')

        # los bordes claros...
        canvas.create_line((x + f, y + alto - f, x + ancho - f, y + alto - f), fill='white')
        canvas.create_line((x + ancho - f, y + alto - f, x + ancho - f, y + f), fill='white')

def cube(canvas):
    x, y, ancho, alto = 100, 100, 60, 60
    canvas.create_rectangle((x, y, x + ancho, y + alto), outline='navy', fill='navy')
    canvas.create_line((100, 100, 130, 70), fill='lime')
    canvas.create_line((160, 100, 190, 70), fill='lime')
    canvas.create_line((130, 70, 190, 70), fill='lime')
    canvas.create_line((190, 70, 190, 130), fill='lime')
    canvas.create_line((160, 160, 190, 130), fill='lime')

def bars(canvas):
    canvas.create_rectangle((100, 120, 130, 200), outline='blue')
    canvas.create_rectangle((130, 85, 160, 200), outline='red')
    canvas.create_rectangle((161, 160, 190, 200), outline='yellow')
    canvas.create_rectangle((190, 100, 220, 200), outline='lime')
    canvas.create_line((70, 200, 250, 200), fill='black')

def pie(canvas):
    x, y, ancho, alto = 100, 100, 100, 100
    canvas.create_arc((x, y, x + ancho, y + alto), start=0, extent=45, outline='blue', fill='blue', style=ARC)
    canvas.create_arc((x, y, x + ancho, y + alto), start=45, extent=90, outline='red', fill='red', style=ARC)
    canvas.create_arc((x, y, x + ancho, y + alto), start=135, extent=135, outline='yellow', fill='yellow', style=ARC)
    canvas.create_arc((x, y, x + ancho, y + alto), start=270, extent=90, outline='lime', fill='lime', style=ARC)

def face(canvas):
    canvas.create_oval((100, 100, 160, 160), outline='red')
    canvas.create_oval((110, 115, 125, 125), outline='blue', fill='blue')
    canvas.create_line((127, 134, 133, 134), fill='blue')
    canvas.create_arc((120, 138, 140, 148), start=180, extent=180, outline='blue', style=ARC)

def pacman(canvas):
    x, y, ancho, alto = 100, 100, 50, 50
    canvas.create_arc((x, y, x + ancho, y + alto), start=45, extent=315, outline='red', fill='red', style=PIESLICE)
    canvas.create_oval((x + 10, y + 10, x + 2 + ancho // 3, y + 2 + alto // 3), outline='white', fill='white')
    canvas.create_oval((x + 16, y + 16, x + ancho / 4, y + alto / 4), outline='black', fill='black')


def render():
    # configuracion inicial de la ventana principal...
    root = Tk()
    root.title('Cuestionario')

    # calculo de resolucion en pixels de la pantalla...
    maxw = root.winfo_screenwidth()
    maxh = root.winfo_screenheight()

    # ajuste de las dimensiones y coordenadas de arranque de la ventana...
    root.geometry("%dx%d+%d+%d" % (maxw, maxh, 0, 0))

    # un lienzo de dibujo dentro de la ventana...
    canvas = Canvas(root, bg='white', width=maxw, height=maxh)
    canvas.grid(column=0, row=0)

    # desarrollar la gráfica...
    pacman(canvas)
    face(canvas)

    # lanzar el ciclo principal de control de eventos de la ventana...
    root.mainloop()


if __name__ == '__main__':
    render()