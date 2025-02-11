import os
import random

VERSION = 1.3

class bingo():

    def __init__(self):

        while True:
            # 메뉴 불러오기
            self.clearScreen() # 최초에 화면 클리어
            self.sel_menu = self.setMenu()
            self.clearScreen()

            if self.sel_menu == 1:
                # PvE
                print('컴퓨터 대전')
                
                try:
                    num_block = int(input('칸 수를 입력해 주세요(최소 3개 이상) > ')) # 빙고 칸 수 입력
                except ValueError as e: # 숫자 외 다른 문자 입력(소수점 포함)
                    print('칸 수를 정확히 입력해 주세요.\n'
                        '처음 메뉴로 돌아갑니다.')
                    input()
                    continue
                    
                if num_block >= 3:
                    my_bingo = self.set_bingo(num_block) # 내 빙고판 만들기
                    com_bingo = self.set_bingo(num_block) # 컴퓨터 빙고판 만들기
                    self.PvE_game(my_bingo, com_bingo, num_block) # 메인 게임 들어가기
                else:
                    # 2이하 수 입력
                    print('칸 수를 3이상 입력해 주세요.\n'
                        '처음 메뉴로 돌아갑니다.')

            elif self.sel_menu == 2:
                # PvP | 미구현(네트워크 공부 후 개발 예정)
                print('유저 대전\n'
                      '현재 미구현\n'
                      '개발 예정입니다.')

            elif self.sel_menu == 3:
                # 게임 종료
                print('빙고게임 종료')
                break

            else:
                # 잘못 입력
                print('잘 못 입력했습니다.\n'
                    '다시 입력 해 주세요!')
                
            input() # 입력대기 : 엔터치면 넘어감
            self.clearScreen() # 메뉴 기능이 완료되면 화면 클리어
    
    # 메뉴 불러오기 함수
    def setMenu(self):
        self.str_menu = (f'빙고 ver.{VERSION}\n'
                    '1. 컴퓨터 대전\n'
                    '2. 유저 대전\n'
                    '3. 게임종료\n')
        print(self.str_menu)
        try: # 정수 외 다른 형 입력 시 예외처리
            self.sel_menu = int(input('메뉴번호 입력 : '))
        except ValueError as e:
            return 0
        return self.sel_menu

    # 빙고 세팅 함수
    def set_bingo(self, num_block: int):
        self.lst_first = random.sample([i for i in range(1, (num_block**2) + (num_block + 1))], k=num_block**2) # 랜덤 번호 불러오기
        
        self.lst_bingo = []
        # 불러온 번호 2중 배열로 집어넣기
        for i in range(num_block):
            lst_second = []
            for j in range(num_block):
                lst_second.append(self.lst_first.pop())
            self.lst_bingo.append(lst_second)

        return self.lst_bingo

    # PvE 함수
    def PvE_game(self, my_bingo : list, com_bingo : list, num_block : int):
        while True:
            self.clearScreen()

            print('나의 빙고판\n')
            self.result(my_bingo) # 내 빙고판 보기

            # for i in com_bingo: # 컴퓨터 빙고판 보기(임시, 완성된 후 주석처리)
            #     print(i)

            try:
                #나의 턴
                num = int(input(f'제거할 숫자를 입력하세요(1~{(num_block**2) + num_block}) > ')) # 제거할 숫자 입력
                if 1 <= num <= ((num_block**2) + num_block):
                    self.catch_bingo(my_bingo, num) # 내 빙고 번호 지우기
                    self.catch_bingo(com_bingo, num) # 컴퓨터 빙고 번호 지우기

                else: # 제거할 숫자를 잘 못 입력한 경우
                    print('숫자를 잘 못 입력했습니다.\n'
                        '다시 입력 해 주세요.')
                    input()
                    continue

            except ValueError as e: # 문자, 소숫점 등 잘못 입력
                print('제거할 숫자를 정확히 입력해 주세요.')
                input()
                continue
            
            self.clearScreen()

            # 컴퓨터 턴
            self.com_choose(my_bingo, com_bingo)
            
            # 빙고가 맞춰졌는지 확인하기
            user = self.check_bingo(my_bingo)
            com = self.check_bingo(com_bingo)

            # 빙고가 다 맞춰졌을 때 결과 출력
            if (user == True) and (com == True):
                print('비겼습니다.')
                print('Me')
                self.result(my_bingo)
                print('Computer')
                self.result(com_bingo)
                break
            elif (user == True) and (com == False):
                print('당신이 이겼습니다.')
                print('Me')
                self.result(my_bingo)
                print('Computer')
                self.result(com_bingo)
                break
            elif (user == False) and (com == True):
                print('컴퓨터가 이겼습니다.')
                print('Me')
                self.result(my_bingo)
                print('Computer')
                self.result(com_bingo)
                break

    # 번호 지우기 함수
    def catch_bingo(self, bingo : list, num : int):
        for i in range(len(bingo)): # 빙고 번호 찾으면 지우기
            if num in bingo[i]:
                self.in_bingo = bingo[i].index(num)
                bingo[i][self.in_bingo] = 0
        
        return bingo

    # 빙고가 됐는지 확인하는 함수
    def check_bingo(self, bingo: list):
        if self.row_bingo(bingo): # 가로
            return True
        elif self.col_bingo(bingo): # 세로
            return True
        elif self.left_cross(bingo): # 왼쪽 대각선
            return True
        elif self.right_cross(bingo): # 오른쪽 대각선
            return True
        else:
            return False

    # 가로 빙고 확인 함수
    def row_bingo(self, bingo: list):
        for i in range(len(bingo)):
            self.row_ck = 1
            for j in range(len(bingo)):
                if self.row_ck == 1 and bingo[i][j] != 0:
                    self.row_ck = 0
                    break
            if j == (len(bingo) - 1) and self.row_ck == 1:
                return True

    # 세로 빙고 확인 함수
    def col_bingo(self, bingo: list):
        for i in range(len(bingo)):
            for j in range(len(bingo)):
                self.col_ck = 1
                if self.col_ck == 1 and bingo[j][i] != 0:
                    self.col_ck = 0
                    break
            if j == (len(bingo) - 1) and self.col_ck == 1:
                return True

    # 왼쪽 대각선 빙고 확인 함수
    def left_cross(self, bingo: list):
        for i in range(len(bingo)):
            if bingo[i][i] != 0:
                return False
        return True

    # 오른쪽 대각선 빙고 확인 함수
    def right_cross(self, bingo: list):
        for i in range(len(bingo)):
            if bingo[i][len(bingo) - (i + 1)] != 0:
                return False
        return True

    # 컴퓨터 숫자 고르기 함수
    def com_choose(self, my_bingo, com_bingo):
        self.lst_com = list(set(sum(com_bingo, [])))
        if 0 in self.lst_com:
            self.lst_com.remove(0)

        self.num = random.choice(self.lst_com)
        self.catch_bingo(my_bingo, self.num) # 내 번호 지우기
        self.catch_bingo(com_bingo, self.num) # 컴퓨터 번호 지우기
        input('컴퓨터가 숫자를 골랐습니다.\n'
            'Enter를 눌러 주세요.')
        self.clearScreen()

    # 빙고판 보기 함수
    def result(self, bingo):
        for i in bingo:
            for j in range((len(bingo))):
                print(f'{i[j]:4d}', end=' ')
            print('\n')

    # 화면 정리 함수
    def clearScreen(self):
        self.command = 'clear'
        if os.name in ('nt', 'dos'):
            self.command = 'cls'
        
        os.system(self.command)

if __name__ == '__main__':
    app = bingo()