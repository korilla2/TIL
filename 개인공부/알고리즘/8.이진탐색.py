arr = list(range(1, 11))


def binary_search(arr, num):
    s_idx = 0
    e_idx = len(arr) - 1
    while True:
        m_idx = (s_idx + e_idx) // 2
        if s_idx > e_idx:
            return -1
        if num > arr[m_idx]:
            s_idx = m_idx + 1
        elif num < arr[m_idx]:
            e_idx = m_idx - 1
        else:
            return m_idx


print(arr)
print(binary_search(arr, 6))
print(binary_search(arr, 9))
print(binary_search(arr, 11))
