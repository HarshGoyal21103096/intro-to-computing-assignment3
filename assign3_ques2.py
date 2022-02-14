#QUES2
month=int(input("give month="))
if(month in[1,3,5,7,8,10,12]):
    day=int(input("give day="))
    if(1<=day<=31):
        year=int(input("give year="))
        if(1800<=year<=2025):
            print("date-",day,"/",month,"/",year)
            if(month==12 and day==31):
                print("next date-","1/1/",year+1)
            elif(day==31):
                print("next date-","1/",month+1,"/",year)
            else:
                print("next date-",day+1,"/",month,"/",year)
        else:
            print("invalid year")
    else:
        print("invalid date")
elif(month in[4,6,9,11]):
    day=int(input("give day-"))
    if(1<=day<=30):
        year=int(input("give year-"))
        if(1800<=year<=2025):
            print("date-",day,"/",month,"/",year)
            if(day==30):
                print("next date-","1/",month+1,"/",year)
            else:
                print("next date-",day+1,"/",month,"/",year)
        else:
            print("invalid year")
    else:
        print("invalid date")
elif(month==2):
    year=int(input("give year-"))
    if(1800<=year<=2025):
        day=int(input("give day-"))
        if(year%4==0):
            if(1<=day<=29):
                print("date-",day,"/",month,"/",year)
                if(day==29):
                    print("next date-","1/",month+1,"/",year)
                else:
                    print("next date-",day+1,"/",month,"/",year)
            else:
                print("invalid day")
        else:
            if(1<=day<=28):
                print("date-",day,"/",month,"/",year)
                if(day==28):
                    print("next date-","1/",month+1,"/",year)
                else:
                    print("next date-",day+1,"/",month,"/",year)
            else:
                print("invalid day")
    else:
        print("invalid year")
else:
    print("invalid month")
print("done!")
