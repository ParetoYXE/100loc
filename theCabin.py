import pygame,random, os
from pygame.locals import *
from pynput.mouse import Button, Controller
pygame.init()
clock = pygame.time.Clock()


screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

width,height = pygame.display.get_surface().get_size()

background = [255,255,255]
stats = [{'text':"Heat:",'X':width,'Y':80,'value':0},{'text':"Wood:",'X':width,'Y':120,'value':0},{'text':"Energy:",'X':width,'Y':160,'value':100},{'text':"Moves:",'X':width,'Y':190,'value':0},{'text':"Food:",'X':width,'Y':220,'value':0},{'text':"Bullets:",'X':width,'Y':250,'value':0}]
currentMap = 12
entities = [{'name':'player','hp':3000000,'X':500,'Y':300,'height':40,'width':40,"map":currentMap},{'name':'cabin','hp':500,'X':width/2,'Y':height/2,"width":183,"height":188,"map":currentMap},{'name':'AJM9','hp':500,'X':random.randint(1,800),'Y':random.randint(1,700),"width":150,"height":150,"map":currentMap}]
for i in range(random.randint(20,70)):
	entities.append({'name':'tree','hp':random.randint(5,20),'X':random.randint(0,width),'Y':random.randint(0,height),"width":50,"height":90,"map":currentMap})
for j in range(random.randint(1,4)):
	entities.append({'name':'moose','hp':10,'X':random.randint(0,width),'Y':random.randint(0,height),"width":50,"height":90,"map":currentMap})
for k in range(random.randint(1,5)):
	entities.append({'name':'augs','hp':5,'X':random.randint(0,width),'Y':random.randint(0,height),"width":60,"height":60,"map":currentMap})
for l in range(random.randint(1,2)):
	entities.append({'name':'wolf','hp':5,'X':random.randint(0,width),'Y':random.randint(0,height),"width":60,"height":60,"map":currentMap})



waveCount = 0
AJMFound = 0
shotgunFound = 0
deathAnimation = False
deathAnimation2 = False
toggleShotgun = False
settingsMenuToggle = False
helpMenuToggle = False
ammoFound = False
enemyIntensity = 5
wildlifeIntensity = 5

inMenu = True

print("Current Directory: " + os.getcwd())


#Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText

# Main Menu


def gameSetUp():

	global stats, entities, waveCount, AJMFound, shotgunFound, toggleShotgun, currentMap
	currentMap = 12

	stats = [{'text':"Heat:",'X':width - 100,'Y':80,'value':0},{'text':"Wood:",'X':width - 100,'Y':120,'value':0},{'text':"Energy:",'X':width - 100,'Y':160,'value':100},{'text':"Moves:",'X':width - 100,'Y':190,'value':0},{'text':"Food:",'X':width - 100,'Y':220,'value':0},{'text':"Bullets:",'X':width - 100,'Y':250,'value':0}]
	
	entities = [{'name':'player','hp':3,'X':500,'Y':300, 'width':40,'height':40,"map":currentMap},{'name':'cabin','hp':500,'X':width/2,'Y':height/2,"width":100,"height":100,"map":currentMap},{'name':'AJM9','hp':500,'X':random.randint(1,800),'Y':random.randint(1,700),"width":80,"height":80,"map":currentMap}]
	waveCount = 0
	AJMFound = False
	shotgunFound = False
	toggleShotgun = False
	for i in range(random.randint(20,20*(wildlifeIntensity))):
		entities.append({'name':'tree','hp':20,'X':random.randint(0,width/40)*40,'Y':random.randint(0,height/40)*40,"width":50,"height":90,"map":currentMap})
	for j in range(random.randint(1,wildlifeIntensity)):
		entities.append({'name':'moose','hp':10,'X':random.randint(0,width),'Y':random.randint(0,height),"width":50,"height":90,"map":currentMap})
	for k in range(random.randint(1,enemyIntensity)):
		entities.append({'name':'augs','hp':1,'X':random.randint(0,width),'Y':random.randint(0,height),"width":60,"height":60,"map":currentMap})
	for l in range(random.randint(1,wildlifeIntensity)):
		entities.append({'name':'wolf','hp':5,'X':random.randint(0,width),'Y':random.randint(0,height),"width":60,"height":60,"map":currentMap})
	screen.fill(background)
	drawEntities()
	pygame.draw.rect(screen, (0, 0,0), (width-170,60,150,220), 4) 
	pygame.draw.rect(screen,(255,255,255),(width-170,60,150,220))
	drawText()
	pygame.display.update()

