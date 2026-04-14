# Rustenburg PGM Production Forecaster

**Advanced Data Science Portfolio Project**  
**Focus**: Production Performance Analysis & ML Forecasting for Rustenburg Platinum Group Metals (PGM) Operations (2015–2025)

### Business Problem (South African Mining Context)
Rustenburg is the heart of global PGM production. Impala Rustenburg (deeper conventional shafts) experienced significant production pressure, declining from ~1,450 koz 6E (2015) to 1,275 koz (FY2025) due to Eskom load-shedding, safety stoppages, rising unit costs, and PGM price volatility. Sibanye Stillwater Rustenburg/Kroondal showed relatively better resilience through mechanisation.

This project analyses **production performance** as the core KPI and builds advanced ML forecasts incorporating power outages, safety incidents, and financial metrics.

### Key Features
- Real historical data (2015–2025) for Impala Rustenburg (6E) vs Sibanye Rustenburg (4E)
- EDA + correlation analysis (power outages and safety as strongest negative drivers)
- **Advanced ML Forecasting** using Prophet with exogenous regressors (load-shedding, fatalities, platinum price)
- Interactive "What-if" dashboard for scenario testing
- Rustenburg-specific insights relevant to Impala, Sibanye, and the broader SA mining industry

### Tech Stack
- Python, pandas, Prophet (advanced time-series forecasting)
- Feature engineering with external regressors
- Interactive visualisation with Streamlit

### Live Demo
[Open Interactive Dashboard](https://your-streamlit-link-here)  


### How to Run Locally
```bash
streamlit run reports/streamlit_app.py
