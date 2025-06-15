# 팰린드롬
def palindrome(pStr):
    if len(pStr) <= 1:
        return True
    
    if pStr[0] != pStr[-1]:
        return False
    
    return palindrome(pStr[1:-1])


print("결과: ", palindrome("reeeer"))