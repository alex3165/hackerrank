inputCases = open('./input/input00.txt')
inputArr = inputCases.read().split('\n')
rotation = list(map(lambda x: int(x), inputArr[0].split()))[1]
values = list(map(lambda x: int(x), inputArr[1].split()))


def solve(a, d):
    for i in range(d):
        a.append(a.pop(0))
    return a


print(' '.join(map(str, solve(values, rotation))))
