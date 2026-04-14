import pandas as pd
from prophet import Prophet
import warnings
warnings.filterwarnings('ignore')

print("=== Advanced ML Forecasting: Rustenburg PGM Production (FINAL FIXED) ===")

# Load data
df = pd.read_csv('data/processed/rustenburg_master_2015_2025.csv')

# Prepare Prophet format
df_prophet = df.rename(columns={'year': 'ds', 'impala_rustenburg_6e_koz': 'y'}).copy()
df_prophet['ds'] = pd.to_datetime(df_prophet['ds'].astype(str) + '-06-30')

# Add external regressors (advanced)
df_prophet['load_shed_days'] = df['load_shed_days'].values
df_prophet['pgm_fatalities'] = df['pgm_fatalities'].values
df_prophet['pt_price_usd_oz'] = df['pt_price_usd_oz'].values

# Train the model
m = Prophet(yearly_seasonality=True)
m.add_regressor('load_shed_days')
m.add_regressor('pgm_fatalities')
m.add_regressor('pt_price_usd_oz')
m.fit(df_prophet)

# Create future dataframe (2026-2028)
future = m.make_future_dataframe(periods=3, freq='YE')

# Add regressors correctly (historical values + future scenario)
future = future.merge(df_prophet[['ds', 'load_shed_days', 'pgm_fatalities', 'pt_price_usd_oz']], 
                      on='ds', how='left')

# Override the 3 future years with realistic 2026-2028 scenario
future.loc[future.index[-3:], 'load_shed_days'] = [26, 20, 15]
future.loc[future.index[-3:], 'pgm_fatalities'] = [18, 17, 16]
future.loc[future.index[-3:], 'pt_price_usd_oz'] = [1286, 1350, 1400]

# Generate forecast
forecast = m.predict(future)

print("\n2026–2028 Impala Rustenburg Production Forecast (low load-shed scenario):")
print(forecast[['ds', 'yhat']].tail(3).round(0))

print("\n SUCCESS! Advanced ML forecasting is now complete.")
print("   This is the technical highlight of your portfolio.")