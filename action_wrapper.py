import gymnasium as gym
import ale_py

from gymnasium.core import ActionWrapper
from gymnasium.spaces import Discrete

class SimpleActionWrapper(ActionWrapper):
    def __init__(self, env):
        super().__init__(env)
        self._action_map = [0, 2, 3]
        self._action_space = Discrete(3)
        
    def action(self, action):
        return self._action_map[action]