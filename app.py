import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Computer Systems & AI Management", layout="wide")

# ====================================================================
# 🏆 SYMMETRICAL CORPORATE BRANDING BANNER
# ====================================================================
logo_left_col, title_center_col, logo_right_col = st.columns()

with logo_left_col:
    try:
        st.image("LOGOB.png", use_container_width=True)
    except:
        st.caption("🔹 LOGOB Staging")

with title_center_col:
    st.markdown("<h1 style='text-align: center; margin-top: 10px;'>🖥️ Computer Systems and AI Management Cockpit</h1>", unsafe_html=True)

with logo_right_col:
    try:
        st.image("LOGOG.png", use_container_width=True)
    except:
        st.caption("🔸 LOGOG Staging")

st.markdown("---")

# ====================================================================
# PHASE 1: SINGLE-FILE INGESTION (Bypasses broken directory caches)
# ====================================================================
@st.cache_data
def load_baseline_file():
    # Force the app to ONLY look at the one file we know is stable
    target_file = "enterprise_retail_dataT.xlsx"
    try:
        return pd.read_excel(target_file)
    except Exception as e:
        st.error(f"Could not open reference file: {e}")
        return pd.DataFrame()

df_raw = load_baseline_file()

# ====================================================================
# PHASE 2: DATA RENDERING
# ====================================================================
st.header("🗃️ Enterprise Data Vault Selector")

if not df_raw.empty:
    df = df_raw.copy()
    df.columns = [str(c).strip() for c in df.columns]
    
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.strip()
            
    st.markdown("### 📊 Currently Active File: `enterprise_retail_dataT.xlsx`")
    st.markdown("---")
    
    st.sidebar.header("🎯 Dashboard Control Filters")
    filtered_df = df.copy()
    
    if 'Region' in filtered_df.columns:
        region_options = sorted(list(filtered_df['Region'].unique()))
        selected_region = st.sidebar.multiselect("Select Region", options=region_options, default=region_options, key="reg_widget")
        filtered_df = filtered_df[filtered_df['Region'].isin(selected_region)]
        
    if 'Retailer' in filtered_df.columns:
        retailer_options = sorted(list(filtered_df['Retailer'].unique()))
        selected_retailer = st.sidebar.multiselect("Select Retailer", options=retailer_options, default=retailer_options, key=f"ret_widget")
        filtered_df = filtered_df[filtered_df['Retailer'].isin(selected_retailer)]
        
    total_txns = len(filtered_df)
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="📦 Total Ingested Record Rows", value=f"{total_txns:,}")
    with col2:
        st.metric(label="📂 Total Linked Vault Files", value="1 (Isolated Mode)")
        
    st.markdown("---")
    
    if not filtered_df.empty:
        chart_col1, chart_col2 = st.columns(2)
        with chart_col1:
            st.subheader("🏆 Retailer Performance Rankings")
            st.bar_chart(filtered_df.groupby('Retailer')['Volume_USD'].sum().sort_values(ascending=False))
        with chart_col2:
            st.subheader("🔸 Revenue Vol by Market Sector")
            st.bar_chart(filtered_df.groupby('Market_Tier')['Volume_USD'].sum().sort_values(ascending=False))
            
    st.subheader("🔎 Ingested Database Record Stream")
    st.dataframe(filtered_df.head(100), use_container_width=True)
else:
    st.error("❌ Isolated file could not be fetched from GitHub repository structure.")
