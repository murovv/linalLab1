#по определению, размер матрицы не может быть 0!!!
def sum(a, b):
    if a == 0 or b == 0:
        return 0
    if (len(a) != len(b)):
        return 0
    if (len(a[0]) != len(b[0])):
        return 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] += int(b[i][j])
    return a


def multNum(n, a):
    if a == 0:
        return 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = n*a[i][j]
    return a
def transpose(a):
    if (a == 0):
        return 0
    height = len(a)
    width = len(a[0])
    b = [[0 for i in range(height)] for j in range(width)]
    for i in range(height):
        for j in range(width):
            b[j][i] = a[i][j]
    return b


def multMatrix(a, b):
    if (a == 0 or b == 0):
        return 0
    b = transpose(b)
    c = []
    if (len(a[0]) != len(b[0])):
        return 0
    for i in range(len(a)):
        line = []
        for j in range(len(b)):
            el = 0
            for k in range(len(a[i])):
                el = el + int(a[i][k]) * int(b[j][k])
            line.append(el)
        c.append(line)
    return c
inputFile = open("input.txt", "r")
outputFile = open("output.txt", "w")
line = inputFile.readline().split()
alpha = int(line[0])
beta = int(line[1])
matrixes = [[[]] for i in range(5)]
for k in range(5):
    sizes = inputFile.readline().split()
    n = int(sizes[0])
    m = int(sizes[1])
    matrixes[k] = [[0 for t in range(m)] for s in range(n)]
    line = inputFile.readline().split()
    for i in range(n * m):
        matrixes[k][i // m][i % m] = int(line[i])
x = sum(multNum(alpha, matrixes[0]),multNum(beta,transpose(matrixes[1])))
x = multMatrix(matrixes[2],transpose(x))
x = multMatrix(x,matrixes[3])
x = sum(x,multNum(-1,matrixes[4]))
x = sum(x,multNum(-1,matrixes[4]))
if (x == 0):
    outputFile.write("0")
else:
    outputFile.write("1\n")
    outputFile.write(str(len(x))+" "+str(len(x[0]))+"\n")
    for line in x:
        for el in line:
            outputFile.write(str(el)+" ")
        outputFile.write("\n")
