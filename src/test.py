import movements

m = [(0,0),(0,11),(11,11),(11,0),(0,0)]

movements.moveTo(0,0)
do_a_flip()

for x, y in m:
	movements.moveTo(x, y)