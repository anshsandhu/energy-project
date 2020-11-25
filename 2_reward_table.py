import gym
import numpy as np
from tabulate import tabulate

# Define the Agent in our case: Computer

class Agent():
	def __init__(self):
		self.reward_table = np.zeros((2,6))

	def play(self):
		
		# Play the game until it ends after 1000 steps
		# for loop to run it 1000 times

			# Choose action 0 or 1 with 50% probability
			action = env.action_space.sample()

			# Perform the action
			new_state, reward, end_game, _ = env.step(action)

			# Update the reward table
			self.reward_table[state, action] += reward

			# Print the latest information to the Terminal
			print("Started in state {}, took action {}, entered new state {} and received reward {}.".format(state, action, new_state, reward))
			print(tabulate(self.reward_table, showindex="always", headers=["State", "Action 0 (Forward 1 step)", "Action 1 (Back to 0)"]))

			# Update the state
			state = new_state

			end_game += end_game

# Create the Nchain-v0 environment
env = gym.make('NChain-v0')

# Create an intelligent agent
agent = Agent()

# Play the game
agent.play(env)
