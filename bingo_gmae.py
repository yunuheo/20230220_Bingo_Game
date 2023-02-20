import random

# N*N 크기의 빙고판 생성
N = int(input("빙고판 크기 지정: "))
# 전체 빙고 개수
bingoTotal = 0


random_digit = []
random_digit = random.sample(range(1,N*N+1),N*N) # 1부터 N*N까지의 범위중에 N*N개를 중복없이 뽑음.

board = [[0 for i in range(N)] for j in range(N)]

# N*N개의 랜덤 숫자를 우선적으로 생성하여 2차원 리스트 board에 복사
cnt = 0
for i in range(N):
    for j in range(N):
        if cnt >= len(random_digit):
            break
        board[i][j] = random_digit[cnt]
        cnt += 1

# 빙고판 출력
for i in range(N):
    for j in range(N):
        print("%3d"%(board[i][j]),end="  ")
    print()

# 빙고 판정 함수 judgeBingo() 구현
def judgeBingo():
   global bingoTotal
   diagonal_left_star_count = 0
   diagonal_right_star_count = 0
   for i in range(N):
            row_star_count = 0
            col_star_count = 0
            
            for j in range(N):
                # 가로줄빙고 판별
                if board[i][j] == chr(9733):
                    row_star_count += 1
                    if row_star_count == N:
                        bingoTotal += 1
                        row_star_count = 0
                # 세로줄빙고 판별
                if board[j][i] == chr(9733):
                    col_star_count += 1
                    if col_star_count == N:
                        bingoTotal += 1
                        col_star_count = 0
            # 왼쪽에서 오른쪽으로 내려가는 대각선빙고 판별
            if board[i][i] == chr(9733):
                diagonal_left_star_count += 1
                if diagonal_left_star_count == N:
                    bingoTotal += 1
                    diagonal_left_star_count = 0
            # 오른쪽에서 왼쪽으로 올라가는 대각선빙고 판별
            if board[i][N - i - 1] == chr(9733):
                diagonal_right_star_count += 1
                if diagonal_right_star_count == N:
                    bingoTotal += 1
                    diagonal_right_star_count = 0
# 빙고게임 시작
print("===================빙고게임 시작===================")
while True:
   
   userInput = int(input("정수를 입력하시오 : "))

   # 사용자가 입력한 숫자가 board에 있으면 "별모양"으로 변환
   for i in range(N):
       for j in range(N):
           if board[i][j] == userInput:
               board[i][j] = chr(9733)
               break

   # 빙고 판별 함수 judgeBingo() 실행
   judgeBingo()

   # 빙고가 3개 이상이면 빙고판을 출력하고나서 while문 탈출
   if bingoTotal >= 3:
        for i in range(N):
          for j in range(N):
              print("%3s"%(board[i][j]),end="  ")
          print()
        print("************************************************")
        print("*************** ! ! ! BINGO ! ! !***************")
        print("************************************************")
        break     
   # 별모양이 찍힌 빙고판 출력
   for i in range(N):
        for j in range(N):
            print("%3s"%(board[i][j]),end="  ")
        print()
   print('현재 {}빙고'.format(bingoTotal))

   # 83번줄 break 문에 걸리지 않으면 빙고판별 이후 bingoTotal변수가 재사용 되기 때문에 항상 0으로 초기화 함.
   bingoTotal = 0