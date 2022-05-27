def Func2(a:list, b:str, c:int):
    if len(a) > c and c >= 0:
        a.insert(c, b)
    else:
        return "paste operation is not possible"

