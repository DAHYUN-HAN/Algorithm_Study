N,M = map(int, input().split())
board = [list(input()) for _ in range(N)]

def check(first):
    if(first == 'W'):
        second = 'B'
        
        first2 = 'B'
        second2 = 'W'
    else:
        second = 'W'
        
        first2 = 'W'
        second2 = 'B'
    return first, second, first2, second2

def get_change(first, second, new_board):
    change = 0
    for i in range(8):
        for j in range(8):
            if(i % 2 == 0):
                if(j % 2 == 0):
                    if(new_board[i][j] != first):
                        change = change + 1
                else:
                    if(new_board[i][j] != second):
                        change = change + 1
            else:
                if(j % 2 == 0):
                    if(new_board[i][j] != second):
                        change = change + 1
                else:
                    if(new_board[i][j] != first):
                        change = change + 1
    return change

change_count_list = []
new_board = []

for i in range(N-7):
    for j in range(M-7):
        new_board = []
        for line in board[i:i+8]:
            new_board.append(line[j:j+8])
        first, second, first2, second2 = check(new_board[0][0])
        change_count_list.append(get_change(first, second, new_board))
        change_count_list.append(get_change(first2, second2, new_board))
change_count_list = sorted(change_count_list)
print(change_count_list[0])
