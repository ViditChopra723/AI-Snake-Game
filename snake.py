import sys
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
from collections import deque

#set number of rows.
rows = 20
w = 500

"******************************************************     Snake Game code from Tutorial on Pygame code, https://pythonspot.com/snake-with-pygame/ ***********************************************"
class cube(object):
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))
        if eyes:
            centre = dis // 2
            radius = 3
            circleMiddle = (i * dis + centre - radius, j * dis + 8)
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)


class snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self, dir):

        keys = dir

        if keys == 3:
            self.dirnx = -1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        elif keys == 4:
            self.dirnx = 1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        elif keys == 1:
            self.dirnx = 0
            self.dirny = -1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        elif keys == 2:
            self.dirnx = 0
            self.dirny = 1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows - 1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:
                    c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1:
                    c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows - 1)
                else:
                    c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redrawWindow(surface, s, snack, width, rows):
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()


def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows - 1)
        y = random.randrange(rows - 1)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

"*********************************************************************************************************************************** end snake game ***********************************************************"



#################################### code from https://github.com/chuyangliu/snake/blob/master/snake/base/pos.py ##################################\

"               these are basic functions to use in the algorithims.                      "


class _TableCell:

    def __init__(self):
        self.reset()

    def __str__(self):
        return "{ dist: %d  parent: %s  visit: %d }" % \
               (self.dist, str(self.parent), self.visit)
    __repr__ = __str__

    def reset(self):
        # Shortest path
        self.parent = None
        self.dist = sys.maxsize
        # Longest path
        self.visit = False


def direc_from(src_pos, adj_pos):
    " if x the same and y diff = 1 return down, if x the same and y diff = -1 return up"

    if src_pos[0] == adj_pos[0]:
        diff = src_pos[1] - adj_pos[1]
        if diff == 1:

            return 1
        elif diff == -1:

            return 2
    elif src_pos[1] == adj_pos[1]:
        diff = src_pos[0] - adj_pos[0]
        if diff == 1:

            return 3
        elif diff == -1:

            return 4
    return 0


def adj(x, y, direc):
    """Return the adjacent Pos in a given direction."""
    if direc == 4:
        return (x - 1, y)
    elif direc == 3:
        return (x + 1, y)
    elif direc == 2:
        return (x, y - 1)
    elif direc == 1:
        return (x, y + 1)
    else:
        return None


def all_adj(x,y):
    """Return a list of all the adjacent Pos."""
    adjs = []
    direc = [1,2,3,4]

    for dir in direc:
        adjs.append(adj(x,y,dir))
    return adjs


def manhattan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
###########################################################           end of code         ##################################################/


def out_of_bounds(t) :
    if t[0] > rows - 1 or t[0] < 0:
        return 1
    if t[1] > rows - 1 or t[1] < 0:
        return 1
    return 0


def shortest_path(src,dst,snake):
    table = [[_TableCell() for _ in range(rows)]
             for _ in range(rows)]

    queue = deque()
    queue.append([(src[0], src[1])])
    seen = set(src)
    goal = table[dst[0]][dst[1]]

    for se in snake.body:
        seen.add(se.pos)

    if dst == snake.body[-1].pos:
        seen.remove(dst)

    while queue:

        path = queue.popleft()
        x, y = path[-1]
        cur = table[x][y]
        if cur == goal:
            return build_path(path)

        adjs = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for adj in adjs:
            if out_of_bounds(adj):
                adjs.remove(adj)

        for x2, y2 in adjs:
            if 0 <= x2 < rows - 1 and 0 <= y2 < rows - 1 and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    return []

def build_path(path):
    directions = []
    for i in range(len(path) - 1):
        directions.append(direc_from(path[i], path[i + 1]))
    return directions

def opposite(direc):
        """Return the opposite direction."""
        if direc == 3:
            return 4
        elif direc == 4:
            return 3
        elif direc == 1:
            return 2
        elif direc == 2:
            return 1

