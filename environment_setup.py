import numpy as np
import torch
import gymnasium as gym
import ale_py
from action_wrapper import SimpleActionWrapper


gym.register_envs(ale_py)


env = gym.make("ALE/Pong-v5", render_mode="human")
env = SimpleActionWrapper(env)

env.reset()
for _ in range(100):
    action = env.action_space.sample()
    
    obs, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        obs, info = env.reset()
        
env.close()