import gym
import numpy as np

env = gym.make('CartPole-v0') # initialize the environment
alpha = 0.1 # learning rate
gamma = 0.99 # discount factor
epsilon = 1.0 # exploration rate
epsilon_decay = 0.99 # decay rate for epsilon
min_epsilon = 0.01 # minimum value for epsilon
n_episodes = 1000 # number of episodes to run
n_steps = 200 # maximum number of steps per episode
q_table = np.zeros((env.observation_space.n, env.action_space.n)) # initialize Q-table with zeros

for episode in range(n_episodes):
    state = env.reset() # reset environment and get initial state
    total_reward = 0 # keep track of total reward for this episode
    for step in range(n_steps):
        if np.random.uniform() < epsilon:
            action = env.action_space.sample() # take random action
        else:
            action = np.argmax(q_table[state]) # take best action based on Q-table
        next_state, reward, done, info = env.step(action) # take action and observe next state, reward, and done flag
        q_table[state, action] = (1 - alpha) * q_table[state, action] + alpha * (reward + gamma * np.max(q_table[next_state])) # update Q-value for current state and action
        total_reward += reward # add reward to total for this episode
        state = next_state # set current state to next state
        if done:
            break
    epsilon = max(epsilon * epsilon_decay, min_epsilon) # decay exploration rate
    print('Episode {}: Total reward = {}, Epsilon = {}'.format(episode + 1, total_reward, epsilon))

env.close() # close environment
