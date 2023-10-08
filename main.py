#доделать инфоокно


from math import *
from pygame import *
from pygame import Vector2
from defines import *
from functions import *
from functions import Vector2
pygame.init()
pygame.mixer.init()
import time

TPS = 600000
TT = 1000
ticktime = TT
total_ticks = 0

SCALE = 1_000_000_000

ZOOM = 1
SDVYG_ZOOM = Vector2(0,0)
SDVYG = Vector2(0,0)

k_eq_down = 0
k_minus_down = 0
k_left_down = 0
k_up_down = 0
k_down_down = 0
k_right_down = 0
FOCUS_ID = 0





class InfoWindow():

    def __init__(self, id, name, w=300,h=500, contur=4):
        self.windowid = id
        self.w = w
        self.h = h
        self.name = name
        self.cont = contur
        self.pos = Vector2(0,0)
        self.text_color = BLACK
        self.pos = Vector2(WIDHT-self.w, 0)
        # print(physobjlist[FOCUS_ID].name)

        self.text_time = chrift.render(f'Time: {total_ticks*TT/60/60/24}', True, self.text_color)

        self.text_name = chrift.render(f'Name: {physobjlist[FOCUS_ID].name}', True, self.text_color)
        self.text_mass = chrift.render(f'Mass: {physobjlist[FOCUS_ID].mass}', True, self.text_color)

        self.text_speed = chrift.render(f'Global Speed: {physobjlist[FOCUS_ID].speed.length()}', True, self.text_color)
        self.text_boost = chrift.render(f'Global Boost: {physobjlist[FOCUS_ID].boost.length()}', True, self.text_color)

        self.text_orbitalspeed = chrift.render(f'Orbital Speed: None', True, self.text_color)
        self.text_orbitalboost = chrift.render(f'Orbital Boost: None', True, self.text_color)

        self.text_zoom = chrift.render(f'Zoom', True, self.text_color)
    
    def update(self):
        self.text_zoom = chrift.render(f'Zoom: {ZOOM}', True, self.text_color)
        self.text_tityl = big_chrift.render(f'{self.name}', True, self.text_color)
        self.text_time = chrift.render(f'Time: {round(total_ticks*TT/60/60/24, 5)}', True, self.text_color)
        if total_ticks % 5 == 0:

            self.text_name = chrift.render(f'Name: {physobjlist[FOCUS_ID].name}', True, self.text_color)
            self.text_mass = chrift.render(f'Mass: {physobjlist[FOCUS_ID].mass}', True, self.text_color)

            self.text_speed = chrift.render(f'Global Speed: {physobjlist[FOCUS_ID].speed.length()}', True, self.text_color)
            self.text_boost = chrift.render(f'Global Boost: {physobjlist[FOCUS_ID].boost.length()}', True, self.text_color)

            if  type(physobjlist[FOCUS_ID].motherid) == int:
                self.text_orbitalspeed = chrift.render(f'Orbital Speed: {physobjlist[FOCUS_ID].speed.length()- physobjlist[physobjlist[FOCUS_ID].motherid].speed.length()}', True, self.text_color)
                self.text_orbitalboost = chrift.render(f'Orbital Boost: {physobjlist[FOCUS_ID].boost.length() - physobjlist[physobjlist[FOCUS_ID].motherid].boost.length()}', True, self.text_color)
            else:
                self.text_orbitalspeed = chrift.render(f'Orbital Speed: None', True, self.text_color)
                self.text_orbitalboost = chrift.render(f'Orbital Boost: None', True, self.text_color)

        self.rendered_text = [self.text_time, self.text_name, self.text_mass, self.text_speed, self.text_orbitalspeed, self.text_boost, self.text_orbitalboost, self.text_zoom]
        pygame.draw.rect(screen, WINDOWCONT_COLOR, (WIDHT-self.w, 0, WIDHT, self.h))
        pygame.draw.rect(screen, WINDOW_COLOR, (WIDHT-self.w+self.cont, self.cont, WIDHT-self.cont*100, self.h-self.cont*2))
        screen.blit(self.text_tityl, (self.pos.x+self.w/2-30, 10))
        for i in range(len(self.rendered_text)):
            screen.blit(self.rendered_text[i], (self.pos.x+10, 52 + i*26))
            pygame.draw.line(screen, WINDOWCONT_COLOR, (self.pos.x,50 + i*26-4), (self.pos.x+self.w,50 + i*26-4), 4)


