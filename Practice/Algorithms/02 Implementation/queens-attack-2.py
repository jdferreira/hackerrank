#!/usr/bin/env python3

DIRECTIONS = [
    ( 1,  0),
    ( 1,  1),
    ( 0,  1),
    (-1,  1),
    (-1,  0),
    (-1, -1),
    ( 0, -1),
    ( 1, -1),
]

def get_tuple(convert=int):
    return tuple(convert(i) for i in input().split())

def move(here, direction):
    return tuple(h + d for h, d in zip(here, direction))

def get_possible_squares(n, queen, obstacles):
    
    # print('QUEEN = {}'.format(queen))
    # print('OBSTACLES = {}'.format(obstacles))
    
    # A function to detect squares on the outside of the board
    def is_inside(point):
        return all(1 <= coord <= n for coord in point)
    
    res = 0
    
    for direction in DIRECTIONS:
        # print('DIR = {}'.format(direction))
        here = queen
        while True:
            here = move(here, direction)
            # print('HERE = {}'.format(here))
            if is_inside(here) and here not in obstacles:
                res += 1
            else:
                # print('NOT ANY MORE!')
                break
    
    return res


if __name__ == '__main__':
    n, k = get_tuple()
    queen = get_tuple()
    obstacles = {get_tuple() for _ in range(k)}
    
    print(get_possible_squares(n, queen, obstacles))