def main_menu():
 	
    menu=True
    selected="start"
    global inMenu
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    if selected=="settings":
                    	selected = "start"
                    if selected == "settings":
                    	selected = "help"
                    if selected == "help":
                    	selected = "settings"
                    if selected == "quit":
                    	selected = "help"
                elif event.key==pygame.K_DOWN:
                    if(selected == "start"):
                    	selected="settings"
                    elif(selected == "settings"):
                    	selected="help"
                    elif(selected=="help"):
                    	selected = "quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        menu = False
                        inMenu = False
                        gameSetUp()
                        mouse = Controller()
                        mouse.click(Button.left,1)
                    if selected == "settings":
                    	menu = False
                    	global settingsMenuToggle
                    	settingsMenuToggle = True
                    if selected == "help":
                    	menu = False
                    	global helpMenuToggle
                    	helpMenuToggle = True

                    if selected=="quit":
                        pygame.quit()
                        quit()
                if event.key == pygame.K_m:
                	menu = False
                	inMenu = False
                	print(inMenu)
                	mouse = Controller()
                	mouse.click(Button.left,1)
    	  # Main Menu UI
        screen.fill(white)
        font = "VCR_OSD_MONO.ttf"
 
        title=text_format("The Cabin", font, 90, black)
        if selected=="start":
            text_start=text_format("START", font, 75, red)
        else:
            text_start = text_format("START", font, 75, black)
        if selected=="settings":
        	text_setting=text_format("SETTINGS", font, 75, red)
        else:
        	text_setting=text_format("SETTINGS", font, 75, black)
        if selected=="help":
        	text_help=text_format("HELP",font,75,red)
        else:
        	text_help=text_format("HELP",font,75,black)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, red)
        else:
            text_quit = text_format("QUIT", font, 75, black)
 
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        settings_rect=text_setting.get_rect()
       	help_rect = text_help.get_rect()
        quit_rect=text_quit.get_rect()
 
        # Main Menu Text
        screen.blit(title, (width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (width/2 - (start_rect[2]/2), 300))
        screen.blit(text_setting, (width/2 - (settings_rect[2]/2), 360))
        screen.blit(text_help,(width/2-(help_rect[2]/2),420))
        screen.blit(text_quit, (width/2 - (quit_rect[2]/2), 480))
        pygame.display.update()
        clock.tick(30)
        pygame.display.set_caption("The Cabin")

def help_main_menu():
	help_menu = True
	selected="back"
	font = "VCR_OSD_MONO.ttf" 
	while help_menu:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RETURN:
					if selected=="back":
						global helpMenuToggle
						helpMenuToggle = False
						help_menu = False



		text_Click = text_format("CLICK TO MOVE - Click in the direction you wish to move.",font,18,black)
		text_Attack = text_format("A to Attack - Press the 'A' key to enter attack mode. Click to attack.",font,18,black)
		text_Toggle = text_format("X to swap weapons - Once you find another weapon press X to toggle.",font,18,black)
		text_Harvest = text_format("CLICK TO HARVEST - Click to harvest wood from trees when nearby.",font,18,black)
		text_Heat = text_format("CLICK TO HEAT - Click to heat the cabin with wood when inside.",font,18,black)
		text_Restart = text_format("R to Restart - Press the 'R' key to restart the game.",font,18,black)
		text_Click_rect = text_Click.get_rect()
		text_Attack_rect = text_Attack.get_rect()
		text_Toggle_rect = text_Attack.get_rect()
		text_Harvest_rect = text_Harvest.get_rect()
		text_Heat_rect = text_Heat.get_rect()
		text_Restart_rect = text_Restart.get_rect()

		# Main Menu UI
		screen.fill(white)
		title=text_format("HELP", font, 90, black)
		title_rect=title.get_rect()
		screen.blit(title, (width/2 - (title_rect[2]/2), 100))
		screen.blit(text_Click,(width/2 -(text_Click_rect[2]/2),350))
		screen.blit(text_Attack,(width/2-(text_Attack_rect[2]/2),400))
		screen.blit(text_Toggle,(width/2-(text_Toggle_rect[2]/2),450))
		screen.blit(text_Harvest,(width/2 - (text_Harvest_rect[2]/2),500))
		screen.blit(text_Heat,(width/2 - (text_Heat_rect[2]/2),550))
		screen.blit(text_Restart,(width/2 - (text_Restart_rect[2]/2),600))



		pygame.display.update()
		clock.tick(30)
		pygame.display.set_caption("The Cabin")


def setting_main_menu():

    setting_menu=True
    selected="enemyIntensity"
    font = "VCR_OSD_MONO.ttf" 
    global enemyIntensity
    global wildlifeIntensity
    while setting_menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    if selected=="wildlifeIntensity":
                    	selected = "enemyIntensity"
                    if selected == "back":
                    	selected = "wildlifeIntensity"
                elif event.key==pygame.K_DOWN:
                    if(selected == "enemyIntensity"):
                    	selected="wildlifeIntensity"
                    else:
                    	selected = "back"
                if event.key==pygame.K_RETURN:
                    if selected=="enemyIntensity":
                    	if(enemyIntensity < 10):
                    		enemyIntensity+=1
                    	else:
                        	enemyIntensity = 1
                    if selected=="wildlifeIntensity":
                    	if(wildlifeIntensity < 10):
                    		wildlifeIntensity+=1
                    	else: 
                    		wildlifeIntensity = 1
                    if selected=="back":
                    	global settingsMenuToggle
                    	settingsMenuToggle = False
                    	setting_menu = False

        # Main Menu UI
        screen.fill(white)
        title=text_format("SETTINGS", font, 90, black)
        if selected=="enemyIntensity":
            text_start=text_format("Enemy Intensity: " + str(enemyIntensity), font, 60, red)
        else:
            text_start = text_format("Enemy Intensity: " + str(enemyIntensity), font, 60, black)
        if selected=="wildlifeIntensity":
        	text_setting=text_format("Wildlife Intensity: " + str(wildlifeIntensity), font, 60, red)
        else:
        	text_setting=text_format("Wildlife Intensity: " + str(wildlifeIntensity), font, 60, black)
        if selected=="back":
            text_quit=text_format("Back", font, 60, red)
        else:
            text_quit = text_format("Back", font, 60, black)
 
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        settings_rect=text_setting.get_rect()
        quit_rect=text_quit.get_rect()
 
        # Main Menu Text
        screen.blit(title, (width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (width/2 - (start_rect[2]/2), 300))
        screen.blit(text_setting, (width/2 - (settings_rect[2]/2), 360))
        screen.blit(text_quit, (width/2 - (quit_rect[2]/2), 420))
        pygame.display.update()
        clock.tick(30)
        pygame.display.set_caption("The Cabin")

 
# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
 
# Game Fonts
font = "VCR_OSD_MONO.ttf"
 
 

def drawText(): 
	global AJMFound
	font = pygame.font.Font('VCR_OSD_MONO.ttf', 20)
	for i in stats:
		text = font.render(i["text"]+str(i['value']), True,[0,0,0])
		textRect = text.get_rect()  
		textRect.center = (i["X"], i["Y"]) 
		screen.blit(text, textRect)
	if(AJMFound):
		img = pygame.image.load('AJM9.png')
		imgSelected = pygame.image.load('AJM9Selected.png')
		if(toggleShotgun == False):
			screen.blit(imgSelected,(width - 150,650))
		else:
			screen.blit(img,(width - 150,650))
	if(shotgunFound):
		img = pygame.image.load('shotgun.png')
		imgSelected = pygame.image.load('shotgunSelected.png')
		if(toggleShotgun == False):
			screen.blit(img,(width - 100,650))
		else:
			screen.blit(imgSelected,(width - 100,650))

def drawEntities():
	for i in entities:
		if(i["name"] == "cabin" or i["name"] == "cabin_heat"):
			if(stats[0]["value"] > 0):
				i["name"] = "cabin_heat"
			else: 
				i["name"] = "cabin"
		else:
			img = pygame.image.load(i['name']+'.png')
			if((i['name'] == "augsDeath" or i["name"] =="augsDeath2" or i['name'] == "augsDeath3") and i['hp'] != -1):
				screen.blit(img,(i['X'],i['Y']))
				i['hp'] = -1
			if(i['hp']>0 and i['map'] == currentMap):
				screen.blit(img,(i['X'],i['Y']))
	if(entities[1]['map'] == currentMap):
		img = pygame.image.load(entities[1]['name']+'.png')
		screen.blit(img,(entities[1]['X'],entities[1]['Y']))
	global ammoFound
	if(ammoFound):

		img = pygame.image.load("Ammo.png")
		screen.blit(img,(350,300))
		ammoFound = False
def gameOver():
	global stats,currentMap
	currentMap = 12
	score = stats[3]["value"]
	stats = [{'text':"Game Over. Press R to restart. You scored ",'X':width/2,'Y':height/2,'value':score}]
	screen.fill(background)
	drawText()

def sort(): 

	for i in range(0,len(entities)):
		print(len(entities))
		if(entities[i]["hp"]<0):
			del entities[i]
			sort()
			break

def collisionDetection(xMouse,yMouse):
	global currentMap
	x = entities[0]['X']
	y = entities[0]['Y']
	for i in range(1,len(entities)):
		if((entities[i]['Y'] + entities[i]['height'] >= y) and (y >=(entities[i]['Y']))):
			if((entities[i]['X'] + entities[i]['width'] >= x) and (x >= (entities[i]['X']))):
				if((entities[i]['name'] == "cabin" and entities[i]["map"]==currentMap) or (entities[i]['name'] == "cabin_heat" and entities[i]["map"]==currentMap)):
						print("In House")
						if(stats[1]['value'] > 0):
							stats[0]['value']+= random.randint(0,3)
							stats[1]['value']-=1
						if(stats[0]['value'] > 0):
							stats[2]['value']+= random.randint(3,7)
							stats[0]['value']-=1
						if(stats[4]['value'] > 0):
							stats[2]['value']+= 1
							stats[4]['value']-=1
				if(entities[i]['name'] == "tree" and entities[i]['hp']>0 and entities[i]["map"]==currentMap):
					if(entities[i]['Y']<= yMouse and yMouse <= (entities[i]['Y']+entities[i]["height"])):
						if(entities[i]['X']<= xMouse and xMouse <= (entities[i]['X']+entities[i]['width'])):
							stats[1]['value']+=1
							entities[i]['hp']-=1
							effect = pygame.mixer.Sound('axeChop.wav')
							effect.play()
				if(entities[i]['name'] == "augs" and entities[i]['hp']>0 and entities[i]["map"]==currentMap):
					stats[2]['value']-=1
				if(entities[i]['name'] == "moose" and entities[i]['hp']>0 and entities[i]["map"]==currentMap):
					hit =  random.randint(0,10)
					stats[4]['value'] += hit
					entities[i]['hp'] -= hit
				if(entities[i]['name'] == "wolf" and entities[i]['hp']>0 and entities[i]["map"]==currentMap):
					hit =  random.randint(1,3)
					stats[2]['value'] -= hit
				if(entities[i]['name'] == "loot" and entities[i]['hp']>0 and entities[i]["map"]==currentMap):
					entities[i]['hp'] -=1
					stats[5]["value"] += random.randint(5,10)
					effect = pygame.mixer.Sound('pickup.wav')
					effect.play()
				if(entities[i]['name'] =="AJM9" and entities[i]['hp']>0 and entities[i]["map"]==currentMap):
					global AJMFound
					print("AJM9")
					AJMFound = True
					stats[5]["value"] = random.randint(5,20)
					entities[i]['hp'] = 0
					effect = pygame.mixer.Sound('pickup.wav')
					effect.play()
				if(entities[i]['name'] =="shotgun" and entities[i]['hp']>0 and entities[i]["map"]==currentMap):
					global shotgunFound
					shotgunFound = True
					entities[i]['hp'] = 0
					effect = pygame.mixer.Sound('pickup.wav')
					effect.play()
				if(entities[i]['name'] == "house" and entities[i]['hp']>0 and entities[i]["map"]==currentMap):
					chance = random.randint(1,10)
					if(chance < 4):
						global ammoFound
						ammoFound = True
						stats[5]["value"] += random.randint(1,3)
						effect = pygame.mixer.Sound('pickup.wav')
						effect.play()
		if(entities[i]['name'] == "fireAttack" and entities[i]["map"]==currentMap):
			posx = entities[i]['X']
			posy = entities[i]['Y']
			entities[i]['hp'] -= 1

			for j in range(0, len(entities)):
				if(entities[j]['Y'] + entities[j]['height'] >= posy) and (posy >=(entities[j]['Y'])):
					if((entities[j]['X'] + entities[j]['width'] >= posx) and (posx >= (entities[j]['X']))):
						if(entities[j]["name"]=="augs" and entities[i]["hp"]>=0 and entities[i]["map"]==currentMap):
							entities[j]['hp'] -= 1

		if(entities[i]['name'] == "ajmAttack" and entities[i]["map"]==currentMap):
			posx = entities[i]['X']
			posy = entities[i]['Y']
			entities[i]['hp'] -= 1

			for j in range(0, len(entities)):
				if(entities[j]['Y'] + entities[j]['height'] >= posy) and (posy >=(entities[j]['Y'])):
					if((entities[j]['X'] + entities[j]['width'] >= posx) and (posx >= (entities[j]['X']))):
						if(entities[j]["name"]=="augs" and entities[i]["hp"]>=0 and entities[j]["map"]==currentMap): 
							entities[j]['hp'] -= 5
							print(entities[j]['hp'])
							if(entities[j]['hp']<=0):
								chance = random.randint(0,3)
								if(chance < 1):
									entities[j]['name'] = "augsDeath"
								elif(chance == 2):
									entities[j]['name'] = "augsDeath2"
								else:
									entities[j]['name'] = "augsDeath3"

		if(entities[i]['name'] == "shotgunAttack" and entities[i]["map"]==currentMap):
			posx = entities[i]['X']
			posy = entities[i]['Y']
			entities[i]['hp'] -= 1

			for j in range(0, len(entities)):
				if(entities[j]['Y'] + entities[i]['height'] >= posy) and (posy >=(entities[j]['Y'])):
					if((entities[i]['X'] + entities[i]['width'] >= posx) and (posx >= (entities[i]['X']))):
						if(entities[j]["name"]=="augs" and entities[i]["hp"]>=0 and entities[i]["map"]==currentMap):
							entities[j]['hp'] -= 10
							entities[j]['name'] = "augsDeath3"
						if(entities[j]["name"]=="wolf" and entities[i]["hp"]>=0 and entities[i]["map"]==currentMap):
							entities[j]['hp'] -= random.randint(2,10)


		if(entities[i]['name'] == "augs" and entities[i]["map"]==currentMap):
			posx = entities[i]['X']
			posy = entities[i]['Y']
			

			for j in range(0, len(entities)):
				if(entities[j]['Y'] + entities[j]['height'] >= posy) and (posy >=(entities[j]['Y'])):
					if((entities[j]['X'] + entities[j]['width'] >= posx) and (posx >= (entities[j]['X']))):
						if(entities[j]["name"]=="augs" and entities[i]["hp"]>0 ):
							entities[i]["X"] += random.randint(-10,10)
							entities[i]["Y"] += random.randint(-10,10)
		if(entities[i]['name'] == "moose" and entities[i]["map"]==currentMap and entities[i]['hp']>0):
			posx = entities[i]['X']
			posy = entities[i]['Y']
			

			for j in range(0, len(entities)):
				if(entities[j]['Y'] + entities[j]['height'] >= posy) and (posy >=(entities[j]['Y'])):
					if((entities[j]['X'] + entities[j]['width'] >= posx) and (posx >= (entities[j]['X']))):
						if(entities[j]["name"]=="tree" and entities[i]["hp"]>=0):
							entities[j]['hp'] -= 5
		if(entities[i]['name'] == "wolf" and entities[i]["map"]==currentMap):
			posx = entities[i]['X']
			posy = entities[i]['Y']
			

			for j in range(0, len(entities)):
				if(entities[j]['Y'] + entities[j]['height'] >= posy) and (posy >=(entities[j]['Y'])):
					if((entities[j]['X'] + entities[j]['width'] >= posx) and (posx >= (entities[j]['X']))):
						if(entities[j]["name"]=="moose" and entities[j]["hp"]>=0):
							entities[j]['hp'] -=1
							entities[i]['hp'] -= random.randint(0,1)

		if(entities[i]['name'] == "cabin" and entities[i]["map"]==currentMap):
			posx = entities[i]['X']
			posy = entities[i]['Y']
			

			for j in range(0, len(entities)):
				if(entities[j]['Y']+entities[i]["height"] >= posy) and ((entities[j]['Y']) >= posy):
					if((entities[j]['X'] + entities[j]['width'] >= posx) and (posx >= (entities[j]['X']))):
						if(entities[j]["name"]=="tree" and entities[j]["hp"]>=0):
							entities[j]['hp'] = 0
				



	#Collision Detecion for map transitions			
	if(y < 50):
		if(currentMap != 0 and currentMap != 1 and currentMap != 2 and currentMap != 3 and currentMap != 4):
			currentMap -=5
			firstTime = True
			for i in entities:
				if(i['map']==currentMap):
					firstTime = False
			if(firstTime):
				for i in range(random.randint(20,20*(wildlifeIntensity))):
					entities.append({'name':'tree','hp':random.randint(5,20),'X':random.randint(0,width),'Y':random.randint(0,height),"width":50,"height":90,"map":currentMap})
				for j in range(random.randint(1,wildlifeIntensity)):
					entities.append({'name':'moose','hp':10,'X':random.randint(0,width),'Y':random.randint(0,height),"width":50,"height":90,"map":currentMap})
				for k in range(random.randint(1,enemyIntensity)):
					entities.append({'name':'augs','hp':5,'X':random.randint(0,width),'Y':random.randint(0,height),"width":60,"height":60,"map":currentMap})
				for l in range(random.randint(1,wildlifeIntensity)):
					entities.append({'name':'wolf','hp':5,'X':random.randint(0,width),'Y':random.randint(0,height),"width":60,"height":60,"map":currentMap})

				settlementChance = random.randint(1,10)
				if(settlementChance < 4):
					for h in range(random.randint(1,3)):
						entities.append({'name':'house','hp':100,'X':random.randint(0,width),'Y':random.randint(0,height),"width":50,"height":90,"map":currentMap})
			entities[0]["map"] = currentMap
			entities[0]["Y"]= height - 100
			print(currentMap)
	if(y > height - 100):
		if(currentMap != 20 and currentMap != 21 and currentMap != 22 and currentMap != 23 and currentMap != 24):
			currentMap +=5
			firstTime = True
			for i in entities:
				if(i['map']==currentMap):
					firstTime = False
			if(firstTime):
				for i in range(random.randint(20,20*(wildlifeIntensity))):
					entities.append({'name':'tree','hp':random.randint(5,20),'X':random.randint(0,width),'Y':random.randint(0,height),"width":50,"height":90,"map":currentMap})
				for j in range(random.randint(1,wildlifeIntensity)):
					entities.append({'name':'moose','hp':10,'X':random.randint(0,width),'Y':random.randint(0,height),"width":50,"height":90,"map":currentMap})
				for k in range(random.randint(1,enemyIntensity)):
					entities.append({'name':'augs','hp':5,'X':random.randint(0,width),'Y':random.randint(0,height),"width":60,"height":60,"map":currentMap})
				for l in range(random.randint(1,wildlifeIntensity)):
					entities.append({'name':'wolf','hp':5,'X':random.randint(0,width),'Y':random.randint(0,height),"width":60,"height":60,"map":currentMap})

				settlementChance = random.randint(1,10)
				if(settlementChance < 4):
					for h in range(random.randint(1,3)):
						entities.append({'name':'house','hp':100,'X':random.randint(0,width),'Y':random.randint(0,height),"width":50,"height":90,"map":currentMap})
			entities[0]["map"] = currentMap
			entities[0]["Y"] = 80
		print(currentMap)
	if(x > width - 150):
		if(currentMap != 4 and currentMap != 9 and currentMap != 14 and currentMap != 19 and currentMap != 24):
			currentMap +=1
			firstTime = True
			for i in entities:
				if(i['map']==currentMap):
					firstTime = False
			if(firstTime):
				for i in range(random.randint(20,20*(wildlifeIntensity))):
					entities.append({'name':'tree','hp':random.randint(5,20),'X':random.randint(0,width),'Y':random.randint(0,height),"width":50,"height":90,"map":currentMap})
				for j in range(random.randint(1,wildlifeIntensity)):
					entities.append({'name':'moose','hp':10,'X':random.randint(0,width),'Y':random.randint(0,height),"width":50,"height":90,"map":currentMap})
				for k in range(random.randint(1,enemyIntensity)):
					entities.append({'name':'augs','hp':5,'X':random.randint(0,width),'Y':random.randint(0,height),"width":60,"height":60,"map":currentMap})
				for l in range(random.randint(1,wildlifeIntensity)):
					entities.append({'name':'wolf','hp':5,'X':random.randint(0,width),'Y':random.randint(0,height),"width":60,"height":60,"map":currentMap})

				settlementChance = random.randint(1,10)
				if(settlementChance < 4):
					for h in range(random.randint(1,3)):
						entities.append({'name':'house','hp':100,'X':random.randint(0,width),'Y':random.randint(0,height),"width":50,"height":90,"map":currentMap})
			entities[0]["map"] = currentMap
			entities[0]["X"] = 60
		print(currentMap)
	if(x < 50):
		if(currentMap != 0 and currentMap != 5 and currentMap != 10 and currentMap != 15 and currentMap != 20):
			currentMap -=1
			firstTime = True
			for i in entities:
				if(i['map']==currentMap):
					firstTime = False
			if(firstTime):
				for i in range(random.randint(20,20*(wildlifeIntensity))):
					entities.append({'name':'tree','hp':random.randint(5,20),'X':random.randint(0,width),'Y':random.randint(0,height),"width":50,"height":90,"map":currentMap})
				for j in range(random.randint(1,wildlifeIntensity)):
					entities.append({'name':'moose','hp':10,'X':random.randint(0,width),'Y':random.randint(0,height),"width":50,"height":90,"map":currentMap})
				for k in range(random.randint(1,enemyIntensity)):
					entities.append({'name':'augs','hp':5,'X':random.randint(0,width),'Y':random.randint(0,height),"width":60,"height":60,"map":currentMap})
				for l in range(random.randint(1,wildlifeIntensity)):
					entities.append({'name':'wolf','hp':5,'X':random.randint(0,width),'Y':random.randint(0,height),"width":60,"height":60,"map":currentMap})

				settlementChance = random.randint(1,10)
				if(settlementChance < 4):
					for h in range(random.randint(1,3)):
						entities.append({'name':'house','hp':100,'X':random.randint(0,width),'Y':random.randint(0,height),"width":50,"height":90,"map":currentMap})
			entities[0]["map"] = currentMap
			entities[0]["X"] = width - 150
		print(currentMap)

def getInput(pos):
	x,y = pos
	if(entities[0]['X'] < x):
		entities[0]['X'] +=20
	if(entities[0]['X'] > x):
		entities[0]['X'] -=20
	if(entities[0]['Y'] < y):
		entities[0]['Y'] +=20
	if(entities[0]['Y'] > y):
		entities[0]['Y'] -=20
def npcAI():
	for i in entities:
		if i['name'] == 'moose':
			i['X'] += random.randint(-10,10)
			i['Y'] += random.randint(-10,10)
		if i['name'] == 'augs':
			i['X'] += (entities[0]['X'] - i['X']) / 10
			i['Y'] += (entities[0]['Y'] - i['Y']) / 10
		if i["name"] == 'wolf':
			moose = False
			for j in entities:
				if(j['name']=='moose' and j['hp']>0):
					i['X'] += (j['X'] - i['X']) / 10
					i['Y'] += (j['Y'] - i['Y']) / 10
					moose = True
					break
			if(not moose):
				i['X'] += (entities[0]['X'] - i['X']) / 10
				i['Y'] += (entities[0]['Y'] - i['Y']) / 10
				
#Initialize the Game
while(inMenu):
	if(settingsMenuToggle):
		setting_main_menu()
	elif(helpMenuToggle):
		help_main_menu()
	else:
		main_menu()

screen.fill(background)
pygame.display.set_caption('The Cabin')
font = pygame.font.Font('VCR_OSD_MONO.ttf', 20)
drawEntities()
#pygame.draw.rect(screen, (0, 0,0), (600,60,150,200), 4) 
#pygame.draw.rect(screen,(255,255,255),(600,60,	width - 50,width))
drawText()
#only call this if necessary. Not in a loop. Reduce Big O()
pygame.display.update()
running = True
attack = False
pygame.mixer.music.load('windSound.wav')
pygame.mixer.music.play(-1)

while (running):
	while(inMenu):
		if(settingsMenuToggle):
			setting_main_menu()
		elif(helpMenuToggle):
			help_main_menu()
		else:
			main_menu()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if(len(stats)>1):
				stats[3]['value'] +=1
				if(stats[2]['value'] > 0):
					x,y = event.pos
					stats[2]['value'] -= 1
					hunger = random.randint(1,10)
					if(hunger < 3):
						if(stats[4]['value'] == 0):
							stats[2]['value'] -= 1
						else:
							stats[4]['value'] -= 1


					collisionDetection(x,y)
					if(not attack):
						getInput(event.pos)
				if(attack):
					x,y = event.pos
					if(AJMFound and stats[5]["value"]>0 and toggleShotgun == False):
						if(abs(x - entities[0]["X"]) < 200):
							if(abs(y - entities[0]["Y"]) < 200):
								entities.append({'name':'ajmAttack','hp':1,'X':x,'Y':y,'width':5, 'height':5,"map":currentMap})
								effect = pygame.mixer.Sound('gunShot.wav')
								effect.play()
								stats[5]["value"] -=1
					elif(shotgunFound and stats[5]["value"]>=3 and toggleShotgun == True):
						if(abs(x - entities[0]["X"]) < 150):
							if(abs(y - entities[0]["Y"]) < 150):
								entities.append({'name':'shotgunAttack','hp':1,'X':x,'Y':y,'width':15, 'height':15,"map":currentMap})
								effect = pygame.mixer.Sound('shotgun.wav')
								effect.play()
								stats[5]["value"] -=3
					else:
						if(abs(x - entities[0]["X"]) < 100):
							if(abs(y - entities[0]["Y"]) < 100):
								if(stats[1]['value']>3):
									stats[1]['value']-=3
									entities.append({'name':'fireAttack','hp':random.randint(1,6),'X':x,'Y':y,'width':40, 'height':10,"map":currentMap})
				screen.fill(background)
				npcAI()
				drawEntities()
				pygame.draw.rect(screen, (0, 0,0), (width-170,60,150,220), 4) 
				pygame.draw.rect(screen,(255,255,255),(width-170,60,150,220))
				drawText()
				if(deathAnimation):
					print("test")
					img = pygame.image.load('augDeath2.png')
					screen.blit(img,(300,200))
					deathAnimation = False
				


				if(stats[2]['value']<=0 or entities[0]['hp'] <= 0):
					gameOver()
				if(random.randint(0,30) < wildlifeIntensity + 2):
					entities.append({'name':'tree','hp':20,'X':random.randint(0,width),'Y':random.randint(0,height),"width":50,"height":90,"map":currentMap})
				if(random.randint(0,100) < wildlifeIntensity):
					entities.append({'name':'moose','hp':10,'X':random.randint(0,width),'Y':random.randint(0,height),"width":50,"height":90,"map":currentMap})
				if(random.randint(0,500) < enemyIntensity+waveCount):
					entities.append({'name':'augs','hp':3,'X':random.randint(0,width),'Y':random.randint(0,height),"width":50,"height":90,"map":currentMap})
					if(waveCount < 300):
						waveCount+=1
					else:
						waveCount = 0
				if(random.randint(0,100) < 2):
					entities.append({'name':'wolf','hp':5,'X':random.randint(0,width),'Y':random.randint(0,height),"width":60,"height":60,"map":currentMap})
				if(random.randint(0,10)<1 and currentMap !=12 and shotgunFound != True):
					shotgunSpawned = False
					for i in entities:
						if(i['name'] == "shotgun"):
							shotgunSpawned = True
					if shotgunSpawned == False:
						entities.append({'name':'shotgun','hp':5,'X':random.randint(0,width),'Y':random.randint(0,height),"width":60,"height":60,"map":currentMap})
				pygame.display.update()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				gameSetUp()
			if event.key == pygame.K_a:
				attack = not attack
				print(attack)
			if event.key == pygame.K_x:
				if(shotgunFound):
					toggleShotgun = not toggleShotgun
			if event.key == pygame.K_m:
				inMenu = not inMenu
				print(inMenu)
