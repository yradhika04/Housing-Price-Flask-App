import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np

# read the data
df = pd.read_csv("housing.csv")
df[['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']] = \
    df[['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']].replace({'yes': 1, 'no': 0})
# df['furnishingstatus'] = df['furnishingstatus'].replace({'furnished': 0, 'semi-furnished': 1, 'unfurnished': 2})
df = pd.get_dummies(df, columns=['furnishingstatus'], drop_first=True)

X = df.drop(['price'], axis=1)
y = df['price']

# split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# fit a decision tree regressor on the training data
decision_tree = DecisionTreeRegressor()
decision_tree.fit(X_train, y_train)
# y_pred = decision_tree.predict(X_test)
# print(metrics.mean_absolute_error(y_pred, y_test))
# print(metrics.mean_squared_error(y_pred, y_test))

# plot feature importance
feature_importance = decision_tree.feature_importances_
sorted_idx = np.argsort(feature_importance)
plt.figure(figsize=(10, 6))
plt.barh(range(len(sorted_idx)), feature_importance[sorted_idx], align='center')
plt.yticks(range(len(sorted_idx)), X.columns[sorted_idx])
plt.xlabel("Feature Importance")
plt.ylabel("Feature")
plt.title("Feature Importance from Decision Tree Regressor")
plt.savefig('features.png')
plt.show()
