import numpy as np
import tensorflow as tf
import gym
import time
# import spinup
import badminton
# from spinup.utils.run_utils import setup_logger_kwargs
import argparse

env = gym.make('badminton-v0')
env.reset()
for i in range(100000):
    env.render()
    action = env.action_space.sample()
    #print(action)
    env.step(action)

'''
parser = argparse.ArgumentParser()
parser.add_argument("--expname", type=str, help='name of experiment', default='1')
args = parser.parse_args()

logger_kwargs = setup_logger_kwargs(f'test{args.expname}.txt')
spinup.td3(lambda: gym.make('badminton-v0'), logger_kwargs=logger_kwargs, save_freq=80, epochs=1000, steps_per_epoch=2000, max_ep_len=500)
'''