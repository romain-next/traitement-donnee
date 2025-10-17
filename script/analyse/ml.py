import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


def ml(df):
    df = df.copy()
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date').reset_index(drop=True)

    df['MA_5'] = df['Close'].rolling(5).mean()
    df['MA_20'] = df['Close'].rolling(20).mean()

    df['EMA_5'] = df['Close'].ewm(span=5, adjust=False).mean()

    df['Momentum_5'] = df['Close'] - df['Close'].shift(5)

    df['ROC_5'] = df['Close'].pct_change(5)

    df['Volatility_5'] = df['Close'].pct_change().rolling(5).std()

    df['High_Low_Range'] = df['High'] - df['Low']

    df['Volume_SMA_5'] = df['Volume'].rolling(5).mean()
    df['Volume_SMA_10'] = df['Volume'].rolling(10).mean()

    df['Target'] = np.where(df['Close'].shift(-1) > df['Close'], 1, 0)

    features = ['MA_5', 'MA_20', 'EMA_5', 'Momentum_5', 'ROC_5',
                'Volatility_5', 'High_Low_Range', 'Volume_SMA_5', 'Volume_SMA_10']

    df_model = df.dropna(subset=features + ['Target'])

    X = df_model[features]
    y = df_model['Target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy du modele RandomForestClassifier: {accuracy:.2%}\n")
    print(classification_report(y_test, y_pred))
