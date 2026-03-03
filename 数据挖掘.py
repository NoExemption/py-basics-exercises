import numpy as np
import pandas as pd

data = {
    "目标": [70,68,87,96,58,62,78,68,84,96],
    "A因素": [0.85,0.75,0.69,0.70,0.43,0.52,0.72,0.62,0.81,0.89],
    "B因素": [1.78,1.96,1.82,1.62,1.78,1.96,1.53,1.89,1.72,1.63]
}

df = pd.DataFrame(data)
corr = df.corr()
print(corr)