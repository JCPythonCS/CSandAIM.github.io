import streamlit as st
import pandas as pd
import os
import math
import re

# 1. Force sidebar to be globally collapsible via the native UI chevron button
st.set_page_config(
    page_title="Computer Systems & AI Management", 
    layout="wide",
    initial_sidebar_state="expanded" 
)

# ====================================================================
# HEADER BANNER: 🏆 SYMMETRICAL BRANDING MATRIX (TEXT-SAFE NO IMAGES)
# ====================================================================
logob_col, title_col, logog_col = st.columns([1, 4, 1])

with logob_col:
    st.markdown("<h4 style='text-align: center; color: #64748B; padding-top: 10px;'>[ SYS-B ]</h4>", unsafe_markdown=True)

with title_col:
    st.markdown("<h1 style='text-align: center; color: #1E293B; margin-top: 0;'>🖥️ Computer Systems and AI Management Cockpit</h1>", unsafe_markdown=True)

with logog_col:
    st.markdown("<h4 style='text-align: center; color: #64748B; padding-top: 10px;'>[ AI-G ]</h4>", unsafe_markdown=True)

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
                try: vault[table_key] = pd.read_excel(file_name, sheet_name='Advanced_Military_Risk_Analysis')
                except Exception: vault[table_key] = pd.read_excel(file_name, sheet_name=0)
            else:
                vault[table_key] = pd.read_excel(file_name, sheet_name=0)
        except Exception: pass
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
        "Choose an Enterprise Data Sheet:", options=available_tables,
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
        if alternative in df.columns: geo_col = alternative; break
    if geo_col:
        geo_options = sorted(list(df[geo_col].unique()))
        selected_geo = st.sidebar.multiselect(f"Filter by {geo_col}:", options=geo_options, default=geo_options)
        filtered_df = filtered_df[filtered_df[geo_col].isin(selected_geo)]
        
    unit_col = None
    for alternative in ['Retailer', 'Active Combat Unit Name']:
        if alternative in df.columns: unit_col = alternative; break
    if unit_col:
        unit_options = sorted(list(df[unit_col].unique()))
        selected_unit = st.sidebar.multiselect(f"Filter by {unit_col}:", options=unit_options, default=unit_options)
        filtered_df = filtered_df[filtered_df[unit_col].isin(selected_unit)]

# ====================================================================
# THE ARCHITECTURE LAYOUT BLUEPRINT GRID TABS
# ====================================================================
tab_analytics, tab_utilities, tab_workspace, tab_simulation = st.tabs([
    "📊 Tab 1: Analytics", "⚙️ Tab 2: Utilities", "💼 Tab 3: Workspace", "✈️ Tab 4: Simulation"
])

# ---- TAB 1: ANALYTICS ----
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
            with chart_col1: st.subheader("🏆 Retailer Rankings"); st.bar_chart(filtered_df.groupby('Retailer')['Volume_USD'].sum().sort_values(ascending=False))
            with chart_col2: st.subheader("🔸 Sector Volume"); st.bar_chart(filtered_df.groupby('Market_Tier')['Volume_USD'].sum().sort_values(ascending=False))
        elif selected_table_key == 'Azure_Remediation_ReportT':
            with chart_col1: st.subheader("🛡️ Azure Vol by Command Tier"); st.bar_chart(filtered_df.groupby('Command Tier').size()) if 'Command Tier' in filtered_df.columns else st.write("")
            with chart_col2: st.subheader("⚙️ Metrics Profile"); st.info("Azure remediation summaries loaded.")
        elif selected_table_key == 'SQLQry8T':
            with chart_col1: st.subheader("💎 Vol by Theater"); st.bar_chart(filtered_df.groupby('Global Theater').size()) if 'Global Theater' in filtered_df.columns else st.write("")
            with chart_col2: st.subheader("📊 Attribute Density"); st.info("Staging table buffers compiled.")
        elif selected_table_key == 'Military_Combat_Force_ReportT':
            with chart_col1: st.subheader("🪖 Unit Distribution"); st.bar_chart(filtered_df.groupby('Active Combat Unit Name').size()) if 'Active Combat Unit Name' in filtered_df.columns else st.write("")
            with chart_col2: st.subheader("📡 Capacity by Command"); st.bar_chart(filtered_df.groupby('Strategic Command Sector').size()) if 'Strategic Command Sector' in filtered_df.columns else st.write("")
        elif 'Advanced_Military_Risk_Analysis' in selected_table_key:
            with chart_col1: st.subheader("⚡ Threat Density"); st.bar_chart(filtered_df.groupby('Active Combat Unit Name').size()) if 'Active Combat Unit Name' in filtered_df.columns else st.write("")
            with chart_col2: st.subheader("🎯 Strategic Risk Exposure"); st.bar_chart(filtered_df.groupby('Strategic Command Sector').size()) if 'Strategic Command Sector' in filtered_df.columns else st.write("")

        st.subheader("📋 System Audit Trail Records")
        st.dataframe(filtered_df, use_container_width=True)
    else: st.warning("⚠️ No enterprise tracking records found.")

