from collections import deque
def solution(cacheSize, cities):
    cache = deque()
    answer = 0
    if(cacheSize == 0):
        return len(cities) * 5
    for i in cities:
        if(len(cache) < cacheSize):
            exist = False
            for k in range(len(cache)):
                if(cache[k] == i.lower()):
                    del cache[k]
                    answer += 1
                    exist = True
                    break
            if(not exist):
                answer += 5
            cache.appendleft(i.lower())
        else:
            exist = False
            for k in range(len(cache)):
                if(cache[k] == i.lower()):
                    del cache[k]
                    answer += 1
                    exist = True
                    break
            if(not exist):
                answer += 5
                cache.pop()
            cache.appendleft(i.lower())
        
    return answer
