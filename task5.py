a=input("enter month")
if  a=='jan' or a=='march' or a=='may' or a=='july' or a=='aug' or a=='oct' or a=='dec':
    print(31)
elif a=='april' or a=='june' or a=='sep' or a=='nov':
    print(30)
elif a=='feb':
    print(28)
else:
    print("error")
    