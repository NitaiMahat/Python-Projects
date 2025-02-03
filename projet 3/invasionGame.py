'''
Alien Invasion Game

In this game, the player controls a spaceship to defeat waves of monsters,
earning points as they go. Each wave increases the speed of the monsters and changes it.
After a certain score, the game transitions to a boss fight, where the
spaceship is transported to a different dimension.
The boss moves diagonally and turns invisible at intervals.
The goal is to defeat the boss to win.

Includes:
- Story introduction before gameplay.
- Monster changes and the speed increase between waves.
- Final boss fight with unique movement and invisibility.
- Health point of the final boss is deducted upon collision and not deducted when invisibile
- Replay features where the starting story mode is skipped.
- Winning window with moving text which is dispalyed after player has won the game.

Assistance:
    I/Our pair gave and received no assistance on this project.

'''
from graphics2 import *
import time
import random
import math


monsterSpeed = 7
SPACESHIP_SPEED = 25
BOSS_STAGE = 10
NUM_WAVE = BOSS_STAGE//2
THRESHOLD = 50
BOSS_HEALTH = 3



def descriptionStartWindow():
    '''
    Displays a description window with game instructions and waits
    for user input to continue.
    '''
    descriptionWindow = GraphWin("Game Description", 550, 300)
    descriptionWindow.setBackground("grey")
    
    description = Text(Point(280, 150), 
                       "Welcome to the Game!\n\n"
                       "Click inside the window to start.\n\n"
                       "Use mouse clicks to move the spaceship.\n"
                       "DONE BY: Zain and Nitai"
                       )
    description.setSize(16)
    description.setStyle('bold')
    description.draw(descriptionWindow)
    
  
    descriptionWindow.getMouse()
    descriptionWindow.close()
    
def storyStartingWindow():
    '''
    Displays a starting window with game description and story
    and waits for user input to begin the game.
    '''
    startWindow = GraphWin("Welcome to the Game!", 550, 300)
    startWindow.setBackground("darkgreen")
    
    description = Text(Point(270, 150), 
                       "Aliens are attacking!\n"
                        f"Shoot aliens to score points. Reach {BOSS_STAGE} points\n"
                        f"to fight the big alien boss.\n {NUM_WAVE} points for new wave.\nSave Earth!"
                       )
    description.setSize(16)
    description.setStyle('bold')
    description.draw(startWindow)
    
  
    startWindow.getMouse()
    startWindow.close()

def distanceBetweenPoints(point1, point2):
    '''
    Calculates the distance between two points
    
    Params:
        point1 (Point): the first point
        point2 (Point): the second point
    
    Returns:
        float: the distance between the two points
    '''
    dx = point2.getX() - point1.getX()
    dy = point2.getY() - point1.getY()
    return math.sqrt(dx**2 + dy**2)


def isCloseEnough(spaceShipImg, monsterImg):
    '''
    Determines if the spaceShip is close enough to the monster to say the spaceShip
    caught the monster.
    
    Params:
        spaceShipImg (Image): the image of the spaceShip
        monsterImg (Image): the image of the monster
    
    Returns:
        bool: True if the spaceShip catches the monster else False
    '''
    spaceShipCenter = spaceShipImg.getCenter()
    monsterCenter = monsterImg.getCenter()
    distance = distanceBetweenPoints(spaceShipCenter, monsterCenter)
    if distance < THRESHOLD:
        return True
    else:
        return False
    
def isDamageCloseEnough(missileImg,monsterImg):
    '''
    Checks if a missile is close enough to a monster to hit it.

    Params:
        missileImg (Image): The missile's image.
        monsterImg (Image): The monster's image.

    Returns:
        bool: True if the missile is close enough to the monster else False
    '''
    missileImgCenter = missileImg.getCenter()
    monsterCenter = monsterImg.getCenter()
    distance = distanceBetweenPoints(missileImgCenter, monsterCenter)
    if distance < THRESHOLD:
        return True
    else:
        return False

def movemonsters(monsterImgList):
    '''
    Moves every monster one monsterSpeed unit down the window
    
    Params:
        monsterImgList (list): the list of falling monsters
    '''
    for monster in monsterImgList:
        monster.move(0, monsterSpeed)

    

