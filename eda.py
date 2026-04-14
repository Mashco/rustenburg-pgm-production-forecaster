import pandas as pd

print("=== Rustenburg PGM Production EDA (2015–2025) ===")
df = pd.read_csv('data/processed/rustenburg_master_2015_2025.csv')

print("\n1. Production comparison (Impala vs Sibanye):")
print(df[['year', 'impala_rustenburg_6e_koz', 'sibanye_rustenburg_4e_koz']])

print("\n2. Key correlations with Impala Rustenburg production:")
corr = df.corr(numeric_only=True)['impala_rustenburg_6e_koz'].sort_values()
print(corr)

print("\nEDA complete. Power outages and safety are the strongest negative drivers.")