
playerhp = 50
playerattack = 5
a = {'name:소형선', 'hp:50','attack:1'}
b = {'name':'중형선', 'hp':'150','attack':'5'}
c = {'name':'대형선', 'hp':'300','attack':'10'}
enemy = [a,b,c]

print("갤러그 게임 시작")
print("난이도를 설정해주세요")
print("1. 쉬움 2.보통 3.어려움")
difficulty = input("난이도를 입력해주세요: ")
if difficulty == "1":
    hp=50
    attack=1
    print("적 비행기 발생")
    print("적 비행기 정보",enemy[0])
    while True:
        print("1. 발사 2. 오른쪽이동 3. 왼쪽이동")
        number = input("숫자를 입력하세요: ")
        print("당신의 입력값?", number)
# 만약에 1번을 누르면 총알 발사
        if number == "1":
            print("총알을 발사합니다.")
            hp=hp-playerattack
            print("상대의 체력",hp)
            print("상대가 아군을 공격합니다.")
            playerhp = playerhp - attack
            print("당신의 체력:",playerhp)
# 만약에 2번을 누르면 오른쪽이동
        if number == "2":
            print("오른쪽으로 이동하였습니다.")
            print("이동하는 동안 기체를 수리하였습니다.")
            playerhp = playerhp + 5
            print("당신의 체력 :",playerhp)
# 만약에 3번을 누르면 왼쪽이동
        if number == "3":
            print("왼쪽으로 이동하였습니다.")
            print("이동하는 동안 기체를 수리하였습니다.")
            playerhp = playerhp + 5
            print("당신의 체력 :",playerhp)
        if hp == 0:
            print("적기를 파괴하였습니다.")
            print("게임에서 승리하였습니다.")
            break
        
        if playerhp == 0:
            print("아군 비행기가 파괴되었습니다.")
            print("게임에서 패배하였습니다...")
            break
if difficulty == "2":
    hp=150
    attack=5
    print("적 비행기 발생")
    print("적 비행기 정보",enemy[1])
    while True:
        print("1. 발사 2. 오른쪽이동 3. 왼쪽이동")
        number = input("숫자를 입력하세요: ")
        print("당신의 입력값?", number)
# 만약에 1번을 누르면 총알 발사
        if number == "1":
            print("총알을 발사합니다.")
            hp=hp-playerattack
            print("상대의 체력",hp)
            print("상대가 아군을 공격합니다.")
            playerhp = playerhp - attack
            print("당신의 체력:",playerhp)
# 만약에 2번을 누르면 오른쪽이동
        if number == "2":
            print("오른쪽으로 이동하였습니다.")
            print("이동하는 동안 기체를 수리하였습니다.")
            playerhp = playerhp + 5
            print("당신의 체력 :",playerhp)
# 만약에 3번을 누르면 왼쪽이동
        if number == "3":
            print("왼쪽으로 이동하였습니다.")
            print("이동하는 동안 기체를 수리하였습니다.")
            playerhp = playerhp + 5
            print("당신의 체력 :",playerhp)
        if hp == 0:
            print("적기를 파괴하였습니다.")
            print("게임에서 승리하였습니다.")
            break
        
        if playerhp == 0:
            print("아군 비행기가 파괴되었습니다.")
            print("게임에서 패배하였습니다...")
            break
if difficulty == "3":
    hp=300
    attack=10
    print("적 비행기 발생")
    print("적 비행기 정보",enemy[2])
    while True:
        print("1. 발사 2. 오른쪽이동 3. 왼쪽이동")
        number = input("숫자를 입력하세요: ")
        print("당신의 입력값?", number)
# 만약에 1번을 누르면 총알 발사
        if number == "1":
            print("총알을 발사합니다.")
            hp=hp-playerattack
            print("상대의 체력",hp)
            print("상대가 아군을 공격합니다.")
            playerhp = playerhp - attack
            print("당신의 체력:",playerhp)
# 만약에 2번을 누르면 오른쪽이동
        if number == "2":
            print("오른쪽으로 이동하였습니다.")
            print("이동하는 동안 기체를 수리하였습니다.")
            playerhp = playerhp + 5
            print("당신의 체력 :",playerhp)
# 만약에 3번을 누르면 왼쪽이동
        if number == "3":
            print("왼쪽으로 이동하였습니다.")
            print("이동하는 동안 기체를 수리하였습니다.")
            playerhp = playerhp + 5
            print("당신의 체력 :",playerhp)
        if hp == 0:
            print("적기를 파괴하였습니다.")
            print("게임에서 승리하였습니다.")
            break
        
        if playerhp == 0:
            print("아군 비행기가 파괴되었습니다.")
            print("게임에서 패배하였습니다...")
            break
        