def movespaceShip(window, spaceShipImg):
    '''
    Moves the spaceship based on the mouse click position relative to
    its current position.

    Params:
        window (GraphWin): The game window.
        spaceShipImg (Image): The spaceship's image.
    '''
    mouseClick = window.checkMouse()
    spaceShipCenterY = spaceShipImg.getCenter().getY()
    spaceShipHeight = spaceShipImg.getHeight()
    spaceShipHeadPoint = spaceShipCenterY - spaceShipHeight / 2
    spaceShipFootPoint = spaceShipCenterY + spaceShipHeight / 2
    
    if mouseClick != None  and spaceShipHeadPoint < mouseClick.getY() and spaceShipFootPoint > mouseClick.getY():
        if mouseClick.getX() < spaceShipImg.getCenter().getX()- THRESHOLD:
            spaceShipImg.move(-SPACESHIP_SPEED, 0)
        elif mouseClick.getX() > spaceShipImg.getCenter().getX() + THRESHOLD:
            spaceShipImg.move(SPACESHIP_SPEED, 0)
    
def movemissile(window, missileList, spaceShipImg):
    '''
    Fires a missile when space is pressed and moves all missiles upwards.

    Params:
        window (GraphWin): The game window.
        missileList (list): List of missile images.
        spaceShipImg (Image): The spaceship's image.
    '''
    
    keyPress = window.checkKey()
    if keyPress == 'space':
        missile = Image(Point(spaceShipImg.getCenter().getX(), spaceShipImg.getCenter().getY()), "damageBall.gif")
        missile.draw(window) 
        missileList.append(missile)
        
    # Moving missile
    for missile in missileList: 
        missile.move(0, -27)  
        if missile.getCenter().getY() < 0:  
            missile.undraw()  
            missileList.remove(missile)
        
              

def addmonsterToWindow(window,score):
    '''
    Adds a monster to a random x-position at the top of the window.

    Params:
        window (GraphWin): The game window.
        score (int): Current score.

    Returns:
        Image: The new monster's image.
    '''
    xPosition = random.randrange(40, 620)
    if score < NUM_WAVE:
        monster = Image(Point(xPosition, 0), 'Boss1.gif')
       
    else:
        monster = Image(Point(xPosition, 0), 'Boss2.gif')
    
 
        

    monster.draw(window)
    return monster

    

def scoreBox(window, score):
    '''
    Displays the current score on the game window.

    Params:
        window (GraphWin): The game window.
        score (int): Current score.

    Returns:
        Text: The score text object.
    '''
    scores = Text(Point(600, 20), f'Score: {score}')
    scores.setSize(16)
    scores.setTextColor("white")
    scores.draw(window)
    return scores


def handleMonsterOutWindow(monsterList, window, score, displayScore):
    
    """
        Lowers score and removes monsters that move off the bottom of the screen. 
        Updates displayed score.
        
        Parameters:
        - monsterList (list): Active monsters in the game.
        - window (GraphWin): Game display window.
        - score (int): Player's score.
        - displayScore (Text): Score display object.
        
        Returns:
        - tuple: Updated score (int) and displayScore (text).
    """
    for monster in monsterList:
        if monster.getCenter().getY() > window.getHeight():
            score -= 1
            monster.undraw()
            monsterList.remove(monster)
            displayScore.undraw()
            displayScore = scoreBox(window, score)
    return score, displayScore

def handleShipCollision(spaceShip, monsterList, window):
    """
    Checks for collisions between the player's spaceship and any active monsters.
    If a collision occurs, undraws all monsters, clears the list, closes the game window, 
    and ends the game with a game-over screen.
    
    Parameters:
    - spaceShip (Image): The player’s spaceship image object.
    - monsterList (list): A list of monster objects currently in the game.
    - window (GraphWin): The game window where all game elements are drawn.
    
    Returns:
    - bool: True if a collision occurs between the spaceship and a monster, ending the game;
            False if no collision occurs.
    """
    for monster in monsterList:
        if isCloseEnough(spaceShip, monster):
            for monster in monsterList:
                monster.undraw()
            monsterList.clear()
            window.close()
            endWindow()
            return True  # Collision occurred
    return False  # No collision

