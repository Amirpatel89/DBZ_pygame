
#  Include pygame
import pygame
import random


from math import fabs



pygame.init()
screen_size_x = 1067
screen_size_y = 600

screen_size = (screen_size_x, screen_size_y)
pygame_screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("DBZ: Goku vs Frieza")
background_image = pygame.image.load("./images/namek.png")

font = pygame.font.Font(None, 25)

# our Hero!
Goku_image_right = pygame.image.load("./images/gokuright.png")
Goku_image_left = pygame.image.load("./images/gokuleft.png")
Goku_image = Goku_image_right

# our Boss!
FriezaImageLeft = pygame.image.load("./images/friezaleft.png")
FriezaImageRight = pygame.image.load("./images/friezaright.png")
Frieza_image = FriezaImageLeft

KrillinNormal = pygame.image.load("./images/krillin.png")
KrillinInvert = pygame.image.load("./images/invertkrillin.png")
Krillin_image = KrillinNormal

SSJGokuNormal = pygame.image.load("./images/ssjgokuleft.png")
SSJGokuInvert = pygame.image.load("./images/ssjgokuright.png")
SSJGoku_image = SSJGokuNormal


mixChannel1 = pygame.mixer.Channel(0)
mixChannel2 = pygame.mixer.Channel(1)
mixChannel3 = pygame.mixer.Channel(2)

mixChannel1.set_volume(1.0)
mixChannel2.set_volume(1.0)
mixChannel3.set_volume(1.0)

friezaWarningSound = pygame.mixer.Sound(file="./sounds/hahaha.wav")
krillinLaughingSound = pygame.mixer.Sound(file="./sounds/krillinlaugh.wav")
goku_angry_Sound = pygame.mixer.Sound(file="./sounds/krillindie.wav")
krillin_explosion_Sound = pygame.mixer.Sound(file="./sounds/explosion.wav")
krillinWarnSound = pygame.mixer.Sound(file="./sounds/krillinlaugh.wav")
Hit_Sound = pygame.mixer.Sound(file="./sounds/hit.wav")
krillinAppearsSound = pygame.mixer.Sound(file="./sounds/krillinlaugh.wav")

Goku = {
    "x": 100,
    "y": 100,
    "speed": 15,
    "wins": 0,
    "height": 175,
    "width": 140
}

Krillin = {
    "x": 700,
    "y": 100,
    "speed": 1,
    "height": 50,
    "width": 50
}

Frieza = {
    "x": 300,
    "y": 300,
    "speed": 35,
    "wins": 0,
    "height": 145,
    "width": 70
}

topLeftCorner = {
    "x": 0,
    "y": 0
}

topRightCorner = {
    "x": screen_size_x,
    "y": 0
}

bottomLeftCorner = {
    "x": 0,
    "y": screen_size_y
}

bottomRightCorner = {
    "x": screen_size_x,
    "y": screen_size_y
}

keys = {
    "esc": 27,
    "space": 32,
    "i": 105,
    "j": 106,
    "k": 107,
    "l": 108,
    "up": 273,
    "down": 274,
    "right": 275,
    "left": 276
}

keys_down = {
    "up": False,
    "down": False,
    "right": False,
    "left": False
}


def keepCharInBounds(character):
    if character['y'] < 0:
        character['y'] = 0
    elif character['y'] + 175 >= screen_size_y:
        character['y'] = screen_size_y - 175
    if character['x'] < 0:
        character['x'] = 0
    elif character['x'] + 100 >= screen_size_x:
        character['x'] = screen_size_x - 100
def keepKrillinInBounds(character):
    if character['y'] < 0:
        randomlyPlaceChar(Krillin)
    elif character['y'] + 175 >= screen_size_y:
        randomlyPlaceChar(Krillin)

    if character['x'] < 0:
        randomlyPlaceChar(Krillin)
    elif character['x'] + 100 >= screen_size_x:
        randomlyPlaceChar(Krillin)


def pointMe(yourPosition, goalPosition):

    delta = [0, 0]
    delta[0] = yourPosition[0] - goalPosition[0]
    delta[1] = yourPosition[1] - goalPosition[1]

    return delta


def randomlyPlaceChar(character):
    character['x'] = random.randint(32, screen_size_x - 50)
    character['y'] = random.randint(32, screen_size_y - 175)
    return (character['x'], character['y'])


def removeObjectFromBackground(object):
    pygame_screen.blit(background_image, (object['x'], object['y']), pygame.Rect(
        object['x'], object['y'], object['height'], object['width']))
    object['x'] = screen_size_x + 100
    object['y'] = screen_size_y + 100
    return (object['x'], object['y'])


def detectCollision(character1, character2):
    distance_between = fabs(
        character1['x'] - character2['x']) + fabs(character1['y'] - character2['y'])

    if distance_between < 85:
        return True

    return (False)


