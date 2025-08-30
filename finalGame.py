# ICD207 Final Project: Beat Catz
# June 2024
# By Aidan and Nimo

# importing libraries 
import pygame
import os
import time
from pygame.locals import *  
from pygame.color import THECOLORS
import random
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()  

# display settings
size = (1150, 730)  
screen = pygame.display.set_mode(size) 
screen.fill((255, 255, 255))  
pygame.display.flip()

# window name and icon
pygame.display.set_caption('BeatCatz')
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# initializing clock
clock = pygame.time.Clock()
keepGoing = True

# ---------------------------------------
#         Initializing Variables
# ---------------------------------------

page = "menu"
titleimg = pygame.transform.scale(pygame.image.load("title.png").convert_alpha(), (450,327))

beats = 0

# coordinates for different note lanes
x, y = 100,100
x1, x2, x3, x4 = 75, 200, 325, 450

# loading songs and sound effects 
fDive = pygame.mixer.Sound("freedomdivecut.mp3")
cCafe = pygame.mixer.Sound("catCafe.mp3")
randomSound = pygame.mixer.Sound("random.mp3")
fDive.set_volume(1)
cCafe.set_volume(1)
randomSound.set_volume(1)

meowEff = pygame.mixer.Sound("meow.mp3")
clickEff = pygame.mixer.Sound("click.wav")
meowEff.set_volume(1)
clickEff.set_volume(1)


# rhythm game map variables 
maps = ["freedom", "cat", "random"]
endScreenTime = 0

# confirmation screen variables
exit = False
confirmationReset = False


# backgrounds
homebg = pygame.image.load("bg1.png").convert_alpha()
playbg = pygame.image.load("bg2.png").convert_alpha()
optionsbg = pygame.image.load("bg3.png").convert_alpha()
rulesbg = pygame.image.load("bg4.png").convert_alpha()
leaderbg = pygame.transform.scale(pygame.image.load("bg5.png").convert_alpha(), (1200, 800))

# homepage decoration images
lake = pygame.transform.scale(pygame.image.load("lake.png").convert_alpha(), (546, 256))
lake_r = lake.get_rect()
lake_r.x, lake_r.y = 650, 210
lakehover = pygame.transform.scale(pygame.image.load("lake.png").convert_alpha(), (553, 263))
tree = pygame.transform.scale(pygame.image.load("tree.png").convert_alpha(), (200, 250))
tree_r = tree.get_rect()
tree_r.x, tree_r.y = 1000, 45
treehover = pygame.transform.scale(pygame.image.load("tree.png").convert_alpha(), (205, 255))
tree2 = pygame.transform.scale(pygame.image.load("tree.png").convert_alpha(), (150, 200))
tree2_r = tree2.get_rect()
tree2_r.x, tree2_r.y = 680, 50
tree2hover = pygame.transform.scale(pygame.image.load("tree.png").convert_alpha(), (155, 205))

# leaderboard images and buttons
leaderbtn = pygame.transform.scale(pygame.image.load("lbbtn.png").convert_alpha(), (273, 199))
leaderbtn_r = leaderbtn.get_rect()
leaderbtn_r.x, leaderbtn_r.y = 800, 450
leaderhover = pygame.transform.scale(pygame.image.load("lbbtn.png").convert_alpha(), (300, 225))
resetFree = pygame.transform.scale(pygame.image.load("reset.png").convert_alpha(), (200, 80))
resetFree_r = resetFree.get_rect()
resetFree_r.x, resetFree_r.y = 100, 640
resetCat = pygame.transform.scale(pygame.image.load("reset.png").convert_alpha(), (200, 80))
resetCat_r = resetCat.get_rect()
resetCat_r.x, resetCat_r.y = 500, 640
resetRandom = pygame.transform.scale(pygame.image.load("reset.png").convert_alpha(), (200, 80))
resetRandom_r = resetRandom.get_rect()
resetRandom_r.x, resetRandom_r.y = 900, 640

# play button
playbtn = pygame.transform.scale(pygame.image.load("playbtn.png").convert_alpha(), (320, 138))
playbtn_r = playbtn.get_rect()
playbtn_r.x, playbtn_r.y = 200, 350
playbtnhover = pygame.transform.scale(pygame.image.load("playbtnhover.png").convert_alpha(), (323, 139))

# option button
opbtn = pygame.transform.scale(pygame.image.load("opbtn.png").convert_alpha(), (320, 138))
opbtn_r = opbtn.get_rect()
opbtn_r.x, opbtn_r.y = 30, 500
opbtnhover = pygame.transform.scale(pygame.image.load("opbtnhover.png").convert_alpha(), (323, 139))
                                    
# instructions/rules button
rlbtn = pygame.transform.scale(pygame.image.load("rlbtn.png").convert_alpha(), (320, 138))
rlbtn_r = rlbtn.get_rect()
rlbtn_r.x, rlbtn_r.y = 380, 500
rlbtnhover = pygame.transform.scale(pygame.image.load("rlbtnhover.png").convert_alpha(), (323, 139))

# freedom dive song icon
freedomDive = pygame.transform.scale(pygame.image.load("freedomdivere.png").convert_alpha(), (350, 350))
freedomHover = pygame.transform.scale(pygame.image.load("freedomdivehover.png").convert_alpha(), (360, 360))
freedom_r = freedomHover.get_rect()
freedom_r.x, freedom_r.x = 300, 100
freedombg = pygame.transform.scale(pygame.image.load("freedomdivebg.png").convert_alpha(), (1200, 750))
freedombg2 = pygame.transform.scale(pygame.image.load("freedomdivebg2.png").convert_alpha(), (1200, 750))

# cat at the cafe song icon
catCafe = pygame.transform.scale(pygame.image.load("catCafe.png").convert_alpha(), (350, 350))
cat_r = catCafe.get_rect()
cat_r.x, cat_r.y = 600, 100
catHover = pygame.transform.scale(pygame.image.load("catcafehover.png").convert_alpha(), (360, 360))
catbg = pygame.transform.scale(pygame.image.load("catcafebg.png").convert_alpha(), (1200, 750))
catbg2 = pygame.transform.scale(pygame.image.load("catcafebg2.png").convert_alpha(), (1200, 750))

# random mode icon
randomBtn = pygame.transform.scale(pygame.image.load("randombtn.png").convert_alpha(), (450, 250))
random_r = randomBtn.get_rect()
random_r.x, random_r.y = 350, 475
randomHover = pygame.transform.scale(pygame.image.load("randomhover.png").convert_alpha(), (460, 260))
randombg = pygame.transform.scale(pygame.image.load("randombg.png").convert_alpha(), (1200, 750))
randombg2 = pygame.transform.scale(pygame.image.load("randombg2.png").convert_alpha(), (1200, 750))

# note sprites
note = pygame.transform.scale(pygame.image.load("note.png").convert_alpha(), (60, 60))
perfectN = pygame.transform.scale(pygame.image.load("perfect.png").convert_alpha(), (60, 60))
perfect_r = perfectN.get_rect()
perfect_r.x, perfect_r.y = 600, 400
perfecthover = pygame.transform.scale(pygame.image.load("perfect.png").convert_alpha(), (63, 63))
greatN = pygame.transform.scale(pygame.image.load("great.png").convert_alpha(), (60, 60))
great_r = greatN.get_rect()
great_r.x, great_r.y = 760, 400
greathover = pygame.transform.scale(pygame.image.load("great.png").convert_alpha(), (63, 63))
okayN = pygame.transform.scale(pygame.image.load("okay.png").convert_alpha(), (60, 60))
okay_r = okayN.get_rect()
okay_r.x, okay_r.y = 920, 400
okayhover = pygame.transform.scale(pygame.image.load("okay.png").convert_alpha(), (63, 63))

# keybind displays for instructions
d_btn = pygame.image.load("D.png").convert_alpha()
f_btn = pygame.image.load("F.png").convert_alpha()
j_btn = pygame.image.load("J.png").convert_alpha()
k_btn = pygame.image.load("K.png").convert_alpha()
blank = pygame.image.load("blankkey.png").convert_alpha()

# back button
backbtn = pygame.transform.scale(pygame.image.load("backbtn.png").convert_alpha(), (150, 75))
backbtn_r = backbtn.get_rect()
backbtn_r.x, backbtn_r.y = 995, 5
backhover = pygame.transform.scale(pygame.image.load("backbtnhover.png").convert_alpha(), (155, 80))

