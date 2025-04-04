
# 택배상자 쌓기

# 헨젤과 그레텔이 과자집에 가면서 돌멩이를 한 알씩 떨어뜨립니다. 돌멩이는 지나온 길의 표시이며, 돌아갈 때는 거꾸로
# 그 돌멩이를 따라가야 집에 도착할 수 있습니다. 직접 구현한 스택을 사용하여, 헨젤과 그레텔이 무사히 집으로
# 돌아가도록 해주세요.
# • 목표:
# • 과자집에 가는 동안 만나는 돌멩이 색깔을 스택에 push
# • 집으로 돌아갈 때는 스택에서 pop하면서 역순으로 이동
# • 이동 경로를 출력

# 스택 초기화
stack = []

#과자집에 가는 경로
path_to_candy_house = ['주황', '초록', '파랑', '보라', '빨강', '노랑']

print("과자집에 가는 길:")
for color in path_to_candy_house:
    print(color, end=' -> ')
    stack.append(color)  # 스택에 push

print("과자집 도착!\n")

print("우리집으로 돌아가는 길:")
while stack:
    color = stack.pop()  # 스택에서 pop
    print(color, end=' -> ')

print("우리집 도착!")
