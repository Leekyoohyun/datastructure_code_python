genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    # 구현해보세요!
    n = len(genre_array)
    gen_total_play_dict = {}
    gen_index_play_dict = {}
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in gen_total_play_dict:
            gen_total_play_dict[genre] = play
            gen_index_play_dict[genre] = [[i, play]]
        else:
            gen_total_play_dict[genre] += play
            gen_index_play_dict[genre].append([i,play])
    print(gen_total_play_dict)

    return gen_index_play_dict

    


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))