def moveFrieza(character, pursue=True):

    target = pointMe([Frieza['x'], Frieza['y']],
                     [character['x'], character['y']])


    global Frieza_image

    if pursue:
        if target[0] < 0:  
            Frieza_image = FriezaImageRight
            Frieza['x'] += Frieza['speed']
        elif target[0] > 0:
            Frieza_image = FriezaImageLeft
            Frieza['x'] -= Frieza['speed']
        else:

            target[0] = 1
    else:  
        if target[0] < 0:  
            Frieza_image = FriezaImageLeft
            Frieza['x'] -= Frieza['speed']
        elif target[0] > 0:
            Frieza_image = FriezaImageRight
            Frieza['x'] += Frieza['speed']
        else:

            target[0] = 1


    if pursue:
        if target[0] <= 32:
            if target[1] <= 0:
                Frieza['y'] += Frieza['speed']
            else:
                Frieza['y'] -= Frieza['speed']
        elif target[1] < 0:  # delta y
            Frieza['y'] += round(fabs(Frieza['speed']
                                         * target[1] / target[0]))
        elif target[1] > 0:
            Frieza['y'] -= round(fabs(Frieza['speed']
                                         * target[1] / target[0]))

    else: 
        if target[0] <= 32:  
            if target[1] <= 0:
                Frieza['y'] -= Frieza['speed']
            else:
                Frieza['y'] += Frieza['speed']
        elif target[1] < 0:  
            Frieza['y'] -= round(fabs(Frieza['speed']
                                         * target[1] / target[0]))
        elif target[1] > 0:
            Frieza['y'] += round(fabs(Frieza['speed']
                                         * target[1] / target[0]))

    keepCharInBounds(Frieza)
def moveKrillin(character, pursue=False):
    
    target = pointMe([Krillin['x'], Krillin['y']],
                     [Frieza['x'], Frieza['y']])

   
    global Krillin_image
    if not pursue:
        if target[0] < 0: 
            Krillin_image = KrillinInvert
            Krillin['x'] -= Krillin['speed']
        elif target[0] > 0:
            Krillin_image = KrillinNormal
            Krillin['x'] += Krillin['speed']
        else:

            target[0] = 1

        if target[0] <= 32: 
            if target[1] <= 0:
                Krillin['y'] -= Krillin['speed']
            else:
                Krillin['y'] += Krillin['speed']
        elif target[1] < 0: 
            Krillin['y'] -= round(fabs(Krillin['speed']
                                         * target[1] / target[0]))
        elif target[1] > 0:
            Krillin['y'] += round(fabs(Krillin['speed']
                                         * target[1] / target[0]))
    else:
        
            print "krillin gonna die"
        
    if ((detectCollision(Krillin, topLeftCorner)) or
        (detectCollision(Krillin, topRightCorner)) or
        (detectCollision(Krillin, bottomLeftCorner)) or
        (detectCollision(Krillin, bottomRightCorner))):
        randomlyPlaceChar(Krillin)

   
    keepKrillinInBounds(Krillin)


game_on = True
advantage_Goku = True
FriezaPursues = True
advantageTimer = 30
advantageStartTicks = pygame.time.get_ticks()
powerTimer = 10
powerStartTicks = 0
powerUp = False

pygame.mixer.music.load("./sounds/music.mp3")
pygame.mixer.music.play(-1)

