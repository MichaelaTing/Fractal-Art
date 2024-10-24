#! /user/bin/python3
# -*- coding: utf-8 -*-

import pygame

pygame.init()
screen = pygame.display.set_caption('康托集')
screen = pygame.display.set_mode([1000, 250])
screen.fill([255, 255, 255])
pygame.display.flip()

len0 = 1000  
leni = len0  
line = 0  


while leni > 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    n = 2**line  
    tep = [0, ]  
    while len(tep) < n:
        nt = (tep[-1] + leni) * 2  
        tepp = []  
        for j in tep:
            tepp.append(nt + j)
        tep.extend(tepp)
    for k in tep:
        pygame.draw.line(screen, [0, 0, 0], [
                         k, 30 * line + 5], [k + leni, 30 * line + 5], 10)
    pygame.display.flip()
    line += 1
    leni = leni / 3

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()