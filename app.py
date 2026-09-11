import streamlit as st
import pandas as pd
import os
import math
import re
from datetime import datetime

# Force sidebar to be globally collapsible via the native UI chevron button
st.set_page_config(
    page_title="Computer Systems & AI Management", 
    layout="wide",
    initial_sidebar_state="expanded" 
)

# Avoid breaking telemetry loops by checking for your module safely
try:
    import workspace_modules as wm
except ImportError:
    st.error("🚨 Missing structural link: Ensure 'workspace_modules.py' is pushed to the same repository root directory.")

# ====================================================================
# HEADER BANNER: 🏆 SYMMETRICAL BRANDING MATRIX (PRODUCTION LOGOS MOUNTED)
# ====================================================================
# Full-Width Title Block guarantees your main text row never wraps or breaks formatting
st.title("🖥️ Computer Systems and AI Management Cockpit")

# Symmetrical layout matrix perfectly sizes and balances your custom corporate emblems
logob_col, center_space, logog_col = st.columns([3, 4, 3])

with logob_col:
    if os.path.exists("LOGOB.png"):
        # We nest a sub-grid [1 part spacer, 3 parts image] to pull the blue logo
        # over to the right and scale it down to perfectly match the green core.
        b_spacer, b_img = st.columns([1, 3])
        with b_img:
            st.image("LOGOB.png", use_container_width=True)
    else:
        st.markdown("<p style='color: #94A3B8; font-size: 11px;'>[ LOGOB.png LOADING ]</p>", unsafe_markdown=True)

with center_space:
    st.write("") # Main visual gap anchor balancing out your distinct business nodes

with logog_col:
    if os.path.exists("LOGOG.png"):
        # We nest a sub-grid [3 parts image, 1 part spacer] to pull the green logo
        # over to the left, squeezing out its pre-baked white canvas side padding.
        g_img, g_spacer = st.columns([3, 1])
        with g_img:
            st.image("LOGOG.png", use_container_width=True)
    else:
        st.markdown("<p style='color: #94A3B8; font-size: 11px;'>[ LOGOG.png LOADING ]</p>", unsafe_markdown=True)

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
    
    # 🌍 1. Dynamic Geographic Theater / Column Filter Range Selector
    geo_col = None
    for alternative in ['Region', 'Regions', 'region', 'Global Theater', 'Command Tier', 'Strategic Command Sector', 'Agency', 'Market_Tier']:
        if alternative in df.columns:
            geo_col = alternative
            break
    if geo_col:
        geo_options = sorted(list(df[geo_col].unique()))
        selected_geo = st.sidebar.multiselect(f"Filter by {geo_col}:", options=geo_options, default=geo_options)
        filtered_df = filtered_df[filtered_df[geo_col].isin(selected_geo)]
        
    # 🛡️ 2. Dynamic Vendor / Active Combat Unit Selector Filter Range
    unit_col = None
    for alternative in ['Retailer', 'Active Combat Unit Name', 'Agency']:
        if alternative in df.columns and alternative != geo_col:
            unit_col = alternative
            break
    if unit_col:
        unit_options = sorted(list(df[unit_col].unique()))
        selected_unit = st.sidebar.multiselect(f"Filter by {unit_col}:", options=unit_options, default=unit_options)
        filtered_df = filtered_df[filtered_df[unit_col].isin(selected_unit)]

# ====================================================================
# THE THEMATIC ARCHITECTURE FIVE-TAB WORKSPACE MATRIX
# ====================================================================
tab_analytics, tab_utilities, tab_workspace, tab_simulation, tab_library = st.tabs([
    "📊 Tab 1: Analytics", 
    "⚙️ Tab 2: Utilities", 
    "💼 Tab 3: Workspace", 
    "✈️ Tab 4: Simulation",
    "📚 Tab 5: Library"
])

