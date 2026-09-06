import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Computer Systems & AI Management", layout="wide")

# 🏆 Professional Company Title Banner
st.title("🖥️ Computer Systems and AI Management Cockpit")
st.markdown("---")

# ====================================================================
# PHASE 1: DATA INGESTION (Loads files into memory once)
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
# PHASE 2: DATA SELECTION
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
    
    # INSTANT DATA CLEANING: Clean text columns BEFORE filtering
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.strip()
            
    st.markdown(f"### 📊 Currently Active File: `{selected_table_key}.xlsx`")
    st.markdown("---")
    
    # ====================================================================
    # PHASE 3: SIDEBAR FILTERS WITH EXPLICIT MEMORY KEYS
    # ====================================================================
    st.sidebar.header("🎯 Dashboard Control Filters")
    filtered_df = df.copy()
    
    # Filter 1: Region 
    if 'Region' in filtered_df.columns:
        region_options = sorted(list(filtered_df['Region'].unique()))
        selected_region = st.sidebar.multiselect(
            "Select Region", 
            options=region_options, 
            default=region_options,
            key=f"widget_region_{selected_table_key}"
        )
        filtered_df = filtered_df[filtered_df['Region'].isin(selected_region)]
        
    # Filter 2: Retailer / Vendor 
    if 'Retailer' in filtered_df.columns:
        retailer_options = sorted(list(filtered_df['Retailer'].unique()))
        selected_retailer = st.sidebar.multiselect(
            "Select Retailer", 
            options=retailer_options, 
            default=retailer_options,
            key=f"widget_retailer_{selected_table_key}"
        )
        filtered_df = filtered_df[filtered_df['Retailer'].isin(selected_retailer)]
        
    # 📊 Top-Level Summary Cards (KPIs)
    total_txns = len(filtered_df)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="📦 Total Ingested Record Rows", value=f"{total_txns:,}")
    with col2:
        st.metric(label="📂 Total Linked Vault Files", value=f"{len(available_tables)}")
        
    st.markdown("---")
    
    # ====================================================================
    # PHASE 4: DYNAMIC MULTI-SHEET VISUALIZATION LOGIC
    # ====================================================================
    if not filtered_df.empty:
        chart_col1, chart_col2 = st.columns(2)
        
        # 🟢 CASE 1: RETAIL DATA CHIPS
        if selected_table_key == 'enterprise_retail_dataT':
            with chart_col1:
                st.subheader("🏆 Retailer Performance Rankings")
                chart_data = filtered_df.groupby('Retailer')['Volume_USD'].sum().sort_values(ascending=False)
                st.bar_chart(chart_data)
            with chart_col2:
                st.subheader("🔸 Revenue Vol by Market Sector")
                chart_data = filtered_df.groupby('Market_Tier')['Volume_USD'].sum().sort_values(ascending=False)
                st.bar_chart(chart_data)
                
        # 🔵 CASE 2: AZURE REMEDIATION ARCHITECTURE
        elif selected_table_key == 'Azure_Remediation_ReportT':
            # Check the actual column names in your sheet and map dynamically
            first_col = filtered_df.columns[0]
            second_col = filtered_df.columns[1] if len(filtered_df.columns) > 1 else first_col
            
            with chart_col1:
                st.subheader("🛡️ Azure Task Vol Distribution")
                # Group by your first text column (e.g., Status, Resource, or Category)
                chart_data = filtered_df.groupby(first_col).size().sort_values(ascending=False)
                st.bar_chart(chart_data)
            with chart_col2:
                st.subheader("⚙️ System Metrics Profile Overview")
                st.info("Azure remediation summary logs are loaded. Use the bottom audit grid to inspect live fix states.")
                
        # 🟡 CASE 3: SQL QUERY 8 STAGING
        elif selected_table_key == 'SQLQry8T':
            first_col = filtered_df.columns[0]
            
            with chart_col1:
                st.subheader("💎 Query Metric Frequency")
                chart_data = filtered_df.groupby(first_col).size().sort_values(ascending=False)
                st.bar_chart(chart_data)
            with chart_col2:
                st.subheader("📊 Query Attribute Density")
                st.info("Database records are compiled. Charts will dynamically adjust based on column structural constraints.")
                
        # ⚪ CASE 4: DEFAULT STANDARD GRID FOR OTHER 20 SHEETS
        else:
            with chart_col1:
                st.subheader("🔎 Database Column Overview")
                st.write(df.dtypes.astype(str))
            with chart_col2:
                st.subheader("💡 Analysis Insight Staging")
                st.info("Select a core metrics file from the top dropdown menu to map specialized visual summaries.")
                
    else:
        st.warning("⚠️ No data matches your current filter selections. Please re-check an option box!")
        
    # 🗒️ Live Interactive Grid Audit
    st.subheader("🔎 Ingested Database Record Stream")
    st.dataframe(filtered_df.head(100), use_container_width=True)

else:
    st.error("❌ Critical Error: No valid Excel spreadsheets found in your GitHub repository.")
