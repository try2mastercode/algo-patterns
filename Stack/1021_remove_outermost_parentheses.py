text="(()())(())"#input(":")
def fun(t):
    s=[]
    count=0
    for  i in t:
        if i=="(":
            if count>0:
                s.append(i)
            count+=1
        else :
            count-=1
            if count>0:
                s.append(i)
    return "".join(s)
print(fun(text))
