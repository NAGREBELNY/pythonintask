#Напишите программу, которая бы при запуске случайным образом отображала название одного из двух спутников Марса.
# Нагребельный Ю.А., Вариант 16.
import random
rando=random.randint(1,2)
if rando==1:
  print("Фобос - один из двух спутником Марса")
elif rando==2:
  print("Деймос - один из двух спутников Марса")
input("Нажмите ENTER для продолжения")