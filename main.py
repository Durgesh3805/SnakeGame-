import pygame  #Importing pygame module
x=pygame.init() #Init. pygame 
gameWindow = pygame.display.set_mode((700,500)) 
pygame.display.set_caption("Flappy Bird")



exitGame= False
gameOver= False

# Creating game loop
while not exitGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitGame = True
        if event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_RIGHT:
                print("Pressed right arrow key")



        




pygame.quit()
print("Thank you for using")
quit()



