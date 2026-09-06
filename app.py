import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Computer Systems & AI Management", layout="wide")

# 🏆 Professional Company Title Banner
st.title("🖥️ Computer Systems and AI Management Cockpit")
st.markdown("---")

# ====================================================================
# PHASE 1: DATA INGESTION (Executed ONCE and cached in cloud memory)
# ====================================================================
@st.cache_data
def load_all_enterprise_data():
    data_folder = '.'
    all_files = [f for f in os.listdir(data_folder) if f.lower().endswith(('.xlsx', '.xls'))]
    
    vault = {}
    for file_name in all_files:
        table_key = file_name.replace('.xlsx', '').replace('.xls', '')
        try:
            vault[table_key] = pd.read_excel(file_name)
        except:
            pass
    return vault

# Initialize the global data vault database
database = load_all_enterprise_data()

# ====================================================================
# PHASE 2: DATA SELECTION (Using baseline df)
# ====================================================================
st.header("🗃️ Enterprise Data Vault Selector")
available_tables = sorted(list(database.keys()))

if available_tables:
    selected_table_key = st.selectbox(
        "Choose an Enterprise Data Sheet to View:", 
        options=available_tables,
        index=available_tables.index('enterprise_retail_dataT') if 'enterprise_retail_dataT' in available_tables else 0
    )
    
    # Extract a fresh copy of the baseline data
    df = database[selected_table_key].copy()
    
    # Clean all text columns IMMEDIATELY to prevent character matching freezes
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.strip()
            
    st.markdown(f"### 📊 Currently Active File: `{selected_table_key}.xlsx`")
    st.markdown("---")
    
    # ====================================================================
    # PHASE 3: INTERACTIVE FILTERING LOGIC (Using filtered_df down below)
    # ====================================================================
    st.sidebar.header("🎯 Dashboard Control Filters")
    
    # Initialize the secondary dataframe that will be filtered step-by-step
    filtered_df = df.copy()
    
    # Filter 1: Region (State-locked with a file-specific key)
    if 'Region' in filtered_df.columns:
        region_options = sorted(list(filtered_df['Region'].unique()))
        selected_region = st.sidebar.multiselect(
            "Select Region", 
            options=region_options, 
            default=region_options,
            key=f"widget_region_{selected_table_key}"  # <-- Key tells Streamlit to remember your clicks
        )
        filtered_df = filtered_df[filtered_df['Region'].isin(selected_region)]
        
    # Filter 2: Retailer / Vendor (State-locked with a file-specific key)
    if 'Retailer' in filtered_df.columns:
        retailer_options = sorted(list(filtered_df['Retailer'].unique()))
        selected_retailer = st.sidebar.multiselect(
            "Select Retailer", 
            options=retailer_options, 
            default=retailer_options,
            key=f"widget_retailer_{selected_table_key}"  # <-- Key tells Streamlit to remember your clicks
        )
        filtered_df = filtered_df[filtered_df['Retailer'].isin(selected_retailer)]
        
    # 📊 Top-Level Summary Cards (KPIs) using the final filtered data
    total_txns = len(filtered_df)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="📦 Total Ingested Record Rows", value=f"{total_txns:,}")
    with col2:
        st.metric(label="📂 Total Linked Vault Files", value=f"{len(available_tables)}")
        
    st.markdown("---")
    
    # ====================================================================
    # PHASE 4: RENDER CHARTS AND TABLES
    # ====================================================================
    if not filtered_df.empty:
        chart_col1, chart_col2 = st.columns(2)
        
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
        st.warning("⚠️ No data matches your current filter selections. Please re-check a store box!")
        
    # 🗒️ Live Interactive Grid Audit
    st.subheader("🔎 Ingested Database Record Stream")
    st.dataframe(filtered_df.head(100), use_container_width=True)

else:
    st.error("❌ Critical Error: No valid Excel spreadsheets found in your GitHub repository.")
