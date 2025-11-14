# 1. 장르 배열과 재생수 배열을 동시에 순회하면서, a. 장르 : [인덱스, 재생수] 담고 있는 배열과 b. 장르: 총 재생수 배열 만들기
# 2. b를 총 재생수 기준으로 정렬
# 3. b에서 장르를 하나씩 꺼내서(총 재생수 내림차순) a[장르]로 [인덱스, 재생수] 배열을 가져와서 재생수 기준으로 정렬해 변수 x에 담기
# 4. x에서 하나씩 꺼내는데, 최대 2개만 꺼낼 수 있도록 조정한 후, 인덱스를 최종 결과 배열 result에 넣기

def get_melon_best_album(genre_array, play_array):

    # 1
    genre_index_play_dict = {}
    genre_total_play_dict = {}
    i = 0
    for i in range(len(genre_array)):
        genre = genre_array[i]
        index = i
        play = play_array[i]

        if genre not in genre_index_play_dict:
            genre_index_play_dict[genre] = [[index, play]]
            genre_total_play_dict[genre] = play
        else:
            genre_index_play_dict[genre].append([index, play])
            genre_total_play_dict[genre] += play

    # 2
    sorted_genre_total_play_dict = sorted(genre_total_play_dict.items(), key=lambda x: x[1], reverse=True)

    # 3, 4
    result = []
    for genre, _ in sorted_genre_total_play_dict:
        sorted_index_play_list = sorted(genre_index_play_dict[genre], key= lambda x: x[1], reverse=True)
        count = 0
        for index_play in sorted_index_play_list:
            if count == 2:
                break
            else:
                result.append(index_play[0])
                count += 1

    return result

print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))