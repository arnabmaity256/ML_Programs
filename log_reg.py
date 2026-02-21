import math


def sigmoid(z):
    return ( 1 / (1 + math.exp(-z)))

def model(hours):
    return (2* hours - 64)

# Question 1
print("Question 1")

z = model(33)

print(f"z: {z}")

probOfPass = sigmoid(z)

print(f"Probability of Pass: {probOfPass}")

# Question 2

print("Question 2")

probOfPass = 0.95

z = - math.log((1-probOfPass) / probOfPass )


hours = (z + 64) / 2

print(f"Minimum Study hours: {hours}")