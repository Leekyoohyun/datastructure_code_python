#버블정렬
def bubbleSort(ary):
    n = len(ary)
    for end in range(n-1, 0, -1):
        for cur in range(0, end):
            if (ary[cur] > ary[cur+1]):
                ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
    
    return ary

#개선버전
def bubbleSortUpgrade(ary):
    n = len(ary)
    for end in range(n-1, 0, -1):
        changeYN = False
        print("#사이클", ary)
        for cur in range(0, end):
            if (ary[cur] > ary[cur+1]):
                ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
                changeYN = True
        if not changeYN:
            break
    
    return ary