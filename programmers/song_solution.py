def solution(m, musicinfos):
    answer = ''
    music_list = []
    for i in musicinfos:
        info_list = i.split(',')
        time = (int(info_list[1][:2]) * 60 + int(info_list[1][3:5]))-(int(info_list[0][:2]) * 60 + int(info_list[0][3:5]))
        music = ''
        music = change_music(info_list[3])
        music = music*time
        music_list.append([music[:time], info_list[2]])
    music_list = sorted(music_list, key = lambda x:len(x[0]), reverse=True)
    
    
    listen = change_music(m)
    for i in music_list:
        if(listen in i[0]):
            return i[1]
            
    return "(None)"

def change_music(s):
    music = ''
    for j in range(len(s)-1):
        if(s[j].isalpha() and s[j+1] != '#'):
            print(s[j])
            music += s[j].lower()
        elif(s[j+1] == '#'):
            music += s[j].upper()
    if(s[-1] != '#'):
        music += s[-1].lower()
    return music
