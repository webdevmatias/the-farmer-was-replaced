import utils



def moveToPlant(dest_x, dest_y, entity):
	x = get_pos_x()
	y = get_pos_y() 
	
	while x < dest_x:
		utils.plantEntity(entity)
		utils.harvestPlantation(entity)
		move(East)
		x += 1

	while x > dest_x:
		utils.plantEntity(entity)
		utils.harvestPlantation(entity)
		move(West)
		x -= 1

	while y < dest_y:
		utils.plantEntity(entity)
		utils.harvestPlantation(entity)
		move(North)
		y += 1

	while y > dest_y:
		utils.plantEntity(entity)
		utils.harvestPlantation(entity)
		move(South)
		y -= 1


def moveTo(dest_x, dest_y):
	x = get_pos_x()
	y = get_pos_y() 
	
	while x < dest_x:
		move(East)
		x += 1

	while x > dest_x:
		move(West)
		x -= 1

	while y < dest_y:
		move(North)
		y += 1

	while y > dest_y:
		move(South)
		y -= 1

	 
	
	
	
	