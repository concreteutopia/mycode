#!/usr/bin/env python3

from crayon import *

print("░▒▓")

print("\u0420\u043e\u0441\u0441\u0438\u044f")

print("\u2588\u2589\u258a\u258b\u258c\u258d\u258e\u258f\u2593\u2592\u2591")

#my_grayscale_color = gray(0) # (0 - 23)

#my_rgb_color = rgb(0, 0, 0) # (0 - 5) scale to accomodate 216 colors


for x in range(0,24):
    my_grayscale_color = gray(x)
    color_config = {'fg':my_grayscale_color, 'bg':0}
    printout("\u2588", color=color_config)

