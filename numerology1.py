n=input("enter your date of birth(1-31) : ",)
def fun(n):
   if len(n) == 1 :
      return int(n)
   total = 0
   for i in n :
       total += int(i)
   return fun(str(total))

print("your life path number is ",fun(n))  


 

