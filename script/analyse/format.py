def cac40_format_analyse(df):
    """
       Calcul des données importante pour la prediction
    """
    # Moyennes mobiles
    df['MA_10'] = df['Close'].rolling(window=10).mean()
    df['MA_20'] = df['Close'].rolling(window=20).mean()

    # Momentum long sur 20 jours
    df['Momentum_20'] = df['Close'] - df['Close'].shift(20)

    df.to_parquet('data/clean/cac40_format.parquet')

    return df