def int_cheack(number_name:str="")-> int:
    """catch a name of number and return a integer"""
    lst_cheack=["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    for i in range(0,9+1):
        if lst_cheack[i] == number_name:
            return i
    return "Your name number have problem"
d=int_cheack("Two")
print(d)