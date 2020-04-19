import pandas as pd
from matplotlib import pyplot as plt

#### Creating df. You can turn any dicitonary with list values as a dataframe.

dfA = pd.DataFrame({'A':[1,2,3,4]})
dfB = pd.DataFrame({'B':[5,6,7,8]})
dfZ = pd.DataFrame({'D':[22,23,24,25]})

# print(dfA)
# print(dfB)

C = {'C':['hustle','bustle','biddily','bop'],'D':['yodle','bodle','grumble','bumble']}
dfC = pd.DataFrame(C)
print('dfC',dfC)


#### Joining two df.

dfD = pd.concat([dfA,dfB], axis = 0) #Joins two dfs vertically by index
print('dfD: ',dfD)
dfE = pd.concat([dfA,dfB], axis = 1)
print('dfE: ',dfE)

dfF = pd.concat([dfE,dfC], axis = 0) #default axis is 0 columns
print('dfF: ',dfF)

dfG = pd.concat([dfE,dfC], axis = 1)
print('dfG: ',dfG)


#df = df[df['Column Name'].isin(list of values)] finds all rows with values in a list.


#### TRANSPOSING THE df.

dfH = dfE.T
print('dfE.T: ',dfH)


#### Group by function ####

df = pd.DataFrame({'a':['oregon','oregon','Washington','Washington'],'b':[1,2,4,3]})
print(df)
print(df.groupby('a').sum())

df1 = df.set_index('a')
df1 = df.reset_index()
print("df1: ",df1)


#### Plotting multiple scatter plots
df = pd.concat([dfE,dfZ], axis = 1)
print(df)
ax1 = df.plot(x = 'A', y = 'B',kind = 'scatter', c = 'D')
df.plot(x = 'A', y = 'D', kind = 'scatter',c = 'B', ax = ax1)

plt.show()
