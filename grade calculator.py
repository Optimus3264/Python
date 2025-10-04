#Grade calculator
#write a program that takes a students marks and assigns a grade based on this scale :
#90+=A , 80-89=B , 70-79=C , 60-69=D, <60=F

a = int(input('enter a marks: '))
if a>90:
    print('grade is A')

elif a>79 and a<90:
    print('grade is B')

elif a>69 and a<80:
    print('grade is C')

elif a==60 and a<70:
    print('grade is D')

else :
    print('grade is F')

    
