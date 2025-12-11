num=123
num_str=str(num)
reversed_num=[]

for i in range(len(num_str)-1,-1,-1):
    reversed_num.append(num_str[i])

print('reversed_num:',reversed_num)
