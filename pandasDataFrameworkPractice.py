import pandas as pd 
import seaborn as sns 

df = sns.load_dataset('titanic')

"""
[] vs ()

df[]
df.loc[]

.groupby() 
"""

# df.info()

# 25~35세 여성의 산 사람과 죽은 사람의 수를 알고 싶을 때는 어떻게 해야할까요?

# 만약 성별별로 (즉, 남자 여자 각각으로) 요금의 평균을 확인해보고 싶다면 어떻게 해야할까요?

# 한개 이상의 컬럼 데이터를 불러올때 (sex, age, fare)