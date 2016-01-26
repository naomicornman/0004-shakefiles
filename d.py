import os
fname = os.path.join('tempdata', 'tragedies', 'hamlet')
hamletfile = open(fname, 'r')
for x in range (6):
	print (hamletfile.readline().strip())
hamletfile.close()