import streamlit as st
import pandas as pd
import math
import re

def render_translator():
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
                st.info(GoogleTranslator(source=src_lang_code, target=langs[tgt]).translate(text))
            except Exception:
                st.error("Engine Translation Endpoint Timeout Error")

def render_calculator():
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
                st.success(f"**Computed Valuation Metrics:** `{round(res, 8) if isinstance(res, float) else res}`")
            except Exception:
                st.error("Variance Equation Parsing Error")
        if st.button("Flush Calculation Buffer"):
            st.session_state.calc_input = ""
            st.rerun()

def render_invoice():
    st.subheader("🧾 Invoice Generator Engine")
    if "invoice_items" not in st.session_state:
        st.session_state.invoice_items = []
        
    i1, i2, i3 = st.columns(3)
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
        st.markdown(f"**Subtotal:** ${sub:,.2f} | **Tax Overage:** ${tx:,.2f} | **Grand Matrix Valuation: ${sub+tx:,.2f}**")
        st.download_button(label="💾 Live Export PDF/CSV Generation Matrix", data=inv_df.to_csv(index=False).encode('utf-8'), file_name=f"{inv_num}_invoice_matrix.csv", mime="text/csv", use_container_width=True)
        if st.button("Flush Active Matrix Rows"):
            st.session_state.invoice_items = []
            st.rerun()

def render_renamer():
    st.subheader("📁 Bulk File Renamer Engine")
    asset_list = ["MIL-C-CombatUnit_Draft.xlsx", "Azure_Report_STG-04.csv"]
    raw_txt = st.text_area("Target Asset Strings Array (One per row):", value="\\n".join(asset_list), key="renamer_txt_area")
    prefix_str = st.text_input("Inject Core Prefix Handle:", "2026_SecOps_")
    strip_fedmil = st.checkbox("Enable Specific FedMil Prefix Strippers (Removes 'MIL-C-' and 'STG-')", value=True)
    
    if raw_txt:
        records = []
        for name in [n.strip() for n in raw_txt.replace("\\n", "\n").split("\n") if n.strip()]:
            b, e = name.rsplit(".", 1) if "." in name else (name, "")
            if strip_fedmil:
                b = b.replace("MIL-C-", "").replace("STG-", "")
            records.append({"Original": name, "Preview Result": f"{prefix_str}{re.sub(r'[\s\-]+', '_', b)}" + (f".{e}" if e else "")})
        st.table(pd.DataFrame(records))

def render_runway():
    st.subheader("📉 Runway Simulator Dashboard")
    s_col1, s_col2 = st.columns(2)
    with s_col1:
        cash = st.number_input("Asset Liquidity Cash Reserves ($):", value=75000.0)
        rev = st.number_input("Baseline Asset Vector Inflow ($/Mo):", value=14000.0)
        burn = st.number_input("System Maintenance Overhead Outflow ($/Mo):", value=19500.0)
        hz = st.slider("Forecast Extrapolation Horizon (Months):", 6, 60, 24)
        flight_capacity_vector = st.slider("Simulated Operations Load Flight Scale:", 0.5, 2.5, 1.0, step=0.1)
    with s_col2:
        adjusted_burn = burn * flight_capacity_vector
        net = rev - adjusted_burn
        if net >= 0:
            st.success(f"🚀 Vector Trajectory Sustainable: Infinite Lifecycle. Net Flow: +${net:,.2f}/mo")
        else:
            st.error(f"🚨 Vector Exhaustion Warning: Depletion vector modeled in {cash / abs(net):.1f} months. (Adjusted Burn Rate: ${adjusted_burn:,.2f}/mo)")
        st.line_chart(pd.DataFrame([{"Month": m, "Reserves Vector": max(0.0, cash + (net * m))} for m in range(hz + 1)]).set_index("Month"))
