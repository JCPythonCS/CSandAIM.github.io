import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Computer Systems & AI Management", layout="wide")

# 🏆 Professional Company Title Banner
st.title("🖥️ Computer Systems and AI Management Cockpit")
st.markdown("---")

# ====================================================================
# PHASE 1: DATA INGESTION (Loaded once and cached)
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
    
    # FIX: For the heavy 16,384-column risk file, clean out blank columns first to prevent memory overflows
    if selected_table_key == 'Advanced_Military_Risk_AnalysisT':
        df = df.dropna(axis=1, how='all')
    
    # 🧼 INSTANT DATA CLEANING: Standardize all text columns BEFORE filtering
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.strip()
            
    st.markdown(f"### 📊 Currently Active File: `{selected_table_key}.xlsx`")
    st.markdown("---")
    
    # ====================================================================
    # PHASE 3: SIDEBAR FILTERS (Now Armed with Military Commands)
    # ====================================================================
    st.sidebar.header("🎯 Dashboard Control Filters")
    filtered_df = df.copy()
    
    # 🌍 1. Dynamic Geographic Region / Theater Filter
    geo_col = None
    for alternative in ['Region', 'Regions', 'region', 'Global Theater', 'Command Tier', 'Strategic Command Sector']:
        if alternative in df.columns:
            geo_col = alternative
            break
    
    if geo_col:
        geo_options = sorted(list(df[geo_col].unique()))
        selected_geo = st.sidebar.multiselect(
            f"Filter by {geo_col}", 
            options=geo_options, 
            default=geo_options,
            key=f"widget_geo_{selected_table_key}"
        )
        filtered_df = filtered_df[filtered_df[geo_col].isin(selected_geo)]
        
    # 🛡️ 2. Dynamic Vendor / Active Combat Unit Filter
    unit_col = None
    for alternative in ['Retailer', 'Active Combat Unit Name']:
        if alternative in df.columns:
            unit_col = alternative
            break
            
    if unit_col:
        unit_options = sorted(list(df[unit_col].unique()))
        selected_unit = st.sidebar.multiselect(
            f"Filter by {unit_col}", 
            options=unit_options, 
            default=unit_options,
            key=f"widget_unit_{selected_table_key}"
        )
        filtered_df = filtered_df[filtered_df[unit_col].isin(selected_unit)]
        
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
            with chart_col1:
                st.subheader("🛡️ Azure Task Vol by Command Tier")
                if 'Command Tier' in filtered_df.columns:
                    chart_data = filtered_df.groupby('Command Tier').size().sort_values(ascending=False)
                    st.bar_chart(chart_data)
            with chart_col2:
                st.subheader("⚙️ System Metrics Profile Overview")
                st.info("Azure remediation summary logs are loaded. Use the bottom audit grid to inspect live fix states.")
                
        # 🟡 CASE 3: SQL QUERY 8 STAGING
        elif selected_table_key == 'SQLQry8T':
            with chart_col1:
                st.subheader("💎 Query Metric Vol by Global Theater")
                if 'Global Theater' in filtered_df.columns:
                    chart_data = filtered_df.groupby('Global Theater').size().sort_values(ascending=False)
                    st.bar_chart(chart_data)
            with chart_col2:
                st.subheader("📊 Query Attribute Density")
                st.info("Database records are compiled. Charts will dynamically adjust based on column structural constraints.")
                
        # ⚔️ CASE 4: MILITARY COMBAT FORCE REPORT
        elif selected_table_key == 'Military_Combat_Force_ReportT':
            with chart_col1:
                st.subheader("🪖 Unit Volume Distribution")
                if 'Active Combat Unit Name' in filtered_df.columns:
                    chart_data = filtered_df.groupby('Active Combat Unit Name').size().sort_values(ascending=False)
                    st.bar_chart(chart_data)
            with chart_col2:
                st.subheader("📡 Force Capacity by Command Sector")
                if 'Strategic Command Sector' in filtered_df.columns:
                    chart_data = filtered_df.groupby('Strategic Command Sector').size().sort_values(ascending=False)
                    st.bar_chart(chart_data)
                    
        # 🚨 CASE 5: ADVANCED MILITARY RISK ANALYSIS
        elif selected_table_key == 'Advanced_Military_Risk_AnalysisT':
            with chart_col1:
                st.subheader("⚡ Threat Density by Combat Unit")
                if 'Active Combat Unit Name' in filtered_df.columns:
                    chart_data = filtered_df.groupby('Active Combat Unit Name').size().sort_values(ascending=False)
                    st.bar_chart(chart_data)
            with chart_col2:
                st.subheader("🎯 Strategic Risk Exposure Index")
                if 'Strategic Command Sector' in filtered_df.columns:
                    chart_data = filtered_df.groupby('Strategic Command Sector').size().sort_values(ascending=False)
                    st.bar_chart(chart_data)
                
        # ⚪ CASE 6: DEFAULT STANDARD GRID FOR OTHER SHEETS
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
