from user_inputs import user_input
from make_number import make_number
from make_number import make_number_pc
def user_guesse():
    print("Guide!!!\nfocous on your type\nuse key words\nfor quit type(quit)")
    make_number(int(input("minumom number:")),int(input("maximom number:")))
def pc_guesse():
    print("Guide!!!\nfocous on your type\nuse key words\nfor quit type(quit)")
    make_number_pc(int(input("minumom number:")),int(input("maximom number:")))
def main():
    order=input("do u want you guesse a number and coumpioter find -->(pc)\nor\ndo u want coupioter guesse and you find -->(me)\nuse key!!!!")
    if order == "pc":
        user_guesse()
    elif order == "me":
        pc_guesse()
    else:
        return "Eror worning value!!"
main()