import matplotlib.pyplot as plt

def cac40_important_value(df):
    """
        Trace un graph avec plusieurs variables importantes pour l'analyse
        notamment la volatilité, le prix moyen, le volume et le prix de fermeture
    """

    # Calcul de la volatilite
    df['Volatility'] = df['High'] - df['Low']
    df['Avg_Price'] = (df['High'] + df['Low']) / 2

    fig, ax1 = plt.subplots(figsize=(14,6))

    # Prix Close
    ax1.plot(df['Date'], df['Close'], color='blue', label='Close')
    ax1.plot(df['Date'], df['Avg_Price'], color='purple', linestyle='--', label='Avg Price')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Close', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.grid(True)

    # Axe pour le Volume
    ax2 = ax1.twinx()
    ax2.bar(df['Date'], df['Volume'], color='orange', alpha=0.3, label='Volume')
    ax2.set_ylabel('Volume', color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')

    # Axe pour la Volatilite
    ax3 = ax1.twinx()
    ax3.spines['right'].set_position(('outward', 60)) 
    ax3.plot(df['Date'], df['Volatility'], color='green', label='Volatility', linestyle='--')
    ax3.set_ylabel('Volatility', color='green')
    ax3.tick_params(axis='y', labelcolor='green')

    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    lines_3, labels_3 = ax3.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2 + lines_3, labels_1 + labels_2 + labels_3, loc='upper left')

    plt.title('Close, Volume, prix moyen et Volatility')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()