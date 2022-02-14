#QUES5
word="ABCDEFGHIJK"
counter=1
#we first identify the pattern which says that
#we need to first leave gaps equal to (counter-1) where counter tells
#the row no. and the alphabets should decrease after every row
while(counter<7):
    print(" "*(counter-1),word[0:11-((counter-1)*2)])
    counter=counter+1
print("done!")
