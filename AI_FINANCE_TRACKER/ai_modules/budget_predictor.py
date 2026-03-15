import numpy as np
from sklearn.linear_model import LinearRegression

def predict_spending(df):

    monthly = df.groupby("date")["amount"].sum()

    X = np.arange(len(monthly)).reshape(-1,1)
    y = monthly.values

    model = LinearRegression()
    model.fit(X,y)

    pred = model.predict([[len(monthly)]])

    return round(pred[0],2)