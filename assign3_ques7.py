#QUES7
#fibonacci sequence
first_term=int(input("give a number-"))
second_term=int(input("give a number-"))
#now it will keep on printing the sequence till you say y and to stop it say n
sum=first_term+second_term
series=[first_term,second_term]
n="y"
while(n=="y"):
    series.append(series[len(series)-1]+series[len(series)-2])
    print(series)
    n=input("give y to continue and n to stop going further-")
print("now we got a list having a fibonacci series-")
print(series)
#now lets find average of the resultant fibonacci series
sum=0
for i in series:
    sum=sum+i
print("average of the sequence-")
print(sum/len(series))
print("done!")
