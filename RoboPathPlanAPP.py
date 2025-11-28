import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def m(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def astar(grid, start, end):
    rows, cols = grid.shape
    open_set = []
    open_set.append((m(start, end), 0, start, [start]))
    visited = set()
    while open_set:
        open_set.sort()
        f, g, pos, path = open_set.pop(0)
        if pos == end:
            return path
        if pos in visited:
            continue
        visited.add(pos)
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = pos[0]+dx, pos[1]+dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx,ny] == 0 and (nx,ny) not in visited:
                open_set.append((g+1+m((nx,ny), end), g+1, (nx,ny), path+[(nx,ny)]))
    return None

def visualize(grid, path, start, end):
    colored = np.full(grid.shape, 'white', dtype='object')
    colored[grid == 1] = 'black'
    for x, y in path:
        colored[x, y] = 'red'
    colored[start] = 'green'
    colored[end] = 'blue'
    cmap = {'white': (1,1,1), 'black': (0,0,0), 'red': (1,0,0), 'green': (0,1,0), 'blue': (0,0,1)}
    rgb_grid = np.zeros(grid.shape + (3,))
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            rgb_grid[i, j] = cmap[colored[i, j]]
    plt.imshow(rgb_grid)
    plt.show()

def robot_path_planning():
    while True:
        rows = int(input("Grid rows: "))
        cols = int(input("Grid cols: "))
        grid = np.zeros((rows, cols), dtype=int)
        obs_count = int(input("Number of obstacles: "))
        for _ in range(obs_count):
            x, y = map(int, input("Obstacle position x y: ").split())
            grid[x, y] = 1
        sx, sy = map(int, input("Start position x y: ").split())
        ex, ey = map(int, input("End position x y: ").split())
        start, end = (sx, sy), (ex, ey)
        df = pd.DataFrame(grid)
        print(df)
        path = astar(grid, start, end)
        if path:
            print("Path found:", path)
            visualize(grid, path, start, end)
        else:
            print("No valid path found")
        if input("Try different positions? (y/n): ").lower() != 'y':
            break

robot_path_planning()