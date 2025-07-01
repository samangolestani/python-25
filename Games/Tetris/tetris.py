import pygame
import random

# Initialize constant
WIDTH, HEIGHT, =300, 600
TILE_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = WIDTH // TILE_SIZE, HEIGHT // TILE_SIZE

# Colors

BLACK = (0,0,0)
WHITE = (255,255,255)
COLORS = [
    (0,255,255), # Cyan
    (255, 165, 0), # Orange
    (0,255,0), # Green
    (255,255,0), # Yellow
    (128,0,128), #Purple
    (255,0,0), # Red
    (0,0,255) # Blue
]

SHAPES = [
    [[1,1,1],[0,1,0]], # T-shape
    [[1,1],[1,1]], # O-shape
    [[1,1,1,1]], # I-shape
    [[0,1,1], [1,1,0]], # S-shape
    [[1,1,0], [0,1,1]], # Z-shape
    [[1,1,1],[1,0,0]], # L-shape
    [[1,1,1], [0,0,1]] # J-shape
]

def create_grid():
    return [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

def draw_grid(surface, grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x]:
                pygame.draw.rect(surface, COLORS[grid[y][x] -1],(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE,TILE_SIZE))
                
def draw_shape(surface, shape, position):
    for y, row in enumerate(shape):
        for x, value in enumerate(row):
            if value:
                rect_x = (position[0]+x)* TILE_SIZE
                rect_y = (position[1]+y)*TILE_SIZE
                if rect_x>=0 and rect_y>=0:
                    pygame.draw.rect(surface, COLORS[value-1], (rect_x,rect_y ,TILE_SIZE,TILE_SIZE))
                
def check_collision(grid, shape, offset):
    for y, row in enumerate(shape):
        for x, value in enumerate(row):
            if value:
                grid_x = x+ offset[0]
                grid_y = y+ offset[1]
                if grid_x< 0 or grid_x>= GRID_WIDTH or grid_y>= GRID_HEIGHT or (grid_y>=0 and grid[grid_y][grid_x]):
                    return True
    return False
def merge_shape(grid, shape,position):
    for y, row in enumerate(shape):
        for x, value in enumerate(row):
            if value:
                grid[y+position[1]][x+position[0]] = value

def clear_lines(grid):
    lines_to_clear = 0
    for y in range(GRID_HEIGHT):
        if all(grid[y]):
            lines_to_clear +=1
            del grid[y]
            grid.insert(0,[0 for _ in range(GRID_WIDTH)])
    return lines_to_clear

def main():
    pygame.init()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    grid = create_grid()
    score = 0

    current_shape = random.choice(SHAPES)
    current_color = random.randint(1, len(COLORS))
    shape_position = [GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0]

    while True:
        surface.fill(BLACK)
        draw_grid(surface, grid)
        draw_shape(surface,current_shape,shape_position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    shape_position[0] -= 1
                    if check_collision(grid,current_shape,shape_position):
                        shape_position[0] += 1
                if event.key == pygame.K_RIGHT:
                    shape_position[0] += 1
                    if check_collision(grid,current_shape,shape_position):
                        shape_position[0] -= 1
                if event.key == pygame.K_DOWN:
                    shape_position[1] += 1
                    if check_collision(grid,current_shape,shape_position):
                        shape_position[1] -= 1
                if event.key == pygame.K_UP:
                    current_shape = [[current_shape[y][x] for y in range(len(current_shape))] for x in range(len(current_shape[0])-1,-1,-1)]
                    if check_collision(grid, current_shape,shape_position):
                        current_shape = [[current_shape[y][x] for y in range(len(current_shape) -1 , -1,-1)] for x in range(len(current_shape[0]))]
        shape_position[1] += 1
        if check_collision(grid,current_shape,shape_position):
            shape_position[1] -= 1
            merge_shape(grid,current_shape,shape_position)
            score += clear_lines(grid)
            current_shape = random.choice(SHAPES)
            current_color = random.randint(1,len(COLORS))
            shape_position = [GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0]
            if check_collision(grid,current_shape,shape_position):
                pygame.quit()
                return
            
        draw_grid(surface,grid)
        pygame.display.flip()
        clock.tick(4)

if __name__ == "__main__":
    main()