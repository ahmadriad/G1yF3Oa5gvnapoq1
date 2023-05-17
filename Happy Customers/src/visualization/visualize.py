import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px
data= pd.read_csv("C:/Users/97155/Downloads/ACME-HappinessSurvey2020.csv")
plt.hist(data[data.columns[0]],color="black")
plt.xlabel("Happiness")
plt.ylabel("Count")
px.box(data,x=data["Y"],y=data[data.columns[1]]).update_traces(marker_color="black").update_layout(template="seaborn")
px.box(data,x=data["Y"],y=data[data.columns[2]]).update_traces(marker_color="black").update_layout(template="seaborn")
px.box(data,x=data["Y"],y=data[data.columns[3]]).update_traces(marker_color="black").update_layout(template="seaborn")
px.box(data,x=data["Y"],y=data[data.columns[4]]).update_traces(marker_color="black").update_layout(template="seaborn")
px.box(data,x=data["Y"],y=data[data.columns[5]]).update_traces(marker_color="black").update_layout(template="seaborn")
px.box(data,x=data["Y"],y=data[data.columns[6]]).update_traces(marker_color="black").update_layout(template="seaborn")
corr=data.corr()



sb.heatmap(corr,annot=True, fmt=".2f")
