from display import *
from draw import *

s = new_screen()
c = [ 255, 255, 255 ]

draw_line(XRES/4, YRES/3, XRES/4 + 10, YRES/3, s, c)
draw_line(XRES/4, YRES/3, XRES/4 - 10, YRES/3, s, c)

draw_line(XRES/4 + 10, YRES/3, XRES/4 + 10, YRES/3+10, s, c)
draw_line(XRES/4 - 10, YRES/3, XRES/4 - 10, YRES/3+10, s, c)

draw_line(XRES/4 + 10, YRES/3+10, XRES/4 + 25, YRES/3+10, s, c)
draw_line(XRES/4 - 10, YRES/3+10, XRES/4 - 25, YRES/3+10, s, c)

draw_line(XRES/4 + 25, YRES/3+10, XRES/4 + 25, YRES/3, s, c)
draw_line(XRES/4 - 25, YRES/3+10, XRES/4 - 25, YRES/3, s, c)

draw_line(XRES/4 + 25, YRES/3, XRES/4 + 40, YRES/3, s, c)
draw_line(XRES/4 - 25, YRES/3, XRES/4 - 40, YRES/3, s, c)

draw_line(XRES/4 + 40, YRES/3, XRES/4 + 40, YRES/3+25, s, c)
draw_line(XRES/4 - 40, YRES/3, XRES/4 - 40, YRES/3+25, s, c)
draw_line(XRES/4 - 40, YRES/3+25, XRES/4 + 40, YRES/3+25, s, c)

draw_line(XRES/4 - 35, YRES/3+30, XRES/4 - 35, YRES/3+25, s, c)
draw_line(XRES/4 + 35, YRES/3+30, XRES/4 + 35, YRES/3+25, s, c)
draw_line(XRES/4 - 35, YRES/3+30, XRES/4 + 35, YRES/3+30, s, c)

draw_line(XRES/4 - 30, YRES/3+40, XRES/4 - 30, YRES/3+30, s, c)
draw_line(XRES/4 + 30, YRES/3+40, XRES/4 + 30, YRES/3+30, s, c)
draw_line(XRES/4 - 30, YRES/3+40, XRES/4 + 30, YRES/3+40, s, c)

draw_line(XRES/4 - 23, YRES/3+40, XRES/4 - 32, YRES/3+150, s, c)
draw_line(XRES/4 + 23, YRES/3+40, XRES/4 + 32, YRES/3+150, s, c)
draw_line(XRES/4 - 32, YRES/3+150, XRES/4 + 32, YRES/3+150, s, c)

draw_line(XRES/4 - 35, YRES/3+150, XRES/4 - 35, YRES/3+155, s, c)
draw_line(XRES/4 + 35, YRES/3+150, XRES/4 + 35, YRES/3+155, s, c)
draw_line(XRES/4 - 35, YRES/3+150, XRES/4 + 35, YRES/3+150, s, c)
draw_line(XRES/4 - 35, YRES/3+155, XRES/4 + 35, YRES/3+155, s, c)

draw_line(XRES/4 - 40, YRES/3+165, XRES/4 - 40, YRES/3+155, s, c)
draw_line(XRES/4 + 40, YRES/3+165, XRES/4 + 40, YRES/3+155, s, c)
draw_line(XRES/4 - 40, YRES/3+155, XRES/4 + 40, YRES/3+155, s, c)
draw_line(XRES/4 - 40, YRES/3+165, XRES/4 + 40, YRES/3+165, s, c)

draw_line(XRES/4 - 55, YRES/3+185, XRES/4 - 50, YRES/3+165, s, c)
draw_line(XRES/4 + 55, YRES/3+185, XRES/4 + 50, YRES/3+165, s, c)
draw_line(XRES/4 - 50, YRES/3+165, XRES/4 + 50, YRES/3+165, s, c)
draw_line(XRES/4 - 55, YRES/3+185, XRES/4 + 55, YRES/3+185, s, c)

draw_line(XRES/4 - 57, YRES/3+195, XRES/4 - 57, YRES/3+185, s, c)
draw_line(XRES/4 + 57, YRES/3+195, XRES/4 + 57, YRES/3+185, s, c)
draw_line(XRES/4 - 57, YRES/3+185, XRES/4 + 57, YRES/3+185, s, c)
draw_line(XRES/4 - 57, YRES/3+195, XRES/4 + 57, YRES/3+195, s, c)

draw_line(XRES/4 - 55, YRES/3+195, XRES/4 - 55, YRES/3+198, s, c)
draw_line(XRES/4 + 55, YRES/3+195, XRES/4 + 55, YRES/3+198, s, c)
draw_line(XRES/4 - 55, YRES/3+198, XRES/4 + 55, YRES/3+198, s, c)
#-----------------------------
c = [ 128, 128, 128]

draw_line(XRES*3/4, YRES/3, XRES*3/4 + 10, YRES/3, s, c)
draw_line(XRES*3/4, YRES/3, XRES*3/4 - 10, YRES/3, s, c)

