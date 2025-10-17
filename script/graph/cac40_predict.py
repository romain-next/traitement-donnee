import matplotlib.pyplot as plt

def predict_graph(df):
    """
        Trace la courbe qui permet de voir l'efficacite de la prediction
        en affichant en plus des courbes reelles, des indicteurs sur ce que
        le modèle à prévu
    """
    plt.figure(figsize=(14,6))

    # Trace du cours reel
    plt.plot(df['Date'], df['Close'], color='blue', label='Close Price')

    # Point ou on predit une hausse
    plt.scatter(
        df.loc[df['Prediction']==1, 'Date'],
        df.loc[df['Prediction']==1, 'Close'],
        color='green', marker='^', label='Up', s=100, alpha=0.7
    )

    # Point ou on predit une baisse
    plt.scatter(
        df.loc[df['Prediction']==0, 'Date'],
        df.loc[df['Prediction']==0, 'Close'],
        color='red', marker='v', label='Down', s=100, alpha=0.7
    )

    plt.title('CAC40 - Close Price et Prediction')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()