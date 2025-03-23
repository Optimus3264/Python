#Write a program to calculate grade based on marks range
#where 90+=A, 80-89=B, 70-79=C, 60-69-D, 60<=F

Marks=int(input('Enter marks:'))
if  Marks>90 or Marks==90:
    print('Grade is A')
elif Marks>79 and Marks<90:
    print('Grade is B')
elif Marks>69 and Marks<80:
    print('Grade is C')
elif Marks>59 and Marks<70:
    print('Grade is D')
else:
    print('Grade is F')