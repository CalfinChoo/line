from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    print(screen)
    pass
    deltaX = x1 - x0
    deltaY = y1 - y0
    try:
        m = abs(deltaY) / abs(deltaX)
    except ZeroDivisionError:
        for y in range(deltaY):
            if (y0 > y1): screen[int(y1 + y)][int(x0)] = color
            else: screen[int(y0 + y)][int(x0)] = color
        return
    #d = 2A + B
    #A = deltaY
    #B = -deltaX
    # if (m > 0 and m < 1):
    #     d = func(dXY(y0, y1), -1 * dXY(x0, x1))
    #     while (x0 <= x1):
    #         screen[x0][y0] = color
    #         if (d > 0):
    #             y0 = y0 + 1
    #             d =  d + -2 * dXY(x0, x1)
    #         x0 = x0 + 1

def dXY(xy0, xy1):
    return xy1 - xy0

def func(a, b):
    d = 2 * a + b
    return d
