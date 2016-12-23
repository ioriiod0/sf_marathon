# -*- coding: utf-8 -*-
# @Author: ioriiod0
# @Date:   2016-12-23 12:21:34
# @Last Modified by:   ioriiod0
# @Last Modified time: 2016-12-23 14:03:50

from env.env import Env,RandomPolicy
from deep_q.deep_q import DeepQ


if __name__ == '__main__':
	policy = RandomPolicy(16,4)
	env = Env(size=(4,4),n = 8,entry_point=0,exit_point=15,peek_reward=150,max_steps=15,random_policy = policy)
	deep_q = DeepQ(5,16,env)
	deep_q.load()
	# deep_q.train()
	# deep_q.save()
	deep_q.test()