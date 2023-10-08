from math import *
# from defines import *
import pygame
pygame.init()
from pygame import *
import time

# def angle_on(vector1:Vector2, vector2:Vector2):
#     sr = vector2 - vector1
#     try:
#         atg = (atan(sr.y / sr.x))
#     except ZeroDivisionError:
#         atg = pi
#     if sr.x <= 0:
#         atg += pi
#     return degrees(atg)
# a = Vector2(0, -55)
# b = Vector2(-55, 0)
# print(a.length())

# # c = Vector2(0, 3)
# # d = Vector2(3, 0)
# # print(c / 2)
# print(angle_on(a,b))
# print((b+a).as_polar()[1])
# print(a.angle_to(b))
# print(radians(a.angle_to(b)))
# print(a.distance_to(b))
# print(b.distance_to(a))

# print(1.17647e+8*pi*2/1.122/24/60/60)
# print(not not False)



SIDE = 1000

screen = pygame.display.set_mode((SIDE, SIDE))
clock = pygame.time.Clock()



radius = 200
angle = 0
pos = Vector2(radius * cos(radians(angle)), sin(radians(angle))*radius)
zone = Vector2(25, 75)
screen.fill((0,0,0))
pygame.draw.ellipse(screen, (255,0,0), pygame.Rect((SIDE/2 - radius-zone.x, SIDE/2 - radius-zone.y, radius*2,  radius*2 )), 3)
pygame.draw.ellipse(screen, (0,255,0), pygame.Rect((SIDE/2 - radius-zone.x, SIDE/2 - radius, radius*2,  radius*2 )), 3)
pygame.draw.ellipse(screen, (0,0,255), pygame.Rect((SIDE/2 - radius, SIDE/2 - radius-zone.y, radius*2,  radius*2 )), 3)
pygame.draw.ellipse(screen, (255,255,255), pygame.Rect((SIDE/2 - radius, SIDE/2 - radius, radius*2,  radius*2 )), 3)

while 1:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    if angle < 360:
        pos = Vector2(SIDE/2 +radius * cos(radians(angle)), SIDE/2 + sin(radians(angle))*radius)
        pygame.draw.rect(screen, (255,255,255), pygame.Rect((pos.x-zone.x, pos.y-zone.y, zone.x, zone.y)), 1, 1)
        angle += 0.1
    clock.tick(30)
    pygame.display.flip()
    # print(pos)


# a = int(input())
# b = input().split()
# maxl = 0
# maxzn = None
# ln = 0
# i = 0
# old = 'adadadadadadadadadsv32'
# for el in b:
#     i += 1

#     if el == old and i == len(b):
#         ln += 1
#         maxl = ln 
#         maxzn = old

#     elif el == old:
#         ln += 1

#     elif ln > maxl :
#         maxl = ln 
#         maxzn = old
#         ln = 0

#     else:
#         ln = 0
#     old = el 
    
# if maxzn == None:
#     maxzn = b[0]
# print(maxzn, maxl+1)


        # N, x, y = map(int, input().split())
        # n = 1
        # t = min(x, y)
        # t1 = -1
        # print(n)
        # if N == 1:
        #     print(t)
        # else:
        #     while 1:
        #         t1 += 1
        #         if t1 % x == 0:
        #             n += 1
        #         if t1 % y == 0:
        #             n += 1
        #         if n >= N: break
        #         print(n)
        # print(t+t1)

# S, N = map(int, input().split())
# mlist = input().split()

# for i in range(len(mlist)):
#     mlist[i] = [0, int(mlist[i])]


# med = mlist[-1][1] - mlist[0][1]
# med /= N - 1
# # print(f'med=  {med}')


# mlist[0][0] = 1
# min = 999999
# localpos = 0
# lastcow = 0
# for i in range(N):
#     for j in range(len(mlist)):
#         try:
#             localpos = mlist[j][1] - lastcow
#         except IndexError:
#             if abs(localpos) < min: min = abs(localpos)
#             localpos = 9999
#         try:
#             if mlist[j][0]: 
#                 if localpos < min: min = abs(localpos)
#                 localpos = 9999
#                 lastcow = mlist[j][1]
#                 continue
#             elif abs(localpos -med) <= abs(localpos - mlist[j][1] + mlist[j-1][1]- med) and abs(localpos -med) <= abs(localpos - mlist[j][1] + mlist[j+1][1]- med):
#                 mlist[j][0] = 1
#                 lastcow = mlist[j][1]
#                 if localpos < min: min = localpos
#                 localpos = 99999
#         except IndexError:
#             mlist[j][0] = 1
#             if localpos < min: min = abs(localpos)
#             localpos = 9999
#         # print(f'localpos  {localpos}')

# print(mlist)
# print(min)


