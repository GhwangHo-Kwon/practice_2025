import random

VERSION = 1.0

def run():

    while True:
        sel_menu = setMenu()

        if sel_menu == 1:
            print('컴퓨터랑 합니다.')
            num_block = int(input('칸 수를 입력해 주세요(최소 3개 이상) > '))
            if num_block >= 3:
                my_bingo = set_bingo(num_block)
                com_bingo = set_bingo(num_block)
                main_game(my_bingo, com_bingo, num_block)
            else:
                print('다시 입력해 주세요.\n'
                      '처음 메뉴로 돌아갑니다.')

        elif sel_menu == 2:
            print('유저랑 합니다.')

        elif sel_menu == 3:
            break

        else:
            print('잘 못 입력했습니다.\n'
                  '다시 입력 해 주세요!')

def setMenu():
    str_menu = (f'빙고 ver.{VERSION}\n'
                '1. 컴퓨터랑 하기\n'
                '2. 유저랑하기\n'
                '3. 게임종료\n')
    print(str_menu)
    sel_menu = int(input('메뉴번호 입력 : '))
    return sel_menu

def set_bingo(num_block):
    lst_first = random.sample([i for i in range(1, (num_block**2) + 21)], k=num_block**2)
    # random.shuffle(lst_first)
    lst_bingo = []
    for i in range(num_block):
        lst_second = []
        for j in range(num_block):
            lst_second.append(lst_first.pop())
        lst_bingo.append(lst_second)

    return lst_bingo

def main_game(my_bingo : list, com_bingo : list, num_block : int):
    while True:
        for i in my_bingo:
            print(i)
        print('')
        for i in com_bingo:
            print(i)

        num = int(input(f'제거할 숫자를 입력하세요(1~{(num_block**2) + 20}) > '))
        if 1 <= num <= ((num_block**2) + 20):
            catch_bingo(my_bingo, com_bingo, num)
        else:
            break

        check_bingo(my_bingo, com_bingo)

def catch_bingo(my_bingo : list, com_bingo : list, num : int):
    for i in range(len(my_bingo)):
        if num in my_bingo[i]:
            in_bingo = my_bingo[i].index(num)
            my_bingo[i][in_bingo] = 0
    
    for i in range(len(com_bingo)):
        if num in com_bingo[i]:
            in_bingo = com_bingo[i].index(num)
            com_bingo[i][in_bingo] = 0
    
    return my_bingo, com_bingo

def check_bingo(my_bingo, com_bingo):
    pass

if __name__ == '__main__':
    print('빙고게임 시작!')
    run()

print('빙고게임 종료')