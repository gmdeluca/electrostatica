
#
#  https://gist.github.com/cristhianboujon/3010fe9966d2c6402f16747a67151144 
#

import tkinter as tk
import time


class Particula:
    def __init__(self, x, y, radio, color='blue'):
        self.circulo = canvas.create_oval(
            x - radio, y - radio, x + radio, y + radio, fill=color
        )

    def mover(self):
        canvas.move(self.circulo, 1, 0)


if __name__ == '__main__':
    root = tk.Tk()

    # create canvas
    canvas = tk.Canvas(root)
    canvas.pack()

    # create objects
    p = Particula(50, 50, 20)
    p2 = Particula(100, 100, 5, 'red')

    while True:
        time.sleep(0.025)
        p.mover()
        p2.mover()

        canvas.update()