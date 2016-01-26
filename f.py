import os
fname = os.path.join('tempdata', 'tragedies', 'romeoandjuliet')
romeoandjulietfile = open(fname, 'r')
line_num = 0
#for x in romeoandjulietfile:
	#line_num += 1
#romeoandjulietfile.close()

#print(fname, "has", line_num, "lines")

for n in range(4766 - 5): 
	line_num += 1
	romeoandjulietfile.readline()
for line in romeoandjulietfile:
	line_num += 1
	print(line_num)
	print(line.strip())  
    #the_line = str(line_num) + ": " + line.strip()

romeoandjulietfile.close()
