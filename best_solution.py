def solution(genres, plays):
    answer = []
    genre = {}
    for i in range(len(genres)):
        if(genres[i] in genre):
            genre[genres[i]][1].append((i, plays[i]))
            genre[genres[i]] = [genre[genres[i]][0] + plays[i], genre[genres[i]][1]]
        else:
            genre[genres[i]] = [plays[i], [(i, plays[i])]]
    genre = sorted(genre.items(), key=(lambda x:x[1]), reverse=True)
    for i in genre:
        list = sorted(i[1][1], key=lambda x:x[1], reverse = True)
        answer.append(list[0][0])
        if(len(list) > 1):
            answer.append(list[1][0])
    return answer
