#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)

#for의 경우 어떤 것을 반복하고 반복하는 각 아이템에 대해 뭔가를 해야할 때 유용하다.
#while의 경우 전체 순서에서 몇 번째에 해당하는지 어떤 아이템을 반복할지가 아닌,
#그저 특정 작업을 설정한 조건에 도달할 때까지 수 없이 반복 수행하고자 할 때 사용한다.


#for의 경우 실행 횟수를 사전에 설정해두기 때문에 이 경우는 리스트가 끝나면 실행이 중단되고
#이 경우는 범위의 상한선에 이르면 중단되지만

#while의 경우 특정 조건이 거짓으로 전환될 때까지 계속 실행되기 때문에
#만약 조건이 거짓이 되지 않는다면 소위 무한 반복이라 불리는 반복문이 된다.