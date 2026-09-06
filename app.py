import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Computer Systems & AI Management", layout="wide")

# 🏆 Professional Company Title Banner
st.title("🖥️ Computer Systems and AI Management Cockpit")
st.markdown("---")

# ====================================================================
# PHASE 1: DATA INGESTION (Scans ALL tabs inside every file)
# ====================================================================
@st.cache_data
def load_all_enterprise_data():
    data_folder = '.'
    all_files = [f for f in os.listdir(data_folder) if f.lower().endswith(('.xlsx', '.xls'))]
    
    vault = {}
    for file_name in all_files:
        table_key = file_name.replace('.xlsx', '').replace('.xls', '')
        try:
            xl = pd.ExcelFile(file_name)
            target_sheet = xl.sheet_names[0]
            
            # Explicitly search for your preferred worksheet tab phrase
            for sheet in xl.sheet_names:
                if 'Advanced' in sheet or 'Risk' in sheet:
                    target_sheet = sheet
                    break
            
            temp_df = pd.read_excel(file_name, sheet_name=target_sheet)
            
            if temp_df.empty or len(temp_df.columns) <= 1:
                for sheet in xl.sheet_names:
                    alt_df = pd.read_excel(file_name, sheet_name=sheet)
                    if not alt_df.empty and len(alt_df.columns) > 1:
                        temp_df = alt_df
                        break
                        
            vault[table_key] = temp_df
        except:
            pass
    return vault

database = load_all_enterprise_data()

# ====================================================================
# PHASE 2: DATA SELECTION & FUZZY HEADER CLEANING
# ====================================================================
st.header("🗃️ Enterprise Data Vault Selector")
available_tables = sorted(list(database.keys()))

if available_tables:
    selected_table_key = st.selectbox(
        "Choose an Enterprise Data Sheet to View:", 
        options=available_tables,
        index=available_tables.index('enterprise_retail_dataT') if 'enterprise_retail_dataT' in available_tables else 0
    )
    
    df = database[selected_table_key].copy()
    
    # Drop completely blank trailing column fields to optimize parsing
    df = df.dropna(axis=1, how='all')
    
    # 🧼 FIX: Clear out hidden white spaces, tracking chars, and casing errors in column headers
    cleaned_columns = []
    for col in df.columns:
        col_str = str(col).strip()
        # Explicitly map fuzzy column strings to your targeted names
        if 'combat unit' in col_str.lower() or 'unit name' in col_str.lower():
            cleaned_columns.append('Active Combat Unit Name')
        elif 'command sector' in col_str.lower() or 'strategic' in col_str.lower():
            cleaned_columns.append('Strategic Command Sector')
        else:
            cleaned_columns.append(col_str)
    df.columns = cleaned_columns
    
    # Clean text data inside rows uniformly
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.strip()
            
    st.markdown(f"### 📊 Currently Active File: `{selected_table_key}.xlsx`")
    st.markdown("---")
    
    # ====================================================================
    # PHASE 3: SIDEBAR FILTERS (Fully State-Locked)
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
        
    # KPI metrics cards
    total_txns = len(filtered_df)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="📦 Total Ingested Record Rows", value=f"{total_txns:,}")
    with col2:
        st.metric(label="📂 Total Linked Vault Files", value=f"{len(available_tables)}")
        
    st.markdown("---")
    
    # ====================================================================
    # PHASE 4: DYNAMIC MULTI-SHEET CHARTS
    # ====================================================================
    if not filtered_df.empty:
        chart_col1, chart_col2 = st.columns(2)
        
        # Retail Charts
        if selected_table_key == 'enterprise_retail_dataT':
            with chart_col1:
                st.subheader("🏆 Retailer Performance Rankings")
                chart_data = filtered_df.groupby('Retailer')['Volume_USD'].sum().sort_values(ascending=False)
                st.bar_chart(chart_data)
            with chart_col2:
                st.subheader("🔸 Revenue Vol by Market Sector")
                chart_data = filtered_df.groupby('Market_Tier')['Volume_USD'].sum().sort_values(ascending=False)
                st.bar_chart(chart_data)
                
        # Azure Charts
        elif selected_table_key == 'Azure_Remediation_ReportT':
            with chart_col1:
                st.subheader("🛡️ Azure Task Vol by Command Tier")
                if 'Command Tier' in filtered_df.columns:
                    chart_data = filtered_df.groupby('Command Tier').size().sort_values(ascending=False)
                    st.bar_chart(chart_data)
            with chart_col2:
                st.subheader("⚙️ System Metrics Profile Overview")
                st.info("Azure remediation summary logs are loaded successfully.")
                
        # SQL Charts
        elif selected_table_key == 'SQLQry8T':
            with chart_col1:
                st.subheader("💎 Query Metric Vol by Global Theater")
                if 'Global Theater' in filtered_df.columns:
                    chart_data = filtered_df.groupby('Global Theater').size().sort_values(ascending=False)
                    st.bar_chart(chart_data)
            with chart_col2:
                st.subheader("📊 Query Attribute Density")
                st.info("Database records are compiled seamlessly.")
                
        # Military Combat Force Charts
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
                    
        # Advanced Military Risk Charts (Now fully supported by the cleaning logic)
        elif 'Advanced_Military_Risk_Analysis' in selected_table_key:
            with chart_col1:
                st.subheader("⚡ Threat Density by Combat Unit")
                if 'Active Combat Unit Name' in filtered_df.columns:
                    chart_data = filtered_df.groupby('Active Combat Unit Name').size().sort_values(ascending=False)
                    st.bar_chart(chart_data)
                else:
                    st.info("Dynamic unit scanning failed to locate required data headers.")
            with chart_col2:
                st.subheader("🎯 Strategic Risk Exposure Index")
                if 'Strategic Command Sector' in filtered_df.columns:
                    chart_data = filtered_df.groupby('Strategic Command Sector').size().sort_values(ascending=False)
                    st.bar_chart(chart_data)
                
        # Default view
        else:
            with chart_col1:
                st.subheader("🔎 Database Column Overview")
                st.write(df.dtypes.astype(str))
            with chart_col2:
                st.subheader("💡 Analysis Insight Staging")
                st.info("Select a core metrics file from the top dropdown menu to map specialized visual summaries.")
                
    else:
        st.warning("⚠️ No data matches your current filter selections. Please re-check an option box!")
        
    st.subheader("🔎 Ingested Database Record Stream")
    st.dataframe(filtered_df.head(100), use_container_width=True)

else:
    st.error("❌ Critical Error: No valid Excel spreadsheets found in your GitHub repository.")
