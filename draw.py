from display import *

def draw_line( x0, y0, x1, y1, screen, color):
    x0 = int(x0)
    x1 = int(x1)
    y0 = int(y0)
    y1 = int(y1)
    deltaX = dXY(x0, x1)
    deltaY = dXY(y0, y1)
    try:
        m = deltaY / deltaX
    except ZeroDivisionError: #vertical
        for y in range(abs(deltaY)):
            if (y0 > y1): screen[y1 + y][x0] = color.copy()
            else: screen[y0 + y][x0] = color.copy()
        return
    if (m == 0): #horizontal
        for x in range(abs(deltaX)):
            if (x0 > x1): screen[y0][x1 + x] = color.copy()
            else: screen[y0][x0 + x] = color.copy()
    if (m > 0 and m <= 1): #octant 1 + 5
        d = func(dXY(y0, y1), -1 * dXY(x0, x1))
        if (x0 < x1):
            while (x0 < x1):
                screen[y0][x0] = color.copy()
                if (d > 0):
                    y0 = y0 + 1
                    d =  d + -2 * dXY(x0, x1)
                x0 = x0 + 1
                d = d + 2 * dXY(y0, y1)
        else:
            while (x0 > x1):
                screen[y0][x0] = color.copy()
                if (d > 0):
                    y0 = y0 - 1
                    d =  d + -2 * dXY(x1, x0)
                x0 = x0 - 1
                d = d + 2 * dXY(y1, y0)
    if (m > 1): #octants 2 + 6
        d = func(-1 * dXY(x0, x1), dXY(y0, y1))
        if (x0 < x1):
            while (x0 < x1):
                screen[y0][x0] = color.copy()
                if (d < 0):
                    x0 = x0 + 1
                    d = d + 2 * dXY(y0, y1)
                y0 = y0 + 1
                d =  d + -2 * dXY(x0, x1)
        else:
            while (x0 > x1):
                screen[y0][x0] = color.copy()
                if (d < 0):
                    x0 = x0 - 1
                    d =  d + 2 * dXY(y1, y0)
                y0 = y0 - 1
                d = d + -2 * dXY(x1, x0)
    if (m < -1): #octants 3 + 7
        d = func(-1 * dXY(x0, x1), dXY(y0, y1))
        if (x0 < x1):
            while (x0 < x1):
                screen[y0][x0] = color.copy()
                if (d < 0):
                    x0 = x0 + 1
                    d =  d + -2 * dXY(y0, y1)
                y0 = y0 - 1
                d = d - 2 * dXY(x0, x1)
        else:
            while (x0 > x1):
                screen[y0][x0] = color.copy()
                if (d > 0):
                    x0 = x0 - 1
                    d = d + 2 * dXY(y1, y0)
                y0 = y0 + 1
                d =  d + 2 * dXY(x1, x0)
    if (m < 0 and m >= -1): #octants 4 + 8
        d = func(dXY(y0, y1), -1 * dXY(x0, x1))
        if (x0 < x1):
            while (x0 < x1):
                screen[y0][x0] = color.copy()
                if (d > 0):
                    y0 = y0 - 1
                    d =  d + -2 * dXY(x0, x1)
                x0 = x0 + 1
                d = d - 2 * dXY(y0, y1)
        else:
            while (x0 > x1):
                screen[y0][x0] = color.copy()
                if (d < 0):
                    y0 = y0 + 1
                    d =  d + 2 * dXY(x1, x0)
                x0 = x0 - 1
                d = d + 2 * dXY(y1, y0)


def dXY(xy0, xy1):
    return int(xy1 - xy0)

def func(a, b):
    d = 2 * a + b
    return d
