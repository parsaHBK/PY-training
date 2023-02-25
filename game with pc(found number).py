import random

name = input("waht is your name ? ")
minimom =(int(input("your minimom number in game?")))
maximom =(int(input("your maximom number in game?")))

order = input ("do u want use number to here or just want keep on your mine ? (here , keep)")
i = (int)
i = 0
if(order == "here"):
    c_ansewr = (int(input("use your number for i guess?")))

    while (True):
        i+=1
        ansewr = int(random.randint(minimom,maximom))
        print("my",i,"ansewr is:",ansewr) 
        if(ansewr == c_ansewr):                                                 #find ansewr
            print("im find ansewr " ,name,"hip hip horra!!ansewr is :",ansewr)
            break
        a = input ("its bigger or smaller ? (type bigger , smaller , quit): ")
        if(a == "bigger"):
            maximom = ansewr
        elif(a == "smaller"):
            minimom = ansewr
        elif(a == "quit"):
            print("ok this program is end !!")
            break
        else:
            print("please focous !!! eror you do worng !!!")

elif (order == "keep"):
    print("ok so if i find number u should tell me !")
    while (True):
        i+=1
        ansewr = int(random.randint(minimom,maximom))
        print("my",i,"ansewr is:",ansewr) 
        a = input ("its bigger or smaller ? (type bigger , smaller , found , quit): ")
        if(a == "found"):                                                       #find ansewr
            print("im find ansewr " ,name,"hip hip horra!!ansewr is :",ansewr)
            break
        elif(a == "bigger"):
            maximom = ansewr
        elif(a == "smaller"):
            minimom = ansewr
        elif(a == "quit"):
            print("ok this program is end !!")
            break
        else:
            print("please focous !!! eror you do worng !!!")
