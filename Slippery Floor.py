from collections import deque

def slippery_floor(width, height, start_x, start_y, obstacles):
    if start_x == 0 or start_y == 0 or start_x == width - 1 or start_y == height - 1:
        return 0

    grid = [[0] * width for i in range(height)]
    for ox, oy in obstacles:
        grid[oy][ox] = 1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque()
    visited = set()

    for i in range(4):
        queue.append((start_x, start_y, i, 0))
        visited.add((start_x, start_y, i))
    
    while queue:
        x, y, direction, obstacles_hit = queue.popleft()
        dx, dy = directions[direction]
        
        while True:
            new_x, new_y = x + dx, y + dy

            if new_x < 0 or new_y < 0 or new_x >= width or new_y >= height:
                return obstacles_hit

            if grid[new_y][new_x] == 1:
                
                for i in range(4):
                    if i != direction and (new_x, new_y, i) not in visited:
                        visited.add((new_x, new_y, i))
                        queue.append((new_x, new_y, i, obstacles_hit + 1))
                break

            x, y = new_x, new_y

    return "IMPOSSIBLE"