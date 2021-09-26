import os
import config
import numpy as np
import pandas as pd


A = np.random.rand(10,3)
B = np.random.rand(10,3)


A = np.random.rand(10,3)
B = np.random.rand(10,3)

df = pd.DataFrame(A)
df2 = pd.DataFrame(B)

df.to_csv(os.path.join(config.ROOT_DIR,'data','file.csv'))
df2.to_csv(os.path.join(config.ROOT_DIR,'data','file2.csv'))


print(df)