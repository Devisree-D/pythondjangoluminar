num=int(input("enter a number : ")) #123 input any 3 digit number
result=0 #initialize a variable result
while(num>0): #set condition until num is equal or less than zero
    digit=num%10 # 123%10=3............12%10=2....1%10=1
    result=result+digit**3 #0+3^3=27... 27+2^3=35....35+1^3=36
    num=num//10 #123//10=12............12//10=1......1//10=0
print(result) #36