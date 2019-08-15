MOVE = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def q1(matrix):
    m = len(matrix)
    n = len(matrix[0])
    total = 0
    for i in range(m):
        for j in range(n):
            total += matrix[i][j] * 6
            if matrix[i][j] > 1:
                total -= (matrix[i][j] - 1) * 2
            if j > 0:
                total -= min(matrix[i][j], matrix[i][j - 1]) * 2
            if i > 0:
                total -= min(matrix[i][j], matrix[i - 1][j]) * 2
    return total


if __name__ == '__main__':
    NM = list(map(int, input().strip().split(" ")))
    n = NM[0]
    m = NM[1]
    nums_input = []
    for i in range(n):
        line = list(map(int, input().strip().split(" ")))
        nums_input.append(line)

    print(q1(nums_input))
