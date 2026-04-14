import streamlit as st
import pandas as pd

st.title("🚀 Rustenburg PGM Production Forecaster")
st.markdown("**Impala vs Sibanye Rustenburg Production (2015–2025)**")

df = pd.read_csv('data/processed/rustenburg_master_2015_2025.csv')

st.line_chart(df.set_index('year')[['impala_rustenburg_6e_koz', 'sibanye_rustenburg_4e_koz']])

st.subheader("What-if Scenario for 2026")
load_shed = st.slider("Load-shedding days in 2026", 0, 365, 26)
impact = (load_shed / 26) * 8
st.write(f"**Predicted impact on Impala 2026 production**: -{impact:.1f}%")
st.caption("Advanced DS portfolio project for SA mining")