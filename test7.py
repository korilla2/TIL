
sudoku = [list(range(1, 10)) for _ in range(9)]
from1to9 = set(range(1, 10))

zipSudoku = list(map(list, zip(*sudoku)))   # 세로줄을 가로줄로 반전
for i in range(3):
    for j in range(3):
        if set(sudoku[i*3:(i*3)+3][0:3][j]) != from1to9 or set(zipSudoku[i*3:(i*3)+3][0:3][j]) != from1to9:
            print(f'{i}', sudoku[i*3:(i*3)+3][0:3][j])

            check = 0
