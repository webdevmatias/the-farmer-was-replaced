import movements
from entities import CROPS, NATURAL

n = get_world_size()

def plantEntity(entity):
	if entity in NATURAL:
		plant(entity)

	elif entity in CROPS:
		if get_ground_type() == Grounds.Soil:
			plant(entity)
		else:
			till()
			plant(entity)


def harvestPlantation(entity):
	if can_harvest():
		harvest()
		plantEntity(entity)
	else:
		if get_entity_type() == Entities.Dead_Pumpkin:
			till()
			plantEntity(entity)


def verifyWater():
	if get_water() < 0.3:
		use_item(Items.Water)


def toxic():
	use_item(Items.Fertilizer)