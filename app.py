import streamlit as st
import pandas as pd
import os
import workspace_modules as wm

# Force sidebar to be globally collapsible via the native UI chevron button
st.set_page_config(
    page_title="Computer Systems & AI Management", 
    layout="wide",
    initial_sidebar_state="expanded" 
)

# ====================================================================
# HEADER BANNER: 🏆 SYMMETRICAL BRANDING MATRIX (PRODUCTION LOGOS MOUNTED)
# ====================================================================
# 1. Main outer grid splits screen to hold Left Logo, Center Area, Right Logo
logob_col, center_area_col, logog_col = st.columns([1, 4, 1])

with logob_col:
    if os.path.exists("LOGOB.png"):
        st.image("LOGOB.png", use_container_width=True)
    else:
        st.write("✨")

with center_area_col:
    # 2. Nested Sub-Grid splits the wide center area [Left Spacer, Center Title, Right Spacer]
    # This natively forces the text box block to sit perfectly centered.
    sub_spacer_L, sub_title_core, sub_spacer_R = st.columns([1, 6, 1])
    
    with sub_title_core:
        # Native, safe title element safely aligned by the grid framework
        st.title("🖥️ Computer Systems and AI Management Cockpit")

with logog_col:
    if os.path.exists("LOGOG.png"):
        st.image("LOGOG.png", use_container_width=True)
    else:
        st.write("🚀")

st.markdown("---")

# ====================================================================
# PHASE 1: GLOBAL DATA INGESTION (Cached Framework Loops)
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
            if 'Advanced_Military_Risk_Analysis' in table_key:
                try:
                    vault[table_key] = pd.read_excel(file_name, sheet_name='Advanced_Military_Risk_Analysis')
                except Exception:
                    vault[table_key] = pd.read_excel(file_name, sheet_name=0)
            else:
                vault[table_key] = pd.read_excel(file_name, sheet_name=0)
        except Exception:
            pass
    return vault

database = load_all_enterprise_data()
available_tables = sorted(list(database.keys()))

# ====================================================================
# UNIFIED SIDEBAR FILTER SETS (Brings back the native hide clickable arrow)
# ====================================================================
st.sidebar.header("🎯 Dashboard Control Filters")
selected_table_key = None
filtered_df = pd.DataFrame()

if available_tables:
    selected_table_key = st.sidebar.selectbox(
        "Choose an Enterprise Data Sheet:", 
        options=available_tables,
        index=available_tables.index('enterprise_retail_dataT') if 'enterprise_retail_dataT' in available_tables else 0
    )
    
    df = database[selected_table_key].copy()
    if 'Advanced_Military_Risk_Analysis' in selected_table_key:
        df = df.dropna(axis=1, how='all')
    
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.strip()
            
    filtered_df = df.copy()
    
    geo_col = None
    for alternative in ['Region', 'Regions', 'region', 'Global Theater', 'Command Tier', 'Strategic Command Sector']:
        if alternative in df.columns:
            geo_col = alternative
            break
    if geo_col:
        geo_options = sorted(list(df[geo_col].unique()))
        selected_geo = st.sidebar.multiselect(f"Filter by {geo_col}:", options=geo_options, default=geo_options)
        filtered_df = filtered_df[filtered_df[geo_col].isin(selected_geo)]
        
    unit_col = None
    for alternative in ['Retailer', 'Active Combat Unit Name']:
        if alternative in df.columns:
            unit_col = alternative
            break
    if unit_col:
        unit_options = sorted(list(df[unit_col].unique()))
        selected_unit = st.sidebar.multiselect(f"Filter by {unit_col}:", options=unit_options, default=unit_options)
        filtered_df = filtered_df[filtered_df[unit_col].isin(selected_unit)]

# ====================================================================
# THE ARCHITECTURE LAYOUT BLUEPRINT GRID TABS
# ====================================================================
tab_analytics, tab_utilities, tab_workspace, tab_simulation = st.tabs([
    "📊 Tab 1: Analytics", 
    "⚙️ Tab 2: Utilities", 
    "💼 Tab 3: Workspace", 
    "✈️ Tab 4: Simulation"
])

with tab_analytics:
    st.header("🗃️ Command Data Engine")
    if selected_table_key and not filtered_df.empty:
        st.markdown(f"### 📊 Currently Active File Stream: `{selected_table_key}.xlsx`")
        col1, col2 = st.columns(2)
        col1.metric(label="📦 Total Ingested Record Rows", value=f"{len(filtered_df):,}")
        col2.metric(label="📂 Total Linked Vault Files", value=f"{len(available_tables)}")
        st.markdown("---")
        chart_col1, chart_col2 = st.columns(2)
        
        if selected_table_key == 'enterprise_retail_dataT':
            with chart_col1:
                st.subheader("🏆 Retailer Performance Rankings")
                st.bar_chart(filtered_df.groupby('Retailer')['Volume_USD'].sum().sort_values(ascending=False))
            with chart_col2:
                st.subheader("🔸 Revenue Vol by Market Sector")
                st.bar_chart(filtered_df.groupby('Market_Tier')['Volume_USD'].sum().sort_values(ascending=False))
        elif selected_table_key == 'Azure_Remediation_ReportT':
            with chart_col1:
                st.subheader("🛡️ Azure Task Vol by Command Tier")
                if 'Command Tier' in filtered_df.columns: st.bar_chart(filtered_df.groupby('Command Tier').size())
            with chart_col2:
                st.subheader("⚙️ System Metrics Profile Overview"); st.info("Azure remediation summary logs loaded.")
        elif selected_table_key == 'SQLQry8T':
            with chart_col1:
                st.subheader("💎 Query Metric Vol by Global Theater")
                if 'Global Theater' in filtered_df.columns: st.bar_chart(filtered_df.groupby('Global Theater').size())
            with chart_col2:
                st.subheader("📊 Query Attribute Density"); st.info("Database records compiled.")
        elif selected_table_key == 'Military_Combat_Force_ReportT':
            with chart_col1:
                st.subheader("🪖 Unit Volume Distribution")
                if 'Active Combat Unit Name' in filtered_df.columns: st.bar_chart(filtered_df.groupby('Active Combat Unit Name').size())
            with chart_col2:
                st.subheader("📡 Force Capacity by Command Sector")
                if 'Strategic Command Sector' in filtered_df.columns: st.bar_chart(filtered_df.groupby('Strategic Command Sector').size())
        elif 'Advanced_Military_Risk_Analysis' in selected_table_key:
            with chart_col1:
                st.subheader("⚡ Threat Density by Combat Unit")
                if 'Active Combat Unit Name' in filtered_df.columns: st.bar_chart(filtered_df.groupby('Active Combat Unit Name').size())
            with chart_col2:
                st.subheader("🎯 Strategic Risk Exposure Index")
                if 'Strategic Command Sector' in filtered_df.columns: st.bar_chart(filtered_df.groupby('Strategic Command Sector').size())

        st.subheader("📋 System Audit Trail Records")
        st.dataframe(filtered_df, use_container_width=True)
    else:
        st.warning("⚠️ No enterprise tracking records found in current workspace root.")

with tab_utilities:
    wm.render_translator()
    st.markdown("---")
    wm.render_calculator()

with tab_workspace:
    wm.render_invoice()
    st.markdown("---")
    wm.render_renamer()

with tab_simulation:
    wm.render_runway()
