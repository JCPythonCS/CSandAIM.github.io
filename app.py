import streamlit as st
import pandas as pd
import os
import math
import re

# Force sidebar to be globally collapsible via the native UI chevron button
st.set_page_config(
    page_title="Computer Systems & AI Management", 
    layout="wide",
    initial_sidebar_state="expanded" 
)

# ====================================================================
# HEADER BANNER: 🏆 SYMMETRICAL BRANDING MATRIX (FAIL-SAFE IMAGE SECTOR)
# ====================================================================
logob_col, title_col, logog_col = st.columns([1, 4, 1]) # Column sizing grid provides ideal title balance

with logob_col:
    # Fail-safe check for exact case-sensitive filename matching
    if os.path.exists("LOGOB.png"):
        st.image("LOGOB.png", width=120)
    else:
        st.markdown("<p style='text-align: center; color: #94A3B8; font-size: 11px; padding-top: 20px;'>[ LOGOB.png N/A ]</p>", unsafe_markdown=True)

with title_col:
    # Clean Python 3.14 layout configuration for the center Enterprise Title Banner
    st.markdown("<h1 style='text-align: center; color: #1E293B; margin-top: 0;'>🖥️ Computer Systems and AI Management Cockpit</h1>", unsafe_markdown=True)

with logog_col:
    # Fail-safe check for exact case-sensitive filename matching
    if os.path.exists("LOGOG.png"):
        st.image("LOGOG.png", width=120)
    else:
        st.markdown("<p style='text-align: center; color: #94A3B8; font-size: 11px; padding-top: 20px;'>[ LOGOG.png N/A ]</p>", unsafe_markdown=True)

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
    
    # 🌍 1. Geographic Theater Range Selector Filter
    geo_col = None
    for alternative in ['Region', 'Regions', 'region', 'Global Theater', 'Command Tier', 'Strategic Command Sector']:
        if alternative in df.columns:
            geo_col = alternative
            break
    if geo_col:
        geo_options = sorted(list(df[geo_col].unique()))
        selected_geo = st.sidebar.multiselect(f"Filter by {geo_col}:", options=geo_options, default=geo_options)
        filtered_df = filtered_df[filtered_df[geo_col].isin(selected_geo)]
        
    # 🛡️ 2. Active Combat Unit Name Selector Filter
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
                if 'Command Tier' in filtered_df.columns:
                    st.bar_chart(filtered_df.groupby('Command Tier').size().sort_values(ascending=False))
            with chart_col2:
                st.subheader("⚙️ System Metrics Profile Overview")
                st.info("Azure remediation summary logs are loaded. Use the bottom audit grid to inspect live fix states.")
                
        elif selected_table_key == 'SQLQry8T':
            with chart_col1:
                st.subheader("💎 Query Metric Vol by Global Theater")
                if 'Global Theater' in filtered_df.columns:
                    st.bar_chart(filtered_df.groupby('Global Theater').size().sort_values(ascending=False))
            with chart_col2:
                st.subheader("📊 Query Attribute Density")
                st.info("Database records are compiled. Charts will dynamically adjust based on column structural constraints.")
                
        elif selected_table_key == 'Military_Combat_Force_ReportT':
            with chart_col1:
                st.subheader("🪖 Unit Volume Distribution")
                if 'Active Combat Unit Name' in filtered_df.columns:
                    st.bar_chart(filtered_df.groupby('Active Combat Unit Name').size().sort_values(ascending=False))
            with chart_col2:
                st.subheader("📡 Force Capacity by Command Sector")
                if 'Strategic Command Sector' in filtered_df.columns:
                    st.bar_chart(filtered_df.groupby('Strategic Command Sector').size().sort_values(ascending=False))
                    
        elif 'Advanced_Military_Risk_Analysis' in selected_table_key:
            with chart_col1:
                st.subheader("⚡ Threat Density by Combat Unit")
                if 'Active Combat Unit Name' in filtered_df.columns:
                    st.bar_chart(filtered_df.groupby('Active Combat Unit Name').size().sort_values(ascending=False))
            with chart_col2:
                st.subheader("🎯 Strategic Risk Exposure Index")
                if 'Strategic Command Sector' in filtered_df.columns:
                    st.bar_chart(filtered_df.groupby('Strategic Command Sector').size().sort_values(ascending=False))

        st.subheader("📋 System Audit Trail Records")
        st.dataframe(filtered_df, use_container_width=True)
    else:
        st.warning("⚠️ No enterprise tracking records found in current workspace root.")

