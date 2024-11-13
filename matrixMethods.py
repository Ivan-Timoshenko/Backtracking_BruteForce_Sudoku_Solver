import random

def create_matrix(size: int, fixes: int) -> tuple[list[list[str]], list[list[int]]]:
    matrix = [['.' for i in range(size)] for k in range(size)]
    already_set = []
    while fixes > 0:
        x, y = random.randint(0, size-1), random.randint(0, size-1)
        value = random.randint(1, size)
        if [x,y] not in already_set:
            already_set.append([x, y, value])
            matrix[x][y] = value
            fixes -= 1

    return matrix, already_set

def solver(field: list[list[str]], fixes: list[list[int]]) -> list[list[str]]:
    for row in range(len(field)):
        fixed_rows = [a[0] for a in fixes]
