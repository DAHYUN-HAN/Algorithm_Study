import numpy as np

def solution(board, moves):
    answer = 0
    x = np.array(board).shape[0]
    basket = []
    for move in moves:
        for j in range(x):
            pick = board[j][move-1]
            board[j][move-1] = 0
            if(pick != 0):
                if basket:
                    if(basket[-1] == pick):
                        answer = answer + 2
                        basket = basket[:-1]
                    else:
                        basket.append(pick)
                else:
                    basket.append(pick)
                break;
    return answer