# --------------------------------------------------------------------
# 📊 TAB 1: ANALYTICS (🗃️ Command Data Engine)
# --------------------------------------------------------------------
with tab_analytics:
    st.header("🗃️ Command Data Engine")
    
    if selected_table_key and not filtered_df.empty:
        st.markdown(f"### 📊 Currently Active File Stream: `{selected_table_key}.xlsx`")
        
        col1, col2 = st.columns(2)
        col1.metric(label="📦 Total Ingested Record Rows", value=f"{len(filtered_df):,}")
        col2.metric(label="📂 Total Linked Vault Files", value=f"{len(available_tables)}")
        st.markdown("---")
        
        # ====================================================================
        # COCKPIT V4.0: MASTER UNIVERSAL VISUALIZATION ENGINE (FUZZY MAPPING)
        # ====================================================================
        chart_col1, chart_col2 = st.columns(2)
        
        # 🧼 STEP 1: Scan columns to isolate the best Categorical Anchor (X-Axis)
        x_categorical = None
        for possible_x in ['Retailer', 'Region', 'Market_Tier', 'Command Tier', 'Agency', 
                           'Active Combat Unit Name', 'Regions', 'region', 'Global Theater', 'Strategic Command Sector']:
            if possible_x in filtered_df.columns:
                x_categorical = possible_x
                break
        
        # Fallback to absolute first string header column if no pattern matches
        if not x_categorical:
            for col in filtered_df.columns:
                if filtered_df[col].dtype == 'object' or len(filtered_df[col].unique()) < 30:
                    x_categorical = col
                    break

        # 🧼 STEP 2: Scan columns to isolate the best Numerical Metric (Y-Axis)
        y_numerical = None
        for possible_y in ['Volume_USD', 'Total Financial Footprint', 'Total Active Units', 'Precise Unit Cost (MSRP)', 
                           'Volume', 'USD', 'Total', 'Amount', 'Sales', 'Cost']:
            if possible_y in filtered_df.columns:
                y_numerical = possible_y
                break
                
        # Fallback to absolute first numeric data column if no pattern matches
        if not y_numerical:
            for col in filtered_df.columns:
                if pd.api.types.is_numeric_dtype(filtered_df[col]):
                    y_numerical = col
                    break

        # 🧼 STEP 3: RENDER THE CHARTS DYNAMICALLY BASED ON DISCOVERED MAPS
        with chart_col1:
            if x_categorical:
                if y_numerical:
                    st.subheader(f"🏆 Metric Distribution Profile (`{y_numerical}` by `{x_categorical}`)")
                    chart_data = filtered_df.groupby(x_categorical)[y_numerical].sum().sort_values(ascending=False)
                    st.bar_chart(chart_data)
                else:
                    st.subheader(f"🪖 Operational Volume Logs (Record Counts by `{x_categorical}`)")
                    chart_data = filtered_df.groupby(x_categorical).size().sort_values(ascending=False)
                    st.bar_chart(chart_data)
            else:
                st.subheader("📊 General Profile Summary")
                st.info("Ingested data sheet is uniform. Review the lower audit grid for cell-by-cell row analysis.")

        with chart_col2:
            # 🧼 STEP 4: Look for specialized timeline or alternative column metrics
            date_col = None
            for alternative in ['Timestamp', 'Date', 'Year', 'Month', 'Created_At']:
                if alternative in filtered_df.columns:
                    date_col = alternative
                    break
                    
            alternative_y = None
            if x_categorical and y_numerical:
                for possible_alt in ['Precise Unit Cost (MSRP)', 'Total Active Units', 'Market_Tier']:
                    if possible_alt in filtered_df.columns and possible_alt != y_numerical:
                        alternative_y = possible_alt
                        break

            # Case A: If it's a retail file with a Timestamp column, plot an automatic trend line
            if date_col and y_numerical:
                st.subheader(f"📈 Strategic Trend Timeline (Over `{date_col}`)")
                try:
                    timeline_df = filtered_df.copy()
                    timeline_df[date_col] = pd.to_datetime(timeline_df[date_col])
                    timeline_data = timeline_df.groupby(timeline_df[date_col].dt.date)[y_numerical].sum()
                    st.line_chart(timeline_data)
                except Exception:
                    timeline_data = filtered_df.groupby(date_col)[y_numerical].sum()
                    st.line_chart(timeline_data)
                    
            # Case B: If it's an agency file with multiple numbers, plot the secondary metric bar chart
            elif alternative_y:
                st.subheader(f"📊 Secondary Allocation Profile (`{alternative_y}` by `{x_categorical}`)")
                alt_chart_data = filtered_df.groupby(x_categorical)[alternative_y].sum().sort_values(ascending=False)
                st.bar_chart(alt_chart_data)
                
            # Case C: Fallback infrastructure overview view
            else:
                st.subheader("⚙️ System Metrics Profile Overview")
                st.success(f"✅ Data Vault structural sync complete for sheet: `{selected_table_key}`")
                st.info("Sidebar control filters are actively mapping variables. Use the hide chevron (>) to scale viewports.")

        # Raw Data Audit Trail Matrix Window Grid View remains unified at the bottom
        st.markdown("---")
        st.subheader("📋 System Audit Trail Records")
        st.dataframe(filtered_df, use_container_width=True)
    else:
        st.warning("⚠️ No enterprise tracking records found in current workspace root.")

# --------------------------------------------------------------------
# ⚙️ TAB 2: UTILITIES (⚙️ Multi-Engine Operations Suite)
# --------------------------------------------------------------------
with tab_utilities:
    if 'wm' in locals():
        wm.render_translator()
        st.markdown("---")
        wm.render_calculator()
        wm.render_codec()
    else:
        st.error("Module functions temporarily offline.")

# --------------------------------------------------------------------
# 💼 TAB 3: WORKSPACE (💼 Business Automation Module)
# --------------------------------------------------------------------
with tab_workspace:
    if 'wm' in locals():
        wm.render_invoice()
        st.markdown("---")
        wm.render_renamer()
        st.markdown("---")
    else:
        st.error("Module functions temporarily offline.")

# --------------------------------------------------------------------
# ✈️ TAB 4: SIMULATION (✈️ Tactical Modeling Runway)
# --------------------------------------------------------------------
with tab_simulation:
    if 'wm' in locals():
        wm.render_runway()
    else:
        st.error("Module functions temporarily offline.")

# --------------------------------------------------------------------
# 📚 TAB 5: LIBRARY (📚 Global System Asset Library & Multimedia Center)
# --------------------------------------------------------------------
with tab_library:
    if 'wm' in locals():
        wm.render_library_catalog()
    else:
        st.error("Module functions temporarily offline.")
