import matplotlib.pyplot as plt

def cac40_close(df):
    """
        Trace la courbe toute simple des valeurs de close dans le temps
    """
    plt.figure(figsize=(12,6))
    plt.plot(df["Date"], df["Close"], label="CAC40 Close", color="blue")
    plt.title("CAC40 - Evolution du Close")
    plt.xlabel("Date")
    plt.ylabel("Close")
    plt.grid(True)
    plt.legend()
    plt.show()