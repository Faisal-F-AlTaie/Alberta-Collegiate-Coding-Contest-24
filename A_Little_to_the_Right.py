# We Got 24.50 as our answer rather than 46.666... as the correct answer

import heapq

def dijkstra(n, m, heights, boosts):
    
    directions = [(-1, 0, 100), (1, 0, 100), (0, -1, 100), (0, 1, 100),
                  (-1, -1, 150), (-1, 1, 150), (1, -1, 150), (1, 1, 150)]
    
    
    pq = [(0, 0, 0)]  # (time, x, y)
    dist = [[float('inf')] * m for _ in range(n)]
    dist[0][0] = 0


    boost_map = {}
    for r1, c1, r2, c2, s in boosts:
        
        if (r1, c1) not in boost_map:
            boost_map[(r1, c1)] = []
        boost_map[(r1, c1)].append((r2, c2, s))


    while pq:
        time, x, y = heapq.heappop(pq)
        
        if (x, y) == (n - 1, m - 1):
            return time
        
        if time > dist[x][y]:
            continue


        for dx, dy, distance in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                
                if heights[nx][ny] > heights[x][y]:
                    travel_time = (heights[nx][ny] - heights[x][y]) / 10.0
                else:
                    travel_time = 1.0

                new_time = time + travel_time * (distance / 10.0)
                
                if new_time < dist[nx][ny]:
                    dist[nx][ny] = new_time
                    heapq.heappush(pq, (new_time, nx, ny))


        if (x, y) in boost_map:
            for r2, c2, boost_time in boost_map[(x, y)]:
                new_time = time + boost_time
                if new_time < dist[r2][c2]:
                    dist[r2][c2] = new_time
                    heapq.heappush(pq, (new_time, r2, c2))

    return dist[n - 1][m - 1]

n, m = map(int, input().split())

heights = [list(map(int, input().split())) for _ in range(n)]

b = int(input())

boosts = [tuple(map(int, input().split())) for _ in range(b)]

result = dijkstra(n, m, heights, boosts)

print(f"{result:.10f}")
