#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 22:58:17 2025

@author: ben
"""

import numpy as np

from envs.tic_tac_toe import TicTacToe

env = TicTacToe()
state = env.reset()
env.render()

done = False
while not done:
    actions = env.available_actions()
    action = actions[np.random.randint(len(actions))]
    state, reward, done = env.step(action)
    env.render()
    
print("Game over! Reward:", reward)