def cal(operator,num1,num2): return operator(num1,num2)
result = cal(lambda n1,n2 : n1*n2,10,20 )
print(result)
