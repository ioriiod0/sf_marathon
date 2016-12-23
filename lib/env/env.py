# -*- coding: utf-8 -*-
# @Author: ioriiod0
# @Date:   2016-12-23 10:34:37
# @Last Modified by:   ioriiod0
# @Last Modified time: 2016-12-23 12:52:53

import random
import numpy as np

random.seed()

class ACTION_SPACE:
	EAST = 0
	WEST = 1
	SOUTH = 2
	NORTH = 3
	STAY = 4
	# PEEK = 5


class StaticPolicy(object):
	def __init__(self,total,n):
		self.n = n
		self.total = total
		self.sample = random.sample(range(total),n)

	def __call__(self,n):
		return self.sample


class Env(object):
	"""docstring for Env"""
	def __init__(self, size=(10,10),n = 20,entry_point=0,exit_point=99,peek_reward=150,max_steps=100,random_policy=None):
		super(Env, self).__init__()
		self.size = size
		self.len = size[0] * size[1]
		self.n = n
		self.max_steps = max_steps
		self.entry_point = entry_point
		self.exit_point = exit_point
		self.loc = entry_point
		self.collected = 0
		self.peek_reward = peek_reward
		self.random_policy = random_policy
		
	def gen_cargos(self,n):
		ns = self.random_policy(n)
		for i in ns:
			self.state[i] = 1

	def get_state(self):
		pos = np.zeros(self.len)
		pos[self.loc] = 1
		return np.hstack([self.state,pos])

	@property
	def is_finished(self):
		self.loc == self.exit_point or self.steps == self.max_steps

	def auto_peek(self):
		if self.state[self.loc] == 1:
			self.state[self.loc] = 0
			self.collected += 1
			return self.peek_reward

		return -10

	def reset(self):
		self.state = np.zeros(self.len)
		self.gen_cargos(self.n)
		self.loc = self.entry_point
		self.collected = 0
		self.steps = 0
		return self.get_state()

	def step(self,action):
		self.steps += 1
		cord = self.loc / self.size[0],self.loc % self.size[0]

		assert cord[0] >= 0 and cord[0] < self.size[0]
		assert cord[1] >= 0 and cord[1] < self.size[1]
		# if action == ACTION_SPACE.EAST:
		# 	if cord[1] == 0:
		# 		return 0,self.get_state(),self.is_finished,{}
		# 	else:
		# 		self.loc -= 1
		# 		r = self.auto_peek()
		# 		return r,self.get_state(),self.is_finished,{}

		if action == ACTION_SPACE.EAST:
			if cord[1] == self.size[0] - 1:
				return self.get_state(),0,self.is_finished,{}
			else:
				self.loc += 1

		elif action == ACTION_SPACE.WEST:
			if cord[1] == 0:
				return self.get_state(),0,self.is_finished,{}
			else:
				self.loc -= 1

		elif action == ACTION_SPACE.NORTH:
			if cord[0] == 0:
				return self.get_state(),0,self.is_finished,{}
			else:
				self.loc -= self.size[0]

		elif action == ACTION_SPACE.SOUTH:
			if cord[0] == self.size[1] - 1:
				return self.get_state(),0,self.is_finished,{}
			else:
				self.loc += self.size[0]

		elif action == ACTION_SPACE.STAY:
			return self.get_state(),0,self.is_finished,{}

		r = self.auto_peek()
		return self.get_state(),r,self.is_finished,{}

		# elif action == ACTION_SPACE.PEEK:
		# 	return 0,self.get_state(),self.is_finished,{}
		
	def render(self,*args,**kwargs):
		pass















		