import numpy as np

class ParkingEnvironment:
    def __init__(self):
        self.wall_pos = 0.2  # position of the wall
        self.curb_pos = 0.8  # position of the curb
        self.car_pos = 0.5   # initial position of the car
        self.action_space = [0, 1, 2]  # actions: move left, stay, move right
        self.observation_space = [0, 1, 2, 3]  # observations: car is far from curb, close to curb, touching curb, or hit wall
        self.max_steps = 10   # maximum number of steps allowed
        self.step_count = 0   # current step count
    
    def reset(self):
        self.car_pos = 0.5
        self.step_count = 0
        return self._get_observation()
    
    def step(self, action):
        self.step_count += 1
        reward = -1   # default reward for taking an action
        done = False   # flag indicating whether episode is over
        if action == 0:
            self.car_pos -= 0.1   # move left
        elif action == 2:
            self.car_pos += 0.1   # move right
        if self.car_pos < 0:
            self.car_pos = 0   # car hits left wall
            done = True
        elif self.car_pos > 1:
            self.car_pos = 1   # car hits right wall
            done = True
        elif abs(self.car_pos - self.curb_pos) < 0.05:
            reward = 10   # car is close to curb
            done = True
        elif abs(self.car_pos - self.curb_pos) < 0.01:
            reward = 50   # car touches curb
            done = True
        elif abs(self.car_pos - self.wall_pos) < 0.05:
            reward = -50   # car hits wall
            done = True
        if self.step_count >= self.max_steps:
            done = True   # maximum number of steps reached
        return self._get_observation(), reward, done, {}
    
    def _get_observation(self):
        if abs(self.car_pos - self.curb_pos) < 0.01:
            return 2   # car touches curb
        elif abs(self.car_pos - self.curb_pos) < 0.05:
            return 1   # car is close to curb
        elif self.car_pos < self.wall_pos or self.car_pos > (self.curb_pos + 0.1):
            return 3   # car hits wall
        else:
            return 0   # car is far from curb