# ---- TAB 2: UTILITIES ----
with tab_utilities:
    st.header("⚙️ Multi-Engine Operations Suite")
    st.subheader("🌐 Global Language Translation Engine")
    from deep_translator import GoogleTranslator
    try: langs = {k.title(): v for k, v in GoogleTranslator().get_supported_languages(as_dict=True).items()}
    except Exception: langs = {"English": "en", "Spanish": "es", "French": "fr"}
        
    t_c1, t_c2 = st.columns(2)
    with t_c1:
        src = st.selectbox("Source Language Context:", ["auto"] + sorted(list(langs.keys())))
        text = st.text_area("Direct Clipboard Paste Line:", key="trans_paste_input")
    with t_c2:
        tgt = st.selectbox("Target Output Language Context:", sorted(list(langs.keys())), index=list(sorted(langs.keys())).index("Spanish") if "Spanish" in langs else 0)
        st.write("**Processed Translation:**")
        if text:
            try: st.info(GoogleTranslator(source="auto" if src=="auto" else langs[src], target=langs[tgt]).translate(text))
            except Exception: st.error("Engine Translation Timeout")
            
    st.markdown("---")
    st.subheader("🧮 Strategic Calculator Node")
    if "calc_input" not in st.session_state: st.session_state.calc_input = ""
    calc_col1, calc_col2 = st.columns(2)
    with calc_col1:
        expr = st.text_input("Formula Buffer Entry Line:", value=st.session_state.calc_input, key="st_calc_box")
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
                st.success(f"**Computed Metrics:** `{round(res, 8) if isinstance(res, float) else res}`")
            except Exception: st.error("Equation Parsing Error")
        if st.button("Flush Calculation Buffer"): st.session_state.calc_input = ""; st.rerun()

# ---- TAB 3: WORKSPACE ----
with tab_workspace:
    st.header("💼 Business Automation Module")
    st.subheader("🧾 Invoice Generator Engine")
    if "invoice_items" not in st.session_state: st.session_state.invoice_items = []
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
            if d: st.session_state.invoice_items.append({"Description": d, "Qty": q, "UnitPrice": p, "Total": round(q * p, 2)}); st.rerun()
                
    if st.session_state.invoice_items:
        inv_df = pd.DataFrame(st.session_state.invoice_items)
        st.dataframe(inv_df, use_container_width=True)
        sub = inv_df["Total"].sum()
        tx = round(sub * (tax_rate / 100), 2)
        st.markdown(f"**Subtotal:** ${sub:,.2f} | **Tax Overage:** ${tx:,.2f} | **Grand Matrix Valuation: ${sub+tx:,.2f}**")
        st.download_button(label="💾 Live Export PDF/CSV Generation Matrix", data=inv_df.to_csv(index=False).encode('utf-8'), file_name=f"{inv_num}_invoice_matrix.csv", mime="text/csv", use_container_width=True)
        if st.button("Flush Active Matrix Rows"): st.session_state.invoice_items = []; st.rerun()
            
    st.markdown("---")
    st.subheader("📁 Bulk File Renamer Engine")
    asset_list = ["MIL-C-CombatUnit_Draft.xlsx", "Azure_Report_STG-04.csv"]
    raw_txt = st.text_area("Target Asset Strings Array (One per row):", value="\\n".join(asset_list), key="renamer_txt_area")
    prefix_str = st.text_input("Inject Core Prefix Handle:", "2026_SecOps_")
    strip_fedmil = st.checkbox("Enable Specific FedMil Prefix Strippers (Removes 'MIL-C-' and 'STG-')", value=True)
    
    if raw_txt:
        records = []
        for name in [n.strip() for n in raw_txt.replace("\\n", "\n").split("\n") if n.strip()]:
            b, e = name.rsplit(".", 1) if "." in name else (name, "")
            if strip_fedmil: b = b.replace("MIL-C-", "").replace("STG-", "")
            records.append({"Original": name, "Preview Result": f"{prefix_str}{re.sub(r'[\s\-]+', '_', b)}" + (f".{e}" if e else "")})
        st.table(pd.DataFrame(records))
