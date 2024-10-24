#! /user/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import pylab as pl
import time
from matplotlib import cm

def IterPoint(c):
    z = c
    for i in range(1, 100): 
        if abs(z) > 2:
            break  
        z = z ** 2 + c
    return i  

def drawMandelbrot(cx, cy, d):
    x0, x1, y0, y1 = cx - d, cx + d, cy - d, cy + d
    y, x = np.ogrid[y0:y1:200j, x0:x1:200j]
    c = x + y * 1j
    start = time.process_time()
    mandelbrot = np.frompyfunc(IterPoint, 1, 1)(c).astype(np.float)
    print("time=", time.process_time() - start)
    pl.imshow(mandelbrot, cmap=cm.Blues_r, extent=[x0, x1, y0, y1])
    pl.gca().set_axis_off()


x, y = 0.27322626, 0.595153338

pl.subplot(231)
drawMandelbrot(-0.5, 0, 1.5)
for i in range(2, 7):
    pl.subplot(230 + i)
    drawMandelbrot(x, y, 0.2 ** (i - 1))
pl.subplots_adjust(0.02, 0, 0.98, 1, 0.02, 0)
pl.show()

