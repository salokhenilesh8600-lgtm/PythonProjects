from sklearn.ensemble import IsolationForest

def detect_fraud(df):

    X = df[["amount"]]

    model = IsolationForest(contamination=0.05)

    df["fraud"] = model.fit_predict(X)

    frauds = df[df["fraud"] == -1]

    return frauds