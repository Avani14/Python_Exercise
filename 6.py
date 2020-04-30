def add(n1,n2): return n1+n2
def sub(n1,n2): return n1-n2
def calculate(operation,n1,n2): return operation(n1,n2)
result = calculate(add,1,2)
print(result)
