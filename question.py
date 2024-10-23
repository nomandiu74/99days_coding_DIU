t=int(input())
l=[]
for _ in range(t):

    n=int(input())
    s=input()
    a=0
    b=0
    c=0
    d=0
    e=0
    for i in range(len(s)):
        if s[i]=='A':
            a+=1
        elif s[i]=='B':
            b+=1
        elif s[i]=='C':
            c+=1
        elif s[i]=='D':
            d+=1
        elif s[i]=='?':
            e+=1
    
    if a>n:
        a=n
    if b>n:
        b=n
    if c>n:
        c=n
    if d>n:
        d=n
    if a==0 and b==0 and c==0 and d==0 and e>0:
        l.append(0)
    else:
        l.append(a+b+c+d)
for i in range(len(l)):
    print(l[i])