import pygame,random
pygame.init()
width=800
height=800
background = [255,255,255]
stats = [{'text':"Heat:",'X':661,'Y':80,'value':0},{'text':"Wood:",'X':664,'Y':120,'value':0},{'text':"Food:",'X':663,'Y':160,'value':0},{'text':"Energy:",'X':663,'Y':190,'value':30}]
entities = [{'name':'player','hp':3,'X':500,'Y':300},{'name':'cabin','hp':500,'X':width/2,'Y':height/2,"width":100,"height":100}]
for i in range(random.randint(4,12)):
	entities.append({'name':'tree','hp':5,'X':random.randint(0,width),'Y':random.randint(0,height),"width":50,"height":90})
screen = pygame.display.set_mode( [width, height ] )
screen.fill(background)
pygame.display.set_caption('100LOC')
font = pygame.font.Font('freesansbold.ttf', 20)
def drawText(): 
	for i in stats:
		text = font.render(i["text"]+str(i['value']), True,[0,0,0])
		textRect = text.get_rect()  
		textRect.center = (i["X"], i["Y"]) 
		screen.blit(text, textRect)
def drawEntities():
	for i in entities:
		img = pygame.image.load(i['name']+'.png')
		if(i['hp']>0):
			screen.blit(img,(i['X'],i['Y']))
def gameOver():
	img = pygame.image.load("gameOver.png")
	screen.blit(img,(0,0))

def collisionDetection():
	x = entities[0]['X']
	y = entities[0]['Y']
	for i in range(1,len(entities)):
		if(entities[i]['Y']< y and y < entities[i]['Y']+entities[i]['height']):
			if(entities[i]['X'] < x and x < entities[i]['X']+entities[i]['width']):
				if(entities[i]['name'] == "cabin"):
					if(stats[1]['value'] > 0):
						stats[0]['value']+= random.randint(0,3)
						stats[1]['value']-=1
					if(stats[0]['value'] > 0):
						stats[3]['value']+= random.randint(0,3)
						stats[0]['value']-=1
				if(entities[i]['name'] == "tree" and entities[i]['hp']>0):
					stats[1]['value']+=1
					entities[i]['hp']-=1
def getInput(pos):
	x,y = pos
	if(entities[0]['X'] < x):
		entities[0]['X'] +=10
	if(entities[0]['X'] > x):
		entities[0]['X'] -=10
	if(entities[0]['Y'] < y):
		entities[0]['Y'] +=10
	if(entities[0]['Y'] > y):
		entities[0]['Y'] -=10
drawEntities()
drawText()
#only call this if necessary. Not in a loop. Reduce Big O()
pygame.display.update()
running = True
while (running):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if(stats[3]['value'] > 0):
				collisionDetection()
				getInput(event.pos)
				stats[3]['value'] -= 1
			screen.fill(background)
			drawEntities()
			drawText()
			if(stats[3]['value']<=0):
				gameOver()
			pygame.display.update()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				stats = [{'text':"Heat:",'X':661,'Y':80,'value':0},{'text':"Wood:",'X':664,'Y':120,'value':0},{'text':"Food:",'X':663,'Y':160,'value':0},{'text':"Energy:",'X':663,'Y':190,'value':30}]
				entities = [{'name':'player','hp':3,'X':500,'Y':300},{'name':'cabin','hp':500,'X':width/2,'Y':height/2,"width":100,"height":100}]
				for i in range(random.randint(4,12)):
					entities.append({'name':'tree','hp':5,'X':random.randint(0,width),'Y':random.randint(0,height),"width":50,"height":90})
				screen.fill(background)
				drawEntities()
				drawText()
				pygame.display.update()