# --------------------------------------------------------------------
# ⚙️ TAB 2: UTILITIES (⚙️ Multi-Engine Operations Suite)
# --------------------------------------------------------------------
with tab_utilities:
    st.header("⚙️ Multi-Engine Operations Suite")
    
    st.subheader("🌐 Global Language Translation Engine")
    from deep_translator import GoogleTranslator
    try:
        langs = {k.title(): v for k, v in GoogleTranslator().get_supported_languages(as_dict=True).items()}
    except Exception:
        langs = {"English": "en", "Spanish": "es", "French": "fr"}
        
    t_c1, t_c2 = st.columns(2)
    with t_c1:
        src = st.selectbox("Source Language Context:", ["auto"] + sorted(list(langs.keys())))
        text = st.text_area("Direct Clipboard Paste Line:", placeholder="Paste text rows straight from your clipboard...", key="trans_paste_input")
    with t_c2:
        tgt = st.selectbox("Target Output Language Context:", sorted(list(langs.keys())), index=list(sorted(langs.keys())).index("Spanish") if "Spanish" in langs else 0)
        st.write("**Processed Translation:**")
        if text:
            try:
                src_lang_code = "auto" if src == "auto" else langs[src]
                translated_text = GoogleTranslator(source=src_lang_code, target=langs[tgt]).translate(text)
                st.info(translated_text)
            except Exception:
                st.error("Engine Translation Endpoint Timeout Error")
            
    st.markdown("---")
    
    # MODULE 2: Strategic Calculator with Logarithmic scaling
    st.subheader("🧮 Strategic Calculator Node")
    if "calc_input" not in st.session_state:
        st.session_state.calc_input = ""
        
    calc_col1, calc_col2 = st.columns(2)
    with calc_col1:
        expr = st.text_input("Formula Buffer Variance Scaling Entry Line:", value=st.session_state.calc_input, key="st_calc_box")
        b1, b2, b3, b4 = st.columns(4)
        if b1.button("sin", key="sin_b"): st.session_state.calc_input += "math.sin(math.radians("
        if b2.button("cos", key="cos_b"): st.session_state.calc_input += "math.cos(math.radians("
        if b3.button("log₁₀", key="log_b"): st.session_state.calc_input += "math.log10("
        if b4.button("√x", key="sqrt_b"): st.session_state.calc_input += "math.sqrt("
    with calc_col2:
        st.write("**Evaluation Output Node:**")
        if expr:
            try:
                res = eval(expr.replace("^", "**").replace("×", "*").replace("÷", "/"), {"math": math})
                if isinstance(res, float):
                    res = round(res, 8)
                st.success(f"**Computed Valuation Metrics:** `{res}`")
            except Exception:
                st.error("Variance Equation Parsing Error")
        if st.button("Flush Calculation Buffer"):
            st.session_state.calc_input = ""
            st.rerun()

