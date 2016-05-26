def main(b, n):
    counter = 0
    while True:
        make_board(b, n)
        if counter % 2 == 0:
            cur_player = ' X'
            pl_input(cur_player, b, n)
        else:
            cur_player = ' O'
            pl_input(cur_player, b, n)
        counter += 1
        if counter > 2 * n - 2:
            player = check_win(cur_player, b, n)  # проверка является ли комбинация игрока выиграшной
            if player:
                print(player, 'win!')
                break
        if counter == n ** 2:  # если ходы закончились - ничья
            print('draw!')
            break
    make_board(b, n)


def make_board(b, n):  # гененрация игрового поля
    str1 = '-----'
    print(str1 * n + '---')
    for k in b:
        if type(k) is int and k < 10:  # добавляется пробел для внешенего вида
            j = b.index(k)
            b.remove(k)
            b.insert(j, " " + str(k))
        elif type(k) is int:
            j = b.index(k)
            b.remove(k)
            b.insert(j, str(k))
    for i in range(n):
        for j in range(n):
            print(' |', b[j + i * n], end='')
        print(' |')
        print(str1 * n + '---')


def pl_input(pl, b, n):  # ходы игроков
    while True:
        try:
            pl_answer = int(input('where do you want to place ' + pl + '?'))
        except ValueError:
            print('you must enter integer from 1 to ' + str(n ** 2))
            continue
        if 1 <= pl_answer <= n ** 2:
            if pl_answer < 10:
                pl_answer = ' ' + str(pl_answer)
            else:
                pl_answer = str(pl_answer)
            if pl_answer in b:
                j = b.index(pl_answer)
                b.remove(pl_answer)
                b.insert(j, pl)
                break
            else:
                print('this cell is not empty')
        else:
            print('you must enter integer from 1 to 9')


def check_win(pl, b, n):  # проверка на выигращные комбинации
    win = []
    for i in range(0, n ** 2 - n + 1, n):
        lst = range(n)
        one_win = []
        all(b[i] == b[i + j] for j in lst)
        for k in lst:
            one_win.append(b[i + k])
        win.append(one_win)  # выиграши по горизонтали
    for i in range(0, n):
        lst = range(0, n ** 2 - n + 1, n)
        one_win = []
        all(b[i] == b[i + j] for j in lst)
        for k in lst:
            one_win.append(b[i + k])
        win.append(one_win)  # выиграши по вертикали
    for i in range(0, n, n):
        lst = range(0, n ** 2, n + 1)
        one_win = []
        all(b[i] == b[i + j] for j in lst)
        for k in lst:
            one_win.append(b[i + k])
        win.append(one_win)  # диагональ слева направо
    for i in range(n - 1, n):
        lst = list(range(0, n ** 2 - n, n - 1))
        one_win = []
        all(b[i] == b[i + j] for j in lst)
        for k in lst:
            one_win.append(b[i + k])
        win.append(one_win)  # диагональ справа налево
    for i in win:
        if all(j == pl for j in i):
            return pl
    return False


while True:
    try:
        board_size = int(input('which size of board would you like? (ex. if you want 5x5 enter "5")'))  # размер поля
    except ValueError:
        print('you must enter integer > 2')
        continue
    if board_size > 2:
        board = list(range(1, board_size ** 2 + 1))
        main(board, board_size)
        y_n = ''
        while True:
            y_n = input('would you like to restart? y/n')  # предложение переиграть
            if y_n in ('y', 'n'):
                break
            print('Invalid input.')
        if y_n == 'y':
            continue
        elif y_n == 'n':
            break
    else:
        print('you must enter integer > 2')
