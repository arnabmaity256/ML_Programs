"""
(Species, Sepal Length, Sepal Width) -> record format

0 -> Set
1 -> Vir
2 -> Ver

"""
from collections import Counter

records = [(0, 5.3, 3.7), (0, 5.1, 3.8), (1, 7.2, 3.0), (0, 5.4, 3.4), (0, 5.1, 3.3), (0, 5.4, 3.9), (1, 7.4, 2.8), (2, 6.1, 2.8), (1, 7.3, 2.9), (2, 6.0, 2.7), (1, 5.8, 2.8), (2, 6.3, 2.3), (2, 5.1, 2.5), (2, 6.3, 2.5), (3, 5.5, 2.4) ]

k = 5

distance = []

def euclideanDistance(newSepalLength, newSepalWidth):
    """
    ((x-xi)^2 + (y-yi)^2)^1/2

    """
    for i in records:
        p = ((newSepalLength - i[1])**2 + (newSepalWidth - i[2])**2)**0.5
        distance.append((i[0], p))

    for i in distance:
        print(i)

euclideanDistance(5.2, 3.1)

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