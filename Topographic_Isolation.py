def find_topographic_isolation(n, heights):
    result = [0] * n
    left_higher = [float('inf')] * n
    right_higher = [float('inf')] * n

    stack = []
    
    for i in range(n):
        while stack and heights[stack[-1]] < heights[i]:
            stack.pop()
        if stack:
            left_higher[i] = i - stack[-1]
        stack.append(i)


    stack = []
    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] < heights[i]:
            stack.pop()
        if stack:
            right_higher[i] = stack[-1] - i
        stack.append(i)


    for i in range(1, n - 1):
        if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
            min_distance = min(left_higher[i], right_higher[i])
            if min_distance == float('inf'):
                result[i] = -1
            else:
                result[i] = min_distance
                

    return result

n = int(input())
heights = list(map(int, input().split()))
result = find_topographic_isolation(n, heights)
print(" ".join(map(str, result)))
