in_put="3[a2[c]]"
def decode(in_put):
    list1=in_put.replace("[",",").replace("]",",").split(",")
    p=0
    stack=[]
    for i in list1:
        if i.isdigit():
            p=int(i)
        elif i.isalpha():
            for j in range(0,p):
                stack.append(i)
        else:pass
    return "".join(stack)
print(decode(in_put))