import gym
import badminton
from spinup.utils.test_policy import load_policy, run_policy

_, get_action = load_policy('/home/abhishek/Documents/sem8/independent study/spinningup/data/test0.txt')
env = gym.make('badminton-v0')
run_policy(env, get_action)
