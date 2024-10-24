#! /user/bin/python3
# -*- coding: utf-8 -*-

from math import sin, cos, pi
import matplotlib.pyplot as pl
from matplotlib import collections

d = [30, 90, 150, 210, 270, 330]
lines = []
queue = []

def move(j, p, l):
    r = d[j] * pi / 180
    t = (p[0] + l * cos(r), p[1] + l * sin(r))
    lines.append(((p[0], p[1]), (t[0], t[1])))
    queue.append((p[0] + (t[0] - p[0]) / 3, p[1] + (t[1] - p[1]) / 3))
    return t

def Hexagasket(iter=1, L=1.0):
    P = (0.0, 0.0)
    for i in range(iter):
        if i == 0:
            ini = 0
            for j in range(6):
                P = move((ini+j) % 6, P, L)

        elif i==1 :
            init = (6 - 2*i) % 6
            for n in range(6 ** i):
                ini = (n + init) % 6
                P = queue[0]
                queue.pop(0)
                for j in range(6):
                    P = move((ini + j) % 6, P, L)

        elif i==2:
            init = (6 - 2*i) % 6
            for m in range(6):
                init1 = (init + m) % 6
                for n in range(6):
                    ini = (init1 + n) % 6
                    P = queue[0]
                    queue.pop(0)
                    for j in range(6):
                        P = move((ini + j) % 6, P, L)

        elif i==3:
            init = (6 - 2*i) % 6
            for m in range(6):
                init1 = (init + m) % 6
                for n in range(6):
                    init2 = (init1 + n) % 6
                    for k in range(6):
                        ini = (init2 + k) % 6
                        P = queue[0]
                        queue.pop(0)
                        for j in range(6):
                            P = move((ini + j) % 6, P, L)

        elif i==4:
            init = (6 - 2*i) % 6
            for m in range(6):
                init1 = (init + m) % 6
                for n in range(6):
                    init2 = (init1 + n) % 6
                    for k in range(6):
                        init3 = (init2 + k) % 6
                        for s in range(6):
                            ini = (init3 + k) % 6
                            P = queue[0]
                            queue.pop(0)
                            for j in range(6):
                                P = move((ini + j) % 6, P, L)

        L /= 3
    return lines


def draw(ax):
    lines = Hexagasket(5)
    linecollections = collections.LineCollection(lines)
    ax.add_collection(linecollections, autolim=True)
    ax.axis("equal")
    ax.set_axis_off()
    ax.set_xlim(ax.dataLim.xmin, ax.dataLim.xmax)
    ax.invert_yaxis()

fig = pl.figure(figsize=(7, 4.5))
fig.patch.set_facecolor("w")

for i in range(1):
    ax = fig.add_subplot(111)
    draw(ax)
    pl.title('Hexagasket')
    pl.savefig('./hexagasket.jpg')

fig.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)
pl.show()