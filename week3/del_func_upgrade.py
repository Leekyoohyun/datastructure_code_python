# 지정 위치 이후로 모두 삭제하기
list = ['a','b','c','d','e']

def del_all_data(position):
    #예외처리

    for _ in range(len(list)-position):

        for _ in range(len(list)-position):
            kLen = len(list)
            list[position] = None

            for i in range(position+1, kLen):
                list[i-1] = list[i]
                list[i] = None

            del(list[kLen-1])



print(list)
del_all_data(2)
print(list)