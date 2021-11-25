def check(row, column, n) :
    if(row < 0) :
        row = n-1
    if(column >= n) :
        column = 0
    return row, column

n = int(input())
if (n % 2 == 0) : 
    print("입력한 수는 홀수 이어야 함.")
else :
    magic_square = [[0] * n for _ in range(n)]

    row = 0
    column = int(n/2)
    number = 1

    while(number <= n*n) :
        magic_square[row][column] = number
        
        if(number % n == 0) :
            row += 1
        else : 
            row -= 1
            column += 1
        number += 1
        row, column = check(row, column, n)

    for i in range(n) :
        for j in range(n) :
            print(magic_square[i][j], end="\t")
        print()
    
