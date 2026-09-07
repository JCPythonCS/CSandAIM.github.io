import streamlit as st
import pandas as pd
import os
import math
import re

st.set_page_config(page_title="Computer Systems & AI Management", layout="wide")

# 🏆 Professional Company Title Banner
st.title("🖥️ Computer Systems and AI Management Cockpit")
st.markdown("---")

# ====================================================================
# COCKPIT NAVIGATION CONTROL TABS
# ====================================================================
tab_dashboard, tab_tools = st.tabs(["📊 Enterprise Data Vault Dashboard", "🧰 Management Tools Workspace"])

# ====================================================================
# TAB 1: ENTERPRISE DATA VAULT DASHBOARD (Your Original App Script)
# ====================================================================
with tab_dashboard:
    # PHASE 1: DATA INGESTION (Loads files into memory once)
    @st.cache_data
    def load_all_enterprise_data():
        data_folder = '.'
        all_files = [f for f in os.listdir(data_folder) if f.lower().endswith(('.xlsx', '.xls'))]
        
        vault = {}
        for file_name in all_files:
            table_key = file_name.replace('.xlsx', '').replace('.xls', '')
            try:
                xl = pd.ExcelFile(file_name)
                target_sheet = xl.sheet_names
                
                # Fallback sequence ensures the sheet reads properly even with name mismatches
                if 'Advanced_Military_Risk_Analysis' in table_key:
                    try:
                        vault[table_key] = pd.read_excel(file_name, sheet_name='Advanced_Military_Risk_Analysis')
                    except:
                        vault[table_key] = pd.read_excel(file_name, sheet_name=0)
                else:
                    vault[table_key] = pd.read_excel(file_name, sheet_name=0)
            except Exception as e:
                pass
        return vault

    # Initialize the global data vault database
    database = load_all_enterprise_data()

    # PHASE 2: DATA SELECTION
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
        
        # Clean out blank column headers for the massive risk matrix
        if 'Advanced_Military_Risk_Analysis' in selected_table_key:
            df = df.dropna(axis=1, how='all')
        
        # 🧼 INSTANT DATA CLEANING: Standardize text columns BEFORE filtering
        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].astype(str).str.strip()
                
        st.markdown(f"### 📊 Currently Active File: `{selected_table_key}.xlsx`")
        st.markdown("---")
        
        # PHASE 3: SIDEBAR FILTERS (Fully Mapped to Enterprise Columns)
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
        
        # PHASE 4: DYNAMIC MULTI-SHEET VISUALIZATION LOGIC
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
            elif 'Advanced_Military_Risk_Analysis' in selected_table_key:
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

            # Raw Data Audit Trail Matrix Window Grid View
            st.subheader("📋 System Audit Trail Records")
            st.dataframe(filtered_df, use_container_width=True)
        else:
            st.warning("⚠️ The filtered dataset is empty. Adjust your sidebar settings.")
    else:
        st.warning("⚠️ No enterprise tracking records found in current workspace root.")

