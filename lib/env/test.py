# -*- coding: utf-8 -*-
# @Author: ioriiod0
# @Date:   2016-12-23 11:51:39
# @Last Modified by:   ioriiod0
# @Last Modified time: 2016-12-23 12:00:29

from env import *

en = Env(random_policy=RandomPolicy(16, 4))
en.reset()

for i in range(10):
	if i % 2 == 0:
		print en.step(ACTION_SPACE.EAST)
	else:
		print en.step(ACTION_SPACE.SOUTH)
	en.render()
	# print en.reward
# print en.peek_reward