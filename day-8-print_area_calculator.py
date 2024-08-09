#주어진 벽의 높이와 너비를 바탕으로 벽면을 칠하는데
#필요한 페인트 통의 개수를 계산하는 함수를 만들어보기
import math

def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_up_cans = math.cil(num_cans) #올림 계산을 위해 math.ceil() 메서드를 호출
    print(f"You'll need {round_up_cans} cans of paint.")

test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)