def handleMissileCollision(missileList, monsterList, score, displayScore, window):
    """
    Detects missile and monster collisions, increases score, and updates display.
    
    Parameters:
    - missileList (list): A list of missile objects currently in the game.
    - monsterList (list): A list of monster objects currently in the game.
    - score (int): The current score of the player, updated when a missile hits a monster.
    - displayScore (Text): The on-screen text object displaying the current score.
    - window (GraphWin): The game window where all game elements are drawn.
    
    Returns:
    - tuple: The updated score (int) and updated displayScore (Text) after missile-monster collisions.
    """
    for ball in missileList:
        for monster in monsterList:
            if isDamageCloseEnough(ball, monster):
                ball.undraw()
                monster.undraw()
                missileList.remove(ball)
                monsterList.remove(monster)
                score += 1
                displayScore.undraw()
                displayScore = scoreBox(window, score)
    return score, displayScore
    

def gameLoop(window, spaceShip, missile):
    """
    Controls the game flow: player moves, monster spawning, score tracking, 
    and stage progression. Switches to boss stage when score is high enough.
    
    Parameters:
    - window (GraphWin): The game window where all game elements are drawn.
    - spaceShip (Image): The player’s spaceship image object, initially positioned at the bottom of the window.
    - missile (Image): The initial missile object that the player controls to shoot at enemies.
    
    Returns:
    - int: The final score when the player reaches the boss stage.
    """
    global monsterSpeed
    monsterList = []
    missileList = []
    score = 0
    displayScore = scoreBox(window, score)
    wave2TransitionDone = False
    gameRunning = True  
    
    while gameRunning:
        if score < 0:
            window.close()
            endWindow()
            gameRunning = False
            
        
        if score >= NUM_WAVE and not wave2TransitionDone:
            monsterSpeed = 10
            for monster in monsterList:
                monster.undraw()
            monsterList.clear()
            
            wave2Text = Text(Point(333, 200), "Wave 2!")
            wave2Text.setSize(24)
            wave2Text.setTextColor("red")
            wave2Text.setStyle("bold")
            wave2Text.draw(window)
            
            time.sleep(1)
            wave2Text.undraw()
            wave2TransitionDone = True

        movespaceShip(window, spaceShip)
        movemissile(window, missileList, spaceShip)
        
        if random.randrange(100) < 5:
            monster = addmonsterToWindow(window, score)
            monsterList.append(monster)

        movemonsters(monsterList)

        # Handle collisions and updates
        score, displayScore = handleMonsterOutWindow(monsterList, window, score, displayScore)
        if handleShipCollision(spaceShip, monsterList, window):
            window.close()
            endWindow()
            gameRunning = False
            
            

        score, displayScore = handleMissileCollision(missileList, monsterList, score, displayScore, window)

        time.sleep(0.1)

        if score >= BOSS_STAGE:
            return score

        
def bossFight():
    
    """
    This function initializes a new window for the boss fight and manages boss movements, 
    spaceship controls, boss health, and invisibility mechanics. It includes player movement,
    missile attacks and handles game win and game over conditions.

    """
    bossWindow = GraphWin("Boss Fight", 666, 666)
    bossWindow.setBackground("black")

    background = Image(Point(333, 333), "backgroundImage2.gif")
    background.draw(bossWindow)
    time.sleep(0.5)
    currentBossHealth = BOSS_HEALTH
    
    currentBossHealthText = Text(Point(550, 20), f"Boss HP: {currentBossHealth}")
    currentBossHealthText.setSize(16)
    currentBossHealthText.setTextColor("white")
    currentBossHealthText.setStyle("bold")
    currentBossHealthText.draw(bossWindow)

    instructions = Text(Point(333, 20), "Kill Boss to Win!")
    instructions.setSize(16)
    instructions.setTextColor("red")
    instructions.setStyle("bold")
    instructions.draw(bossWindow)

   
    boss = Image(Point(333, 100), "FinalBoss.gif")
    boss.draw(bossWindow)
    bossInvisible = False
    
    
    

    spaceShip = Image(Point(333, 580), "MainShip.gif")
    spaceShip.draw(bossWindow)
    time.sleep(0.5)
    missileList = []

    # Horizontal movement  variables
    bossDirection = 1  
    bossSpeed = 4 
    bossXMin = 50  
    bossXMax = 600  

    while currentBossHealth > 0:
        # Boss vertical movement
        boss.move(0, 2)  

        # Boss horizontal movement
        currentX = boss.getCenter().getX()
        if currentX <= bossXMin or currentX >= bossXMax:
            bossDirection *= -1  # Reverse direction if boss hits boundaries
        boss.move(bossDirection * bossSpeed, 0)

       
        if isCloseEnough(spaceShip, boss):
          
            time.sleep(.5)
            boss.undraw()
            time.sleep(.5)
            spaceShip.undraw()
            time.sleep(.5)
            bossWindow.close()
            endWindow()
 
        
        if boss.getCenter().getY() > bossWindow.getHeight():
            
            time.sleep(1)
            boss.undraw()
            spaceShip.undraw()
            time.sleep(1)
            bossWindow.close()
            endWindow()

        
        if random.randrange(100) <10:
            bossInvisible = not bossInvisible
            if bossInvisible:
                boss.undraw()
            else:
                boss.draw(bossWindow)

        
        movespaceShip(bossWindow, spaceShip)
        movemissile(bossWindow, missileList, spaceShip)

       
        if not bossInvisible:
            for ball in missileList:
                if isDamageCloseEnough(ball, boss):
                    ball.undraw()
                    missileList.remove(ball)
                    currentBossHealth -= 1
                    currentBossHealthText.setText(f"Boss HP: {currentBossHealth}")

       
        if currentBossHealth == 0:
            boss.undraw()
            winText = Text(Point(333, 333), "You Win!")
            winText.setSize(32)
            winText.setTextColor("green")
            winText.setStyle("bold")
            winText.draw(bossWindow)
            time.sleep(1)
            bossWindow.close()
            winWindow()
            

        time.sleep(0.05)


