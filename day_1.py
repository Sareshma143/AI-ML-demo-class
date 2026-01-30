
import numpy as np
import pandas as pd 

#numpy
arr=np.array([10,20,30,40])
print("array",arr)
print("Mean",np.mean(arr))
print("sum",np.sum(arr))

#pandas
data={
    "Name":["A","B","C","D"],
    "Marks":[80,85,90,95]
}
df=pd.DataFrame(data)
print(df)
df.describe()

