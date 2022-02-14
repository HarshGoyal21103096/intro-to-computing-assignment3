#QUES1
string1=input("give a string=")
list1=[]
list2=string1.split()
y=len(list2)
d=dict()
t=dict()
if len(list2)==1:              #it is for 1 word
    for i in string1:          #here i creates a list with the characters
        list1.append(i)
    for j in list1:            #here i created a condition where all unique keys
        if j in d:             #get value 1 and when a key repeats it increases
            d[j]=d[j]+1        #value by 1
        else:
            d[j]=1
    print(d)
else:
    for i in list2:           #this is for multiple words
        if i in t:
            t[i]=t[i]+1
        else:
            t[i]=1
    print(t)
    print("done!")
    