class PhysicObject():

    def __init__(self, name, id: int, motherobj, mass:float, poluos:float, angle:float, radius:float, speed_orb:float, waycolor=BLACK):
        self.mass: float = mass 
        self.name = name
        self.pos: Vector2 = Vector2(poluos*cos(radians(angle)), poluos*sin(radians(angle)))
        self.speed: Vector2 = Vector2(speed_orb*cos(radians(angle+90)), speed_orb*sin(radians(angle+90)))
        if motherobj:
            self.motherid = motherobj.id 
            self.speed += motherobj.speed
            self.pos += motherobj.pos
        else: self.motherid = False
        self.radius: float = radius
        # self.new_pos: Vector2 = Vector2(pos_x, pos_y)
        self.is_update: bool = False
        self.id: int = id
        self.isshowinfo = False

        self.waycolor = waycolor + (125,)
        self.waycolorreversev = (255-waycolor[0], 255-waycolor[1], 255-waycolor[2])

        self.boost: Vector2=Vector2(0,0)
        self.power: Vector2=Vector2(0,0)
        self.way = []
        self.infowindow = 0

    def gravityupdate(self, physobjs):
        self.power = Vector2(0,0)
        for physobj in physobjs:
            if self.id == physobj.id: continue
            try:
                self.power.x += ((G * self.mass * physobj.mass / (self.pos.distance_to(physobj.pos) ** 2)) * cos(angle_on(self.pos, physobj.pos)))
                self.power.y += ((G * self.mass * physobj.mass / (self.pos.distance_to(physobj.pos) ** 2)) * sin(angle_on(self.pos, physobj.pos)))
            except ZeroDivisionError: pass
        self.boost = self.power / self.mass


    def update(self):
        if self.id == FOCUS_ID: is_select = True 
        else: is_select = False
        
        if len(self.way) >= 2**10:
            self.way.pop(0)
        if total_ticks % 10 == 0:
            self.way.append(self.pos.copy())
        if is_select:
            for posw in self.way:
                pygame.draw.circle(screenalpha, self.waycolorreversev, posw/SCALE*ZOOM + SDVYG + SDVYG_ZOOM, 2, 99999)
        else: 
            for posw in self.way:
                pygame.draw.circle(screenalpha, self.waycolor, posw/SCALE*ZOOM + SDVYG + SDVYG_ZOOM, 2, 99999)
        self.pos += (self.speed * ticktime + self.boost * ticktime**2 /2)
        self.speed += self.boost * ticktime
        self.blitpos = self.pos/SCALE*ZOOM + SDVYG + SDVYG_ZOOM
        pygame.draw.circle(screen, WHITE, self.blitpos, self.radius*(ZOOM+99)/100, 99999)
        if is_select: pygame.draw.circle(screen, RED, self.blitpos, self.radius*(ZOOM+99)/100, 1)

        # print(self.way)
        # print(self.pos,';;' ,self.boost)





class Button():

    def __init__(self, w:int, h:int, pos:Vector2, text:str):
        self.w = w
        self.h = h
        self.pos = pos 
        self.text = text
        self.on = False
        self.off = True
        self.color = BLACK
        self.rendered_text = button_chrift.render(self.text, True, self.color)

    def update(self):
            pygame.draw.rect(screen, self.color, (self.pos.x,self.pos.y, self.pos.x+self.w, self.pos.y+self.h))
            screen.blit(self.rendered_text, (self.pos.x, self.pos.y))
        # pygame.draw.rect(screen, self.color, (self.pos.x, self.pos.y, self.pos.x + self.w, self.pos.y + self.h))

    def click(self):
        self.on = not self.on
        self.off = not self.off
        if self.color == WHITE:
            self.color= GREY
        else:
            self.color = WHITE
class ButtonPause(Button):
     
    def  __init__(self, w: int, h: int, pos: Vector2, text: str):
        super().__init__(w, h, pos, text)

    def update(self):
        super().update()

    def click(self):
        super().click()
        global ticktime
        if self.on:
            self.color = GREY
            ticktime = TT
        else:
            BLACK
            ticktime = 0


btn_pause = ButtonPause(80, 30, Vector2(0,0), "PAUSE")

btn_pause.click()
btn_pause.click()


sun = PhysicObject('sun', 0, False, 1.9885e+30, 0, 0, 15,0 , ORANGE)
mercury = PhysicObject('mercury', 1, sun, 333022e+23, 57817445000, 0, 3, 47360, RED)
venus = PhysicObject('venus', 2, sun, 4.8675e+24, 108208930000, 0, 4, 35020, GREEN)

terra = PhysicObject('terra', 3, sun, 5.9726e+24, 1.496e+11, 0, 5, 29800, BLUE)
moon = PhysicObject('moon', 4, terra, 7.3477e+22, 384399000, 0, 3, 1023, GREY)
geostat = PhysicObject('geostat', 5, terra,  440075, 3.5786e+7, 0, 2, 3070, PURPLE)

