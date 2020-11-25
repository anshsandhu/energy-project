import gym
import numpy as np
from tabulate import tabulate
import numpy as np

class Agent():
	def __init__(self):
		self.q_table = np.zeros((2, 6))
		self.learning_rate = 0.05
		self.discount_factor = 0.95
		self.epsilon = 0.5

	def play(self, env):
		
		# Reset the environment before play begins
		#state = env.reset()

		# Play the game until it ends after 1000 steps
		#end_game = False
		while # replace with epochs

			# Choose randomly if the q table is empty or with probability epsilon, otherwise choose the action with the highest reward
			if self.__q_table_is_empty(state) or self.__with_probability(self.epsilon):
				action = self.__get_action_by_choosing_randomly(env)
			else:
				action = self.__get_action_with_highest_expected_reward(state)

			# Perform the action
			new_state, reward, end_game, _ = env.step(action)

			# Update the reward table
			self.q_table[state, action] += self.learning_rate * (reward + self.discount_factor * self._get_expected_reward_in_next_state(new_state) - self.q_table[state, action])

			# Print the latest information to the Terminal
			print("Started in state {}, took action {}, entered new state {} and received reward {}.".format(state, action, new_state, reward))
			print(tabulate(self.q_table, showindex="always", headers=["State", "Action 0 (Forward 1 step)", "Action 1 (Back to 0)"]))

			# Update the state
			state = new_state

	def __q_table_is_empty(self, state):
		return np.sum(self.q_table[state, :]) == 0

	def __with_probability(self, probability):
		return np.random.random() < probability

	def __get_action_by_choosing_randomly(self, env):
		return env.action_space.sample()

	def __get_action_with_highest_expected_reward(self, state):
		return np.argmax(self.q_table[state, :])

	def _get_expected_reward_in_next_state(self, next_state):
		return np.max(self.q_table[next_state, :])

# Create the Nchain-v0 environment
env = gym.make('NChain-v0')

# Create an intelligent agent
agent = Agent()

# Play the game
agent.play(env)


target = np


