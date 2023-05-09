name=input("use ure name :")
age= int(input("use ure age:"))
s = "the name of this user is %s and he is age %d" %(name,age)
print(s)
#can use (%s(str,int,flaot),%d(int),%f(flaot))
#SECEND WAY ANE NEW WAY WITH METHOD
s = "the name of this user is {0} and he is age {1}".format(name,age)
print(s)
"""more help on this link(https://docs.python.org/3.11/library/string.html?highlight=string#module-string)"""
