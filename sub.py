import random

def select(name,check):
    while True:
        my_figures = input(name+'Put 3 different numbers. :')
        counter1 = len(str(my_figures))
        counter2 = len(my_figures)
        sets = len(set(my_figures))
        if counter1 == 3 and counter2 == sets:
            for figure in my_figures:
                try:
                    int_figure = int(figure)
                except:
                    print("Type error! Try again.")
                    continue
                check.append(int_figure)

                for a in range(10):
                    print('#' * 20)
            break
        else:
            print("Type error! Try again.")
            continue
def battle(player,check):
    while True:
        battle_check = []
        print(player + ',Your turn')
        my_figures = input("Predict the opponent numbers. :")
        counter1 = len(str(my_figures))
        counter2 = len(my_figures)
        sets = len(set(my_figures))
        if counter1 == 3 and counter2 == sets:
            for figure in my_figures:
                int_figure = int(figure)
                battle_check.append(int_figure)
            if battle_check == check:
                print(player + ' VICTORY!!')
                return 1
                break
            else:
                hit_count = 0
                for i in range(3):
                    if battle_check[i] == check[i]:
                        hit_count += 1
                print(hit_count,'hit')
                blow_count = len(set(set(battle_check) & set(check)))
                print( blow_count - hit_count, 'blow')
                return 0
                break
        else:
            print("Type error! Try again.")
            continue
