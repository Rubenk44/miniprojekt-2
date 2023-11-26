import pygame
import random
from queue import Queue
#Konstanter
screen_widt, screen_height = 630, 630
tile_size = 30
#hardcoded map :)
grid = [
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],    
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]     
        ]

#det laver gamevinduet.
pygame.init()
screen = pygame.display.set_mode((screen_widt, screen_height))
pygame.display.set_caption("Griddy")

class Map:
    def __init__(self, grid, tile_size):
        self.tile_size = tile_size
        self.grid = grid

    def draw_grid(self, screen):
        #farverne der benyttes
        white, black = ((255,255,255)), ((0,0,0))
        
        #finder længden af collonerne og rækkerne og tagner en firkart som er hvid eller 0 baseret på om det er 1 eller 0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                color = (white)  
                if self.grid[row][col] == 1:
                    color = (black) 

                #tager størrelsen for gridslottet og ganger det på rækken og collonen for derefter at tegne den med disse informationer
                rect_x = col * self.tile_size
                rect_y = row * self.tile_size
                pygame.draw.rect(screen, color, (rect_x, rect_y, self.tile_size, self.tile_size))

    def gen_position_avoiding_1(self):
        #len() bruges til at finde længden af collonerne & rækkerne
        rows = len(self.grid)
        cols = len(self.grid[0])
        #her bruges Random modulet til at vælge en tilfældig gridslot baseret på længden af Rows og cols. -1 fordi sidste tal i rækken
        row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        while self.grid[row][col] == 1:
            row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        return row, col
    
    def generate_start_end(self):
        #her vælger den den collonne og række start og slut
        start_row, start_col = self.gen_position_avoiding_1()
        end_row, end_col = self.gen_position_avoiding_1()
        #dette loop sikre sig at start og slut ikke er i det samme slot.
        while (end_row, end_col) == (start_row, start_col):
            end_row, end_col = self.gen_position_avoiding_1()

        return (start_row, start_col), (end_row, end_col)
   
    def draw_start(self, screen, start_row, start_col):
        #her generes start firkanten med farven grøn
        green = (0,255,0)
        #beregner der hvor den skal baseret på tile sizen og det slot der er blevet generet.
        rect_x = start_col * self.tile_size
        rect_y = start_row * self.tile_size
        pygame.draw.rect(screen, green, (rect_x, rect_y, self.tile_size, self.tile_size))
        
    def draw_end(self, screen, end_row, end_col):
        #her tegnes målets firkant i rød
        red = (255,0,0)
        #beregner det samme som ved start.
        rect_x = end_col * self.tile_size
        rect_y = end_row * self.tile_size
        pygame.draw.rect(screen, red, (rect_x, rect_y, self.tile_size, self.tile_size))

class BFSPath:
    def __init__(self):
        pass

    # laver breadth-first search til at finde vejen fra start til slut
    def bfs(self, grid, start, goal):
        def neighbors(cell):
            #Finder nabogridsslots der er valide 
            row, col = cell
            movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            result = []
            for dr, dc in movements:
                new_row, new_col = row + dr, col + dc
                #Tjekker om den nye celle er inden for gridets grænser og om det er en gyldig vej derefter smider den det ind i variablen results
                if (
                    0 <= new_row < len(grid)
                    and 0 <= new_col < len(grid[0])
                    and grid[new_row][new_col] != 1
                ):
                    result.append((new_row, new_col))
            return result

        frontier = Queue()
        frontier.put(start)
        came_from = {}
        came_from[start] = None

        #her tjekke den griddet ud indtil målet er fundet
        while not frontier.empty():
            current = frontier.get()
            if current == goal:
                break

            # finder nabogridslotne og updater path informationen
            for next_cell in neighbors(current):
                if next_cell not in came_from:
                    frontier.put(next_cell)
                    came_from[next_cell] = current

        return came_from

    # Rekonstruer stien fra start til mål path informationen
    def reconstruct_path(self, start, goal, came_from):
        path = []
        current = goal
        if goal not in came_from:
            return []

        # Rekonstruer stien bagfra så fra målet til start
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()
        return path


def main():
    running = True
    game_map = Map(grid, tile_size)

    start_pos, end_pos = game_map.generate_start_end()

    bfs_path = BFSPath()  # Create an instance of BFSPath
    came_from = bfs_path.bfs(game_map.grid, start_pos, end_pos)  # Use the instance method to perform BFS
    path = bfs_path.reconstruct_path(start_pos, end_pos, came_from)  # Use the instance method to reconstruct the path

    scaled_path = [(y * tile_size + tile_size // 2, x * tile_size + tile_size // 2) for x, y in path]
    game_map.draw_grid(screen)
    game_map.draw_start(screen, *start_pos)
    game_map.draw_end(screen, *end_pos)

    for i in range(len(scaled_path) - 1):
        pygame.draw.line(screen, (0, 0, 255), scaled_path[i], scaled_path[i + 1], 4)
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
