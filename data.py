import pandas as pd
import numpy as np 
df = pd.read_csv('movies.csv')

print (df.head())

#data cleaning

# to check for missing data

for col in df.columns:
    point_missing =np.mean(df[col].isnull())
    print('{} - {}%'.format(col,point_missing))




#replacing the nan column in budget and gross
df['budget'] = df['budget'].fillna(0)
df['gross']= df['gross'].fillna(0)

#changing the data types of the budget and gross column to int

df['budget'] = df['budget'].astype('int64')
df['gross'] = df['gross'].astype('int64')

#checking datatypes for the columns:
print(df.dtypes)



#release date parsing
#to check the validity of release date and year and create correct year column
df['released']=df['released'].astype(str)

df['released']= df['released'].apply(lambda x:x.split('(')[0])
df['Actual_release_year']= df['released'].str[-5:]


#dropping the year and released date from the data column as we wont be using them
df.drop(['year'],axis=1,inplace=True)
df.drop(['released'],axis=1,inplace=True)



#sorting the dataframe by gross column
#pd.set_option('display.max_rows',None)
df.sort_values(by=['gross'],inplace=False,ascending=False)


#checking duplicates in each column of the dataframe
for col in df.columns:
    df[col].drop_duplicates().sort_values(ascending=False)
    


#checking for descriptive function in the dataframe
import outlier as ot
descriptive_stat = ot.custom_summary(df)
print(descriptive_stat)






#checking the final df
print(df)

df.to_csv('cleaned_movie_data.csv',index=False)


