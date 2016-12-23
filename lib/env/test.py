# -*- coding: utf-8 -*-
# @Author: ioriiod0
# @Date:   2016-12-23 11:51:39
# @Last Modified by:   ioriiod0
# @Last Modified time: 2016-12-23 12:00:29

from env import *

en = Env()
en.reset()

for i in range(30):
	print en.step(ACTION_SPACE.STAY)