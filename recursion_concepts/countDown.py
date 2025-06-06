def countDown(countNum):
    if countNum == 0:
        print("발사")
    else:
        
        countDown(countNum-1)
        print(countNum)

countDown(5)