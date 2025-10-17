import pandas as pd
from script.clean.optimize_df import optimize_df
from script.clean.clean_outliers import clean_outliers

def clean_sto(filepath: str) -> pd.DataFrame:
    """
        Nettoie les data du sto et renvoie un dataframe propre
    """
    sto = pd.read_parquet(filepath)
    sto = sto.iloc[1:].copy()
    colsSto = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']

    for col in colsSto:
        sto[col] = pd.to_numeric(sto[col], errors='coerce')

    desired_start = pd.Timestamp("2023-01-01")
    offset_days = (desired_start - pd.Timestamp("1899-12-30")).days - sto['Date'].min()
    sto['Date'] = pd.to_datetime(sto['Date'] + offset_days, origin='1899-12-30', unit='D')
    sto = optimize_df(sto)
    sto = sto.sort_values(by="Date", ascending=True).reset_index(drop=True)
    sto = clean_outliers(sto, ["Open", "High", "Low", "Close", 'Volume'])


    return sto
