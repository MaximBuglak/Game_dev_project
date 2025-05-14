import random

print("Игра: Камень, ножницы, бумага")
print("Чтобы выйти, введи: выход\n")

choices = ["камень", "ножницы", "бумага"]

while True:
    user = input("Твой выбор (камень/ножницы/бумага): ").lower()
    
    if user == "выход":
        print("Игра окончена. Пока!")
        break
    
    if user not in choices:
        print("Неверный ввод. Попробуй снова.")
        continue

    computer = random.choice(choices)
    print("Компьютер выбрал:", computer)

    if user == computer:
        print("Ничья!\n")
    elif (user == "камень" and computer == "ножницы") or \
         (user == "ножницы" and computer == "бумага") or \
         (user == "бумага" and computer == "камень"):
        print("Ты победил!\n")
    else:
        print("Ты проиграл!\n")
