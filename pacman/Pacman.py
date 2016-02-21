import sys
import pygame
from pygame.locals import *
from math import floor
import random


def init_window():
    pygame.init()
    pygame.display.set_mode((512, 512))
    pygame.display.set_caption('Pacman')


def draw_background(scr, img=None):
    if img:
        scr.blit(img, (0, 0))
    else:
        bg = pygame.Surface(scr.get_size())
        bg.fill((128, 128, 128))
        scr.blit(bg, (0, 0))


class Map():
    def __init__(self, map_size, filename='C:/Users/Sergey/PycharmProjects/untitled2/Pacman/resources/map.txt'):
        self.map = []
        self.map_size = map_size
        self.tile_size = tile_size
        with open(filename) as f:
            lines = f.readlines()
            for i in range(len(lines)):
                self.map.append([])
                for j in range(len(lines[i])):
                    self.map[-1].append(Item(lines[i][j], j, i, tile_size, map_size))

    def get(self, x, y):
        return self.map[x][y]


class GameObject(pygame.sprite.Sprite):
    def __init__(self, img, x, y, tile_size, map_size):
        pygame.sprite.Sprite.__init__(self)
        if img != None:
            self.image = pygame.image.load(img)
        else:
            self.image = None
        self.screen_rect = None
        self.x = 0
        self.y = 0
        self.tick = 0
        self.tile_size = tile_size
        self.map_size = map_size
        self.set_coord(x, y)

    def set_coord(self, x, y):
        self.x = x
        self.y = y
        self.screen_rect = pygame.locals.Rect(floor(x) * self.tile_size, floor(y) * self.tile_size, self.tile_size, self.tile_size )

    def game_tick(self):
        self.tick += 1

    def draw(self, scr):
        if self.image != None:
            scr.blit(self.image, (self.screen_rect.x, self.screen_rect.y))


class Ghost(GameObject):
    number = 5
    ghosts = []
    def __init__(self, x, y, tile_size, map_size):
        GameObject.__init__(self, 'C:/Users/Sergey/PycharmProjects/untitled2/Pacman/resources/ghost.png', x, y, tile_size, map_size)
        self.direction = 0
        self.velocity = 4.0 / 10.0

    def decide(self):
        x, y = int(self.x), int(self.y)
        if y == int(pacman.y):
            for X in range(x, 16):
                if m.map[y][X].isWall:
                    break
                if X == int(pacman.x):
                    return 1
            for X in reversed(range(x)):
                if m.map[y][X].isWall:
                    break
                if X == int(pacman.x):
                    return 3
        if x == int(pacman.x):
            for Y in range(y, 16):
                if m.map[Y][x].isWall:
                    break
                if Y == int(pacman.y):
                    return 2
            for Y in reversed(range(y)):
                if m.map[Y][x].isWall:
                    break
                if Y == int(pacman.y):
                    return 4

    def game_tick(self):
        super(Ghost, self).game_tick()

        if self.tick % 2 == 0 or self.direction == 0:
            self.direction = random.randint(1, 4)

        choice = self.decide()
        if choice:
            self.direction = choice

        if self.direction == 1:
            if m.map[int(self.y)][int(self.x+self.velocity)].isWall == False:
                self.x += self.velocity
                if self.x >= self.map_size-1:
                    self.x = self.map_size-1
                    self.direction = random.randint(1,4)
        elif self.direction == 2:
            if m.map[int(self.y+self.velocity)][int(self.x)].isWall == False:
                self.y += self.velocity
                if self.y >= self.map_size-1:
                    self.y = self.map_size-1
                    self.direction = random.randint(1,4)
        elif self.direction == 3:
            if m.map[int(self.y)][int(self.x-self.velocity)].isWall == False:
                self.x -= self.velocity
                if self.x <= 0:
                    self.x = 0
                    self.direction = random.randint(1,4)
        elif self.direction == 4:
            if m.map[int(self.y-self.velocity)][int(self.x)].isWall == False:
                self.y -= self.velocity
                if self.y <= 0:
                    self.y = 0
                    self.direction = random.randint(1,4)
        self.set_coord(self.x, self.y)

def draw_ghost(screen):
    for a in Ghost.ghosts:
        a.draw(screen)

def create_ghost():
    Ghost.ghosts = [Ghost(0, 0,tile_size, map_size) for a in range (Ghost.number)]

def tick_ghost():
    for a in Ghost.ghosts:
        a.game_tick()

class Pacman(GameObject):

    def __init__(self, x, y, tile_size, map_size, m):
        GameObject.__init__(self, 'C:/Users/Sergey/PycharmProjects/untitled2/Pacman/resources/pacman.png', x, y, tile_size, map_size)
        self.direction = 0
        self.velocity = 4.0 / 10.0

    def game_tick(self):
        super(Pacman, self).game_tick()
        if self.direction == 1:
            if m.map[int(self.y)][int(self.x)+1].isWall == False:
                self.x += self.velocity
                if self.x >= self.map_size-1:
                    self.x = self.map_size-1

        elif self.direction == 2:
            if m.map[int(self.y)+1][int(self.x)].isWall == False:
                self.y += self.velocity
                if self.y >= self.map_size-1:
                    self.y = self.map_size-1

        elif self.direction == 3:
            if m.map[int(self.y)][int(self.x)-1].isWall == False:
                self.x -= self.velocity
                if self.x <= 0:
                    self.x = 0

        elif self.direction == 4:
            if m.map[int(self.y)-1][int(self.x)].isWall == False:
                self.y -= self.velocity
                if self.y <= 0:
                    self.y = 0

        if m.map[int(self.y)][int(self.x)].food == True:
            m.map[int(self.y)][int(self.x)] = pygame.image.load('C:/Users/Sergey/PycharmProjects/untitled2/Pacman/resources/wall.png')



        self.set_coord(self.x, self.y)


class Item(GameObject):

    def __init__(self, char, x, y, tile_size, map_size):
        GameObject.__init__(self, None, x, y, tile_size, map_size)
        self.isWall = False
        self.food = False
        #self.isBreakable = False

        if char == 'X':
            self.image = pygame.image.load('C:/Users/Sergey/PycharmProjects/untitled2/Pacman/resources/wall.png')
            self.isWall = True

        if char == '.':
            self.image = pygame.image.load('C:/Users/Sergey/PycharmProjects/untitled2/Pacman/resources/food.png')
            self.food = True

    def game_tick(self):
        super(Item, self).game_tick()


def process_events(events, pacman):
    for event in events:
        if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit(0)
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                pacman.direction = 3
            elif event.key == K_RIGHT:
                pacman.direction = 1
            elif event.key == K_UP:
                pacman.direction = 4
            elif event.key == K_DOWN:
                pacman.direction = 2
            elif event.key == K_SPACE:
                pacman.direction = 0


if __name__ == '__main__':
    init_window()
    tile_size = 32
    map_size = 16
    m = Map(map_size)
    ghost = Ghost(0, 0, tile_size, map_size)
    pacman = Pacman(5, 9, tile_size, map_size, m)
    create_ghost()

    background = pygame.image.load("C:/Users/Sergey/PycharmProjects/untitled2/Pacman/resources/background.png")
    screen = pygame.display.get_surface()


    while 1:
        process_events(pygame.event.get(), pacman)
        pygame.time.delay(100)
        pacman.game_tick()
        tick_ghost()
        for line in m.map:
            for item in line:
                item.game_tick()
        draw_background(screen, background)
        for line in m.map:
            for item in line:
                item.draw(screen)
        pacman.draw(screen)
        ghost.draw(screen)
        ghost.game_tick()
        draw_ghost(screen)
        pygame.display.update()