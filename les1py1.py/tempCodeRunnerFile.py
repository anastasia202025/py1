a=int(input())  #123
a1= a//100      # нахождение 1 цифры числа
a2= (a%100)//10 # нахождение 2 цифры числа
a3 = a%10       # нахождение 3 цифры числа
print(a1+a2+a3)