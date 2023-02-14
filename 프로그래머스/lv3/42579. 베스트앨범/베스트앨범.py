
def solution(genres, plays):
    answer = []

    music = dict()
    music_plays = dict()

    for i in range(len(plays)):
        if genres[i] not in music:
            music[genres[i]] = plays[i]
        else:
            music[genres[i]] += plays[i]

        if genres[i] not in music_plays:
            music_plays[genres[i]] = [(plays[i],i)]
        else:
            music_plays[genres[i]].append((plays[i],i))


    music_list = list(music.items())
    music_list.sort(key=lambda x:(-x[1]))

    for i in music_plays:
        music_plays[i].sort(key=lambda x:(-x[0]))

    for i in music_list:

        if len(music_plays[i[0]]) ==1:
            answer.append(music_plays[i[0]][0][1])
        else:
            answer.append(music_plays[i[0]][0][1])
            answer.append(music_plays[i[0]][1][1])


    return answer