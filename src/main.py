while True:
	for i in range(4):
		if can_harvest():
			harvest()
			if i > 1:
				till()
				plant(Entities.Carrot)
		else:
			plant(Entities.Bush)
			move(West)
		move(North)
		

			
		
		
		