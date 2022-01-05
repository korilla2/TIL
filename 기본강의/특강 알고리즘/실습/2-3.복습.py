class Node():
    def __init__(self):
        self.data = None
        self.next = None


def printnode(head):
    current = head
    print(current.data, end=' ')
    while current.next is not None:
        current = current.next
        print(current.data, end=' ')
    print()


def insert_node(finddata, insertdata):
    global head, current, pre
    if head.data == finddata:
        node = Node()
        node.data = insertdata
        node.next = head
        head = node
        return
    current = head
    while current.next is not None:
        pre = current
        current = current.next
        if current.data == finddata:
            node = Node()
            node.data = insertdata
            node.next = current
            pre.next = node
            return
    node = Node()
    node.data = insertdata
    current.next = node
    return


head, current, pre = None, None, None

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
node = Node()
node.data = my_list[0]
head = node

for data in my_list[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.next = node

printnode(head)
insert_node(5, 999)
printnode(head)
