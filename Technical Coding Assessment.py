l = []
n = int(input("Enter the size of list :-"))
for i in range(0,n):
    ele = input("Enter the value of string :-")
    l.append(ele)
print(l)
l.sort(key=lambda x:x[-2])
print(l)