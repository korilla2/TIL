import random


def findMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if ary[minIdx] > ary[i]:
            minIdx = i
    return minIdx


# testAry = [55, 88, 33, 77]
before = [random.randint(10, 99) for _ in range(20)]
after = []

print('정렬 전-->', before)
for i in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del before[minPos]

print('정렬 후-->', after)
