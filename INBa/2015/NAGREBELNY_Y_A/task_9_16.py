#Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать. Компьютер сообщает игроку, сколько букв 
#в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет". Вслед за 
#тем игрок должен попробовать отгадать слово.
# Нагребельный Ю.А., Вариант 16.
import random
words = ("питон", "информатика", "юрий", "алексей", "июнь", "вторник", "музыка")
rando=random.choice(words)
rando=randi
num=len(rando)
drob=random.randrange(num)
print("Привет. Я хочу загадать слово, чтобы ты его отгадал.\nДля начала ты можешь попытаться отгадать буквы, но у тебя 5 попыток!")
print("Я загадал слово. В нем",num," букв")
i=0
vvod=input("Введи букву: ")
while i>4:
  if vvod in randi:
    print("Такая буква есть!")
  else:
    print("Такой буквы нет!")
vvod=input("У тебя кончились попытки. Теперь попробуй отгадать слово.")
while vvod!=randi:
  vvod=input("Неправильно. Попытайся еще: ")
print("Угадал. Это слово ",randi)
input("Нажмите ENTER для продолжения)
