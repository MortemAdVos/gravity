from pygame import *
from math import *


def angle_on(vector1:Vector2, vector2:Vector2):
    sr = vector2 - vector1
    try:
        atg = (atan(sr.y / sr.x))
    except ZeroDivisionError:
        atg = pi
    if sr.x <= 0:
        atg += pi
    return atg