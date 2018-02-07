def homework(x,*n):
    if len(n) == 0:
        raise TypeError("tuple is empty")
    else:
        for i in n:
            int(i)
            if not isinstance(i,(int,float)):
                raise TypeError("type must int or float")

    for i in n:
        x = x * i
        
    return x