# --------------------------------------------------------------------
# 💼 TAB 3: WORKSPACE (💼 Business Automation Module)
# --------------------------------------------------------------------
with tab_workspace:
    st.header("💼 Business Automation Module")
    
    # MODULE 3: Invoice & Quote Generator
    st.subheader("🧾 Invoice Generator Engine")
    if "invoice_items" not in st.session_state:
        st.session_state.invoice_items = []
        
    i1, i2, i3 = st.columns(3)
    client = i1.text_input("Client Organization:", "Enterprise Operations Command")
    inv_num = i2.text_input("System Voucher ID:", "VCH-9921")
    tax_rate = i3.slider("Regional Compliance Tax Scale (%)", 0.0, 25.0, 8.0)
    
    with st.expander("Add Entry Line Item", expanded=True):
        l1, l2, l3 = st.columns(3)
        d = l1.text_input("Line Item Description Field")
        q = l2.number_input("Unit Quantity Multiplier", min_value=1, value=1)
        p = l3.number_input("Cost Rate per Unit ($)", min_value=0.0, value=0.0)
        if st.button("Commit Line Entry Row"):
            if d:
                st.session_state.invoice_items.append({"Description": d, "Qty": q, "Unit Price": p, "Total": round(q * p, 2)})
                st.rerun()
                
    if st.session_state.invoice_items:
        inv_df = pd.DataFrame(st.session_state.invoice_items)
        st.dataframe(inv_df, use_container_width=True)
        sub = inv_df["Total"].sum()
        tx = round(sub * (tax_rate / 100), 2)
        grand = sub + tx
        st.markdown(f"**Subtotal:** ${sub:,.2f} | **Tax Overage:** ${tx:,.2f} | **Grand Matrix Valuation: ${grand:,.2f}**")
        
        # LIVE DATA GENERATION EXPORT MATRIX
        csv_data = inv_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="💾 Live Export PDF/CSV Generation Matrix",
            data=csv_data,
            file_name=f"{inv_num}_invoice_matrix.csv",
            mime="text/csv",
            use_container_width=True
        )
        if st.button("Flush Active Matrix Rows"):
            st.session_state.invoice_items = []
            st.rerun()
            
    st.markdown("---")
    
    # MODULE 4: Bulk File Renamer Engine with Specific FedMil Prefix Strippers
    st.subheader("📁 Bulk File Renamer Engine")
    
    asset_list = ["MIL-C-CombatUnit_Draft.xlsx", "Azure_Report_STG-04.csv"]
    asset_string_format = "\\n".join(asset_list)
    
    raw_txt = st.text_area("Target Asset Strings File Array (One file per row):", value=asset_string_format, key="renamer_txt_area")
    prefix_str = st.text_input("Inject Core Corporate Prefix Handle:", "2026_SecOps_")
    strip_fedmil = st.checkbox("Enable Specific FedMil Prefix Strippers (Removes 'MIL-C-' and 'STG-')", value=True)
    
    if raw_txt:
        records = []
        clean_lines = raw_txt.replace("\\n", "\n").split("\n")
        for name in [n.strip() for n in clean_lines if n.strip()]:
            b, e = name.rsplit(".", 1) if "." in name else (name, "")
            if strip_fedmil:
                b = b.replace("MIL-C-", "").replace("STG-", "")
            b = re.sub(r'[\s\-]+', '_', b)
            records.append({"Original": name, "Preview Result": f"{prefix_str}{b}" + (f".{e}" if e else "")})
        st.table(pd.DataFrame(records))

# --------------------------------------------------------------------
# ✈️ TAB 4: SIMULATION (✈️ Tactical Modeling Runway)
# --------------------------------------------------------------------
with tab_simulation:
    st.header("✈️ Tactical Modeling Runway")
    
    # MODULE 5: Runway Simulator Dashboard
    st.subheader("📉 Runway Simulator Dashboard")
    
    s_col1, s_col2 = st.columns(2)
    with s_col1:
        cash = st.number_input("Asset Liquidity Cash Reserves ($):", value=75000.0)
        rev = st.number_input("Baseline Asset Vector Inflow ($/Mo):", value=14000.0)
        burn = st.number_input("System Maintenance Overhead Outflow ($/Mo):", value=19500.0)
        hz = st.slider("Forecast Extrapolation Horizon (Months):", 6, 60, 24)
        
        # Flight Capacity Vector Ingestion Sliders
        st.markdown("**✈️ Live Flight Capacity / Vector Ingestion Sliders**")
        flight_capacity_vector = st.slider("Simulated Operations Load Flight Scale:", 0.5, 2.5, 1.0, step=0.1)
    
    with s_col2:
        adjusted_burn = burn * flight_capacity_vector
        net = rev - adjusted_burn
        
        if net >= 0:
            st.success(f"🚀 Vector Trajectory Sustainable: Infinite Lifecycle. Net Flow: +${net:,.2f}/mo")
        else:
            months_val = cash / abs(net)
            st.error(f"🚨 Vector Exhaustion Warning: Depletion vector modeled in {months_val:.1f} months. (Adjusted Burn Rate: ${adjusted_burn:,.2f}/mo)")
            
        t_data = [{"Month": m, "Reserves Vector": max(0.0, cash + (net * m))} for m in range(hz + 1)]
        st.line_chart(pd.DataFrame(t_data).set_index("Month"))
