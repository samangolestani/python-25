import random
import matplotlib.pyplot as plt
import numpy as np
import csv
import os,csv,sys,time,random

def generate_maze(width, height):
    #  Create a grid filled with walls (1)
    maze = [[1 for _ in range(width)] for _ in range(height)]

    def carve_passages(x, y):
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)   #Randomize the directions to create a unique maze
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                maze[y + dy // 2][x + dx // 2] = 0   #Carve a passage (0)
                maze[ny][nx] = 0  # Carve the next cell (0)
                carve_passages(nx, ny)   #Recur to continue carving

    #  Start carving from the top-left corner
    maze[1][1] = 0
    maze[len(maze)-2][len(maze)-1] = 'B'  
    carve_passages(1, 1)

    return maze

def print_maze(maze):
    for row in maze:
        print(' '.join(map(str, row)))  # Print maze as numbers

def plot_maze(maze):
     #Convert maze to a numpy array for plotting
    maze_np = np.array(maze)
    plt.imshow(maze_np, cmap='gray_r')  # Use 'gray_r' to have wall as black and passage as white
    plt.axis('off')
    plt.show()

def save_maze_to_csv(maze, filename):
    with open(filename, mode='w', newline='') as maze_file:
        writer = csv.writer(maze_file)
        for row in maze:
            writer.writerow(row)
    print(f'Maze saved to {filename}')

#  Maze dimensions (width and height must be odd numbers)
width, height = 21, 21
size =  int(input("Please enter the size of n for n x n maze.(n should be odd)"))
while size%2 == 0:
    size = int(input("n should be odd!. Try again:"))
maze = generate_maze(size, size)
inp = input("enter file name:")
save_maze_to_csv(maze,inp)


def get_maze(inp):
    f = open(inp, 'r')
    reader = csv.reader(f)
    maze = []
    for line in reader:
        maze.append(line)
    return maze

def display_maze(m ,path):
    m2 = m[:]
    os.system('clear')

    for item in path:
        m2[item[0]][item[1]] = '.'
    
    m2[path[-1][0]][path[-1][1]] = 'm'

    draw = ""

    for row in m2: 
        for item in row:
            item = str(item).replace("1",bytes((219,)).decode('cp437'))
            item = str(item).replace("0", " ")
            item = str(item).replace("2", " ")

            draw += item
        draw += "\n"
    print(draw)

def move(path):
    time.sleep(0.1)
    cur = path[-1]
    display_maze(maze,path)
    possibles = [(cur[0],cur[1] +1) , (cur[0],cur[1] -1),
                 (cur[0] +1,cur[1]),(cur[0] -1,cur[1])]
    random.shuffle(possibles)

    for item in possibles:
        if item[0]<0 or item[1]<0 or item[0]>len(maze) or item[1] > len(maze[0]):
            continue
        elif maze[item[0]][item[1]] in ['1','2']:
            continue
        elif item in path:
            continue
        elif maze[item[0]][item[1]] == 'B':
            path = path + (item,)
            display_maze(maze,path)
            input("Solution found,press enter to leave!")
            os.system('clear')
            sys.exit()
        else:
            newpath = path + (item,)
            move(newpath)
            maze[item[0]][item[1]] = '2'
            display_maze(maze,path)
            time.sleep(0.2)

maze = get_maze(inp)
move(((1,0),))

