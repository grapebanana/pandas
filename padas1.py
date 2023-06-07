###
import pandas as pd

dict_data = {'a':1,'b':2,'c':3}

sr= pd.Series(dict_data)

print(type(sr))

print('\n')
print(sr)
###  1-1
 
import pandas as pd
list_data= ['2019-01-02',3.14,'ABC',100,True]

sr= pd.Series(list_data)
print(sr)
###  1-2 

idx= sr.index
val=sr.values
print(idx)
print('\n')
print(val)
### 1-3

tup_data=('영인','2010-05-01','여','True')
sr= pd.Series(tup_data,index=['이름','생년월일','성별','학생여부'])
print(sr)

print(sr[0])
print(sr['이름'])

print(sr[[1,2]])
print('\n')
print(sr[['생년월일','성별']])

print(sr[1:2])
print('\n')
print(sr[['생년월일','성별']])
###

dict_data={'c0':[1,2,3],'c1':[4,5,6,],'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15]}

df = pd.DataFrame(dict_data)

print(type(df))
print('\n')
print(df)
###
