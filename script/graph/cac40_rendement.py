import numpy as np
import matplotlib.pyplot as plt

def cac40_rendement(df):
    """
        Trace un histogramme qui donne les rendements
    """
    df['Return'] = np.log(df['Close'] / df['Close'].shift(1))

    returns = df['Return'].dropna()

    plt.figure(figsize=(10,6))
    plt.hist(returns, bins=15, color='blue', alpha=0.7, edgecolor='black')
    plt.title('Distribution des rendements du CAC40')
    plt.xlabel('Rendement')
    plt.ylabel('Fréquence')
    plt.grid(True)
    plt.show()