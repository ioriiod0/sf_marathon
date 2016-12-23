# -*- coding: utf-8 -*-
# @Author: ioriiod0
# @Date:   2016-12-23 10:34:37
# @Last Modified by:   ioriiod0
# @Last Modified time: 2016-12-23 14:13:05

import random
import numpy as np

random.seed()

class ACTION_SPACE:
	EAST = 0
	WEST = 1
	SOUTH = 2
	NORTH = 3
	# STAY = 4
	# PEEK = 5


class RandomPolicy(object):
	def __init__(self,total,n):
		self.n = n
		self.total = total

	def __call__(self,n,state=None,init=True):
		if init:
			return random.sample(range(self.total),n)
		else:
			free = [ i for i,p in enumerate(state) if p == 0]
			return random.sample(free,n)



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
		# print pos
		# print self.state
		return np.hstack([self.state,pos])

	@property
	def is_finished(self):
		self.loc == self.exit_point or self.steps >= self.max_steps
		# if self.loc == self.exit_point or self.steps >= self.max_steps:
			# print self.steps, self.collected, self.loc
		return self.loc == self.exit_point or self.steps >= self.max_steps

	def auto_peek(self):
		reward = 0
		if self.state[self.loc] == 1:
			self.state[self.loc] = 0
			self.collected += 1
			reward += self.peek_reward
		if self.is_finished:
			# reward += 500
			pass

		reward -= 10
		return reward

	def reset(self):
		self.state = np.zeros(self.len)
		self.gen_cargos(self.n)
		self.loc = self.entry_point
		self.collected = 0
		self.steps = 0
		return self.get_state()

	def step(self,action):
		# print "action",action
		self.steps += 1
		cord = self.loc / self.size[0],self.loc % self.size[0]
		# print "cord:",cord

		assert cord[0] >= 0 and cord[0] < self.size[0]
		assert cord[1] >= 0 and cord[1] < self.size[1]

		if action == ACTION_SPACE.EAST:
			if cord[1] != self.size[0] - 1:
				self.loc += 1

		elif action == ACTION_SPACE.WEST:
			if cord[1] != 0:
				self.loc -= 1

		elif action == ACTION_SPACE.NORTH:
			if cord[0] != 0:
				self.loc -= self.size[0]

		elif action == ACTION_SPACE.SOUTH:
			if cord[0] != self.size[1] - 1:
				self.loc += self.size[0]

		# elif action == ACTION_SPACE.STAY:
		# 	pass

		r = self.auto_peek()

		# if self.steps % 5 == 0:
		# 	ns = self.random_policy(1,self.state,init=False)
		# 	for n in ns:
		# 		self.state[n] = 1

		# if self.steps == self.max_steps and self.loc != self.exit_point:
		# 	r -= 1000

		return self.get_state(),r,self.is_finished,{}

		
	def render(self,*args,**kwargs):
		for i in range(self.size[0] + 1):
			print '--',
		print '\n',
		for i in range(self.size[1]):
			print '|',
			for j in range(self.size[0]):
				if i * self.size[0] + j == self.loc:
					print '* ',
				else:
					print '%d ' % int(self.state[i * self.size[0] + j]),
			print '|'
		for i in range(self.size[0] + 1):
			print '--',
		print '\n'















		