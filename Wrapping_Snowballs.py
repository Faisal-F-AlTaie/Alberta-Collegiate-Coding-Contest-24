import math

def wrapping_snowballs():
    # Read the radius of the snowball and the number of pieces of paper
    R_ball, N = map(int, input().split())
    
    # Iterate over each piece of paper
    for _ in range(N):
        R_i = int(input())  
        
        if R_i >= R_ball:
        
        
            max_covered_area = 2 * math.pi * R_ball**2
        else:
            # Calculate the height of the spherical cap
            h = R_ball - math.sqrt(R_ball**2 - R_i**2)
            
            # Calculate the surface area of the spherical cap
            max_covered_area = 2 * math.pi * R_ball * h
        
        # Print the maximum surface area covered, formatted to 12 decimal places
        print(f"{max_covered_area:.12f}")


wrapping_snowballs()
