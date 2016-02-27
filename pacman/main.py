import sys
from pygame.locals import *
import game_objects


def init_window(size, tile):
    game_objects.pygame.init()
    game_objects.pygame.display.set_mode((size*tile, size*tile))
    game_objects.pygame.display.set_caption('Pacman')


def draw_background(scr, img=None):
    if img:
        scr.blit(img, (0, 0))
    else:
        bg = game_objects.pygame.Surface(scr.get_size())
        bg.fill((128, 128, 128))
        scr.blit(bg, (0, 0))


class Map:
    """
   Type that describes game map. Contains matrix of cell objects, food quantity on a map,
   square map size and tile size.
   Class Variables:
       var map
       set of sets of cell objects
       var foods
       food quantity
       var map_size
       length of sets and sets of sets of cell objects
       var tile_size
       pixel size of cell object
   Functions
   def __init__(self, map_size, filename='./resources/map.txt')
   Creates map scheme of defined size according to text file (filename). Counts initial food quantity.
   def get(self, x, y):
   Returns cell object with coordinates x and y
    """

    def __init__(self, filename):
        self.map = []
        self.foods = 0
        with open(filename) as f:
            lines = f.readlines()
            self.map_size = len(lines)
            for j in range(self.map_size):
                self.map.append([])
                for i in range(self.map_size):
                    self.map[-1].append(game_objects.Item(lines[j][i], float(i), float(j), tile_size))
                    if self.map[j][i] == 'F':
                        self.foods += 1

    def get(self, x, y):
        return self.map[y][x]


def process_events(events):
    for event in events:
        if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit(0)
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                pacman.direction = 'left'
            elif event.key == K_RIGHT:
                pacman.direction = 'right'
            elif event.key == K_UP:
                pacman.direction = 'up'
            elif event.key == K_DOWN:
                pacman.direction = 'down'
            elif event.key == K_SPACE:
                pacman.direction = 'none'


game_tick = 0
tile_size = 32
m = Map('C:/Users/Sergey/PycharmProjects/untitled2/Pacman/resources/map.txt')
init_window(m.map_size, tile_size)
pacman = game_objects.Pacman(1, 15, tile_size)
ghosts = [game_objects.Ghost(8, 0, tile_size) for a in range(5)]
background = game_objects.pygame.image.load("C:/Users/Sergey/PycharmProjects/untitled2/Pacman/resources/background.png")
screen = game_objects.pygame.display.get_surface()

if __name__ == '__main__':
    while pacman.is_alive:
        process_events(game_objects.pygame.event.get())
        game_objects.pygame.time.delay(100)
        pacman.game_tick(m, tile_size)
        for ghost in ghosts:
            ghost.game_tick(pacman, m, tile_size)
        draw_background(screen, background)
        for line in m.map:
            for item in line:
                item.draw(screen)
        pacman.draw(screen)
        for ghost in ghosts:
            ghost.draw(screen)
        game_objects.pygame.display.update()
        game_tick += 1
        if m.foods == 0:
            print('GAME OVER')
