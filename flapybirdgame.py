import random
import pygame
import sys
from pygame.locals import *
FPS = 32
SCREENWIDTH = 327
SCREENHIEGHT = 500
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHIEGHT))
GAME_SOUNDS = {}
playerX=30

def welcomeScreen():
        """ this function is for only welcome screen """
        while True:
                for event in pygame.event.get():
                        if event.type  == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                                pygame.quit()
                                sys.exit()
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                                return

                        else:
                           SCREEN.blit(background, (0, 0))
                           SCREEN.blit(message, (30, 80))
                           pygame.display.update()
                           FPS_CLOCK.tick(FPS)


def getRandomPipe():
        offset=150
        pipeheight = (500-offset)/2
        upperpipeY = -(527-pipeheight)
        lowerpipeY = 500-pipeheight
        pipex=SCREENWIDTH+10
        y = random.randint(-pipeheight,pipeheight)
        upperpipeY = upperpipeY - y
        lowerpipeY = lowerpipeY - y
        pipe={"upperx":pipex,"uppery":upperpipeY,"lowerx":pipex,"lowery":lowerpipeY}
        return pipe

def maingame():
        newpipe1 = getRandomPipe()
        newpipe2 = getRandomPipe()
        upperpipeslist = [
                       {"x":SCREENWIDTH+200 , "y":newpipe1["uppery"] },
                       # {"x":SCREENWIDTH+400, "y":newpipe2["uppery"] }
                         ]
        lowerpipeslist = [
                {"x": SCREENWIDTH + 200, "y": newpipe1["lowery"]},
                # {"x": SCREENWIDTH + 400, "y": newpipe2["lowery"]}
        ]
        pipeVelX=-4
        playerVelY = -9
        playerMaxVelY = 10
        playerMinVelY = -8
        playerAccY = 1
        playerFlapAccv = -8
        playerFlapped=False
        playerY = 180

        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                                pygame.quit()
                                sys.exit()
                        if event.type == pygame.KEYDOWN and(event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                                if playerY > 0:
                                        playerVelY=playerFlapAccv
                                        playerFlapped = True
                                        # gamesound.play()


                # check for score
                # playerMidPos = playerX + player.get_width()/2
                # for pipe in upperpipeslist:
                #         pipeMidPos = pipe["x"] + upperpipe.get_width()/2
                #         if pipeMidPos <= playerMidPos < pipeMidPos+4:
                #                 score +=1
                #                 print(f"your score is {score}")
                #                 sound.play()
                if playerVelY <= playerMaxVelY and not playerFlapped:
                        playerVelY += playerAccY
                if playerFlapped:
                        playerFlapped=False
                playerHeight=player.get_height()
                playerY=playerY + min(playerVelY,SCREENHIEGHT-playerY-playerHeight)
                for Upipe , Lpipe in zip(upperpipeslist,lowerpipeslist):
                        Upipe["x"] += pipeVelX
                        Lpipe["x"] +=pipeVelX
                if 0<upperpipeslist[0]["x"]<5:
                        newpipe=getRandomPipe()
                        a={"x":newpipe["upperx"],"y":newpipe["uppery"]}
                        b={"x":newpipe["lowerx"],"y":newpipe["lowery"]}
                        upperpipeslist.append(a)
                        lowerpipeslist.append(b)
                if upperpipeslist[0]["x"] < -upperpipe.get_width():
                        upperpipeslist.pop(0)
                        lowerpipeslist.pop(0)
                SCREEN.blit(background, (0, 0))
                for Upipe, Lpipe in zip(upperpipeslist, lowerpipeslist):
                        SCREEN.blit(upperpipe,(Upipe["x"],Upipe["y"]))
                        SCREEN.blit(lowerpipe,(Lpipe["x"],Lpipe["y"]))
                SCREEN.blit(player, (playerX, playerY))
                pygame.display.update()
                FPS_CLOCK.tick(FPS)



if __name__ == '__main__':
        pygame.init()
        pygame.display.set_caption("flappy bird game")
        FPS_CLOCK = pygame.time.Clock()
        # game sprites
        player = pygame.image.load('gameimg/bee.png').convert_alpha()
        background = pygame.image.load('gameimg/background.jpg').convert()
        lowerpipe= pygame.transform.rotate(pygame.image.load('gameimg/pipe.png').convert_alpha(), 180)
        upperpipe = pygame.image.load('gameimg/pipe.png').convert_alpha()
        message = pygame.image.load('gameimg/message.png').convert_alpha()
        # run game
        welcomeScreen()
        maingame()




