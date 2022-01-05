# 함수부
def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen - 1] = friend


def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen - 1, position, -1):
        katok[i] = katok[i - 1]
        katok[i - 1] = None
    katok[position] = friend


def delete_data(position):
    katok[position] = None
    kLen = len(katok)
    for i in range(position + 1, kLen):
        katok[i-1] = katok[i]
        katok[i] = None
    del katok[kLen - 1]


katok = []

if __name__ == '__main__':
    while True:

        select = int(input('선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)-->'))

        if select == 1:
            data = input('추가할 데이터 -->')
            add_data(data)
            print(katok)
        elif select == 2:
            pos = int(input('삽입할 위치 -->'))
            data = input('추가할 데이터 -->')
            insert_data(pos, data)
            print(katok)
        elif select == 3:
            pos = int(input('삭제할 위치 -->'))
            delete_data(pos)
            print(katok)
        elif select == 4:
            print(katok)
            break
        else:
            print('1 ~ 4 사이의 숫자를 입력하세요')
