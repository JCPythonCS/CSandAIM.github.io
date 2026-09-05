import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Computer Systems & AI Management", layout="wide")

# 🏆 Professional Company Title Banner
st.title("🖥️ Computer Systems and AI Management Cockpit")
st.markdown("---")

# 📂 Automatically scan and load ALL Excel files in the repository
data_folder = '.'
all_files = [f for f in os.listdir(data_folder) if f.lower().endswith(('.xlsx', '.xls'))]

database = {}
for file_name in all_files:
    # Use the clean file name without extension as the selection key
    table_key = file_name.replace('.xlsx', '').replace('.xls', '')
    try:
        database[table_key] = pd.read_excel(file_name)
    except:
        pass

# 🗂️ Master Table Selector Dropdown
st.header("🗃️ Enterprise Data Vault Selector")
available_tables = sorted(list(database.keys()))

if available_tables:
    selected_table_key = st.selectbox(
        "Choose an Enterprise Data Sheet to View:", 
        options=available_tables,
        index=available_tables.index('enterprise_retail_dataT') if 'enterprise_retail_dataT' in available_tables else 0
    )
    
    # Extract the active active spreadsheet dataframe
    df = database[selected_table_key]
    st.markdown(f"### 📊 Currently Active File: `{selected_table_key}.xlsx`")
    st.markdown("---")
    
    # 🎛️ Dynamically Build Sidebar Filters Based on Columns Existing in the Sheet
    st.sidebar.header("🎯 Dashboard Control Filters")
    
    filtered_df = df.copy()
    
    # Apply Region Filter if Column Exists
if 'Region' in df.columns:
    # Ensure cleanup only processes the underlying master df once per rerun
    df['Region'] = df['Region'].astype(str).str.strip()
    
    # Extract the static full list of all possible regions
# ==========================================
# PHASE 1: CLEAN RAW DATA ONCE (Top of script)
# ==========================================
if 'Region' in df.columns:
    # Ensure cleanup only processes the underlying master df once per rerun
    df['Region'] = df['Region'].astype(str).str.strip()
    
    # Extract the static full list of all possible regions
    ALL_REGIONS = sorted(list(df['Region'].unique()))
else:
    ALL_REGIONS = []


# ==========================================
# PHASE 2: UI GENERATION AND FILTERING
# ==========================================
if ALL_REGIONS:
    # Notice: Use a hardcoded static string list for options & defaults to stop rendering loops
    selected_region = st.sidebar.multiselect(
        "Select Region", 
        options=ALL_REGIONS, 
        default=ALL_REGIONS
    )
    
    # Explicit wildcard catch: if the user deletes all chips, reset to ALL data rows
    if not selected_region:
        filtered_df = df
    else:
        # Crucial: Filter against 'df' as the base, keeping your options pool clean
        filtered_df = df[df['Region'].isin(selected_region)]
        
    # Apply Retailer/Vendor Filter if Column Exists
    if 'Retailer' in df.columns:
        df['Retailer'] = df['Retailer'].astype(str).str.strip()
        retailer_options = sorted(list(df['Retailer'].unique()))
        selected_retailer = st.sidebar.multiselect("Select Retailer", options=retailer_options, default=retailer_options)
        filtered_df = filtered_df[filtered_df['Retailer'].isin(selected_retailer)]
        
    # 📊 Top-Level Summary Cards (KPIs)
    total_txns = len(filtered_df)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="📦 Total Ingested Record Rows", value=f"{total_txns:,}")
    with col2:
        st.metric(label="📂 Total Linked Vault Files", value=f"{len(available_tables)}")
        
    st.markdown("---")
    
    # 📊 Render Graphical Analytics
    if not filtered_df.empty:
        chart_col1, chart_col2 = st.columns(2)
        
        # Dynamically draw charts based on available columns
        with chart_col1:
            if 'Retailer' in filtered_df.columns and 'Volume_USD' in filtered_df.columns:
                st.subheader("🏆 Retailer Performance Rankings")
                chart_data = filtered_df.groupby('Retailer')['Volume_USD'].sum().sort_values(ascending=False)
                st.bar_chart(chart_data)
            else:
                st.subheader("🔎 Database Column Overview")
                st.write(df.dtypes.astype(str))
                
        with chart_col2:
            if 'Market_Tier' in filtered_df.columns and 'Volume_USD' in filtered_df.columns:
                st.subheader("🔸 Revenue Vol by Market Sector")
                chart_data = filtered_df.groupby('Market_Tier')['Volume_USD'].sum().sort_values(ascending=False)
                st.bar_chart(chart_data)
            else:
                st.subheader("💡 Analysis Insight Staging")
                st.info("Select a data sheet from the dropdown above to map visual charts dynamically.")
    else:
        st.warning("⚠️ No data matches your current filter selections.")
        
    # 🗒️ Live Interactive Grid Audit
    st.subheader("🔎 Ingested Database Record Stream")
    st.dataframe(filtered_df.head(100), use_container_width=True)

else:
    st.error("❌ Critical Error: No valid Excel spreadsheets found in your GitHub repository.")
