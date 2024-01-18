import pandas as pd
import numpy as np

#Series.map()
data1 = pd.Series(['c','c++','java','python',np.nan])
print(data1.map({'c':'primary'}))

'''
Series.std()  standard deviation
syntax -> Series.std(axis=None, skipna=None, level=None, ddof=1, numeric_only=None, **kwargs)
'''
print(np.std([4,7,2,1,6,3]))
print(np.std([6,9,15,2,-17,15,4]))

'''
Series.to_frame()
syntax -> Series.to_frame(name=None)  
'''
s = pd.Series(["a", "b", "c"],
name="vals")
print(s.to_frame())