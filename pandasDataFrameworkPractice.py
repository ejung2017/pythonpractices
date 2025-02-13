import pandas as pd 
import seaborn as sns 

df = sns.load_dataset('titanic')

df1 = df[['sex', 'age']]
df2 = df[['fare', 'pclass']]

print(df1)
print(df2)

"""
[] vs ()

df[]
df.loc[]

.groupby() 
"""

"""
order matters 
CORRECT: 
df.groupby('sex')['fare'].mean()


df['fare'].groupby('sex').mean() # KeyError: 'sex'
df[['fare']] -> dataframe
df['fare'] -> series

df[['fare','sex']].groupby('sex').mean() 

ERRORS: 
df['fare'].groupby('sex').mean() # KeyError: 'sex' 
    # groupbu('sex') can not have an average value 
df['fare'].mean().groupby('sex') # AttributeError: 'numpy.float64' object has no attribute 'groupby'
    # fare.mean() can't be grouped by sex 
"""

# df.info()

# 25~35세 여성의 산 사람과 죽은 사람의 수를 알고 싶을 때는 어떻게 해야할까요?

# 만약 성별별로 (즉, 남자 여자 각각으로) 요금의 평균을 확인해보고 싶다면 어떻게 해야할까요?

# 한개 이상의 컬럼 데이터를 불러올때 (sex, age, fare)