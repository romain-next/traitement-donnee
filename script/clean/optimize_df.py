import pandas as pd

def optimize_df(df):
    """
        Remplace les date par de vraies date et cherche à optimiser 
        les integer et float pour réduire leur taille
    """
    df_optimized = df.copy()
    for col in df_optimized.columns:
        if df_optimized[col].dtype == 'object':
            if "date" in col.lower():
                df_optimized[col] = pd.to_datetime(df_optimized[col], errors='coerce')
            elif df_optimized[col].nunique() < len(df_optimized) / 2:
                df_optimized[col] = df_optimized[col].astype('category')
        elif str(df_optimized[col].dtype).startswith('int'):
            df_optimized[col] = pd.to_numeric(df_optimized[col], downcast='integer')
        elif str(df_optimized[col].dtype).startswith('float'):
            df_optimized[col] = pd.to_numeric(df_optimized[col], downcast='float')

    return df_optimized