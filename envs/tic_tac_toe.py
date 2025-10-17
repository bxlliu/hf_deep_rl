#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 22:39:30 2025

@author: ben
"""

import numpy as np

class TicTacToe:
    def __init__(self):
        self.reset()
    
    def reset(self):
        'Reset the board to empty. X always goes first.'
        self.board = np.zeros((3,3), dtype = int) # board where 0 = empty space, 1 = X, -1 = 0
        self.current_player = 1 # 1 = X, -1 = O
        self.done = False
        self.winner = None
        return self.board.copy()
    
    def available_actions(self):
        'Return list of empty positions as (row, col) tuples'
        return [(r, c) for r in range(3) for c in range(3) if self.board[r, c] == 0]
    
    def step(self, action):
        """Apply action for current player.
        action: (row, col)
        returns: next_state, reward, done"""
        if self.done:
            raise ValueError("Game is over, call reset() to start a new game")
        r, c = action
        if self.board[r, c] != 0:
            raise ValueError("Invalid move! Position already taken.")
        
        self.board[r, c] = self.current_player
        
        # check for winner
        self.winner = self.check_winner()
        if self.winner is not None:
            self.done = True
            if self.winner == 1:
                reward = 1
            else:
                reward = -1
                
        elif len(self.available_actions()) == 0:
            self.done = True
            reward = 0 # draw
        else:
            reward = 0
            self.current_player *= -1 # switch player
        return self.board.copy(), reward, self.done
    def check_winner(self):
        """ check board for winner, return 1 if X wins, -1 if O wins, None otherwise"""
        lines = []
        
        lines.extend(list(self.board)) # rows
        lines.extend(list(self.board.T)) # cols
        lines.append([self.board[i,i] for i in range(3)]) # diagonal
        lines.append([self.board[i,2-i] for i in range(3)]) # antidiagonal
        
        for line in lines:
            if sum(line) == 3:
                return 1 # X wins
            elif sum(line) == -3:
                return -1
            
        return None
    
    def render(self):
        """Print the board"""
        symbol_map = {1: "X", -1: "O", 0: " "}
        print("\n".join(["|".join([symbol_map[cell] for cell in row]) for row in self.board]))
        print()