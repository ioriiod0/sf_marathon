# -*- coding: utf-8 -*-
# @Author: ioriiod0
# @Date:   2016-12-23 10:21:21
# @Last Modified by:   ioriiod0
# @Last Modified time: 2016-12-23 12:46:09

import numpy as np

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Convolution2D, Permute
from keras.optimizers import Adam
import keras.backend as K

from rl.agents.dqn import DQNAgent
from rl.policy import LinearAnnealedPolicy, BoltzmannQPolicy, EpsGreedyQPolicy
from rl.memory import SequentialMemory
from rl.core import Processor
from rl.callbacks import FileLogger, ModelIntervalCheckpoint, TrainEpisodeLogger


class EnvProcessor(Processor):
	def process_observation(self, observation):
		print observation.shape
		return observation

	def process_state_batch(self, batch):
		processed_batch = batch.astype('float32')
		processed_batch = processed_batch.reshape(-1,processed_batch.shape[2])
		return processed_batch

class DeepQ(object):
	"""docstring for DeepQ"""
	def __init__(self, nb_actions, state_dim, env):
		super(DeepQ, self).__init__()
		self.env = env
		self.nb_actions = nb_actions
		self.state_dim = state_dim
		self.model = model = Sequential()
		model.add(Dense(1024,input_dim = state_dim * 2))
		model.add(Activation('relu'))
		model.add(Dense(512))
		model.add(Activation('relu'))
		model.add(Dense(256))
		model.add(Activation('relu'))
		model.add(Dense(nb_actions))
		model.add(Activation('linear'))

		print model.summary()
		self.processor = processor = EnvProcessor()
		self.policy = policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=1., value_min=.1, value_test=.05,
							  nb_steps=100000)

		self.memory =  memory = SequentialMemory(limit=1000000, window_length=1)
		dqn = DQNAgent(model=model, nb_actions=nb_actions, policy=policy, memory=memory,
			   processor=processor, nb_steps_warmup=1000, gamma=.99, target_model_update=0.001,
			   train_interval=4, batch_size=256) #delta_clip=1.
		dqn.compile(Adam(lr=.001), metrics=['mae'])

		self.dqn = dqn

	def train(self):
		weights_filename = 'dqn_weights.h5f'
		checkpoint_weights_filename = 'dqn_weights_{step}.h5f'
		log_filename = 'dqn_log.json'
		callbacks = [ModelIntervalCheckpoint(checkpoint_weights_filename, interval=25000)]
		callbacks += [TrainEpisodeLogger()]
		self.dqn.fit(self.env, callbacks=callbacks, nb_steps=175000, log_interval=1000)

		# After training is done, we save the final weights one more time.
		self.dqn.save_weights(weights_filename, overwrite=True)

	def test(self):
		weights_filename = 'dqn_weights.h5f'
		self.dqn.load_weights(weights_filename)
		self.dqn.test(self.env, nb_episodes=10)




		