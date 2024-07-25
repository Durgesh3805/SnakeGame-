import pygame ,random

pygame.init()


#Colors
white =(255,255,255)
red =(255,0,0)
black =(0,0,0)

#Dimentions and variables


exitGame =False
gameOver =False
snakeX=45
snakeY=55
size=10
fps =30
velocityX =0;
velocityY=0;
screenWidth=900
screenHeight=500
foodX=random.randint(0,int(screenWidth/1.5))
foodY =random.randint(0,int(screenHeight/1.5))


score = 0



clock =pygame.time.Clock()



pygame.display.set_caption("Snake Game")
gameWindow=pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.update()

  

while not exitGame:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            exitGame = True
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT:
                velocityX =5
                velocityY =0
            if event.key == pygame.K_LEFT:
                velocityX = -5
                velocityY =0

            if event.key == pygame.K_UP:
                velocityY =-5
                velocityX =0

            if event.key == pygame.K_DOWN:
                velocityY =+5
                velocityX =0

    snakeX +=velocityX
    snakeY +=velocityY
    if abs(snakeX -foodX) <6 and abs(snakeY-foodY)<6:
        score +=1
        print(f"Score :{score}")
        foodX=random.randint(0,int(screenWidth/1.5))
        foodY =random.randint(0,int(screenHeight/1.5))



    gameWindow.fill(white)
    
    pygame.draw.rect(gameWindow,red,[foodX ,foodY,size,size])
    pygame.draw.rect(gameWindow,black,[snakeX ,snakeY,size,size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()




