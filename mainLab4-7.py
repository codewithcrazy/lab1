import math

# 4-1
arr = [x for x in range(20)]
for i in arr:
    if (i % 9 == 0):
        continue
    else:
        print(i)
print()


# 4-2
def foo(x, N):
    y = 0.0
    multiply = 1

    for i in range(1, N+1):
        x = math.sin(x)
        multiply *= 2 * i
        y += x / multiply
    return y

print(foo(2.22, 4))
print()


# 5-1
n = [1.0, 0.3, 322.0, 102.2, 228.1, 148.8, -10.2, -0.2]
C = 40
quantityMoreC = 0
for x in n:
    if x > C:
        quantityMoreC += 1

maxIndex = 0
maxAbs = abs(n[0])

for i in range(1, len(n)):
    if abs(n[i]) > maxAbs:
        maxAbs = abs(n[i])
        maxIndex = i


result = 1
for x in n[maxIndex + 1:]:
    result *= x

print(quantityMoreC)
print(result)
print()


# 6-1
matrix = [
    [1, 2, 3, 4],
    [2, -2, -4, 4],
    [1, 0, 8, 8],
    [2, 3, 2, 2]
]

def firstZeroColumn(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(cols):
        for j in range(rows):
            if matrix[j][i] == 0:
                return i
    return None

def rowCharacteristic(row):
    return sum(x for x in row if x < 0 and x % 2 == 0)

def sortByCharacteristic(matrix):
    return sorted(matrix, key=rowCharacteristic, reverse=True)


sortedMatrix = sortByCharacteristic(matrix)

print(firstZeroColumn(matrix))
for row in sortedMatrix:
    print(row)
print()


# 7-1
words = ["abc", "cba", "amogus", "java", "death", "avaj"]
duplicateWords = words.copy()

result = []
for word in words:
    reverseWord = word[::-1]

    if reverseWord not in duplicateWords:
        result.append(reverseWord)

print([x[::-1] for x in result])