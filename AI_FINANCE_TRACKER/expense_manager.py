import pandas as pd
from database import get_transactions

def get_dataframe():

    data = get_transactions()

    df = pd.DataFrame(data, columns=[
        "id","type","amount","category","description","date"
    ])

    return df