import copy

def solution(m, n, board):
    answer = 0
    
    new_board = []
    for i in range(m):
        inner_list = []
        for j in range(n):
            inner_list.append(board[i][j])
        new_board.append(inner_list)
        
    
    while(True):
        is_change = False        
        check_board = [[0]*n for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                a = new_board[i][j]
                b = check(i, j+1, m, n, new_board)
                c = check(i+1, j, m, n, new_board)
                d = check(i+1, j+1, m, n, new_board)

                if(a != '0' and a == b and b == c and c == d and d == a):
                    is_change = True

                    check_board[i][j] = 1
                    check_board[i][j+1] = 1
                    check_board[i+1][j] = 1
                    check_board[i+1][j+1] = 1
        change_board = copy.deepcopy(new_board)
        if(is_change):
            for q in range(n-1, -1, -1):
                save_list = []
                index = 0
                for p in range(m-1, -1, -1):
                    if(check_board[p][q] == 1):
                        save_list.append(p)
                        change_board[p][q] = '0'
                        is_save = True
                    else:
                        if(save_list):
                            change_board[p][q] = '0'
                            save_list.append(p)
                            if(index < len(save_list)):
                                change_board[save_list[index]][q] = new_board[p][q]
                            index += 1
            
            new_board = copy.deepcopy(change_board)
        else:
            break
    
    for i in range(m):
        for j in range(n):
            if(new_board[i][j] == '0'):
                answer += 1
            
    return answer

def check(i, j, m, n, board):
    if(i < 0 or j < 0 or i >=m or j >= n):
        return '0'
    else:
        return board[i][j]
        
        
    
    
