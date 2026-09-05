import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Enterprise Metrics Cockpit", layout="wide")

# 🏆 Title Banner
st.title("🛡️ Chieftess AI - Enterprise Operations Cockpit")
st.markdown("---")

# 📂 Load the Data Local to the Container
data_folder = '.'
all_files = [os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.lower().endswith(('.xlsx', '.xls'))]

database = {}
for file_path in all_files:
    file_name = os.path.basename(file_path)
    table_name = os.path.splitext(file_name)[0]
    try:
        database[table_name] = pd.read_excel(file_path)
    except:
        pass

# 🚨 Verify Main Table is Loaded
if 'enterprise_retail_dataT' in database:
    df = database['enterprise_retail_dataT']

    # 📈 Interactive Sidebar Filters
    st.sidebar.header("🎯 Dashboard Control Filters")
    selected_region = st.sidebar.multiselect("Select Region", options=df['Region'].unique(), default=df['Region'].unique())
    selected_retailer = st.sidebar.multiselect("Select Retailer", options=df['Retailer'].unique(), default=df['Retailer'].unique())

    # Apply Filters Dynamically
    filtered_df = df[(df['Region'].isin(selected_region)) & (df['Retailer'].isin(selected_retailer))]

    # 📊 Top-Level Summary Cards (KPIs)
    total_vol = filtered_df['Volume_USD'].sum()
    total_txns = len(filtered_df)

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="💰 Total Combined Sales Volume", value=f"${total_vol:,.2f}")
    with col2:
        st.metric(label="📦 Total Ingested Transactions", value=f"{total_txns:,}")

    st.markdown("---")

    # 📊 Layout Charts Columns
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.subheader("🏆 Retailer Performance Rankings")
        retailer_sales = filtered_df.groupby('Retailer')['Volume_USD'].sum().sort_values(ascending=False)
        st.bar_chart(retailer_sales)

    with chart_col2:
        st.subheader("🔸 Revenue Vol by Market Sector")
        tier_sales = filtered_df.groupby('Market_Tier')['Volume_USD'].sum().sort_values(ascending=False)
        st.bar_chart(tier_sales)

    # 🗒️ Raw Data Audit Grid
    st.subheader("🔎 Ingested Database Record Stream")
    st.dataframe(filtered_df.head(100), use_container_width=True)

else:
    st.error("❌ Critical Error: 'enterprise_retail_dataT.xlsx' table not found in workspace.")
