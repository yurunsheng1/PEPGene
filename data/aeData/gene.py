import os.path as p
import numpy as np

with open(p.abspath(p.dirname(__file__)+'\\eval.txt'),'w') as f:
	
	for _ in range(500):
		
		seq = [0]*330
		for j in range(15):	
			seq[22*j+np.random.randint(0,22)] = 1
		f.write(','.join([str(i) for i in seq])+'\n')