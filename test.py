import pandas as pd
import numpy as np 
from collections import OrderedDict
df = pd.read_csv('movies.csv')

print(df.head())

df['budget'] = df['budget'].fillna(0)
df['gross']= df['gross'].fillna(0)
df['rating']= df['rating'].fillna(0)

#changing the data type
df['budget'] = df['budget'].astype('int64')
df['gross'] = df['gross'].astype('int64')



#parsing function

#release date parsing
#to check the validity of release date and year and create correct year column
df['released']=df['released'].astype(str)

df['released']= df['released'].apply(lambda x:x.split('(')[0])
df['Actual_release_year']= df['released'].str[-5:]


#dropping the year and released date from the data column as we wont be using them
df.drop(['year'],axis=1,inplace=True)
df.drop(['released'],axis=1,inplace=True)


#print(df.dtypes)

#check for outliers

import outlier as ot
outlier_result = ot.custom_summary(df)
print(outlier_result)