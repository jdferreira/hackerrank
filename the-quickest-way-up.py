#!/usr/bin/env python3

BOARD_SIZE = 100

class Board:
    def __init__(self, ladders, snakes):
        self.size = BOARD_SIZE
        self.ladders = dict(ladders)
        self.snakes = dict(snakes)

    def slide(self, n):
        """
        If `n` is a square with the start of a ladder or a snake, return the end
        of that ladder or snake; otherwise, just return n. Additionally, if the
        result is not within the bounds of the board, return None.
        """
        
        n = self.ladders.get(n, n)
        n = self.snakes.get(n, n)
        
        if n < 1 or n > self.size:
            n = None
        
        return n
    
    def solve(self):
        layer_depth = 0
        current_layer = {1}
        
        in_a_layer = [None] + [False] * self.size
        in_a_layer[1] = True
        
        while True:
            destinations = {self.slide(i + die) for i in current_layer for die in range(1, 7)}
            destinations.discard(None)
            
            layer_depth += 1
            current_layer = destinations
            
            for i in list(current_layer):
                if i == self.size:
                    return layer_depth
                
                if in_a_layer[i]:
                    current_layer.discard(i)
                else:
                    in_a_layer[i] = True
            
            if not current_layer:
                return -1

def get_pairs(n):
    return [tuple(int(i) for i in input().split()) for _ in range(n)]

def get_board():
    n_ladders = int(input())
    ladders = get_pairs(n_ladders)
    
    n_snakes = int(input())
    snakes = get_pairs(n_snakes)

    return Board(ladders, snakes)


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        print(get_board().solve())
