def revrese(lst: list=[])-> list:
    """
    a function catch a list
    than revrse the list
    return a list after reversed
    """
    temp = []
    if not isinstance(lst,list):
        raise TypeError("worning!!!input list please")
    for i in range (len(lst)-1,0-1,-1):
        temp.append(lst[i])
    return temp