mars = PhysicObject('mars', 6, sun, 6.4171e+23, 2.279382e+11, 0, 4, 24130, RED)
fobos = PhysicObject('fobos', 7,  mars, 1.072e+16, 9.3772e+7, 0, 1, 2138, WHITE)
daimos = PhysicObject('daimos', 8, mars, 1.4762e+15, 2.3458e+7, 0,1, 1351.3, BLACK)

jupiter = PhysicObject('jupiter', 9, sun, 1.8986e+27, 7.785472e+11, 0, 9, 13070, YELLOW)
metida = PhysicObject('metida', 10, jupiter, 3.7e+16, 1.27690e+8, 0, 1, 3150)
adratea = PhysicObject('adratea', 11, jupiter, 2.0e+15, 1.2869e+8, 0, 1, 3137)
carpo = PhysicObject('carpo', 12, jupiter, 4.5e+13, 1.7144873e+10, 0, 1, 2732)
amaltea = PhysicObject('amaltea',13, jupiter, 2.08e+18, 1.81366e+8, 0, 1, 2657)
fiva = PhysicObject('fiva', 14, jupiter, 4.3e+17, 2.21889e+8, 0, 1, 23923)
io = PhysicObject('io', 15, jupiter, 8.9e+22, 4.217e+8, 0, 1, 17334, YELLOW)
evrope = PhysicObject('evrope', 16, jupiter, 4.8e+22, 6.71034e+8, 0, 1, 13740, GREEN)
ganimed = PhysicObject('ganimed', 17, jupiter, 1.5e+23, 1.070412e+9, 0, 1, 10880)
callisto = PhysicObject('callisto', 18, jupiter, 1.1e+23, 1.882709e+9, 0, 1, 8204, RED)
femisto = PhysicObject('femisto',19, jupiter, 6.9e+14, 7.393216e+9, 0, 1, 4137)
leda = PhysicObject('leda', 20, jupiter, 1.1e+16, 1.1451971e+10, 0, 1, 3457)
gimalia = PhysicObject('gimalia', 21, jupiter, 4.2e+18, 1.1451971e+10 , 0, 1, 3323)
lisitea = PhysicObject('lisitea', 22, jupiter, 6.3e+16, 1.174056e+10, 0, 1, 3294)
elara = PhysicObject('elara', 23, jupiter, 8.7e+17, 1.1778034e+10, 0, 1, 3299)
dia = PhysicObject('dia', 24, jupiter, 9.0e+13, 1.2570424e+10, 0, 1, 3286)

saturn = PhysicObject('saturn', 25, sun, 5.684e+26, 1.429394069e+12, 0, 9, 9.69e+3, WHITE)
mimas = PhysicObject('mimas', 26, saturn, 4e+19, 1.85539e+8, 0, 1, 14992)
encelad = PhysicObject('encelad', 27, saturn, 1.1e+20, 2.37948e+8, 0, 1, 12360)
tetis = PhysicObject('tetis', 28, saturn, 6.2e+20, 2.94619e+8 , 0, 1, 11276)
diona = PhysicObject('diona', 29, saturn, 1.1e+21, 3.77396e+8, 0, 1, 10165 )
rea = PhysicObject('rea', 0, saturn, 2.3e+21, 5.27108e+8, 0, 1, 8518)
titan = PhysicObject('titan', 0, saturn, 1.35e+23, 1.22187e+9, 0, 1, 5554)
uapet = PhysicObject('uapet', 0, saturn, 1.8e+21, 3.56082e+9, 0, 1, 3278)
yanus = PhysicObject('yanus', 0, saturn, 1.89388e+18, 1.515e+8, 0, 1, 15807)

uranus =PhysicObject('uranus', 0, sun, 8.6813e+25, 2.876679082e+12, 0, 8, 6810)
miranda = PhysicObject('miranda', 0, uranus, 6.6e+19, 1.2939e+8, 0, 1, 6657)
ariel = PhysicObject('ariel', 0, uranus, 1.35e+21, 1.9102e+8, 0, 1, 5512)
umbriel = PhysicObject('umbriel', 0, uranus, 1.17e+21, 2.663e+8, 0, 1, 4673 )
titania = PhysicObject('titania', 0, uranus, 3.53e+21, 4.3591e+8, 0, 1, 3641)
oberon = PhysicObject('oberon', 0, uranus, 3.01e+21, 5.8352e+8, 0, 1, 3152)

