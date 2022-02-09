from tarfile import BLOCKSIZE
import pygame

SIZE = 800

WIN = pygame.display.set_mode((SIZE, SIZE))

BLOCK_PER_LINE = 40

BLOCK_SIZE = SIZE/BLOCK_PER_LINE

WHITE = (255,255,255)
BLACK = (0,0,0)

def draw_screen():
    WIN.fill(BLACK)

    for i in range(1, BLOCK_PER_LINE):
        line_y = pygame.Rect(i * BLOCK_SIZE, 0, 1, SIZE)
        pygame.draw.rect(WIN, WHITE, line_y)

        line_x = pygame.Rect(0, i * BLOCK_SIZE, SIZE, 1)
        pygame.draw.rect(WIN, WHITE, line_x)


def main ():
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                quit()
        draw_screen()
        pygame.display.update()

main()