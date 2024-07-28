#dirty_dozen = ["Strawberries","Spinach", "Kale","Nectarines","Apples","Grapes","Peaches",
               #"Cherries","Pears","Tomatoes","Celery","Potatoes"]

#과일과 채소 구분 방법
fruits = ["Strawberries","Nectarines","Apples","Grapes","Peaches","Cherries","Pears"]
vegetables = ["Spinach","Kale","Tomatoes","Celery","Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[0][0])

#dirty_dozen[0][0]은 fruits, strawberries를 나타내고
#[1][0]은 vegetables, spinach를 나타낸다.
#즉 앞에는 과일인지 채소인지를 묻는 리스트이고, 뒤에 부분은 해당 리스트에 포함된 값을 의미한다.