import pandas as pd

data = {
    'year': [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025],
    'impala_rustenburg_6e_koz': [1450,1320,1280,1250,1200,950,1275,1232,1198,1284,1275],
    'sibanye_rustenburg_4e_koz': [810,778,698,687,650,610,660,673,679,610,611],
    'impala_unit_cost_r_oz': [12000,13500,14800,15200,16500,18000,20922,21000,21500,20922,22491],
    'revenue_per_oz_r': [22000,18000,21000,24000,28000,22000,25257,25000,24000,25257,25172],
    'load_shed_days': [50,120,180,220,280,150,300,335,200,83,26],
    'pgm_fatalities': [22,18,19,16,21,18,22,19,22,19,19],
    'pt_price_usd_oz': [950,900,950,850,850,700,1100,950,1000,986,1286]
}

df = pd.DataFrame(data)
df.to_csv('data/processed/rustenburg_master_2015_2025.csv', index=False)
print("Master dataset created as CSV (simple & works on Windows)")
print(df)