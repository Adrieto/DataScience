from tkinter import *
ventana = Tk()

ventana.title("Cuadrados recursivos")

canvas = Canvas(ventana, width=1000, height=700)
canvas.grid(column=0, row=0)

def dibujar (canvas, x, y, lado): # x, y representa el centro del cuadrado
    if lado > 1:
        r = lado // 2

        dibujar(canvas, x - r, y + r, r)
        dibujar(canvas, x - r, y - r, r)
        dibujar(canvas, x + r, y + r, r)
        dibujar(canvas, x + r, y - r, r)

        # COLOCO ESTA LINEA AL FINAL PARA QUE LOS CUADRADOS GRANDES QUEDEN POR ENCIMA
        canvas.create_rectangle(x - r, y - r, x + r, y + r, outline="yellow", fill="blue")

dibujar(canvas, 500, 350, 300)

ventana.mainloop()