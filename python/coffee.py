coffee = 10
while True:
    money = int(input("돈을 넣어주세요: "))
    if money >= 300:
        print("커피를 줍니다.")
        coffee = coffee -1
        print(f"거스름돈 {money-300} 입니다.")
        print(f"남은 커피는 {coffee}개 입니다.")
    else:
        print("돈을 돌려주고 커피를 주지 않습니다.")
    if coffee == 0:
        print("끝")
        break