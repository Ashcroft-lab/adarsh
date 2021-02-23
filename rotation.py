list1 = list(input("enter valus of list ").split(" "))
iteration = int(input("enter iteration"))
for i in range(iteration):
    list1.insert(0,list1[-1])
    list1.pop()
print(list1)
