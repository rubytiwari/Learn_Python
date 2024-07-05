#-------------------Find out second minimum value in the list----------------------------
def mymini(list1):
    mini = list1[0]
    for i in range(n):
        if list1[i] < mini:
            mini = list1[i]
    return mini

n = int(input("Enter the number of elements in the list "))
list1 = []
for i in range(n):
    v1 = int(input("Enter the list element "))
    list1.append(v1)

mini = mymini(list1)
print("minimum number is = {}".format(mini))
secondmini = max(list1)
for i in range(n):
    if list1[i] > mini and list1[i] < secondmini :
        secondmini = list1[i]
print("second minimum number is = {}".format(secondmini))
