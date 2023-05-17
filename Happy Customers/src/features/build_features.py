import pandas as pd
import numpy as np

data= pd.read_csv("C:/Users/97155/Downloads/ACME-HappinessSurvey2020.csv")
features = data.drop(["Y","X2","X4","X3"],axis=1)
target = data['Y']