# exit button
exitbtn = pygame.image.load("exitbtn.png").convert_alpha()
exit_r = exitbtn.get_rect()
exit_r.x, exit_r.y = 5, 5
exithover = pygame.transform.scale(pygame.image.load("exitbtn.png").convert_alpha(), (60, 60))
confirmation = pygame.transform.scale(pygame.image.load("confirmation.png").convert_alpha(), (500, 400))
conYes = pygame.transform.scale(pygame.image.load("yes.png").convert_alpha(), (150, 105))
yesHover = pygame.transform.scale(pygame.image.load("yes.png").convert_alpha(), (155, 110))
yes_r = conYes.get_rect()
yes_r.x, yes_r.y = 425, 370
conNo = pygame.transform.scale(pygame.image.load("no.png").convert_alpha(), (150, 105))
noHover = pygame.transform.scale(pygame.image.load("no.png").convert_alpha(), (155, 110))
no_r = conNo.get_rect()
no_r.x, no_r.y = 620, 370

# scroll images for leaderboard
scrollFree = pygame.transform.scale(pygame.image.load("freedomdivescroll.png").convert_alpha(), (400, 550))
scrollCat = pygame.transform.scale(pygame.image.load("catcafescroll.png").convert_alpha(), (400, 550))
scrollRandom = pygame.transform.scale(pygame.image.load("randomscroll.png").convert_alpha(), (400, 550))

# play again button
playAgain = pygame.transform.scale(pygame.image.load("playagain.png").convert_alpha(), (300, 100))
play_r = playAgain.get_rect()
play_r.x, play_r.y = 475, 550
playAgainhover = pygame.transform.scale(pygame.image.load("playagain.png").convert_alpha(), (305, 105))

# options images and buttons
optionimg = pygame.transform.scale(pygame.image.load("optionsbox.png").convert_alpha(), (1000, 600))
up = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("up.png").convert_alpha(), (80, 80)), 90)
up_r = up.get_rect()
up_r.x, up_r.y = 650, 380
uphover = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("up.png").convert_alpha(), (85,85)), 90)
down = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("down.png").convert_alpha(), (80,80)), 90)
down_r = up.get_rect()
down_r.x, down_r.y = 960, 380
downhover = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("down.png").convert_alpha(), (85,85)), 90)
reset = pygame.transform.scale(pygame.image.load("reset.png").convert_alpha(), (200, 80))
reset_r = reset.get_rect()
reset_r.x, reset_r.y = 225, 275
resethover = pygame.transform.scale(pygame.image.load("reset.png").convert_alpha(), (205, 85))

# rules images and buttons
rulesimg = pygame.transform.scale(pygame.image.load("rulebox.png").convert_alpha(), (1000, 600))
rulesAliveX = []
rulesAliveY = []
rulesDisplaysY = [0]
rulesDisplaysX = [470]
dead = 15
toOptions = pygame.transform.scale(pygame.image.load("bird.jpg").convert(), (60, 20))
toOptions_r = toOptions.get_rect()
toOptions_r.x, toOptions_r.y = 575, 595

# confirmation button for leaderboard reset
conImg = pygame.transform.scale(pygame.image.load("resetcon.png").convert_alpha(), (500, 400))
conX = pygame.transform.scale(pygame.image.load("confx.png").convert_alpha(), (50, 50))
conX_r = conX.get_rect()
conX_r.x, conX_r.y = 750, 200
conXhover = pygame.transform.scale(pygame.image.load("confx.png").convert_alpha(), (55, 55))

# volume control buttons for instructions page
vol100 = pygame.image.load("100percent.png").convert_alpha()
vol100_r = vol100.get_rect()
vol100_r.x, vol100_r.y = 600, 550
vol100hover = pygame.transform.scale(pygame.image.load("100percent.png").convert_alpha(), (105, 105))
vol75 = pygame.image.load("75percent.png").convert_alpha()
vol75_r = vol75.get_rect()
vol75_r.x, vol75_r.y = 475, 550
vol75hover = pygame.transform.scale(pygame.image.load("75percent.png").convert_alpha(), (105, 105))
vol50 = pygame.image.load("50percent.png").convert_alpha()
vol50_r = vol50.get_rect()
vol50_r.x, vol50_r.y = 350, 550
vol50hover = pygame.transform.scale(pygame.image.load("50percent.png").convert_alpha(), (105, 105))
vol25 = pygame.image.load("25percent.png").convert_alpha()
vol25_r = vol25.get_rect()
vol25_r.x, vol25_r.y = 225, 550
vol25hover = pygame.transform.scale(pygame.image.load("25percent.png").convert_alpha(), (105, 105))
vol0 = pygame.image.load("0percent.png").convert_alpha()
vol0_r = vol0.get_rect()
vol0_r.x, vol0_r.y = 100, 550
vol0hover = pygame.transform.scale(pygame.image.load("0percent.png").convert_alpha(), (105, 105))

# end screen ui
endbanner = pygame.transform.scale(pygame.image.load("highscorebanner.png").convert_alpha(), (600, 300))
scrollStats = pygame.transform.scale(pygame.image.load("statscroll.png").convert_alpha(), (670, 790))
scrollDied = pygame.transform.scale(pygame.image.load("gameover.png").convert_alpha(), (670, 790))

# hard mode ui and variable initializing
off = pygame.image.load("off.png").convert_alpha()
off_r = off.get_rect()
off_r.x, off_r.y = 200, 400
offhover = pygame.transform.scale(pygame.image.load("off.png").convert_alpha(), (205, 85))
on = pygame.image.load("on.png").convert_alpha()
on_r = on.get_rect()
on_r.x, on_r.y = 200, 400
onhover = pygame.transform.scale(pygame.image.load("on.png").convert_alpha(), (205, 85))
offBtn = True
hard = False
hardAlive = True

# dictionary for different buttons hover status
played = {
    playbtn: False,
    rlbtn: False,
    opbtn: False,
    lake: False,
    tree: False,
    tree2: False,
    exitbtn: False,
    leaderbtn: False,
    backbtn: False,
    up: False,
    down: False,
    resetFree: False,
    resetCat: False,
    resetRandom: False,
    freedomDive: False,
    catCafe: False,
    randomBtn: False,
    reset : False,
    conYes : False,
    conNo : False,
    perfectN : False,
    greatN : False,
    okayN : False,
    conX : False,
    vol0 : False,
    vol25 : False,
    vol50 : False,
    vol75 : False,
    vol100 : False,
    playAgain : False,
    off : False,
    on : False
}

# font
myfont = pygame.font.Font("Chewy-Regular.ttf", 25)
test=pygame.display.get_driver()

# difficulties for random mode and user interface 
current = 2
colors = [(66, 245, 78), (252, 243, 71), (245, 5, 5), (232, 71, 237), (145, 33, 237), (199, 74, 153), (100, 73, 105), (245, 157, 91)]
difficulties = ["easy", "normal", "hard", "insane", "expert", "master", "nightmare", "meow"]
lowerbound = [50, 30, 20, 15, 10, 9, 7, 5]
higherbound = [150, 60, 45, 35, 30, 25, 20, 15]

# ---------------------------------------
#               Functions
# ---------------------------------------