draw_line(XRES*3/4 + 10, YRES/3, XRES*3/4 + 10, YRES/3+10, s, c)
draw_line(XRES*3/4 - 10, YRES/3, XRES*3/4 - 10, YRES/3+10, s, c)

draw_line(XRES*3/4 + 10, YRES/3+10, XRES*3/4 + 25, YRES/3+10, s, c)
draw_line(XRES*3/4 - 10, YRES/3+10, XRES*3/4 - 25, YRES/3+10, s, c)

draw_line(XRES*3/4 + 25, YRES/3+10, XRES*3/4 + 25, YRES/3, s, c)
draw_line(XRES*3/4 - 25, YRES/3+10, XRES*3/4 - 25, YRES/3, s, c)

draw_line(XRES*3/4 + 25, YRES/3, XRES*3/4 + 40, YRES/3, s, c)
draw_line(XRES*3/4 - 25, YRES/3, XRES*3/4 - 40, YRES/3, s, c)

draw_line(XRES*3/4 + 40, YRES/3, XRES*3/4 + 40, YRES/3+25, s, c)
draw_line(XRES*3/4 - 40, YRES/3, XRES*3/4 - 40, YRES/3+25, s, c)
draw_line(XRES*3/4 - 40, YRES/3+25, XRES*3/4 + 40, YRES/3+25, s, c)

draw_line(XRES*3/4 - 35, YRES/3+30, XRES*3/4 - 35, YRES/3+25, s, c)
draw_line(XRES*3/4 + 35, YRES/3+30, XRES*3/4 + 35, YRES/3+25, s, c)
draw_line(XRES*3/4 - 35, YRES/3+30, XRES*3/4 + 35, YRES/3+30, s, c)

draw_line(XRES*3/4 - 30, YRES/3+40, XRES*3/4 - 30, YRES/3+30, s, c)
draw_line(XRES*3/4 + 30, YRES/3+40, XRES*3/4 + 30, YRES/3+30, s, c)
draw_line(XRES*3/4 - 30, YRES/3+40, XRES*3/4 + 30, YRES/3+40, s, c)

draw_line(XRES*3/4 - 23, YRES/3+40, XRES*3/4 - 32, YRES/3+150, s, c)
draw_line(XRES*3/4 + 23, YRES/3+40, XRES*3/4 + 32, YRES/3+150, s, c)
draw_line(XRES*3/4 - 32, YRES/3+150, XRES*3/4 + 32, YRES/3+150, s, c)

draw_line(XRES*3/4 - 35, YRES/3+150, XRES*3/4 - 35, YRES/3+155, s, c)
draw_line(XRES*3/4 + 35, YRES/3+150, XRES*3/4 + 35, YRES/3+155, s, c)
draw_line(XRES*3/4 - 35, YRES/3+150, XRES*3/4 + 35, YRES/3+150, s, c)
draw_line(XRES*3/4 - 35, YRES/3+155, XRES*3/4 + 35, YRES/3+155, s, c)

draw_line(XRES*3/4 - 40, YRES/3+165, XRES*3/4 - 40, YRES/3+155, s, c)
draw_line(XRES*3/4 + 40, YRES/3+165, XRES*3/4 + 40, YRES/3+155, s, c)
draw_line(XRES*3/4 - 40, YRES/3+155, XRES*3/4 + 40, YRES/3+155, s, c)
draw_line(XRES*3/4 - 40, YRES/3+165, XRES*3/4 + 40, YRES/3+165, s, c)

draw_line(XRES*3/4 - 55, YRES/3+185, XRES*3/4 - 50, YRES/3+165, s, c)
draw_line(XRES*3/4 + 55, YRES/3+185, XRES*3/4 + 50, YRES/3+165, s, c)
draw_line(XRES*3/4 - 50, YRES/3+165, XRES*3/4 + 50, YRES/3+165, s, c)
draw_line(XRES*3/4 - 55, YRES/3+185, XRES*3/4 + 55, YRES/3+185, s, c)

draw_line(XRES*3/4 - 57, YRES/3+195, XRES*3/4 - 57, YRES/3+185, s, c)
draw_line(XRES*3/4 + 57, YRES/3+195, XRES*3/4 + 57, YRES/3+185, s, c)
draw_line(XRES*3/4 - 57, YRES/3+185, XRES*3/4 + 57, YRES/3+185, s, c)
draw_line(XRES*3/4 - 57, YRES/3+195, XRES*3/4 + 57, YRES/3+195, s, c)

draw_line(XRES*3/4 - 55, YRES/3+195, XRES*3/4 - 55, YRES/3+198, s, c)
draw_line(XRES*3/4 + 55, YRES/3+195, XRES*3/4 + 55, YRES/3+198, s, c)
draw_line(XRES*3/4 - 55, YRES/3+198, XRES*3/4 + 55, YRES/3+198, s, c)


display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
