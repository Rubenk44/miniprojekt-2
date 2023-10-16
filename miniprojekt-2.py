import pygame
import random

Width, Height = 600, 600
Tile_Size = 30
Rows = Height // Tile_Size
Cols = Width // Tile_Size
color_white = (255, 255, 255)
color_black = (0, 0, 0)
#andreas anbefaler manuelt map (manuel array hvor der er forskelligt terrain)
def draw_grid():
    for row in range(Rows):
        for col in range(Cols):
            rect = pygame.Rect(col * Tile_Size, row * Tile_Size, Tile_Size, Tile_Size)
            pygame.draw.rect(screen, color_black, rect, width=1)
#manuelt map Procedural Generation
def cost_grid():
    box_list = []
    for row in range(Rows):
        row_values = []
        for col in range(Cols):
            value = random.choice([0, 1])
            row_values.append(value)
        box_list.append(row_values)
    return box_list

def Gen_Goal_Pos():
    goal_positions = [[0] * Cols for _ in range(Rows)]
    goal_row, goal_col = random.randint(0, Rows-1), random.randint(0, Cols-1)
    goal_positions[goal_row][goal_col] = 1
    return goal_positions

def Gen_Goal_Rect(goal_positions):
    for row in range(Rows):
        for col in range(Cols):
            if goal_positions[row][col] == 1:
                rect = pygame.Rect(col * Tile_Size, row * Tile_Size, Tile_Size, Tile_Size)
                pygame.draw.rect(screen, (0, 255, 0), rect)

def gen_startpos():
    start_pos = (random.randint(0, Rows-1), random.randint(0, Cols-1))
    return start_pos

def Draw_Start_Rect(start_pos):
    rect = pygame.Rect(start_pos[1] * Tile_Size, start_pos[0] * Tile_Size, Tile_Size, Tile_Size)
    pygame.draw.rect(screen, (255, 0, 0), rect)

def main_function():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption("Grid Example")

    # Generate goal and start positions
    goal_positions = Gen_Goal_Pos()
    start_pos = gen_startpos()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(color_white)
        draw_grid()

        # Draw goal and start rectangles
        Gen_Goal_Rect(goal_positions)
        Draw_Start_Rect(start_pos)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main_function()
