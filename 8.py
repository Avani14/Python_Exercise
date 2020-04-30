x={'a':1,'b':2}
y={'c':3}
z={**x,**y}
print(z)
z=dict(x, **y)
print(z)
