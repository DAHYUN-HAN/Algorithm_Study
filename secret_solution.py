def solution(n, arr1, arr2):
    map_arr1 = []
    map_arr2 = []
    answer = []
    
    map_arr1 = map(arr1, n)
    map_arr2 = map(arr2, n)
    
    for i in range(len(map_arr1)):
        new_map_list= ''
        for j in range(len(map_arr1[i])):
            if(map_arr1[i][j] or map_arr2[i][j] == 1):
                new_map_list = new_map_list + '#'
            else:
                new_map_list = new_map_list + ' '
        answer.append(new_map_list)

    return answer

def map(arr, n):
    map_arr = []
    for i in arr:
        solve_list = solve(i)
        for k in range(n-len(solve_list)):
            solve_list.append(0)
        solve_list = list(reversed(solve_list))
        map_arr.append(solve_list)
    return map_arr
        

def solve(i):
    solve_list = []
    while(i != 0):
        solve_list.append(i%2)
        i = i // 2
    return solve_list
