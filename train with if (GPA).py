GPA = (int(input("use number of GPA betwaen (0<GPA<20):")))

if (GPA > 0 and GPA <= 5):
    print("your GPA is: F")
elif (GPA > 5 and GPA <= 10):
    print("your GPA is: D")
elif (GPA > 10 and GPA <= 15):
    print("your GPA is: C")
elif (GPA > 15 and GPA <= 18):
    print("your GPA is: B")
elif (GPA > 18 and GPA <= 20):
    print("your GPA is: A")
else:
    print("eror !! read guide")