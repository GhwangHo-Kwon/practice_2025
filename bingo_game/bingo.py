import random

VERSION = 1.1

# 첫 실행 함수
def run():

    while True:
        # 메뉴 불러오기
        sel_menu = setMenu()

        if sel_menu == 1:
            # PvE
            print('컴퓨터랑 합니다.')
            num_block = int(input('칸 수를 입력해 주세요(최소 3개 이상) > ')) # 빙고 칸 수 입력
            if num_block >= 3:
                my_bingo = set_bingo(num_block) # 내 빙고판 만들기
                com_bingo = set_bingo(num_block) # 컴퓨터 빙고판 만들기
                main_game(my_bingo, com_bingo, num_block) # 메인 게임 들어가기
            else:
                # 잘못 입력
                print('다시 입력해 주세요.\n'
                      '처음 메뉴로 돌아갑니다.')

        elif sel_menu == 2:
            # PvP
            print('유저랑 합니다.')

        elif sel_menu == 3:
            # 게임 종료
            break

        else:
            # 잘못 입력
            print('잘 못 입력했습니다.\n'
                  '다시 입력 해 주세요!')

# 메뉴 불러오기 함수
def setMenu():
    str_menu = (f'빙고 ver.{VERSION}\n'
                '1. 컴퓨터랑 하기\n'
                '2. 유저랑하기\n'
                '3. 게임종료\n')
    print(str_menu)
    sel_menu = int(input('메뉴번호 입력 : '))
    return sel_menu

# 빙고 세팅 함수
def set_bingo(num_block: int):
    lst_first = random.sample([i for i in range(1, (num_block**2) + 21)], k=num_block**2) # 랜덤 번호 불러오기
    # random.shuffle(lst_first)
    lst_bingo = []
    # 불러온 번호 2중 배열로 집어넣기
    for i in range(num_block):
        lst_second = []
        for j in range(num_block):
            lst_second.append(lst_first.pop())
        lst_bingo.append(lst_second)

    return lst_bingo

# 메인 게임 함수
def main_game(my_bingo : list, com_bingo : list, num_block : int):
    while True:
        for i in my_bingo: # 내 빙고판 보기
            print(i)
        print('')
        for i in com_bingo: # 컴퓨터 빙고판 보기(임시, 완성된 후 주석처리)
            print(i)

        num = int(input(f'제거할 숫자를 입력하세요(1~{(num_block**2) + 20}) > ')) # 제거할 숫자 입력
        if 1 <= num <= ((num_block**2) + 20):
            catch_bingo(my_bingo, com_bingo, num) # 번호 지우기 함수

            user = check_bingo(my_bingo) # 빙고가 됐는지 확인하는 함수
            com = check_bingo(com_bingo)

            # 빙고가 다 맞춰졌을 때 결과
            if (user == True) and (com == True):
                print('비겼습니다.')
                break
            elif (user == True) and (com == False):
                print('당신이 이겼습니다.')
                break
            elif (user == False) and (com == True):
                print('컴퓨터가 이겼습니다.')
                break

        else: # 제거할 숫자를 잘 못 입력한 경우
            print('숫자를 잘 못 입력했습니다.\n'
                  '다시 입력 해 주세요.')

# 번호 지우기 함수
def catch_bingo(my_bingo : list, com_bingo : list, num : int):
    for i in range(len(my_bingo)): # 빙고 번호 찾으면 지우기
        if num in my_bingo[i]:
            in_bingo = my_bingo[i].index(num)
            my_bingo[i][in_bingo] = 0
    
    for i in range(len(com_bingo)):
        if num in com_bingo[i]:
            in_bingo = com_bingo[i].index(num)
            com_bingo[i][in_bingo] = 0
    
    return my_bingo, com_bingo

# 빙고가 됐는지 확인하는 함수
def check_bingo(bingo: list):
    if row_bingo(bingo):
        return True
    elif col_bingo(bingo):
        return True
    elif left_cross(bingo):
        return True
    elif right_cross(bingo):
        return True
    else:
        return False

# 가로 빙고 확인
def row_bingo(bingo: list):
    for i in range(len(bingo)):
        row_ck = 1
        for j in range(len(bingo)):
            if row_ck == 1 and bingo[i][j] != 0:
                row_ck = 0
                break
        if j == (len(bingo) - 1) and row_ck == 1:
            return True

# 세로 빙고 확인
def col_bingo(bingo: list):
    for i in range(len(bingo)):
        for j in range(len(bingo)):
            col_ck = 1
            if col_ck == 1 and bingo[j][i] != 0:
                col_ck = 0
                break
        if j == (len(bingo) - 1) and col_ck == 1:
            return True

# 왼쪽 대각선 빙고 확인
def left_cross(bingo: list):
    for i in range(len(bingo)):
        for j in range(len(bingo)):
            if (i == j) and bingo[i][j] != 0:
                return False
    return True

# 오른쪽 대각선 빙고 확인
def right_cross(bingo: list):
    for i in range(len(bingo)):
        for j in range(len(bingo)):
            if ((len(bingo) - (i + 1)) == j) and bingo[i][j] != 0:
                return False
    return True

# 메인 함수
if __name__ == '__main__':
    print('빙고게임 시작!')
    run()

print('빙고게임 종료')