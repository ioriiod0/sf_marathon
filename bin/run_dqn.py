# -*- coding: utf-8 -*-
# @Author: ioriiod0
# @Date:   2016-12-23 12:21:34
# @Last Modified by:   ioriiod0
# @Last Modified time: 2016-12-23 12:37:40

from env.env import Env,StaticPolicy
from deep_q.deep_q import DeepQ


if __name__ == '__main__':
	policy = StaticPolicy(100,20)
	env = Env(random_policy = policy)
	deep_q = DeepQ(5,100,env)
	deep_q.train()
	deep_q.test()