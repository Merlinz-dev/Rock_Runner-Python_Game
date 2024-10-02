import pygame

pygame.init()
interface = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("RockRunner")
Bg = pygame.image.load('Background.PNG')

def GameOver():
    interface.blit(Bg, (0, 0))
    text = font.render('GameOver', 1, (0, 0, 0))
    text2 = font2.render('Press Enter To Runagain', 1, (0, 0, 0))
    interface.blit(text, (240, 200))
    interface.blit(text2, (200, 400))
    pygame.display.update()

font = pygame.font.SysFont('comicsans', 120, True)
font2 = pygame.font.SysFont('comicsans', 60, True)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] :
        import MainProgram
        MainProgram.main()
        pygame.quit()
    elif keys[pygame.K_ESCAPE] :
        pygame.quit()

    GameOver()

pygame.quit()

