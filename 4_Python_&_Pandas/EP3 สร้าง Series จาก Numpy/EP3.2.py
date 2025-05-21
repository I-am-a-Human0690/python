import pandas as pd
ps = pd.Series([1,2,3,4])
print(ps,type(ps))
b = [1,2,3,4]
a = pd.Series(b)
print(a,type(a))
r=([1,23,],[1,2,3])
O=[[1,23,],[1,2,3]]
print(type(r),type(O))