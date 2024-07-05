list1=[]
N = int(input())

for i in range(N):
    command = input()
    list2 = command.split(" ")
    if list2[0] == 'insert':
        list1.insert(int(list2[1]),int(list2[2]))
    if list2[0] == 'remove':
        list1.remove(int(list2[1]))
    if list2[0] == 'print':
        print (list1)
    if list2[0] == 'pop':
        list1.pop()
    if list2[0] == 'append':
        list1.append(int(list2[1]))
    if list2[0] == 'reverse':
        list1.reverse()
    if list2[0] == 'sort':
        list1.sort()
