import pygame
pygame.init()
pygame.mixer.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (240, 240, 80)
ORANGE = (202, 75, 25) 
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (222, 100, 0)            #Цвета
PURPLE = (150, 0, 222)
DARK_GREEN = (0, 75, 0)
HYPERCORIDOR_COLOR = (255, 255, 255, 100)
NEBULA_COLOR = (160, 30, 200, 150)
GREY = (99, 99, 99)

OLD_COLOR = (160, 160, 120)
WINDOW_COLOR = (200,200, 180)
WINDOWCONT_COLOR = (120, 120, 60)




MAX_ZOOM = 1000
MIN_ZOOM = 0.01
ZOOM_SDVYG = 1.015

G = 0.000000000066743015151515151515151515     # Грав постоянная  6.67430(15) * 10 **(-11)

HIGHT = pygame.display.Info().current_h * 0.96
WIDHT = pygame.display.Info().current_w * 1  # Параметры дисплея

chrift = pygame.font.Font(None, int(24))
button_chrift = pygame.font.Font(None, int(36))
big_chrift = pygame.font.Font(None, int(55))

screen = pygame.display.set_mode((WIDHT, HIGHT))
screenalpha = screen.convert_alpha()
clock = pygame.time.Clock()