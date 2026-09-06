import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Computer Systems & AI Management", layout="wide")

# 🏆 Professional Company Title Banner
st.title("🖥️ Computer Systems and AI Management Cockpit")
st.markdown("---")

# ====================================================================
# PHASE 1: DATA INGESTION (Scans ALL tabs inside every repository file)
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
            
            # Prioritize an internal worksheet tab containing your targeted data
            for sheet in xl.sheet_names:
                if 'Advanced' in sheet or 'Risk' in sheet or 'Military' in sheet:
                    target_sheet = sheet
                    break
            
            temp_df = pd.read_excel(file_name, sheet_name=target_sheet)
            
            # If the selected sheet turns out to be blank, inspect alternative tabs
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

# Initialize the global data vault database
database = load_all_enterprise_data()

# ====================================================================
# PHASE 2: DATA SELECTION & BULLETPROOF COLUMN MAPPING
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
    
    # Drop completely blank trailing column fields to optimize memory allocation
    df = df.dropna(axis=1, how='all')
    
    # 🧼 Clean tracking spaces from raw header strings immediately
    df.columns = [str(c).strip() for c in df.columns]
    
    # 🤖 ABSOLUTE FIX: Automatic Index Fallback Logic for Advanced Defense Files
    cleaned_columns = list(df.columns)
    
    # Dynamically extract all available string column headers
    text_cols = [c for c in df.columns if df[c].dtype == 'object' or df[c].dtype == 'string']
    
    for i, col in enumerate(df.columns):
        col_lower = col.lower()
        # Map out Unit / Vendor Name Column
        if 'combat unit' in col_lower or 'unit name' in col_lower or 'retailer' in col_lower:
            cleaned_columns[i] = 'Active Combat Unit Name'
        # Map out Geographic Region / Sector Column
        elif 'command sector' in col_lower or 'strategic' in col_lower or 'region' in col_lower or 'theater' in col_lower or 'tier' in col_lower:
            cleaned_columns[i] = 'Strategic Command Sector'
            
    # Apply the mapped labels back onto the DataFrame
    df.columns = cleaned_columns
    
    # 🚨 CRITICAL FALLBACK: If names are completely hidden or custom, map them by position index
    if 'Advanced_Military_Risk_Analysis' in selected_table_key or 'Military_Combat_Force' in selected_table_key:
        if 'Active Combat Unit Name' not in df.columns and len(text_cols) > 0:
            df = df.rename(columns={text_cols[0]: 'Active Combat Unit Name'})
        if 'Strategic Command Sector' not in df.columns and len(text_cols) > 1:
            df = df.rename(columns={text_cols[1]: 'Strategic Command Sector'})
            
    # Standardize data rows text spacing uniformly
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.strip()
            
    st.markdown(f"### 📊 Currently Active File: `{selected_table_key}.xlsx`")
    st.markdown("---")
    
    # ====================================================================
    # PHASE 3: SIDEBAR FILTERS (Fully State-Locked to Prevent Loops)
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
        
    # Top-Level KPI Summary metrics cards
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
        
        # 🟢 CASE 1: RETAIL DATA LOGS
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
                st.info("Azure remediation summary logs are compiled successfully.")
                
        # 🟡 CASE 3: SQL QUERY 8 STAGING
        elif selected_table_key == 'SQLQry8T':
            with chart_col1:
                st.subheader("💎 Query Metric Vol by Global Theater")
                if 'Global Theater' in filtered_df.columns:
                    chart_data = filtered_df.groupby('Global Theater').size().sort_values(ascending=False)
                    st.bar_chart(chart_data)
            with chart_col2:
                st.subheader("📊 Query Attribute Density")
                st.info("Database records are compiled seamlessly.")
                
        # ⚔️ CASE 4: MILITARY COMBAT FORCE REPORT & ADVANCED RISK ENGINES (Unified Handling)
        elif 'Combat_Force' in selected_table_key or 'Risk_Analysis' in selected_table_key:
            with chart_col1:
                st.subheader("⚡ Operational Threat Density by Combat Unit")
                # Look for whatever assigned label name is active to draw the graph
                active_unit_label = 'Active Combat Unit Name' if 'Active Combat Unit Name' in filtered_df.columns else unit_col
                if active_unit_label and active_unit_label in filtered_df.columns:
                    chart_data = filtered_df.groupby(active_unit_label).size().sort_values(ascending=False)
                    st.bar_chart(chart_data)
                else:
                    st.info("Insufficient text column indices to populate an operational unit chart layout.")
                    
            with chart_col2:
                st.subheader("🎯 Strategic Risk Capacity Exposure Index")
                active_geo_label = 'Strategic Command Sector' if 'Strategic Command Sector' in filtered_df.columns else geo_col
                if active_geo_label and active_geo_label in filtered_df.columns:
                    chart_data = filtered_df.groupby(active_geo_label).size().sort_values(ascending=False)
                    st.bar_chart(chart_data)
                else:
                    st.info("Insufficient text column indices to populate a regional sector chart layout.")
                
        # ⚪ CASE 5: DEFAULT ATTRIBUTE GRID FOR REMAINING 18 VAULT FILES
        else:
            with chart_col1:
                st.subheader("🔎 Database Column Overview")
                st.write(df.dtypes.astype(str))
            with chart_col2:
                st.subheader("💡 Analysis Insight Staging")
                st.info("Select a core metrics file from the top dropdown menu to map specialized visual summaries.")
                
    else:
        st.warning("⚠️ No data matches your current filter selections. Please re-check an option box!")
        
    # 🗒️ Live Interactive Grid Audit Stream
    st.subheader("🔎 Ingested Database Record Stream")
    st.dataframe(filtered_df.head(100), use_container_width=True)

else:
    st.error("❌ Critical Error: No valid Excel spreadsheets found in your GitHub repository.")
