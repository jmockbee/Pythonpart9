year = int(input("Enter a year: "))
if  year % 4!= 0:
    print ("common")

elif year % 100!= 0:
    print ("leap year")

elif year % 400!= 0:
    print ("common")
else:
    print('leap')
print("The year is :", year)