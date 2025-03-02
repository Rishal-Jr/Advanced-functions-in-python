number1=[1,2,3]
number2=[4,5,6]
result=map(lambda x,y:x+y,number1,number2)
print("Addition of two lists:")
print(list(result))
num=[1,2,3,4,5]
def sqr(n):
    return n*n
squre=list(map(sqr,num))
print("Squres of nums")
print(squre)

