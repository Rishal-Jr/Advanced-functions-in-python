s1={1,2,3}
s2={'a','b','c'}
s3=list(zip(s1,s2))
print(s3,"\n")

list1=[10,20,30,40]
list2=[100,200,300,400]
for x,y in zip(list1,list2[::-1]):
    print(x,y)

stocks=['reliance','infoys','tcs']
prices=[2175,1125,4567] 
new_dict={stocks: prices for stocks,prices in zip(stocks,prices)}
print('\n{}'.format(new_dict))   