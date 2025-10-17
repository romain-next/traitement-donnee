import pandas as pd
from script.clean.optimize_df import optimize_df
from script.clean.clean_outliers import clean_outliers


def clean_cac40(filepath: str) -> pd.DataFrame:
    """
        Nettoie les data du cac40 et renvoie un dataframe propre
    """
    print("Clean CAC40")
    cac40 = pd.read_csv(filepath)
    colsCac40 = ['Open', 'High', 'Low', 'Close', 'Volume']
    for col in colsCac40:
        cac40[col] = pd.to_numeric(cac40[col], errors='coerce')
    
    cac40 = optimize_df(cac40)
    cac40 = cac40.sort_values(by="Date", ascending=True).reset_index(drop=True)
    cac40 = clean_outliers(cac40, ["Open", "High", "Low", "Close", "Volume"])
    return cac40
