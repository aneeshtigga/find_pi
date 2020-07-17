import random

def find_pi(n):
    points_in_circle = 0
    points_in_total = 0
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1:
            points_in_circle += 1
        points_in_total += 1
    return 4*points_in_circle/points_in_total

#master branch