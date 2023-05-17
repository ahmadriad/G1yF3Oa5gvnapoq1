from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px

data= pd.read_csv("C:/Users/97155/Downloads/ACME-HappinessSurvey2020.csv")

features = data.drop(["Y", "X2", "X4", "X3"], axis=1)
target = data['Y']

seed = 1
np.random.seed(seed)
test_size = .25
x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=test_size, random_state=seed)

np.random.seed(seed)

clf = RandomForestClassifier(criterion='gini'
                             , max_depth=10
                             , min_samples_split=6
                             , random_state=seed)

clf.fit(x_train, y_train)
RandomForestClassifier(max_depth=10, min_samples_split=6, random_state=1)
np.random.seed(seed)
sets = ["Training", "Testing"]
x_sets = [x_train, x_test]
y_sets = [y_train, y_test]
sources_clf = {}
for i in range(0, 2):
    y_pre_cls = clf.predict(x_sets[i])
    acc = accuracy_score(y_sets[i], y_pre_cls)
    sources_clf[sets[i]] = acc

sources_clf
{'Training': 0.7659574468085106, 'Testing': 0.75}
x_values = list(sources_clf.keys())
y_values = list(sources_clf.values())
plt.plot(x_values, y_values)


y_pre = clf.predict(x_test)

plt.hist(y_pre, label="Predited")

plt.hist(y_test, alpha=0.5, label="Actual value", bins=30)
plt.xlabel("Happiness")
plt.legend()


