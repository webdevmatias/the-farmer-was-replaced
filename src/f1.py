import movements
import utils

entity = Entities.Grass

while True:
	x = 0
	y = 0
	
	for x in range(12):
		if x % 2 == 0:
			movements.moveToPlant(x, 0, entity)
			movements.moveToPlant(x, 11, entity)
		else:
			movements.moveToPlant(x, 11, entity)
			movements.moveToPlant(x, 0, entity)
	do_a_flip()
	movements.moveTo(0,0)