name = ['STAR','lala',"hhh"]

def normalize(name):
    if not isinstance(name,str):
        raise TypeError("name type not str")
    print(name)

L = map(normalize,name)