# ====================================================================
# TAB 2: MANAGEMENT TOOLS WORKSPACE (All 5 New Utilities)
# ====================================================================
with tab_tools:
    st.header("🧰 Custom Operational Tools")
    st.write("Access your supplementary standalone calculations and utilities.")
    
    selected_tool = st.selectbox(
        "Select a Workspace Utility to Launch:",
        ["Scientific Calculator", "Multi-Language Translator", "Invoice & Quote Generator", "Runway Simulator", "Bulk File Renamer"]
    )
    st.markdown("---")

    # ---- 1. SCIENTIFIC CALCULATOR ----
    if selected_tool == "Scientific Calculator":
        if "calc_input" not in st.session_state:
            st.session_state.calc_input = ""
            
        c1, c2 = st.columns(2)
        with c1:
            expr = st.text_input("Enter expression:", value=st.session_state.calc_input, key="calc_box")
            b_col1, b_col2, b_col3, b_col4 = st.columns(4)
            if b_col1.button("sin"): st.session_state.calc_input += "math.sin(math.radians("
            if b_col2.button("cos"): st.session_state.calc_input += "math.cos(math.radians("
            if b_col3.button("tan"): st.session_state.calc_input += "math.tan(math.radians("
            if b_col4.button("√"): st.session_state.calc_input += "math.sqrt("
        with c2:
            st.write("#### Output Panel")
            if expr:
                try:
                    res = eval(expr.replace("^", "**").replace("π", "math.pi"), {"math": math})
                    st.success(f"**Result:** {res}")
                except: 
                    st.error("Syntax Error")
            if st.button("Clear Buffer"):
                st.session_state.calc_input = ""
                st.rerun()

    # ---- 2. TRANSLATOR ----
    elif selected_tool == "Multi-Language Translator":
        from deep_translator import GoogleTranslator
        try:
            langs = {k.title(): v for k, v in GoogleTranslator().get_supported_languages(as_dict=True).items()}
        except:
            langs = {"English": "en", "Spanish": "es", "French": "fr"}
            
        t_c1, t_c2 = st.columns(2)
        with t_c1:
            src = st.selectbox("From Language:", ["auto"] + sorted(list(langs.keys())))
            text = st.text_area("Source Text Box:")
        with t_c2:
            tgt = st.selectbox("To Language:", sorted(list(langs.keys())), index=list(sorted(langs.keys())).index("Spanish") if "Spanish" in langs else 0)
            st.write("**Translation Output:**")
            if text:
                try:
                    st.info(GoogleTranslator(source="auto" if src == "auto" else langs[src], target=langs[tgt]).translate(text))
                except: 
                    st.error("Engine Connection Error")

    # ---- 3. INVOICE GENERATOR ----
    elif selected_tool == "Invoice & Quote Generator":
        if "invoice_items" not in st.session_state:
            st.session_state.invoice_items = []
        i_c1, i_c2, i_c3 = st.columns(3)
        client = i_c1.text_input("Client:", "Valued Client")
        inv_num = i_c2.text_input("Invoice #:", "INV-1001")
        tax_rate = i_c3.slider("Tax Rate (%)", 0.0, 25.0, 8.0)
        
        with st.expander("Add Entry Line Item", expanded=True):
            l1, l2, l3 = st.columns(3)
            d = l1.text_input("Line Description")
            q = l2.number_input("Qty", min_value=1, value=1)
            p = l3.number_input("Price ($)", min_value=0.0, value=0.0)
            if st.button("Append Line Item"):
                if d:
                    st.session_state.invoice_items.append({"Description": d, "Qty": q, "Unit Price": p, "Total": round(q * p, 2)})
                    st.rerun()
                    
        if st.session_state.invoice_items:
            inv_df = pd.DataFrame(st.session_state.invoice_items)
            st.dataframe(inv_df, use_container_width=True)
            sub = inv_df["Total"].sum()
            tx = round(sub * (tax_rate / 100), 2)
            st.markdown(f"**Subtotal:** ${sub:,.2f} | **Tax:** ${tx:,.2f} | **Grand Total: ${sub+tx:,.2f}**")
            if st.button("Reset Invoice Frame"):
                st.session_state.invoice_items = []
                st.rerun()

    # ---- 4. RUNWAY SIMULATOR ----
    elif selected_tool == "Runway Simulator":
        r_c1, r_c2 = st.columns(2)
        with r_c1:
            cash = st.number_input("Starting Cash ($):", value=50000.0)
            rev = st.number_input("Monthly Revenue ($):", value=8000.0)
            burn = st.number_input("Monthly Cost Outflow ($):", value=12000.0)
            hz = st.slider("Horizon Range (Months):", 6, 60, 24)
        with r_c2:
            net = rev - burn
            if net >= 0: 
                st.success(f"Infinite runway! Net Cashflow: +${net:,.2f}")
            else:
                months_val = cash / abs(net)
                st.error(f"Depletion Warning: Cash exhausted in {months_val:.1f} months.")
            t_data = [{"Month": m, "Balance": max(0.0, cash + (net * m))} for m in range(hz + 1)]
            st.line_chart(pd.DataFrame(t_data).set_index("Month"))

    # ---- 5. BULK RENAMER ----
    elif selected_tool == "Bulk File Renamer":
        raw_txt = st.text_area("Target Filenames:", "Asset_01.png\nDocument_Draft.docx")
        prefix_str = st.text_input("Prepend Prefix:", "2026_Audit_")
        c_choice = st.selectbox("Transformation Type:", ["Keep Case", "Lower", "Upper"])
        
        if raw_txt:
            records = []
            for name in [n.strip() for n in raw_txt.split("\n") if n.strip()]:
                b, e = name.rsplit(".", 1) if "." in name else (name, "")
                b = re.sub(r'[\s\-]+', '_', b)
                if c_choice == "Lower": 
                    b, e = b.lower(), e.lower()
                elif c_choice == "Upper": 
                    b, e = b.upper(), e.upper()
                records.append({"Original": name, "Preview Result": f"{prefix_str}{b}" + (f".{e}" if e else "")})
            st.table(pd.DataFrame(records))
