import pandas as pd
L =[[1,2,3],[2,3,4],[3,4,5]]
df1 = pd.DataFrame(L, columns= ['Test1','Test2','Test3'], index = ['roll number1','roll number2','roll number3'])
df1

d = {'one': pd.Series([1,2,3]),'two':pd.Series([4,5,6])}
df2 = pd.DataFrame(d)
df2
df2['three']= pd.Series([6,7,8])     #ADDING TO TABLE


del df2['four']
df2.sum()
df2.mean()
(df1.reindex_like(df2, method = 'ffill'))



s = pd.Series(['ajay','Anish','TREHAN'])
s.str.lower()


#LOCATION
df.loc[:,['A','C']]
df.iloc[0:4,0:2]
df.groupby(['Year','Rank']).Points.sum()
print(pd.merge(df1,df2, on = ['id','subjectid']))

pd.concat([df1,df2], axis =0,ignore_index = True)
df1.append(df2)
df = df.set_index("Date")