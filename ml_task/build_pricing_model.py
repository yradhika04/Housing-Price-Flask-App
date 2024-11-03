import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import joblib

# read the data
df = pd.read_csv("housing.csv")

# only keeping the top 4 most imp features
# area, bedrooms, bathrooms, parking
X = df.drop(['price', 'stories', 'mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning',
             'prefarea', 'furnishingstatus'], axis=1, inplace=False)
y = df['price']

# train a decision tree on the entire data
decision_tree = DecisionTreeRegressor()
model = decision_tree.fit(X, y)

with open('../decision_tree.joblib', 'wb') as f:
    joblib.dump(model, f)
