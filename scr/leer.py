import pandas as pd


def leer_datos(path):
    df=pd.read_csv(path)
    return df





if __name__ == "__main__":
    df=leer_datos('data/books.csv')
    print(df.head())


