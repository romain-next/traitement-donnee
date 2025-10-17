import pandas as pd
from script.clean.cac40 import clean_cac40
from script.clean.sto import clean_sto
from script.graph.cac40_predict import predict_graph
from script.analyse.format import cac40_format_analyse
from script.analyse.predict import cac40_predict
from script.analyse.ml import ml

pd.set_option('display.max_columns', None)

# Chargement des datasets et nettoyage
cac40 = clean_cac40("data/raw/cac40.csv")
sto = clean_sto("data/raw/STO.parquet")

# Apercu
print("=== CAC40 ===")
print(cac40.info())
print(cac40.head(20), "\n")

print("=== STO ===")
print(sto.head(10), "\n")
print(sto.info())

# Vérification des valeurs manquantes
print("=== Valeurs manquantes ===")
for name, df in [("cac40", cac40), ("sto", sto)]:
    print(f"\n{name}:")
    print(df.isna().sum())

# Vérification de la période temporelle
for name, df in [("cac40", cac40), ("sto", sto)]:
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        print(f"\n{name}: {df['Date'].min()} => {df['Date'].max()}")

# formatage pour la prediction
cac40 = cac40_format_analyse(cac40)

# calcul de la prediction
cac40Predict=cac40_predict(cac40)

# affichage du graph avec les prédicions
predict_graph(cac40Predict)

# prediction avec un meilleur modele
ml(cac40Predict)