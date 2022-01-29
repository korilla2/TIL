T = int(input())

for i in range(T):
    time = list(map(int, input().split()))

    hour = time[0] + time[2]
    minute = time[1] + time[3]

    if minute >= 60:
        minute = minute - 60
        hour += 1

    if hour > 12:
        hour = hour - 12

    print(f'#{i+1} {hour} {minute}')
