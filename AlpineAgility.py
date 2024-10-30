# One of our test cases was returning "TOO SLOW", rather than the correct answer of 10

from heapq import heappop, heappush

def alpine_agility(n, m, heights):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1), (-1, -1), (1, 1)]
    visited = [[False] * m for _ in range(n)]
    heap = [(-10, 0, 0)]  
    visited[0][0] = True

    while heap:
        speed, x, y = heappop(heap)
        speed = -speed
        
        if x == n - 1 and y == m - 1:
            return speed

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
           
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                height_diff = heights[nx][ny] - heights[x][y]
                new_speed = speed
                
                if height_diff < 0:
                     # Gains 1 m/s when going downhill
                    new_speed += 1 
                    # Speed remains the same on flat ground
                elif height_diff == 0:
                    pass  
                else:
                    
                    if height_diff <= 10:
                         # Loses 10 m/s for small uphill climbs
                        new_speed -= 10 
                    else:
                         # Loses 20 m/s for large uphill climbs
                        new_speed -= 20 
                
                if new_speed > 0:
                    visited[nx][ny] = True
                    
                    heappush(heap, (-new_speed, nx, ny))
                    

    return "TOO SLOW"

n, m = map(int, input().split())

heights = [list(map(int, input().split())) for _ in range(n)]

print(alpine_agility(n, m, heights))
