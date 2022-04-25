def change(music):
    if 'A#' in music:
        music = music.replace('A#', 'a')
    
    if 'F#'in music:
        music = music.replace('F#', 'f')
    
    if 'C#' in music:
        music = music.replace('C#', 'c')
    
    if 'G#' in music:
        music = music.replace('G#', 'g')
    
    if 'D#' in music:
        music = music.replace('D#', 'd')
    
    return music

def solution(m, musicinfos):
    answer = []
    index = 0
    
    for info in musicinfos:
        index += 1
        music = info.split(',')
        start = music[0].split(':')
        end = music[1].split(':')
        
        play_time = (int(end[0]) * 60 + int(end[1])) - (int(start[0]) * 60 + int(start[1]))
        
        changed = change(music[3])
        
        music_len = len(changed)
        
        play_melody = changed * (play_time // music_len) + changed[:play_time % music_len]
        
        m = change(m)
        
        if m in play_melody:
            answer.append([play_time, index, music[2]])
    
    if not answer:
        return "(None)"
    
    elif len(answer) == 1:
        return answer[0][2]
    
    else:
        answer = sorted(answer, key = lambda x: (-x[0], x[1]))
        return answer[0][2]


m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]	

result = solution(m, musicinfos)