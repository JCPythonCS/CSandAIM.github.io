import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Computer Systems & AI Management", layout="wide")

# 🏆 Professional Company Title Banner
st.title("🖥️ Computer Systems and AI Management Cockpit")
st.markdown("---")

# 📂 Load the Data Local to the Repository
data_folder = '.'
all_files = [os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.lower().endswith(('.xlsx', '.xls'))]

database = {}
for file_path in all_files:
    file_name = os.path.basename(file_path)
    # Correctly store the exact string file name as the key
    table_name = os.path.splitext(file_name)[0]
    try:
        database[table_name] = pd.read_excel(file_path)
    except Exception as e:
        pass

# 🚨 Verify Main Table is Loaded
if 'enterprise_retail_dataT' in database:
    df = database['enterprise_retail_dataT']
    
    # Force clean strings and strip hidden tracking spaces to make buttons responsive
    df['Region'] = df['Region'].fillna('USA').astype(str).str.strip()
    df['Retailer'] = df['Retailer'].fillna('Unknown').astype(str).str.strip()
    
    # 🎛️ Interactive Sidebar Filters
    st.sidebar.header("🎯 Dashboard Control Filters")
    
    # Dynamically extract available options from the spreadsheet data column rows
    region_options = sorted(list(df['Region'].unique()))
    retailer_options = sorted(list(df['Retailer'].unique()))
    
    selected_region = st.sidebar.multiselect("Select Region", options=region_options, default=region_options)
    selected_retailer = st.sidebar.multiselect("Select Retailer", options=retailer_options, default=retailer_options)
    
    # Apply matching rules using precise Boolean intersections
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
    if not filtered_df.empty:
        chart_col1, chart_col2 = st.columns(2)
        
        with chart_col1:
            st.subheader("🏆 Retailer Performance Rankings")
            retailer_sales = filtered_df.groupby('Retailer')['Volume_USD'].sum().sort_values(ascending=False)
            st.bar_chart(retailer_sales)
            
        with chart_col2:
            st.subheader("🔸 Revenue Vol by Market Sector")
            tier_sales = filtered_df.groupby('Market_Tier')['Volume_USD'].sum().sort_values(ascending=False)
            st.bar_chart(tier_sales)
    else:
        st.warning("⚠️ No data matches your current filter selections. Please select at least one Retailer!")
        
    # 🗒️ Raw Data Audit Grid
    st.subheader("🔎 Ingested Database Record Stream")
    st.dataframe(filtered_df.head(100), use_container_width=True)

else:
    st.error("Critical Error: 'enterprise_retail_dataT' table not found in repository.")
