import heapq

def dijkstra(grid, n, m, boost_tracks):
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    distances = [[float('inf')] * m for _ in range(n)]
    distances[0][0] = 0
    pq = [(0, 0, 0)]
    
    while pq:
        current_time, x, y = heapq.heappop(pq)
        
        if (x, y) == (n-1, m-1):
            return current_time
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                height_diff = grid[nx][ny] - grid[x][y]
                travel_time = 1
                
                if height_diff > 0:
                    travel_time += height_diff
                else:
                    travel_time += 0.5 * abs(height_diff)
                
                if (x, y, nx, ny) in boost_tracks or (nx, ny, x, y) in boost_tracks:
                    travel_time /= 2
                
                if current_time + travel_time < distances[nx][ny]:
                    distances[nx][ny] = current_time + travel_time
                    heapq.heappush(pq, (distances[nx][ny], nx, ny))
    
    return -1

def solve_speedy_slopes():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    b = int(input())
    boost_tracks = set()
    
    for i in range(b):
        r1, c1, r2, c2 = map(int, input().split())
        boost_tracks.add((r1, c1, r2, c2))
        boost_tracks.add((r2, c2, r1, c1))

    result = dijkstra(grid, n, m, boost_tracks)
    print(f"{result:.10f}")

# Example usage:
# solve_speedy_slopes()
