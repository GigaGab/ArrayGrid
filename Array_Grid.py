import pygame

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# SIZES
WIDTH = 20
HEIGHT = 20
MARGIN = 5
CELLS = 10

# CREATE 2D ARRAY
grid = []

for row in range(CELLS):
    grid.append([])
    for column in range(CELLS):
        grid[row].append(0)
grid[1][5] = 1

# WINDOW
pygame.init()
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("ARRAY GRID")
done = False
clock = pygame.time.Clock()

# LOOP
while not done:
    for event in pygame.event.get():
        # close window check
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            grid[row][column] = 1
            print("Clock", pos, "Grid Coordinates: ", row, column)

    # screen
    screen.fill(BLACK)
    # draw grid
    for row in range(CELLS):
        for column in range(CELLS):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN,
                                             (MARGIN + HEIGHT) * row + MARGIN,
                                             WIDTH, HEIGHT])

    # set frame
    clock.tick(60)
    pygame.display.flip()
# QUIT PYGAME
pygame.quit()
