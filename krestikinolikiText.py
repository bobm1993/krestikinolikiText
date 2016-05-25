def main(b):
    counter = 0
    while True:
        make_board(b)
        if counter % 2 == 0:
            pl_input('X', b)
        else:
            pl_input('O', b)
        counter += 1
        if counter > 4:
            player = check_win(b)
            if player:
                print(player, 'win!')
                break
        if counter == 9:
            print('draw!')
            break
    make_board(b)


def make_board(b):
    print('-------------')
    for i in range(3):
        print('|', b[0 + i * 3], '|', b[1 + i * 3], '|', b[2 + i * 3], '|')
        print("-------------")


def pl_input(pl, b):
    while True:
        try:
            pl_answer = input('where do you want to place ' + pl + '?')
            pl_answer = int(pl_answer)
        except ValueError:
            print('you must enter integer from 1 to 9')
            continue
        if 1 <= pl_answer <= 9:
            if pl_answer in b:
                j = b.index(pl_answer)
                b.remove(pl_answer)
                b.insert(j, pl)
                break
            else:
                print('this cell is not empty')
        else:
            print('you must enter integer from 1 to 9')


def check_win(b):
    win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win:
        if b[i[0]] == b[i[1]] == b[i[2]]:
            return b[i[0]]
    return False

while True:
    board = list(range(1, 10))
    main(board)
    y_n = ''
    while True:
        y_n = input('would you like to restart? y/n')
        if y_n in ('y', 'n'):
            break
        print('Invalid input.')
    if y_n == 'y':
        continue
    elif y_n == 'n':
        break
