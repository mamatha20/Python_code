def birthdayCakeCandles(s):
    i=1
    l=[]
    while i<=s:
        num=int(input("enter your number ="))
        l.append(num)
        i+=1
    print(l)
    j=0
    max=0
    while j<len(l):
        if max<l[j]:
            max=l[j]
        j+=1
    print(max)
    k=0
    c=0
    while k<len(l):
        if max==l[k]:
            c+=1
        k+=1
    print(c)
birthdayCakeCandles(s=int(input("enter your number")))
