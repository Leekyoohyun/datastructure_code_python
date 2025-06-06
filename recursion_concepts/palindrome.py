# 팰린드롬. 거꾸로 읽어도 똑같게
def palindrome(pStr):
    if len(pStr) <= 1:
        return True # 글자 하나면 그냥 팰린드롬
    
    if pStr[0] != pStr[-1]:
        return False # 처음과 끝이 다르면 그냥 바로 아님
    
    return palindrome(pStr[1:-1])

    # pStr[1:-1]이해하기 
    # pStr=reaver -> pStr[1:-1] = eave -> pStr[1:-1]의 [1:-1] = av