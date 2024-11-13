from time import sleep
from matrixMethods import create_matrix
from sys import stdout
import os

#region Windows Shenanigans
if os.name == "nt":
    import ctypes

    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
#endregion


#region Cursor mover to x: coord[0], y: coord[1]
def jump(coord: list[int]) -> None:
    stdout.write(f'\033[{coord[1]};{coord[0]}H')
#endregion

#region Calculating console position
def pos_calc(row: int, col: int) -> list[int]:
    console_x, console_y = row, 0
    if col+1 == 1:
        console_y = 1
    else:
        console_y = 2*col - 1

    return [console_y, console_x]
#endregion


def display_matrix(data: list[list[str]]) -> None:
    for row in range(len(data)):
        for col in range(len(data[0])):
            poy, pox = pos_calc(row, col)
            jump([pox, poy])
            stdout.write(str(data[row][col]))
            stdout.flush()


stdout.write('\033[2J') #display cleared
stdout.write('\033[?25l') #cursor hidden


matrix, fixes = create_matrix(9, 9*9)
mx, my = 0, 0
while True:
    try:
        display_matrix(matrix)
        sleep(1000000)
    except KeyboardInterrupt:
        break
stdout.write('\033[?25h') #cursor found
stdout.flush()