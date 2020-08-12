import random
import sys

def help():
    print("\nСписок команд")
    print("b - сделать ставку;")
    print("с - взять кредит;")
    print("t - бросок кубиков;")
    print('x - выйти')

credit = 100
bank = 0
bet = int(0)
a = [1, 2, 3, 4, 5, 6]

print("Для вывода списка команд нажмите введите h")

while True:
    
    print("\nДенег: ", credit)
    print("Ставка: ", bet)
    command = input("Введите команду: ")
    
    if command == 'x':
        sys.exit()
    elif command == 'h':
        help()
    elif command == 'c':
        credit = input("Введите сумму кредита: ")
        credit = int(credit)
        print("Ваши текущие деньги: ", credit,"$")
    elif command == 'b':
        bet = input("Введите ставку: ")
        bet = int(bet)
        if bet > credit:
            print("У вас нет столько.")
            bet = 0
        else:
            credit = credit - bet
    elif command == 't':
        if bet == 0:
            print("Задайте ставку.")
        else:
            val1 = random.choice(a)
            val2 = random.choice(a)
            print("\nВыпало у вас: ",val1)
            print("Выпало у 2: ",val2)
            if val1 == val2:
                print("Делайте новый бросок.")
            elif val1 > val2:
                credit = credit + bet * 2
                bet = 0
                print("\nВы выиграли!")
            elif val1 < val2:
                bet = 0
                print("\nВы проиграли...")
    else:
        print("\nНеизвестная команда")
