# import glob
# import os
# tragic_path = os.path.join('tempdata', 'tragedies', '*')
# for fname in tragic_filenames:
# 	print(fname)
# fname = os.path.join('tempdata', 'tragedies', 'hamlet')
# tragicfile = open(fname, 'r')
# line_num = 0
# for x in tragicfile:
#     line_num += 1
# tragicfile.close()
# print(fname, "has", line_num, "lines")

from os.path import join
from glob import glob
tragic_path = join('tempdata', 'tragedies', '*')
tragic_filenames = glob(tragic_path)

for fname in tragic_filenames:
    tragicfile = open(fname, 'r')
    # mylist = tragicfiles.readlines()
    # tragicfiles.close()
    total_lines = 0
    for line in tragicfile:
        total_lines += 1
    tragicfile.close()

    
	
for fname in tragic_filenames:
	tragicfile = open(fname, 'r')
	print(fname, "has", total_lines, "lines")
	starting_line_num = total_lines - 5
	for line_num in range(total_lines): 
		line = tragicfile.readline()
		if line_num >= starting_line_num:
			the_line = str(line_num + 1) + ": " + line.strip()
			print(the_line) 
	tragicfile.close()


