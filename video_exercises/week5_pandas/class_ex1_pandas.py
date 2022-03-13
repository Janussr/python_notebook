import pandas as pd
import numpy as np

#This is our 2d example we slice in this assignment
data = np.array([['','Col1','Col2','col3'],
                ['Row1',1,2,3],
                ['Row2',4,5,6],
                ['Row3',7,8,9]])

#Made this to a variable, in order to do stuff with it like .iloc
df = pd.DataFrame(data=data[1:4,1:4], columns=data[0,1:4], index=data[1:4,0])


print(df)

#Make slices of data:

# second column using column name

print(df['Col2'])

# third column using column index (.iloc[])


print(df.iloc[:,2])

# slice element at third row of second column (use .iloc())

print(df.iloc[2,1])