def longest_path(src,dst, snake):
    path = shortest_path(src,dst, snake)
    if not path:
        return deque()

    table = [[_TableCell() for _ in range(rows)]
             for _ in range(rows)]

    cur = [src[0],src[1]]
    # Set all positions on the shortest path to 'visited'
    table[src[0]][src[1]].visit = True

    for se in snake.body:
        table[se.pos[0]][se.pos[1]].visit = True


    for direc in path:
        c = adj(cur[0], cur[1], direc)
        if not out_of_bounds(c):
            cur = [c[0], c[1]]
            table[cur[0]][cur[1]].visit = True

    # Extend the path between each pair of the positions
    idx, cur = 0, [src[0], src[1]]
    flag = 1
    while flag:
        cur_direc = path[idx]
        nxt = adj(cur[0], cur[1], cur_direc)

        if cur_direc == 3 or cur_direc == 4:
            tests = [1, 2]
        elif cur_direc == 1 or cur_direc == 2:
            tests = [3, 4]

        extended = False
        for test_direc in tests:
            cur_test = adj(cur[0], cur[1],test_direc)
            nxt_test = adj(nxt[0], nxt[1],test_direc)
            if not out_of_bounds(cur_test) and not out_of_bounds(nxt_test) and not table[cur_test[0]][cur_test[1]].visit == True:
                table[cur_test[0]][cur_test[1]].visit = True
                table[nxt_test[0]][nxt_test[1]].visit = True
                path.insert(idx, test_direc)
                path.insert(idx + 2, opposite(test_direc))
                extended = True
                break

        if not extended:
            cur = nxt
            idx += 1
            if idx >= len(path):
                flag = 0

    return path

class greedy():
    def __init__(self, snake, sn):
        self.snake = snake
        self.head = snake.body[0]
        self.tail = snake.body[-1]
        self.snack = sn

    def next_direc(self):
        # Step 1 find shortest path from head to food, if it exists go to step 2, if not go to step 4
        path_to_food = shortest_path(self.head.pos, self.snack.pos, self.snake)

        # Step 2 move the fake snake along this path (need function to move fake snake, fully on path)
        if len(path_to_food) > 0:
                s_copy = self.snake
            # Step 3 find the longest path from fake snake's head to its tail, if it exists return the first direction from
            # the shortest path to the actual snake move
                path_to_tail = longest_path(s_copy.body[0].pos, s_copy.body[-1].pos, s_copy)
                if len(path_to_tail)>1:
                    return [path_to_food[0]]


        # Step 4 find the longest path from actual snake's head to tail. If it exists return this path's first direction to the actual snake. if not go to step 5.
        path_to_tail = longest_path(self.head.pos,self.tail.pos, self.snake)

        if len(path_to_tail)>1:
            return [path_to_tail[0]]

        # Step 5 if none of this works then we need to move the snake away from the food as much as possible so we calculate the manhattan distance of every
        # adajacent square from the head and move the snake towards that direction  (need function to find the adjacent heads, and to determine if it is out of bounds, and a function for manhattan distance)
        max_dist = -1

        direc = 0
        x = self.head.pos[0]
        y = self.head.pos[1]
        ille = []
        for se in snake.body:
            print(se.pos)
            ille.append(se.pos)

        adjs = [(x, y - 1),(x, y + 1),(x - 1, y), (x + 1, y)]
        for i, adji in enumerate(adjs):
            if not out_of_bounds(adji) and adji not in ille:
                dist = manhattan_dist(adji, self.snack.pos)
                if dist > max_dist:
                    max_dist = dist
                    direc = direc_from(self.head.pos, adji)

        return [direc]

def main():
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255, 0, 0), (2, 2))
    s.addCube()
    snack = cube(randomSnack(rows, s), color=(0, 255, 0))
    flag = True
    clock = pygame.time.Clock()

    while flag:

        g = greedy(s, snack)
        next_direc = g.next_direc()
        print("tick", "head is ", s.body[0].pos, "snack is at ",  snack.pos, "going direction ",   next_direc, "score is ", len(s.body))

        for n in next_direc:
            pygame.time.delay(50)
            clock.tick(40)
            if n == 2:
                s.move(2)
            elif n == 1:
                s.move(1)
            elif n == 4:
                s.move(4)
            elif n == 3:
                s.move(3)
            else:
                s.move(1)

            if s.body[0].pos == snack.pos:
                s.addCube()
                snack = cube(randomSnack(rows, s), color=(0, 255, 0))

            for x in range(len(s.body)):
                if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                    print('Score: ', len(s.body))
                    #message_box('You Lost!', 'Play again...')
                    s.reset((2, 2))
                    s.addCube()
                    snack = cube(randomSnack(rows, s), color=(0, 255, 0))
                    break

            redrawWindow(win , s, snack, width, rows)


main()