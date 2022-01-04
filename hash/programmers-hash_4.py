def solution(genres, plays):
    answer = []
    length = len(genres)
    dic = {}
    songs = []
    for i in range(length):
        temp = {}
        temp["genre"] = genres[i]
        temp["play"] = plays[i]
        temp["identify"] = i
        songs.append(temp)
        if genres[i] in dic:
            dic[genres[i]] += plays[i]
        else:
            dic[genres[i]] = plays[i]
    genreRank = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    songs.sort(key=lambda song: (song["genre"], song["play"]), reverse=True)
    tempGenre = ""
    count = 0
    result = {}
    for song in songs:
        if tempGenre != song["genre"]:
            tempGenre = song["genre"]
            count = 0
            result[song["genre"]] = []
        if count < 2:
            result[song["genre"]].append(song["identify"])
            count += 1
    for i in genreRank:
        for j in result[i[0]]:
            answer.append(j)
    return answer
