def cal_cal(mon_1, day_1, mon_2, day_2):
    cal_arr = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = 0
    day = 0
    for i in range(mon_1+1, mon_2):
        month += cal_arr[i]
    if mon_1 == mon_2:
        day += (day_2 - day_1 + 1)
    else:
        day += (cal_arr[mon_1] - day_1 + 1)
        day += day_2
    return month + day


T = int(input())

for i in range(T):
    cal = list(map(int, input().split()))
    result = cal_cal(cal[0], cal[1], cal[2], cal[3])
    print(f'#{i+1} {result}')
