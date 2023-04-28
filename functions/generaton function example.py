def print_big_enough(lst:list=[],number: int=0)-> int:
    """the list a retuen numbers bigger than seccend parameter
    and it will itrabble """
    if not isinstance(lst,list) or not isinstance(number,int):
        raise TypeError("worning!!!input a right values")
    for i in lst:
        if i > number:
            yield i