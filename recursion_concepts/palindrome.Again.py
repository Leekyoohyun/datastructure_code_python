# 팰린드롬 확인하기
def palindrome(pStr):
    if len(pStr) == 0:
        print("올바른 거 입력해라")
        return
    elif len(pStr) <= 1:
        return True
    
    if pStr[0] != pStr[-1]:
        return False
    
    return palindrome[pStr[1:-1]]
    