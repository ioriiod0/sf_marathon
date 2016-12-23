#!/usr/bin/env python 
#encoding: utf-8

from numpy import random
import csv

csvfile = file('randomPoint.csv', 'wb')
writer = csv.writer(csvfile)

for n in random.randint(-10,10,size=(10,2)):

	writer.writerow(n)

csvfile.close()
