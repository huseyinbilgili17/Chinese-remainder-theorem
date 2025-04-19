listofdivisor=[5,9,11]
listofremainders=[4,5,7]
    
i=0
j=0
while len(listofremainders)!= 1:
    n1=listofdivisor.pop(0)
    n2=listofdivisor.pop(0)
    a=listofremainders.pop(0)
    b=listofremainders.pop(0)
    list1= [a%n2]
    list4= [a]
    while True:
        a += n1
        i = a%n2
        if i in list1:
            break
        list1.append(i)
        list4.append(a)
    c=0
    list2=[b%n1]
    list3=[b]
    while True:
        b += n2
        c= b%n1
        if c in list2:
            break
        list3.append(b)
        list2.append(c)
    for i in list3:
        if ((i%n1)==(a%n1)) & ((i%n2)==(b%n2)):
            break
    listofremainders.append(i)
    listofdivisor.append(n1*n2)
    print(listofdivisor)
    print(listofremainders)

print("Answer:")
print(i)

    