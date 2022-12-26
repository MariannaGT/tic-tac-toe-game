def input_data(player_token, tab):
    valid = False
    while not valid:
        player_answer = input("Ваш ход. Введите число от 1 до 9." + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод!")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(tab[player_answer-1]) not in "XO"):
                tab[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9.")