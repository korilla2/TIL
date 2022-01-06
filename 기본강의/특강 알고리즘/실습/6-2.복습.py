class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


memory = []
root = None
dataAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

node = TreeNode()
node.data = dataAry[0]
root = node
memory.append(node)

for data in dataAry[1:]:
    node = TreeNode()
    node.data = data
    current = root
    while True:
        if data < current.data:
            if current.left == None:
                current.left = node
                break
            else:
                current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            else:
                current = current.right
    memory.append(node)

print('완료')

for i in memory:
    print(i.data, end=' ')
print()

# 탐색
find_data = '재남'

current = root
while True:
    if current.data == find_data:
        print(find_data, '찾음')
        break
    elif find_data < current.data:
        if current.left is None:
            print(find_data, '없음')
            break
        current = current.left
    else:
        if current.right is None:
            print(find_data, '없음')
            break
        current = current.right
print('end')
