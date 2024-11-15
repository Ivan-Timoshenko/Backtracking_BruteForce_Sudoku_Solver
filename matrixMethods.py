import random

def create_matrix(size: int, fixes: int) -> tuple[list[list[str]], dict[tuple[int, int], int]]:
    matrix = [['.' for i in range(size)] for k in range(size)]
    already_set = {}

    while len(already_set) < fixes:
        x, y = random.randint(0, size-1), random.randint(0, size-1)
        value = random.randint(1, size)
        if (x, y) not in already_set.keys():
            already_set[(x, y)] = value
            matrix[x][y] = value

    return matrix, already_set