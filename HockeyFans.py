def max_decibel(N, S, M, decibels):
    
    def can_boo(d):
        count, current_length = 0, 0
        
        for i in range(N):
            
            if decibels[i] >= d:
                current_length += 1
                if current_length == S:
                    count += 1
                    current_length = 0
            else:
                current_length = 0
        
        return count >= M

    low, high = 0, max(decibels)
    
    while low < high:
        mid = (low + high + 1) // 2
       
        if can_boo(mid):
            low = mid
        else:
            high = mid - 1
    
    return low

N, S, M = map(int, input().split())

decibels = list(map(int, input().split()))

print(max_decibel(N, S, M, decibels))



