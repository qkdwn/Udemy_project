line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()

letter = position[0].lower()
abc = ["a","b","c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X" #number_index가 앞으로 온 이유는 중첩 리스트를 읽을 때는 바깥에서 안 쪽으로 읽기 때문이다.

print(f"{line1}\n{line2}\n{line3}")