topper_num= int(input())
sum_odd = 0
sum_even = 0
for i in range(len(str(topper_num))):
    if topper_num%2==0:
        remainder = topper_num%10
        topper_num= topper_num//10
        sum_even+= remainder
    elif topper_num %2!=0:
        remainder = topper_num%10
        topper_num = topper_num//10
        sum_odd+= remainder
if sum_odd==sum_even:
    print("true")
else:
    print("false")
        
    