neptun = PhysicObject('neptun', 0, sun, 1.02409e+26, 4.503443661e+12, 0, 10, 5430)
triton = PhysicObject('triton', 0, neptun, 2.1e+22, 3.5448e+8, 0, 1, 4386)
nereida = PhysicObject('nereida', 0, neptun, 3.1e+19, 5.5134e+9, 0, 1, 1113)
protey = PhysicObject('protey', 0, neptun, 5e+19, 1.17647e+8, 0, 1, 7625)


black_hole = PhysicObject('black_hole', 0, sun, sun.mass * 1e+5, 1.0e+12, -45, 15, 0, WHITE)

physobjlist = [sun,
               mercury,
               venus, 
               terra, moon, geostat,
               mars, fobos, daimos,
               jupiter, metida, adratea, carpo, amaltea, fiva, io, evrope, ganimed, callisto, femisto, leda, gimalia, lisitea, elara, dia,
               saturn, mimas, encelad, tetis, diona, rea, titan, uapet,
               uranus, miranda, ariel, umbriel, titania, oberon,
               neptun, triton, nereida, protey
               ]

for obj in physobjlist:
    obj.id = physobjlist.index(obj)


print(len(physobjlist))

infowindow = InfoWindow(0, "Info")

windowlist = [infowindow]



print('//start//')
while 1:

    if btn_pause.on: total_ticks += 1

    # print(btn_pause.on, btn_pause.off)
    # print(sun.infowindow)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.type != pygame.MOUSEWHEEL:
            if event.pos[0] < btn_pause.pos.x + btn_pause.w and event.pos[1] < btn_pause.pos.x + btn_pause.w:
                if event.pos[0] > btn_pause.pos.x and event.pos[1] > btn_pause.pos.x:  
                    # print(2)  
                    btn_pause.click()

            else:
                for planet in physobjlist:
                    if Vector2(event.pos).distance_to(planet.blitpos) < 25:
                        FOCUS_ID = planet.id
                        break

        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_EQUALS:
                k_eq_down = not k_eq_down
            elif event.key == pygame.K_MINUS:
                k_minus_down = not k_minus_down
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                k_left_down = not k_left_down
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                k_up_down = not k_up_down
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                k_down_down = not k_down_down
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                k_right_down = not k_right_down
        
        elif event.type == pygame.MOUSEWHEEL:
            if ZOOM < MAX_ZOOM and event.y > 0:
                ZOOM *= 1 + event.y /100
                SDVYG_ZOOM.x = -WIDHT * (ZOOM - 1) * 0.5
                SDVYG_ZOOM.y = -HIGHT * (ZOOM - 1) * 0.5
                SDVYG *= 1+event.y/100

            elif ZOOM > MIN_ZOOM and event.y < 0:
                ZOOM /= 1-  event.y /100
                SDVYG_ZOOM.x = -WIDHT * (ZOOM - 1) * 0.5
                SDVYG_ZOOM.y = -HIGHT * (ZOOM - 1) * 0.5
                SDVYG /= 1-event.y/100
            
        # 
        # print(event)
    if k_eq_down:
        if ZOOM < MAX_ZOOM:
            ZOOM *= ZOOM_SDVYG
            SDVYG_ZOOM.x = -WIDHT * (ZOOM - 1) * 0.5
            SDVYG_ZOOM.y = -HIGHT * (ZOOM - 1) * 0.5
            SDVYG *= ZOOM_SDVYG
    if k_minus_down:
        if ZOOM > MIN_ZOOM:
            ZOOM /= ZOOM_SDVYG
            SDVYG_ZOOM.x = -WIDHT * (ZOOM - 1) * 0.5
            SDVYG_ZOOM.y = -HIGHT * (ZOOM - 1) * 0.5
            SDVYG /= ZOOM_SDVYG
    if k_left_down:
        # if SDVYG_X < 350 * ZOOM:
            SDVYG.x += 10 #/ ZOOM
    if k_right_down:
        # if SDVYG_X > -350 * ZOOM:
            SDVYG.x -= 10 #/ ZOOM
    if k_up_down:
        # if SDVYG_Y < 350 * ZOOM:
            SDVYG.y += 10 #/ ZOOM
    if k_down_down:
        # if SDVYG_Y > -350 * ZOOM:
            SDVYG.y-= 10 #/ ZOOM
    screenalpha.fill([0,0,0,0])
    screen.fill(OLD_COLOR)


    for physobj in physobjlist:
        physobj.gravityupdate(physobjlist)
    for physobj in physobjlist:
        physobj.update()
    screen.blit(screenalpha, (0,0))
    for window in windowlist:
        window.update()
    btn_pause.update()
    # print(FOCUS_ID)
    clock.tick(TPS)
    pygame.display.flip()
    