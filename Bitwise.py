a=10 #Binary 1010
b=4 #Binary 0100

print('a=', a, 'in binary:', bin(a) )
print('b=', b, 'in binary:', bin(b))

#Bitwiwse AND
print('a & b=', a & b) # 1010 & 0100 = 0000 (0)

#Bitwise OR
print('a or b=', a | b) # 1010 | 0100 = 1110 (14)

#Bitwise XOR
print('a ^ b=', a ^ b) # 1010 ^ 0100 = 1110 (14)

#Bitwise NOT
print('~a=', ~a) # -(a+1) = -11 (inverts bits)

#Bitwise Left shift
print('a << 1=', a << 1) # 10100 (20)

#Bitwise Right shift
print('a >> 1=', a >> 1) # 0101 (5)