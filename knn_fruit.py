"""
(fruit, weight, textureScore) -> record format

0 -> oranage
1 -> Guava

"""
from collections import Counter

records = [(0, 150, 3), (0, 170, 4), (1, 250, 8), (1, 230, 7)]

k = 3

distance = []

def euclideanDistance(newWeight, newTextureScore):
    """
    ((x-xi)^2 + (y-yi)^2)^1/2

    """
    for i in records:
        p = ((newWeight - i[1])**2 + (newTextureScore - i[2])**2)**0.5
        distance.append((i[0], p))

    for i in distance:
        print(i)

euclideanDistance(210, 6)

# Sort
for i in range(0, len(records)):
    for j in range(0, len(records)-i-1):
        x = distance[j]
        y = distance[j+1]
        if x[1] > y[1]:
            distance[j] = y
            distance[j+1] = x

print("Sorted Distance:")
for i in distance:
    print(i)

nearestElements = []

for i in range(0, k):
    p =  distance[i]
    nearestElements.append(p[0])

print(f"{k} most Nearest elements: {nearestElements}")

c = Counter(nearestElements)

print("Result:", c.most_common(1)[0][0])