def animation(image1, image2):
    # function for animation on game page
    if (beats // 12) % 2 == 0:
        screen.blit(image1, (0, 0))
    else:
        screen.blit(image2, (0, 0))


def hover(name, image, hoverimg, coord):
    # function for images that enlargen when mouse hovered over
    global played, playbtn, rlbtn, opbtn
    cats = [playbtn, rlbtn, opbtn]
    if image in cats:
        sound = meowEff
    else:
        sound = clickEff
    if name.collidepoint(pygame.mouse.get_pos()):
        screen.blit(hoverimg, coord)
        if not played[image]:
            sound.play()
            played[image] = True
    else:
        screen.blit(image, coord)
        played[image] = False


def exitPage():
    # displays a confirmation for exiting the page
    screen.blit(confirmation, (350, 150))
    hover(yes_r, conYes, yesHover, (425, 370))
    hover(no_r, conNo, noHover, (620, 370))


def back():
    # back button condensed into a function
    hover(backbtn_r, backbtn, backhover, (995,5))


def menu():
    # menu screen displays
    screen.blit(homebg, (0, 0))
    hover(lake_r, lake, lakehover, (600, 210))
    hover(tree_r, tree, treehover, (950, 45))
    hover(tree2_r, tree2, tree2hover, (640, 50))
    hover(playbtn_r, playbtn, playbtnhover, (200, 350))
    hover(opbtn_r, opbtn, opbtnhover, (30, 500))
    hover(rlbtn_r, rlbtn, rlbtnhover, (380, 500))
    hover(exit_r, exitbtn, exithover, (5, 5))
    screen.blit(titleimg, (150, 30))
    hover(leaderbtn_r, leaderbtn, leaderhover, (800, 450))


def displayf():
    # adding and popping values from the map to the screen
    if beats in displaysY:
        aliveX.append(displaysX.pop(0))
        aliveY.append(0)
    for i in range(len(aliveY)):
        screen.blit(note, (aliveX[i],aliveY[i]))
    for i in range(len(aliveY)):
        aliveY[i] += 3  


def CheckNote(track):
    # checking for accuracy of notes
    global aliveY, combo, combocnt, score, accuracy, notes, health, hardAlive, page
    if page != "endScreen":
        notes += 1
    for note in aliveY:
        if aliveX[aliveY.index(note)] == track:
            if note > 700: # miss
                aliveX.pop(aliveY.index(note))
                aliveY.remove(note)
                combo=1
                combocnt=0
                health -= 20
                break
            elif note > 650 or note > 450 and note <= 500: # okay
                clickNote(aliveX[aliveY.index(note)], note)
                aliveX.pop(aliveY.index(note))
                aliveY.remove(note)
                score += 50 * combo
                accuracy += 0.5
                break
            elif note > 600 or note > 500 and note <= 550: # great
                clickNote(aliveX[aliveY.index(note)], note)
                aliveX.pop(aliveY.index(note))
                aliveY.remove(note)
                score += 80 * combo
                combocnt += 1
                combo += 0.01
                accuracy += 0.8
                if health <= 99:
                    health += 1
                break
            elif note > 550: # perfect
                clickNote(aliveX[aliveY.index(note)], note)
                aliveX.pop(aliveY.index(note))
                aliveY.remove(note)
                score += 100 * combo
                combocnt += 1
                combo += 0.01
                accuracy += 1
                if health <= 98:
                    health += 2
                break
            else: # miss
                combo = 1
                combocnt = 0
                health -= 20
            if health <= 0 and not offBtn:
                hardAlive = False


def clickNote(x,y):
    # displays perfect, great, okay
    global deadY, deadX, deadTime, deadType
    if y > 650 or y > 450 and y<=500:
        deadType.append(okayN)
    elif y > 600 or y > 500 and y<=550:
        deadType.append(greatN)
    elif y > 550:
        deadType.append(perfectN)
    else:
        deadType.append(0)
    deadY.append(y)
    deadX.append(x)
    deadTime.append(0)


def gameFunction():
    # ingame functions and variable transportation
    global aliveY, aliveX, combo, combocnt, notes, deadTime, deadX, deadY, deadType, health, hardAlive
    for item in aliveY:
        if item >= 750:
            aliveX.pop(aliveY.index(item))
            aliveY.remove(item)
            combo = 1
            combocnt = 0
            notes += 1
            health -= 20
    for i in range(len(deadTime)):
        if deadTime[i] <= 10:
            deadTime[i] += 1
            screen.blit(deadType[i], (deadX[i], deadY[i]))
        else:
            deadX.pop(i)
            deadY.pop(i)
            deadTime.pop(i)
            deadType.pop(i)
            break
    if health <= 0 and not offBtn:
        hardAlive = False    


def freedomReset():
    # reset for 'freedom dive' map
    global aliveX, aliveY, deadY, deadX, deadTime, deadType, beats, score, combo, combocnt, accuracy, notes, freedomPlay, displaysY, displaysX, combos, health, hardAlive
    aliveX = []
    aliveY = []
    deadY = []
    deadX = []
    deadTime = []
    deadType = []
    combos = []
    # note mapping for freedom dive
    displaysY = [150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 350, 370, 371, 390, 410, 430, 445, 460, 475, 490, 505, 
                 535, 536, 565, 585, 605, 625, 640, 650, 660, 670, 680, 690, 700, 718, 719, 720, 721, 735, 750, 765, 780, 
                 795, 810, 825, 849, 850, 865, 866, 880, 881, 900, 915, 930, 945, 960, 975, 990, 1000, 1015, 1030, 1045, 1060, 
                 1075, 1090, 1110, 1111, 1125, 1126, 1140, 1141, 1155, 1156, 1170, 1171, 1195, 1196, 1210, 1211, 1225, 1226, 
                 1240, 1241, 1255, 1256, 1275, 1290, 1291, 1305, 1306, 1315, 1330, 1345, 1360, 1375, 1390, 1405, 1425, 1426, 
                 1433, 1440, 1441, 1448, 1455, 1456, 1470, 1480, 1490, 1500, 1510, 1520, 1530, 1540, 1555, 1556, 1570, 1571, 
                 1585, 1586, 1600, 1601, 1620, 1640, 1660, 1680, 1700, 1720, 1740, 1760, 1780, 1800, 1820, 1840, 1841, 1860, 
                 1880, 1900, 1915, 1930, 1945, 1960, 1975, 2005, 2006, 2035, 2055, 2075, 2095, 2110, 2120, 2130, 2140, 2150, 
                 2160, 2170, 2188, 2189, 2190, 2191, 2205, 2220, 2235, 2250, 2265, 2280, 2295, 2319, 2320, 2335, 2336, 2350, 
                 2351, 2370, 2385, 2400, 2415, 2430, 2445, 2460, 2470, 2485, 2500, 2515, 2530, 2545, 2560, 2580, 2581, 2595, 
                 2596, 2610, 2611, 2625, 2626, 2640, 2641, 2665, 2666, 2680, 2681, 2695, 2696, 2710, 2711, 2725, 2726, 2745, 
                 2760, 2761, 2775, 2776, 2785, 2800, 2815, 2830, 2845, 2860, 2875, 2895, 2896, 2903, 2910, 2911, 2918, 2925, 
                 2926, 2940, 2950, 2960, 2970, 2980, 2990, 3000, 3010, 3025, 3026, 3040, 3041, 3055, 3056, 3070, 3071, 3090, 
                 3114, 3127, 3147, 3172, 3195, 3220, 3241, 3251, 3263, 3272, 3297, 3310, 3332, 3343, 3362, 3376, 3388, 3410, 
                 3425, 3441, 3452, 3467, 3479, 3494, 3503, 3528, 3549, 3571, 3583, 3604, 3621, 3636, 3651, 3673, 3698, 3713, 
                 3733, 3744, 3755, 3764, 3785, 3797, 3819, 3843, 3868, 3881, 3900, 3915, 3930, 3943, 3956, 3968, 3990, 4006, 
                 4026, 4050, 4073, 4082, 4104, 4113, 4127, 4146, 4168, 4177, 4197, 4220, 4237, 4262, 4279, 4295, 4307, 4331, 
                 4351, 4362, 4385, 4394, 4418, 4436, 4452, 4465, 4476, 4485, 4506, 4521, 4537, 4559, 4573, 4588, 4604, 4614, 
                 4629, 4653, 4666, 4680, 4704, 4724, 4739, 4758, 4769, 4794, 4815, 4828, 4848, 4857, 4867, 4888, 4904, 4917, 
                 4926, 4951, 4966, 4984, 4997, 5012, 5026, 5044, 5060, 5073, 5091, 5107, 5127, 5142, 5165, 5184, 5199, 5215, 
                 5240, 5255, 5268, 5277, 5289, 5304, 5329, 5347, 5363, 5383, 5394, 5418, 5427, 5446, 5471, 5489, 5503, 5519, 
                 5544, 5556, 5579, 5597, 5618, 5636, 5649, 5662, 5679, 5691, 5701, 5717, 5734, 5759, 5781, 5792, 5803, 5813, 
                 5837, 5859, 5870, 5895, 5907, 5919, 5942, 5964, 5979, 5992, 6007, 6032, 6056, 6072, 6084, 6096, 6107, 6132, 
                 6157, 6169, 6189, 6202, 6214, 6239, 6248, 6264, 6273, 6296, 6307, 6320, 6333, 6355, 6378, 6390, 6399, 6418, 
                 6440, 6456, 6475, 6490, 6511, 6536, 6555, 6576, 6591, 6614, 6636, 6661, 6671, 6696, 6705, 6724, 6749, 6770, 
                 6781, 6797, 6806, 6830, 6843, 6859, 6873, 6888, 6908, 6919, 6929, 6943, 6962, 6971, 6988, 6997, 7021, 7030, 
                 7055, 7064, 7076, 7088, 7106, 7120, 7132, 7148, 7164, 7186, 7203, 7222, 7245, 7266, 7291, 7306, 7315, 7327, 
                 7336, 7352, 7362, 7386, 7402, 7416, 7438, 7456, 7477, 7492, 7516, 7525, 7539, 7563, 7574, 7591, 7616, 7639, 
                 7657, 7682, 7695, 7711, 7735, 7758, 7778, 7792, 7811, 7832, 7848, 7868, 7878, 7892, 7901, 7924, 7933, 7942, 
                 7965, 7982, 8006, 8022, 8037, 8060, 8074, 8086, 8106, 8131, 8154, 8178, 8190, 8214, 8236, 8254, 8263, 8273, 
                 8283, 8296, 8316, 8341, 8361, 8376, 8386, 8406, 8424, 8442, 8461, 8481, 8490, 8515, 8525, 8536, 8558, 8575, 
                 8590, 8602, 8616, 8636, 8654, 8663, 8688, 8704, 8716, 8740, 8752, 8768, 8787, 8809, 8820, 8835, 8855, 8868, 
                 8886, 8895, 8919, 8931, 8950, 8959, 8968, 8978, 8997, 9019, 9036, 9047, 9059, 9069, 9081, 9097, 9113, 9134, 
                 9153, 9174, 9185, 9204, 9224, 9233, 9249, 9271, 9294, 9317, 9333, 9344, 9368, 9384, 9394, 9419, 9435, 9459, 
                 9472, 9481, 9496, 9508, 9524, 9549, 9563, 9573, 9589, 9609, 9633, 9644, 9656, 9677, 9700, 9714, 9736, 9745, 
                 9761, 9777, 9790, 9805, 9830, 9844, 9853, 9865, 9876, 9890, 9908, 9926, 9948, 9965, 9979, 10004, 10014, 10028, 
                 10044, 10055, 10065, 10086, 10098, 10121, 10141, 10153, 10167, 10182, 10198, 10222, 10242, 10263, 10277, 10290, 
                 10301, 10316, 10330, 10342, 10363, 10381, 10395, 10409, 10424, 10445, 10460, 10471, 10489, 10498, 10522, 10532, 
                 10545, 10568, 10586, 10604, 10620, 10633, 10646, 10657, 10676, 10686, 10696, 10716, 10738, 10760, 10774, 10783, 
                 10799, 10823, 10843, 10855, 10871, 10893, 10914, 10927, 10936, 10954, 10963, 10986, 10996, 11008, 11033, 11044, 
                 11060, 11083, 11097, 11120, 11143, 11161, 11184, 11195, 11208, 11226, 11250, 11269, 11284, 11293, 11311, 11330, 
                 11343, 11368, 11384, 11394, 11418, 11433, 11458, 11471, 11480, 11493, 11513, 11522, 11534, 11557, 11572, 11586, 
                 11601, 11622, 11632, 11645, 11659, 11677, 11702, 11713, 11724, 11740, 11758, 11781, 11791, 11802, 11812, 11823, 
                 11834, 11849, 11862, 11885, 11909, 11921, 11931, 11955, 11971, 11980, 12002, 12019, 12041, 12059, 12073, 12098, 
                 12109, 12121, 12131, 12143, 12165, 12175, 12185, 12208, 12227, 12241, 12264, 12275, 12296, 12319, 12342, 12364, 
                 12374, 12389, 12414, 12439, 12454, 12469, 12489, 12508, 12532, 12551, 12566, 12585, 12598, 12612, 12636, 12656, 
                 12667, 12678, 12693, 12706, 12719, 12737, 12749, 12772, 12788, 12804, 12815, 12840, 12858, 12869, 12894, 12911, 
                 12925, 12937, 12959, 12973, 12995, 13011, 13027, 13040, 13054, 13071, 13096, 13111, 13124, 13144, 13166, 13179, 
                 13203, 13223, 13233, 13246, 13270, 13291, 13305, 13326, 13335, 13351, 13373, 13390, 13413, 13434, 13445, 13457, 
                 13477, 13487, 13512, 13521, 13533, 13551, 13570, 13582, 13606, 13619, 13639, 13652, 13675, 13699, 13712, 13737, 
                 13760, 13783, 13799, 13815, 13830, 13850, 13863, 13878, 13888, 13906, 13925, 13945, 13963, 13973, 13995, 14016, 
                 14039, 14048, 14071, 14086, 14096, 14120, 14141, 14159, 14170, 14189, 14207, 14227, 14239, 14261, 14270, 14281, 
                 14292, 14312, 14331, 14341, 14356, 14376, 14393, 14411, 14421, 14438, 14453, 14474, 14497, 14512, 14531, 14556, 
                 14570, 14590, 14602, 14616, 14627, 14648, 14666, 14689, 14705, 14719, 14730, 14743, 14757, 14768, 14789, 14803, 
                 14820, 14836, 14861, 14875, 14893, 14904, 14929, 14943, 14958, 14977, 14997, 15019, 15029, 15052, 15074, 15086, 
                 15110, 15134, 15144, 15165, 15181, 15193, 15216, 15237, 15246, 15266, 15291, 15307, 15327, 15347, 15359, 15381, 
                 15394, 15418, 15443, 15452, 15466, 15478, 15488, 15511, 15536, 15554, 15566, 15582, 15602, 15614, 15635, 15645, 
                 15664, 15683, 15694, 15710, 15735, 15756, 15772, 15783, 15800, 15814, 15828, 15848, 15868, 15883, 15894, 15910, 
                 15929, 15941, 15955, 15979, 15994, 16015, 16039, 16057, 16079, 16096, 16120, 16134, 16154, 16172, 16192, 16203, 
                 16218, 16232, 16244, 16264, 16285, 16307, 16317, 16341, 16364, 16381, 16397, 16419, 16432, 16454, 16466, 16485, 
                 16495, 16513, 16522, 16538, 16548, 16563, 16580, 16598, 16614, 16625, 16635, 16644, 16665, 16677, 16693, 16709, 
                 16733, 16750, 16764, 16781, 16791, 16812, 16821, 16832, 16849, 16859, 16880, 16900, 16918, 16936, 16948, 16969, 
                 16992, 17008, 17028, 17049, 17063, 17075, 17091, 17112, 17132, 17154, 17177, 17202, 17215, 17231, 17242, 17259, 
                 17278, 17294, 17312, 17323, 17341, 17353, 17370, 17379, 17389, 17414, 17425, 17438, 17447, 17468, 17491, 17510, 
                 17522, 17532, 17550, 17573, 17585, 17606, 17627, 17646, 17655, 17680, 17690, 17706, 17718, 17733, 17746, 17765, 
                 17785, 17807, 17817, 17841, 17865, 17885, 17909, 17927, 17950, 17974, 17996, 18015, 18030, 18052, 18062, 18076, 
                 18085, 18101, 18119, 18131, 18150, 18164, 18176, 18186, 18195, 18212, 18221, 18232, 18254, 18266, 18286, 18309, 
                 18332, 18352, 18365, 18388, 18408, 18428, 18453, 18474, 18497, 18510, 18531, 18544, 18554, 18577, 18586, 18599, 
                 18616, 18630, 18643, 18658, 18675, 18686, 18707, 18719, 18743, 18765, 18779, 18791, 18802, 18823, 18843, 18859, 
                 18877, 18889, 18899, 18910, 18935, 18949, 18969, 18978, 18990, 19014, 19037, 19062, 19075, 19094, 19107, 19123, 
                 19133, 19153, 19170, 19192, 19212, 19224, 19245, 19257, 19279, 19303, 19328, 19344, 19356, 19378, 19399, 19423, 
                 19441, 19465, 19485, 19507, 19516, 19529, 19544, 19560, 19575, 19593, 19607, 19616, 19628, 19652, 19664, 19674, 
                 19695, 19713, 19733, 19744, 19761, 19780, 19795, 19819, 19833, 19846, 19860, 19870, 19884, 19901, 19918, 19939, 
                 19955, 19975, 19988, 20001, 20025, 20048, 20072, 20087, 20109, 20118, 20143, 20155, 20167, 20183, 20207, 20230, 
                 20251, 20261, 20281, 20294, 20318, 20332, 20344, 20355, 20365, 20385, 20399, 20414, 20428, 20452, 20462, 20484, 
                 20497, 20506]
    displaysX = [x1, x2, x3, x4, x2, x1, x3, x4, x1, x2, x3, x4, x1, x3, x2, x1, x4, x3, x2, x1, x2, x1, x4, x4, x3, x2, x1, x2, 
                 x1, x4, x1, x4, x1, x4, x1, x2, x3, x4, x1, x2, x1, x2, x1, x2, x1, x3, x4, x1, x2, x3, x4, x1, x2, x3, x4, x3, 
                 x2, x1, x1, x2, x3, x4, x3, x2, x1, x1, x4, x2, x3, x1, x4, x2, x3, x1, x4, x1, x2, x3, x4, x1, x2, x3, x4, x1, 
                 x2, x4, x3, x4, x3, x1, x1, x2, x3, x4, x3, x2, x1, x3, x4, x1, x3, x4, x1, x3, x4, x1, x2, x4, x3, x1, x2, x4, 
                 x3, x1, x2, x3, x4, x1, x2, x3, x4, x1, x2, x3, x4, x2, x1, x3, x4, x1, x2, x3, x4, x1, x3, x2, x1, x4, x3, x2, 
                 x1, x2, x1, x4, x4, x3, x2, x1, x2, x1, x4, x1, x4, x1, x4, x1, x2, x3, x4, x1, x2, x1, x2, x1, x2, x1, x3, x4, 
                 x1, x2, x3, x4, x1, x2, x3, x4, x3, x2, x1, x1, x2, x3, x4, x3, x2, x1, x1, x4, x2, x3, x1, x4, x2, x3, x1, x4, 
                 x1, x2, x3, x4, x1, x2, x3, x4, x1, x2, x4, x3, x4, x3, x1, x1, x2, x3, x4, x3, x2, x1, x3, x4, x1, x3, x4, x1, 
                 x3, x4, x1, x2, x4, x3, x1, x2, x4, x3, x1, x2, x3, x4, x1, x2, x3, x4, x1, x2, x3, x4, x2, x1, x2, x1, x4, x1, 
                 x3, x4, x3, x4, x2, x1, x4, x3, x1, x1, x4, x1, x2, x3, x1, x4, x1, x4, x2, x4, x3, x2, x1, x4, x2, x1, x4, x3, 
                 x4, x2, x4, x1, x2, x4, x1, x4, x2, x1, x3, x2, x1, x4, x1, x4, x1, x4, x2, x1, x3, x2, x4, x2, x3, x2, x4, x1, 
                 x3, x4, x3, x4, x3, x4, x1, x1, x3, x2, x3, x2, x3, x2, x4, x1, x3, x1, x3, x2, x4, x3, x4, x3, x1, x4, x2, x3, 
                 x2, x1, x2, x4, x4, x1, x4, x1, x2, x3, x2, x1, x3, x2, x1, x2, x2, x4, x2, x1, x2, x1, x4, x2, x4, x1, x2, x3, 
                 x2, x4, x3, x2, x4, x3, x1, x4, x2, x3, x1, x2, x4, x3, x4, x1, x3, x1, x4, x2, x1, x4, x2, x1, x4, x3, x4, x2, 
                 x1, x1, x2, x1, x2, x2, x4, x3, x2, x4, x2, x4, x1, x3, x1, x2, x1, x3, x1, x1, x2, x3, x1, x2, x4, x2, x4, x2, 
                 x1, x4, x1, x3, x2, x3, x1, x4, x3, x1, x4, x3, x2, x1, x3, x1, x4, x1, x3, x4, x2, x1, x2, x1, x4, x1, x2, x4, 
                 x3, x1, x2, x3, x1, x3, x1, x2, x3, x1, x4, x1, x4, x3, x2, x1, x2, x1, x2, x4, x1, x3, x1, x3, x4, x3, x4, x3, 
                 x2, x3, x4, x3, x4, x1, x4, x2, x2, x3, x2, x4, x1, x3, x4, x3, x2, x1, x4, x3, x2, x1, x4, x3, x4, x3, x4, x2, 
                 x4, x1, x2, x2, x1, x3, x2, x3, x4, x2, x3, x2, x3, x1, x4, x2, x4, x3, x4, x3, x4, x3, x2, x1, x2, x4, x1, x4, 
                 x1, x2, x1, x2, x4, x1, x3, x4, x2, x4, x1, x4, x1, x3, x4, x3, x4, x1, x4, x1, x3, x4, x2, x4, x3, x2, x3, x3, 
                 x4, x2, x3, x2, x3, x4, x1, x4, x2, x1, x3, x1, x2, x1, x2, x3, x4, x2, x4, x2, x4, x2, x3, x2, x3, x1, x2, x1, 
                 x4, x1, x3, x2, x4, x3, x2, x3, x2, x3, x4, x2, x3, x1, x3, x2, x1, x3, x2, x1, x2, x3, x2, x4, x2, x1, x3, x1, 
                 x3, x2, x1, x1, x4, x1, x4, x1, x3, x1, x4, x3, x2, x1, x1, x2, x3, x4, x2, x2, x4, x3, x1, x3, x2, x1, x2, x3, 
                 x2, x1, x3, x1, x2, x4, x2, x4, x3, x4, x1, x2, x4, x3, x4, x1, x3, x4, x2, x3, x2, x4, x3, x2, x3, x2, x3, x4, 
                 x3, x2, x3, x2, x2, x4, x2, x3, x1, x2, x4, x2, x1, x2, x1, x4, x4, x3, x4, x3, x4, x1, x2, x3, x2, x1, x3, x1, 
                 x3, x1, x2, x4, x1, x4, x1, x4, x1, x2, x3, x4, x2, x1, x3, x1, x4, x2, x3, x1, x4, x3, x4, x3, x1, x4, x1, x3, 
                 x2, x1, x2, x3, x4, x2, x1, x4, x1, x3, x2, x4, x1, x2, x4, x3, x2, x1, x4, x1, x3, x4, x1, x2, x1, x3, x2, x3, 
                 x1, x4, x2, x3, x4, x3, x4, x1, x3, x2, x4, x2, x1, x4, x1, x4, x3, x4, x3, x4, x3, x1, x3, x4, x3, x2, x3, x1, 
                 x3, x2, x3, x4, x1, x4, x1, x3, x1, x2, x4, x3, x4, x3, x4, x3, x1, x3, x4, x1, x4, x1, x3, x2, x3, x1, x2, x3, 
                 x4, x2, x1, x2, x4, x1, x4, x2, x3, x4, x1, x4, x2, x3, x2, x1, x2, x4, x1, x4, x2, x3, x1, x4, x1, x3, x4, x4, 
                 x3, x1, x2, x3, x2, x1, x4, x2, x3, x2, x4, x3, x4, x3, x4, x2, x4, x2, x1, x4, x3, x4, x2, x1, x4, x3, x1, x4, 
                 x2, x4, x1, x2, x4, x3, x2, x4, x2, x3, x4, x3, x2, x4, x3, x1, x2, x4, x1, x4, x3, x4, x2, x3, x1, x4, x1, x1, 
                 x2, x3, x4, x1, x2, x4, x4, x1, x1, x3, x4, x3, x2, x4, x2, x3, x2, x3, x4, x2, x3, x1, x3, x2, x2, x4, x2, x1, 
                 x2, x4, x4, x1, x4, x1, x3, x2, x1, x2, x3, x2, x1, x4, x1, x4, x3, x1, x2, x4, x3, x1, x2, x3, x1, x3, x1, x2, 
                 x3, x4, x3, x3, x2, x1, x3, x1, x2, x3, x2, x3, x2, x1, x3, x4, x3, x4, x3, x4, x1, x1, x4, x1, x3, x2, x4, x3, 
                 x2, x4, x1, x4, x2, x3, x1, x4, x3, x1, x4, x2, x1, x2, x1, x4, x1, x2, x4, x3, x1, x3, x4, x1, x4, x2, x4, x2, 
                 x4, x1, x3, x1, x1, x4, x2, x4, x2, x1, x3, x2, x1, x2, x4, x3, x3, x1, x3, x3, x1, x3, x1, x2, x3, x4, x3, x1, 
                 x3, x2, x4, x1, x2, x3, x2, x4, x1, x4, x3, x4, x3, x1, x3, x1, x3, x4, x2, x4, x3, x1, x3, x4, x2, x3, x1, x4, 
                 x2, x4, x2, x3, x1, x3, x2, x2, x4, x2, x1, x4, x3, x1, x3, x1, x2, x4, x3, x3, x1, x3, x4, x1, x4, x3, x1, x4, 
                 x1, x4, x1, x3, x2, x4, x2, x4, x3, x4, x3, x4, x1, x4, x3, x1, x2, x3, x1, x2, x1, x4, x2, x3, x2, x1, x2, x3, 
                 x2, x4, x3, x4, x3, x2, x4, x1, x2, x4, x3, x4, x1, x3, x1, x3, x4, x2, x4, x3, x1, x4, x4, x2, x1, x4, x2, x1, 
                 x4, x2, x4, x1, x2, x1, x4, x2, x2, x3, x2, x1, x3, x1, x4, x3, x2, x3, x1, x3, x1, x2, x2, x1, x2, x3, x1, x3, 
                 x2, x1, x3, x4, x1, x2, x4, x3, x1, x4, x3, x4, x3, x2, x4, x2, x3, x1, x4, x3, x1, x4, x1, x4, x2, x2, x1, x3, 
                 x2, x1, x4, x3, x4, x2, x1, x3, x4, x2, x4, x1, x3, x4, x2, x2, x3, x1, x3, x4, x1, x4, x1, x3, x1, x4, x1, x3, 
                 x3, x1, x3, x2, x4, x3, x4, x1, x3, x4, x3, x1, x3, x2, x1, x3, x4, x1, x4, x2, x1, x2, x1, x2, x4, x2, x4, x1, 
                 x4, x1, x3, x4, x2, x1, x4, x1, x2, x4, x3, x4, x3, x2, x1, x1, x3, x4, x1, x3, x4, x1, x4]
    # variable resets
    beats = 0
    score = 0
    combo = 1
    combocnt = 0
    accuracy = 0
    notes = 0
    health = 100
    hardAlive = True
    freedomPlay = True   


def catReset():
    # reset for 'freedom dive' map
    global aliveX, aliveY, deadY, deadX, deadTime, deadType, beats, score, combo, combocnt, accuracy, notes, catPlay, displaysX, displaysY, combos, health, hardAlive
    aliveX = []
    aliveY = []
    deadY = []
    deadX = []
    deadTime = []
    deadType = []
    combos = []
    # note mapping for cat at the cafe
    displaysY = [0, 40, 80, 120, 230, 231, 270, 310, 350, 410, 411, 450, 490, 530, 590, 1215, 1225, 1235, 1245, 1490, 1510, 
                 1530, 1550, 1580, 1780, 1824, 1879, 1910, 1964, 2017, 2052, 2090, 2133, 2165, 2225, 2262, 2310, 2350, 2386, 
                 2436, 2490, 2541, 2578, 2612, 2653, 2683, 2730, 2789, 2842, 2901, 2937, 2979, 3023, 3080, 3124, 3163, 3212, 
                 3254, 3314, 3366, 3425, 3477, 3524, 3570, 3624, 3656, 3687, 3729, 3786, 3846, 3886, 3917, 3955, 3999, 4055, 
                 4086, 4137, 4181, 4223, 4277, 4315, 4353, 4399, 4453, 4498, 4556, 4593, 4626, 4674, 4709, 4754, 4793, 4825, 
                 4877, 4926, 4963, 5001, 5051, 5109, 5151, 5181, 5219, 5252, 5289, 5344, 5404, 5460, 5516, 5546, 5599, 5630, 
                 5665, 5700, 5750, 5781, 5840, 5893, 5942, 5988, 6019, 6066, 6126, 6176, 6229, 6284, 6326, 6367, 6426, 6479, 
                 6527, 6563, 6616, 6655, 6713, 6754, 6808, 6858, 6896, 6939, 6989, 7025, 7067, 7122, 7162, 7210, 7258, 7306, 
                 7361, 7408, 7446, 7502, 7558, 7617, 7667, 7724, 7756, 7787, 7821, 7854, 7898, 7934, 7965, 8006, 8059, 8108, 
                 8162, 8204, 8257, 8292, 8330, 8373, 8405, 8465, 8502, 8550, 8590, 8626, 8676, 8730, 8781, 8818, 8852, 8893, 
                 8923, 8970, 9029, 9082, 9141, 9177, 9219, 9263, 9320, 9364, 9403, 9452, 9494, 9554, 9606, 9665, 9717, 9764, 
                 9810, 9864, 9896, 9927, 9969, 10000]
    displaysY.sort()
    displaysX = [x1, x2, x3, x4, x2, x4, x4, x3, x2, x4, x1, x2, x3, x4, x3, x1, x2, x3, x4, x4, x3, x2, x1, x2, x1, x3, x2, 
                 x4, x3, x2, x1, x3, x2, x1, x3, x4, x3, x2, x3, x2, x3, x1, x1, x3, x2, x4, x3, x2, x3, x3, x1, x3, x4, x2, 
                 x4, x4, x1, x3, x2, x3, x3, x3, x2, x1, x1, x3, x1, x2, x2, x2, x3, x3, x2, x4, x2, x2, x2, x2, x1, x3, x4, 
                 x2, x3, x4, x1, x2, x2, x1, x2, x2, x4, x4, x3, x3, x2, x3, x4, x3, x4, x1, x4, x3, x3, x1, x1, x2, x1, x3, 
                 x3, x2, x3, x1, x1, x2, x2, x2, x2, x2, x3, x3, x1, x3, x4, x2, x1, x3, x1, x1, x3, x1, x4, x4, x2, x3, x4, 
                 x1, x3, x1, x1, x1, x2, x2, x1, x2, x3, x3, x2, x4, x2, x3, x1, x4, x4, x2, x4, x2, x1, x4, x3, x3, x2, x2, 
                 x2, x3, x3, x1, x1, x1, x4, x3, x3, x1, x3, x2, x2, x1, x1, x4, x4, x3, x3, x1, x2, x2, x4, x3, x2, x3, x2, 
                 x3, x3, x2, x4, x2, x3, x3, x3, x4, x3, x3, x1, x3, x3, x2, x2, x3, x3, x2, x3, x2, x3, x1, x2, x2, x4, x3, 
                 x2, x3, x2, x2, x4]
    # variable resets
    beats = 0
    score = 0
    combo = 1
    combocnt = 0
    accuracy = 0
    notes = 0
    health = 100
    hardAlive = True
    catPlay = True


def rulesAnimation():
    # animation in the rules screen
    global beats, rulesDisplaysX, rulesDisplaysY, rulesAliveX, rulesAliveY, dead
    rulesDisplaysY.append(rulesDisplaysY[-1] + 300)
    rulesDisplaysX.append(470)
    # appends a new note every 200 ticks
    if beats in rulesDisplaysY:
        rulesAliveX.append(rulesDisplaysX.pop(0))
        rulesAliveY.append(200)
    screen.blit(blank, (470, 400))
    for i in range(len(rulesAliveY)):
        screen.blit(note, (rulesAliveX[i], rulesAliveY[i]))
    for i in range(len(rulesAliveY)):
        rulesAliveY[i] += 1
    if len(rulesAliveY) > 0:
        if rulesAliveY[0] > 400:
            xcoord = rulesAliveX.pop(0)
            ycoord = rulesAliveY.pop(0)
            dead = 0
    # displays a perfect note 
    if dead < 15:
        screen.blit(perfectN, (470, 400))
        dead += 1


def randomReset():
    # reset for random mode
    global aliveX, aliveY, deadY, deadX, deadTime, deadType, beats, score, combo, combocnt, accuracy, notes, displaysX, displaysY, combos, randomPlay, health, hardAlive
    import random
    aliveX = []
    aliveY = []
    deadY = []
    deadX = []
    deadTime = []
    deadType = []
    displaysX = [x1]
    displaysY = [10]
    xVals = [x1, x2, x3, x4]
    combos = []
    lower = lowerbound[current]
    higher = higherbound[current]
    # random map generator
    for gen in range(1500):
        randomx = xVals[random.randint(0,3)]
        while displaysX[-1] == randomx:
            randomx = xVals[random.randint(0,3)]
            if random.randint(0,1) == 1:
                break
        if displaysY[-1] > 15000:
            break
        displaysX.append(randomx)
        displaysY.append(random.randint(displaysY[-1] + lower, displaysY[-1] + higher))
    # variable resets
    beats = 0
    score = 0
    combo = 1
    combocnt = 0
    accuracy = 0
    notes = 0
    health = 100
    hardAlive = True
    randomPlay = True


def gameScreen():
    # in game screen
    global beats, score, combo, combocnt, accuracy, notes, exitbtn, combos
    hover(exit_r, exitbtn, exithover, (5, 5))   
    scoreText = myfont.render(str(round(score)), True, THECOLORS["black"])  
    comboText = myfont.render(str(combocnt), True, THECOLORS["black"])
    comboM = myfont.render(str(round(combo, 2)), True, THECOLORS["black"])
    # preventing zero divsion in accuracy calculations
    try:
        accPercent = str(round(accuracy / notes * 100, 2)) + "%"
    except ZeroDivisionError:
        accPercent = str(round(accuracy, 2)) + "%"
    accuracyText = myfont.render(accPercent, True, THECOLORS["black"]) 
    screen.blit(myfont.render("Score:", True, THECOLORS["black"]), (650,100))
    screen.blit(scoreText, (750,100))
    screen.blit(myfont.render("Combo:", True, THECOLORS["black"]), (650,150))
    screen.blit(comboText, (750,150))
    screen.blit(myfont.render("Combo Multiplier:", True, THECOLORS["black"]), (650,200))
    screen.blit(comboM, (825,200))
    screen.blit(myfont.render("Accuracy:", True, THECOLORS["black"]), (650,250))
    screen.blit(accuracyText, (750,250))
    # functions for hard mode
    if hard:
        healthText = myfont.render(str(health), True, THECOLORS["black"])
        screen.blit(myfont.render("Health:", True, THECOLORS["black"]), (650, 300))
        screen.blit(healthText, (750, 300))
    screen.blit(d_btn, (x1, 570))
    screen.blit(f_btn, (x2, 570))
    screen.blit(j_btn, (x3, 570))
    screen.blit(k_btn, (x4, 570))
    combos.append(combocnt)
    back()


def lbRead(leaderboard):
    # accessing the leaderboard notes files
    global leader, printX, scoreDisplay
    # checking for which leaderboard needs to be accessed
    if leaderboard == "freedom":
        leaderFile = open("Leaderboard_freedom.txt", "r")
        printX = 110
        scoreDisplay = 205
    elif leaderboard == "cat":
        leaderFile = open("Leaderboard_cat.txt", "r")
        printX = 500
        scoreDisplay = 605
    elif leaderboard == "random":
        leaderFile = open("Leaderboard_random.txt", "r")
        printX = 900
        scoreDisplay = 1005
    leader = []
    for line in leaderFile:
        leader.append(str(line))
    leaderFile.close()
    return max(leader)


def lbWrite(leaderboard, score):
    # writing new scores in leaderboard
    global leader
    # reads the correct leaderboard first
    lbRead(leaderboard)
    # checking for which leaderboard needs to be accessed
    if leaderboard == "freedom":
        leaderWrite = open("Leaderboard_freedom.txt", "w")
    elif leaderboard == "cat":
        leaderWrite = open("Leaderboard_cat.txt", "w")
    elif leaderboard == "random":
        leaderWrite = open("Leaderboard_random.txt", "w")
    leader.append(str(score))
    # rewrites file
    for point in leader:
        appendedScore = str(int(float(point))) + "\n"
        leaderWrite.write(appendedScore)
    leaderWrite.close()    


def lb10(leaderboard):
    # ensures that there are only 10 items in the leaderboard at any given time
    global leader
    # checking for which leaderboard needs to be accessed
    if leaderboard == "freedom":
        leaderWrite = open("Leaderboard_freedom.txt", "w")
    elif leaderboard == "cat":
        leaderWrite = open("Leaderboard_cat.txt", "w")
    elif leaderboard == "random":
        leaderWrite = open("Leaderboard_random.txt", "w")  
    tempL = leader 
    leader = []
    # accesses the scores and sorts them
    for item in tempL:
        leader.append(float(item))
    leader.sort(reverse = True)
    # memory only retains the top 10 scores and rewrites them into the file
    leader = leader[:10]
    for point in leader:
        appendedScore = str(int(float(point))) + "\n"
        leaderWrite.write(appendedScore)
    leaderWrite.close()     


def lbFreedom(mapping):
    # retrieves data for displaying leaderboard 
    lbRead(mapping)
    lb10(mapping)
    lbRead(mapping)
    numbers = []
    leaderDisplays = []
    displayCoord = []
    printY = 180
    # prints all of the scores 
    for i in leader:
        numbers.append((printX,printY))
        leaderDisplays.append(str(i))
        displayCoord.append((scoreDisplay, printY))
        printY += 38
    for i in range(len(leaderDisplays)):
        screen.blit(myfont.render(str(i+1) + ":", True, THECOLORS["black"]), (numbers[i]))
        screen.blit(myfont.render(leaderDisplays[i], True, THECOLORS["black"]), displayCoord[i])


def lbreset(mapping):
    # resets a certain leaderboard 
    global leader
    leader = [0,0,0,0,0,0,0,0,0,0]
    if mapping == "freedom":
        leaderWrite = open("Leaderboard_freedom.txt", "w")
    elif mapping == "cat":
        leaderWrite = open("Leaderboard_cat.txt", "w")
    elif mapping == "random":
        leaderWrite = open("Leaderboard_random.txt", "w")
    for point in leader:
        appendedScore = str(int(float(point))) + "\n"
        leaderWrite.write(appendedScore)
    leaderWrite.close()       

# ---------------------------------------
#               Game Loop
# ---------------------------------------

try:
    while keepGoing:
        clock.tick(144)
        screen.fill((255,255,255))
        
        # menu page
        if page == "menu":
            menu()

        # leaderboard page
        elif page == "leader":
            screen.blit(leaderbg, (0,0))
            hover(exit_r, exitbtn, exithover, (5,5))            
            back()
            screen.blit(scrollFree, (-20,70))
            screen.blit(scrollCat, (370,70))
            screen.blit(scrollRandom, (760,70))
            # accessing and displaying different leaderboards
            lbFreedom("freedom")
            lbFreedom("cat")
            lbFreedom("random")
            hover(resetFree_r, resetFree, resethover, (80,620))
            hover(resetCat_r, resetCat, resethover, (470,620))
            hover(resetRandom_r, resetRandom, resethover, (860,620))
            if confirmationReset:
                screen.blit(conImg, (350, 150))
                hover(conX_r, conX, conXhover, (750, 200))  

        # mode selection page
        elif page == "play":
            screen.blit(playbg, (0,0))
            hover(exit_r, exitbtn, exithover, (5, 5))
            hover(freedom_r, freedomDive, freedomHover, (200, 100))
            hover(cat_r, catCafe, catHover, (600, 100))
            hover(random_r, randomBtn, randomHover, (350, 475))            
            back()
            screen.blit(myfont.render("Click on a image to start the game of your choice!", True, THECOLORS["black"]), (325,50))

        # options
        elif page == "options":
            screen.blit(optionsbg, (0, 0))
            screen.blit(optionimg, (75, 80))
            hover(exit_r, exitbtn, exithover, (5, 5))
            hover(up_r, up, uphover, (650, 380))
            hover(down_r, down, downhover, (960, 380))
            # difficulties for random mode
            screen.blit(myfont.render("Random Mode Difficulties", True, THECOLORS["black"]), (725, 200))
            screen.blit(myfont.render("Difficulties: easy - meow", True, THECOLORS["black"]), (725, 300))
            pygame.draw.rect(screen, colors[current], (750,375,200,100), width=0, border_radius=8, border_top_left_radius=-10, border_top_right_radius=-10, border_bottom_left_radius=-10, border_bottom_right_radius=-10)
            if current == 6:
                screen.blit(myfont.render(difficulties[current], True, THECOLORS["white"]), (805, 410))
            else:
                screen.blit(myfont.render(difficulties[current], True, THECOLORS["black"]), (805, 410))
            screen.blit(myfont.render("Data (leaderboard) Reset", True, THECOLORS["black"]), (175, 200))
            hover(reset_r, reset, resethover, (200, 250))
            # volume options
            screen.blit(myfont.render("Volume picker", True, THECOLORS["black"]), (175,500))
            hover(vol100_r, vol100, vol100hover, (600, 550))
            hover(vol75_r, vol75, vol75hover, (475, 550))
            hover(vol50_r, vol50, vol50hover, (350, 550))
            hover(vol25_r, vol25, vol25hover, (225, 550))
            hover(vol0_r, vol0, vol0hover, (100, 550))
            # hard mode
            screen.blit(myfont.render("Hard Mode", True, THECOLORS["black"]), (175,350))
            # alternating between 'on' and 'off'
            if not offBtn:
                on_r.x, on_r.y = 200, 400
                off_r.x, off_r.y = 10000, 10000
                hover(on_r, on, onhover, (200,400))
            else:
                off_r.x, off_r.y = 200, 400
                on_r.x, on_r.y = 10000, 10000                
                hover(off_r, off, offhover, (200, 400))
            back()
            if confirmationReset:
                screen.blit(conImg, (350, 150))
                hover(conX_r, conX, conXhover, (750, 200))     

        # rules
        elif page == "rules":
            keys = [d_btn, f_btn, j_btn, k_btn]
            positions = [(130, 520), (200, 520), (270, 520), (340, 520), (600, 400), (760, 400), (920, 400)]
            screen.blit(rulesbg, (0, 0))
            screen.blit(rulesimg, (75, 80))
            for i in range(4):
                screen.blit(keys[i], positions[i])
            # accuracy displays 
            hover(perfect_r, perfectN, perfecthover, positions[4])
            hover(great_r, greatN, greathover, positions[5])
            hover(okay_r, okayN, okayhover, positions[6])
            rulesAnimation()
            hover(exit_r, exitbtn, exithover, (5, 5))            
            back()
            beats += 1

        # freedom dive page
        elif page == "freedomDive":
            animation(freedombg, freedombg2)
            if freedomPlay:
                fDive.play()
                freedomPlay=False
            gameScreen()
            displayf()
            gameFunction()
            beats+=1
            endScreenTime = displaysY[-1] + 500
            # refreshes leaderboard
            if beats > endScreenTime:
                lbWrite("freedom", score)
                currentMap = "freedom"
                page = "endScreen"
                fDive.stop()
            # ends game for hard mode
            if not hardAlive:
                currentMap = "freedom"
                aliveX = []
                aliveY = []                
                page = "endScreen"
                fDive.stop()

        # cat cafe page
        elif page == "catCafe":
            animation(catbg, catbg2)            
            if catPlay and beats == 50:
                cCafe.play()
                catPlay=False
            gameScreen()
            displayf()
            gameFunction()
            endScreenTime = displaysY[-1] + 500
            beats+=1
            # refreshes leaderboard
            if beats > endScreenTime:
                lbWrite("cat", score)
                currentMap = "cat"
                page = "endScreen"
                cCafe.stop()
            # ends game for hard mode
            if not hardAlive:
                currentMap = "cat"
                aliveX = []
                aliveY = []                
                page = "endScreen" 
                cCafe.stop()

        # random game mode page
        elif page == "random":
            if randomPlay:
                randomSound.play()
                randomPlay=False            
            animation(randombg, randombg2)
            gameScreen()
            displayf()
            gameFunction()
            endScreenTime = displaysY[-1]+500
            beats+=1
            # refreshes leaderboard
            if beats > endScreenTime:
                lbWrite("random", score)
                currentMap = "random"
                page = "endScreen"
                randomSound.stop()
            # ends game for hard mode
            if not hardAlive:
                currentMap = "random"
                page = "endScreen"
                aliveX = []
                aliveY = []
                randomSound.stop()
        
        # end/game over screen
        elif page == "endScreen":
            # determines which mode was played and reads the highest score from that leaderboard
            if currentMap == "freedom":
                highscore = lbRead(currentMap)
            elif currentMap == "cat":
                highscore = lbRead(currentMap)
            elif currentMap == "random":
                highscore = lbRead(currentMap)
            screen.blit(playbg, (0,0))
            hover(exit_r, exitbtn, exithover, (5,5))
            # prevents zero division
            try:
                accPercent = str(round(accuracy/notes*100, 2)) + "%"
            except ZeroDivisionError:
                accPercent = str(round(accuracy, 2)) + "%"
            accuracyText=myfont.render(accPercent, True, THECOLORS["black"]) 
            scoreText = myfont.render(str(round(score)), True, THECOLORS["black"])  
            comboText = myfont.render(str(max(combos)), True, THECOLORS["black"])
            # displays different scroll for hard mode game over and easy mode
            if hardAlive:
                screen.blit(scrollStats, (275, 0))
            else:
                screen.blit(scrollDied, (275, 0))
            # displays statistics
            screen.blit(myfont.render("Score:", True, THECOLORS["black"]), (450,275))
            screen.blit(scoreText, (450, 325))
            screen.blit(myfont.render("HighScore:", True, THECOLORS["black"]), (650,275))
            screen.blit(myfont.render(highscore, True, THECOLORS["black"]), (650, 325))
            screen.blit(myfont.render("Accuracy:", True, THECOLORS["black"]), (450,400))            
            screen.blit(accuracyText, (450, 450))
            screen.blit(myfont.render("Highest Combo:", True, THECOLORS["black"]), (650,400))            
            screen.blit(comboText, (650, 450))
            hover(play_r, playAgain, playAgainhover, (475, 550))
            # congratulates user if they got the most recent high score
            if int(score) == int(highscore) and hardAlive:
                screen.blit(endbanner, (0,0))
            back()
        
        # exit button functions
        if exit: 
            exitPage()
        
        # refreshes display every frame 
        pygame.display.flip()
        
        # handles events
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT:
                keepGoing = False
                
            # handles click events
            if ev.type == MOUSEBUTTONDOWN:
                # exit confirmation event (y/n)
                if not(confirmationReset):
                    if exit_r.collidepoint(pygame.mouse.get_pos()):
                        exit = True
                    if exit:
                        if yes_r.collidepoint(pygame.mouse.get_pos()):
                            keepGoing = False
                        if no_r.collidepoint(pygame.mouse.get_pos()):
                            exit = False
                            break
                # handles events in menu and different buttons
                if page == "menu":
                    if not(exit):
                        if playbtn_r.collidepoint(pygame.mouse.get_pos()):
                            page = "play"
                        if leaderbtn_r.collidepoint(pygame.mouse.get_pos()):
                            page = "leader"
                        if opbtn_r.collidepoint(pygame.mouse.get_pos()):
                            page = "options"
                        if rlbtn_r.collidepoint(pygame.mouse.get_pos()):
                            page = "rules"
                # handles events in leaderboard
                elif page == "leader" and not(confirmationReset):
                    if not(exit):                    
                        if backbtn_r.collidepoint(pygame.mouse.get_pos()):
                            page = "menu"
                        if resetFree_r.collidepoint(pygame.mouse.get_pos()):
                            lbreset("freedom")
                            confirmationReset = True
                        if resetCat_r.collidepoint(pygame.mouse.get_pos()):
                            lbreset("cat")
                            confirmationReset = True
                        if resetRandom_r.collidepoint(pygame.mouse.get_pos()):
                            lbreset("random")
                            confirmationReset = True
                # handles events in play
                elif page == "play":
                    if not(exit):                    
                        if freedom_r.collidepoint(pygame.mouse.get_pos()):
                            page = "freedomDive"
                            freedomReset()
                        if cat_r.collidepoint(pygame.mouse.get_pos()):
                            page = "catCafe"
                            catReset()
                        if random_r.collidepoint(pygame.mouse.get_pos()):
                            page = "random"
                            randomReset()
                        if backbtn_r.collidepoint(pygame.mouse.get_pos()):
                            page = "menu"
                # handles events in options
                elif page == "options" and not(confirmationReset):
                    if not(exit):                    
                        if backbtn_r.collidepoint(pygame.mouse.get_pos()):
                            page = "menu"
                        if down_r.collidepoint(pygame.mouse.get_pos()):
                            if current < 7:
                                current += 1
                            elif current == 7:
                                current = 0
                        elif up_r.collidepoint(pygame.mouse.get_pos()):
                            if current > 0:
                                current -= 1
                            elif current == 0:
                                current = 7
                        elif reset_r.collidepoint(pygame.mouse.get_pos()):
                            for mapping in maps:
                                lbreset(mapping)
                            confirmationReset = True
                        elif vol100_r.collidepoint(pygame.mouse.get_pos()):
                            fDive.set_volume(1)
                            cCafe.set_volume(1)
                            randomSound.set_volume(1)
                            meowEff.set_volume(1)
                            clickEff.set_volume(1)
                            meowEff.play()
                        elif vol75_r.collidepoint(pygame.mouse.get_pos()):
                            fDive.set_volume(0.75)
                            cCafe.set_volume(0.75)
                            randomSound.set_volume(0.75)
                            meowEff.set_volume(0.75)
                            clickEff.set_volume(0.75)
                            meowEff.play()
                        elif vol50_r.collidepoint(pygame.mouse.get_pos()):
                            fDive.set_volume(0.5)
                            cCafe.set_volume(0.5)
                            randomSound.set_volume(0.5)
                            meowEff.set_volume(0.5)
                            clickEff.set_volume(0.5)
                            meowEff.play()
                        elif vol25_r.collidepoint(pygame.mouse.get_pos()):
                            fDive.set_volume(0.25)
                            cCafe.set_volume(0.25)
                            randomSound.set_volume(0.25)
                            meowEff.set_volume(0.25)
                            clickEff.set_volume(0.25)
                            meowEff.play()
                        elif vol0_r.collidepoint(pygame.mouse.get_pos()):
                            fDive.set_volume(0)
                            cCafe.set_volume(0)
                            randomSound.set_volume(0)
                            meowEff.set_volume(0)
                            clickEff.set_volume(0)
                            meowEff.play()
                        elif off_r.collidepoint(pygame.mouse.get_pos()):
                            offBtn = False
                            hard = True
                        elif on_r.collidepoint(pygame.mouse.get_pos()):
                            offBtn = True
                            hard = False
                # handles events in rules
                elif page == "rules":
                    if not(exit):                    
                        if backbtn_r.collidepoint(pygame.mouse.get_pos()):
                            page = "menu"
                        if toOptions_r.collidepoint(pygame.mouse.get_pos()):
                            page = "options"
                # handles events in freedom dive game
                elif page == "freedomDive":
                    if not(exit):                    
                        if backbtn_r.collidepoint(pygame.mouse.get_pos()):
                            freedomReset()
                            fDive.stop()
                            page = "play"
                # handles events in Cat Cafe game
                elif page == "catCafe":
                    if not(exit):                    
                        if backbtn_r.collidepoint(pygame.mouse.get_pos()):
                            catReset()
                            cCafe.stop()
                            page = "play"
                # handles events in random game
                elif page == "random":
                    if not(exit):
                        if backbtn_r.collidepoint(pygame.mouse.get_pos()):
                            randomReset()
                            randomSound.stop()
                            page = "play"
                # handles events in end screen
                elif page == "endScreen":
                    if not(exit):                    
                        if backbtn_r.collidepoint(pygame.mouse.get_pos()):
                            page = "menu"
                            hardAlive = True
                        if play_r.collidepoint(pygame.mouse.get_pos()):
                            page = "play"
                # confirms a leaderboard reset
                elif confirmationReset:
                    if conX_r.collidepoint(pygame.mouse.get_pos()):
                        confirmationReset = False
            # checks notes for freedom dive and cat cafe
            if page == "freedomDive" or "catCafe" or "random":
                if ev.type == pygame.KEYDOWN:
                    if ev.key == K_d:
                        CheckNote(x1)
                    if ev.key == K_f:
                        CheckNote(x2) 
                    if ev.key == K_j:
                        CheckNote(x3)
                    if ev.key == K_k:
                        CheckNote(x4)
finally:
    pygame.quit()
