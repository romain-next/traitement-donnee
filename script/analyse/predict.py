import numpy as np

def cac40_predict(df):
    """
       Applique l'algo de prediction et ajoute une colonne
       qui permet de savoir si on prevoir une hausse ou non.
       Calcul la precision également
    """
    df['Prediction'] = np.where(
        (df['MA_10'] > df['MA_20']) & (df['Momentum_20'] > 0), 1, 0
    )

    df['Actual'] = np.where(df['Close'].diff() > 0, 1, 0)

    cac40_eval = df.dropna(subset=['Prediction', 'Actual'])

    # Calcul de la precision
    accuracy = (cac40_eval['Prediction'] == cac40_eval['Actual']).mean()
    accuracy_percent = accuracy * 100

    print(f"accuracy : {accuracy:.2f} ({accuracy_percent:.2f}%)")

    return cac40_eval