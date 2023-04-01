import pygame
import random

# Initialize font
pygame.font.init()

WIN = pygame.display.set_mode((800, 800))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)

def create_board():
    # Create board
    board = []
    count = 0
    random_numbers = random.sample(range(0, 99), 10)
    for i in range(10):
        board.append([])
        for j in range(10):
            count += 1
            if count in random_numbers:
                board[i].append(11)
            else:
                board[i].append(10)
    return board

def draw_lines():
    # Draw lines
    for i in range(0, 800, 80):
        pygame.draw.line(WIN, BLACK, (i, 0), (i, 800))
        pygame.draw.line(WIN, BLACK, (0, i), (800, i))

def draw_squares(board):
    # Draw squares
    for i in range(10):
        for j in range(10):
            if board[i][j] == 10:
                pygame.draw.rect(WIN, GREY, (i * 80 + 1, j * 80 + 1, 79, 79))
            elif board[i][j] == 11:
                pygame.draw.rect(WIN, GREY, (i * 80 + 1, j * 80 + 1, 79, 79))
            # elif board[i][j] == 12:
            #     pygame.draw.circle(WIN, GREEN, (i * 80 + 40, j * 80 + 40), 30)
            elif board[i][j] == 13:
                pygame.draw.circle(WIN, RED, (i * 80 + 40, j * 80 + 40), 30)
            else:
                font = pygame.font.SysFont('times', 80)
                text = font.render(str(board[i][j]), 1, BLACK)
                WIN.blit(text, (i * 80 + 20, j * 80 + 10))

def calculate_bombs(board, x, y):
    # Calculate bombs
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i >= 0 and i < 10 and j >= 0 and j < 10:
                if board[i][j] == 11:
                    count += 1
    return count



def main():
    # 10 not pressed OK square
    # 11 not pressed bomb square
    # 12 pressed OK square
    # 13 pressed bomb square

    board = create_board()
    real_board = board
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_pos, y_pos = pygame.mouse.get_pos()
                x_pos = x_pos // 80
                y_pos = y_pos // 80
                if board[x_pos][y_pos] == 10:
                    board[x_pos][y_pos] = calculate_bombs(board, x_pos, y_pos)
                elif board[x_pos][y_pos] == 11:
                    board[x_pos][y_pos] = 13
                    print('Game over')
        WIN.fill(WHITE)
        draw_lines()
        draw_squares(board)
        pygame.display.update()

if __name__ == '__main__':
    main()