def winWindow():
    '''
    Displays the end game screen  when players win and displays a moving text and images of the characters of the game.
    '''
    
    window = GraphWin("Winner", 600, 600)
    window.setBackground("white")

    
    background = Image(Point(333, 333), "GameWinBack.gif")
    background.draw(window)

    time.sleep(1)
    spaceShip = Image(Point(300, 444), "MainShip.gif")
    spaceShip.draw(window)
    time.sleep(.5)
    boss = Image(Point(200, 333), "FinalBoss.gif")
    boss.draw(window)
    time.sleep(.5)
    monsterWave1 = Image(Point(300, 333), 'Boss1.gif')
    monsterWave1.draw(window)
    time.sleep(.5)
    monsterWave2 = Image(Point(400, 333), 'Boss2.gif')
    monsterWave2.draw(window)
    time.sleep(.5)

   
    text = Text(Point(300, -50), "After a fierce battle, you defeated the aliens and saved Earth.\nWell done, Captain!.")
    text.setSize(14)
    text.setStyle("bold")
    text.setTextColor("black")
    text.draw(window)

    
    for i in range(13):  
        text.move(0, 20) 
        time.sleep(0.1)  

    
    time.sleep(3)
    window.close()  
    
    
    
def endWindow():
    '''
    Displays the end game when player looses screen and allows the player to exit the game by closing the window or replay the game.
    '''
    newWindow = GraphWin("Game Over", 550, 300)
    newWindow.setBackground("darkgreen")
    
    desc = Text(Point(270, 150), 
                "Game over, you lose! :(\n"
                "Click the window and Press 'R' to play again\n or\n any other key to exit."
               )
    desc.setSize(16)
    desc.setStyle('bold')
    desc.draw(newWindow)
    
    keyPressWindow = newWindow.getKey()
    if keyPressWindow.lower() == 'r':  
        newWindow.close()
        main(skipIntro = True) 
    else:
        exit(-1)


def main(skipIntro=False):
    """
    This function initializes the game window, spaceship, and background. It starts the game loop 
    and upon reaching the required score, closes the main game and initiates the boss fight.
  
    Parameters:
    - skipIntro (bool): If True, bypasses the description and story start windows for a quicker game restart.

    """
    if not skipIntro:
        descriptionStartWindow()
        storyStartingWindow()

    window = GraphWin("Alien Invasion!!!", 666, 666)
    window.setBackground("white")
    background = Image(Point(333, 333), "backgroundImagestart.gif")
    background.draw(window)

    spaceShip = Image(Point(333, 580), "MainShip.gif")
    spaceShip.draw(window)
    
    missile = Image(Point(333, 333), "damageBall.gif")

    
    score = gameLoop(window, spaceShip, missile)

    
    if score >= BOSS_STAGE:
        window.close()  
        bossFight()  


main()