while game_on:  
    pygame_screen.blit(background_image, [0, 0])

    seconds = (pygame.time.get_ticks() - advantageStartTicks) / 1000

    if seconds >= 1:  
        advantageTimer -= 1
        seconds = 0
        advantageStartTicks = pygame.time.get_ticks()
        moveFrieza(Goku, not powerUp)  
        moveKrillin(Krillin)
    if advantageTimer <= 0:  
        if advantage_Goku:  
            advantage_Goku = False
            advantageTimer = 20
            vaderPursues = True
            mixChannel2.play(krillinLaughingSound)
            moveKrillin(Krillin)
        else: 
            mixChannel1.play(krillinLaughingSound)
            advantage_Goku = True
            advantageTimer = 20
            moveKrillin(Krillin)

    

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):  
            
            game_on = False
        elif (event.type == pygame.KEYDOWN):
            
            if (event.key == keys['up'] or event.key == keys['i']):
                keys_down['up'] = True
            elif (event.key == keys['down'] or event.key == keys['k']):
                keys_down['down'] = True
            elif (event.key == keys['right'] or event.key == keys['l']):
                keys_down['right'] = True
            elif (event.key == keys['left']) or event.key == keys['j']:
                keys_down['left'] = True
            elif (event.key == keys['esc']):
                randomlyPlaceChar(Krillin)
            moveFrieza(Goku, FriezaPursues) 
            moveKrillin(Krillin)
        elif (event.type == pygame.KEYUP):
            
            if (event.key == keys['up'] or event.key == keys['i']):
                keys_down['up'] = False
            elif (event.key == keys['down'] or event.key == keys['k']):
                keys_down['down'] = False
            elif (event.key == keys['right'] or event.key == keys['l']):
                keys_down['right'] = False
            elif (event.key == keys['left'] or event.key == keys['j']):
                keys_down['left'] = False
            moveFrieza(Goku, FriezaPursues)  
            moveKrillin(Krillin)

    if keys_down['up']:
        Goku_image = Goku_image_left
        Goku['y'] -= Goku['speed']
    elif keys_down['down']:
        Goku_image = Goku_image_left
        Goku['y'] += Goku['speed']

    if keys_down['left']:
        Goku_image = Goku_image_left
        Goku['x'] -= Goku['speed']
    elif keys_down['right']:
        Goku_image = Goku_image_right
        Goku['x'] += Goku['speed']

    keepCharInBounds(Goku)

   

    if (detectCollision(Frieza, Krillin)):
        if advantage_Goku:
            powerUp = True

            removeObjectFromBackground(Krillin)
            mixChannel2.play(krillin_explosion_Sound)

            FriezaPursues = False

            powerStartTicks = pygame.time.get_ticks()
            if advantageTimer > 10:
                mixChannel1.play(goku_angry_Sound)

    if (detectCollision(Frieza, Goku)):
        mixChannel3.play(Hit_Sound)
        if powerUp:  
            Goku['wins'] += 1
            randomlyPlaceChar(Goku)
            randomlyPlaceChar(Frieza)
        else:
            if advantage_Goku:
                print "Vader caught you while you had the advantage"
                Frieza['wins'] += 1
                randomlyPlaceChar(Goku)
                randomlyPlaceChar(Frieza)
                FriezaPursues = True
            else:
                print "Dark forces are at play!"
                Frieza['wins'] += 2
                randomlyPlaceChar(Goku)
                randomlyPlaceChar(Frieza)
                FriezaPursues = True
                randomlyPlaceChar(Krillin)


    if powerUp:  

        powerSeconds = (pygame.time.get_ticks() - powerStartTicks) / 1000

        if keys_down['up']:
            Goku_image = SSJGokuNormal
            Goku['y'] -= Goku['speed']
        elif keys_down['down']:
            Goku_image = SSJGokuNormal
            Goku['y'] += Goku['speed']

        if keys_down['left']:
            Goku_image = SSJGokuNormal
            Goku['x'] -= Goku['speed']
        elif keys_down['right']:
            Goku_image = SSJGokuInvert
            Goku['x'] += Goku['speed']



        if powerSeconds >= 1: 
            powerTimer -= 1
            powerSeconds = 0
            powerStartTicks = pygame.time.get_ticks()



        if powerTimer <= 0:  
            powerUp = False
            powerTimer = 10
            Goku_image = Goku_image_left
            print "reset Goku_image after SSJ expired"
            mixChannel2.play(krillinLaughingSound)
            if advantage_Goku:  
                randomlyPlaceChar(Krillin)
                mixChannel2.play(krillinAppearsSound)

    if advantage_Goku:
        advantage_text = font.render(
            "Krillin must die: %d" % advantageTimer, True, (255, 255, 255))


        if not powerUp: 
            pygame_screen.blit(Krillin_image, [
                               Krillin['x'], Krillin['y']])
            FriezaPursues = True
            moveKrillin(Krillin)

    else:  
        advantage_text = font.render(
            "Krillin is hiding: %d" % advantageTimer, True, (255, 255, 255))
        FriezaPursues = True
        
        powerTimer = 10  
        powerUp = False


        if Goku_image == KrillinNormal:  
            Goku_image = Goku_image_left

        removeObjectFromBackground(Krillin)

    wins_text = font.render("Goku Score: %d" % (Goku['wins']), True, (255, 255, 255))
    friezawins_text = font.render("Frieza Score: %d" % (Frieza['wins']), True, (255, 255, 255))
    SSJ_text = font.render("Super Saiyan Time: %d" % (powerTimer), True, (255, 200, 10))

    pygame_screen.blit(wins_text, [40, 40])
    pygame_screen.blit(friezawins_text, [300, 40])
    if powerTimer != 10:
        print powerTimer
        pygame_screen.blit(SSJ_text, [800, 40])

    pygame_screen.blit(advantage_text, [600, 40])
    pygame_screen.blit(Frieza_image, [Frieza['x'], Frieza['y']])

    pygame_screen.blit(Goku_image, [Goku['x'], Goku['y']])

    pygame.display.flip()