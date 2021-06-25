import pygame
pygame.init()


width = 1600
height = 800
yellow = (252, 186, 3)
clock =  pygame.time.Clock()

def run_game_loop():
    while True:

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return
        
        game_window = pygame.display.set_mode((width,height))
        game_window.fill(yellow)
        pygame.display.update()

        clock.tick(60)


run_game_loop()

pygame.quit()
quit()