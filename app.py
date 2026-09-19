import streamlit as st
import pandas as pd
import os
import time
import datetime

# =========================================================================
# 🔒 CENTRAL AUTHENTICATION CONTROL PERIMETER GATE
# =========================================================================
st.sidebar.markdown("### 🔑 Terminal Access Authentication")
auth_token = st.sidebar.text_input("Enter Active Subscription License Key:", type="password", help="Paste your unique enterprise alphanumeric credential key here.")

# Initialize the authorization validation parameters natively
is_authorized = False
session_license = "Locked"

# Hardcoded administrative encryption lookup key strings
if auth_token == "C7JW7AXC6B!pD7y":
    is_authorized = True
    session_license = "Administrative Root / Diamond Enterprise"
elif auth_token == "CSAM-SILVER-992":
    is_authorized = True
    session_license = "Silver Node"
elif auth_token == "CSAM-GOLD-774":
    is_authorized = True
    session_license = "Gold Command"
elif auth_token == "CSAM-PLATINUM-120":
    is_authorized = True
    session_license = "Platinum Executive"

# Render the active security status badge inside the sidebar container
if not auth_token:
    st.sidebar.info("⏳ Core Ingestion Node Locked. Awaiting access token entry.")
elif is_authorized:
    st.sidebar.success(f"🟢 {session_license} Connection Fully Verified.")
else:
    st.sidebar.error("❌ Access Denied: Invalid Alphanumeric Credential Block.")

# 🚫 STEP 2: THE ABSOLUTE ENFORCEMENT FILTER SHUTOFF
if not is_authorized:
    st.title("🔒 C-SAM AI Management Cockpit Terminal V4.0")
    st.warning("🔬 **Secure Encryption Firewall Active:** This computing node is running in centralized protected mode. To access your specialized diagnostic suite layout panels, please enter your authorized license key inside the sidebar portal field.")
    st.info("💡 **Subscription Verification:** If you do not have a license, open the pricing cards in the sidebar section to initialize a secure transaction via PayPal.")
    st.stop() # 🛑 This single instruction completely freezes the app right here, blocking your 120 tools from downloading!

# 🚫 STEP 3: TIERED LEVEL BOUNDARY LOCKOUT FILTERS
if session_license == "Silver Node":
    allowed_silver_panels = ["🌐 Utilities (Tab 2)", "📋 Project Management (Tab 7)", "🤖 AI-Ops Parsing (Tab 10)"]
    if 'active_panel' in locals() and active_panel not in allowed_silver_panels:
        st.error("🔒 Security Boundary Alert: Your Silver Node Access tier does not cover this tactical engine block. Please adjust your tab choice or upgrade your license.")
        st.stop()

elif session_license == "Gold Command":
    allowed_gold_panels = ["📊 Analytics (Tab 1)", "✈️ Simulation (Tab 4)", "📦 Supply Chain (Tab 8)", "🏎️ Fleet & Automotive (Tab 9)"]
    if 'active_panel' in locals() and active_panel not in allowed_gold_panels:
        st.error("🔒 Security Boundary Alert: Your Gold Command Access tier does not cover this cybersecurity arena node. Upgrade to Platinum to unlock.")
        st.stop()

# Import all of your specific tool handlers from your workspace_modules.py file
import workspace_modules as wm

# 🖥️ Exact Page Config from your Repository
st.set_page_config(page_title="Computer Systems and AI Management Cockpit", layout="wide")

# 🏆 MASTER TITLE BLOCK DESIGN WITH YOUR DUAL SIDE-SPACED LOGOS
st.title("🛡️ Computer Systems and AI Management Cockpit")

# FIXED LOGO GRID: Allocates a precise 3-column framework to avoid TypeError crashes
col_logo_left, col_title_spacer, col_logo_right = st.columns(3)

with col_logo_left:
    if os.path.exists("LOGOB.png"):
        st.image("LOGOB.png", use_container_width=True)
    else:
        st.caption("🖼️ `LOGOB.png` missing from root repository directory slot")

with col_logo_right:
    if os.path.exists("LOGOG.png"):
        st.image("LOGOG.png", use_container_width=True)
    else:
        st.caption("🖼️ `LOGOG.png` missing from root repository directory slot")

st.markdown("---")

st.markdown("---")
st.markdown("### 💎 Premium SaaS Access")
st.caption("Select your operational tier below to unlock full cockpit capabilities.")

# 🔓 SECURE CSS CONFIGURATION FIREWALL
st.markdown(
    """
    <style>
        /* Forces the sidebar navigation drawer to lock wide open permanently */
        [data-testid="stSidebarCollapseButton"] {
            display: none !important;
        }
        [data-testid="stSidebar"] {
            min-width: 320px !important;
            max-width: 320px !important;
        }
        /* Forces sidebar metric font elements into a tight, compact profile */
        div[data-testid="stSidebar"] div[data-testid="stMetricValue"] {
            font-size: 1.4rem !important;
            font-weight: bold !important;
        }
        div[data-testid="stSidebar"] div[data-testid="stMetricLabel"] {
            font-size: 0.85rem !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ⏱️ ROW 1: COMPACT REGIONAL TIMELINE & EASTERN CLOCK LOCALIZED INSIDE SIDEBAR
st.sidebar.markdown("### 📋 Operations Timeline & Clock")

import datetime
utc_now = datetime.datetime.utcnow()
est_offset = datetime.timedelta(hours=-4) 
est_now = utc_now + est_offset

# Using %a instead of %A shortens "Saturday" to "Sat" immediately so it never cuts off!
st.sidebar.metric(label="⏱️ Eastern Time (EST/EDT)", value=est_now.strftime("%I:%M:%S %p"))
st.sidebar.metric(label="📅 Current System Date", value=est_now.strftime("%a, %b %d, %Y"))
st.sidebar.info("📍 Operational Target: Business Cycle Running Stable")

# 🗓️ ROW 2: AUTOMATED SCROLLABLE MONDAY-FIRST CORPORATE CALENDAR ENGINE
import calendar
st.sidebar.markdown("#### 🗓️ Master Operations Calendar")

# Initialize session state trackers natively so the scroll memory persists
if 'cal_year' not in st.session_state or 'cal_month' not in st.session_state:
    st.session_state.cal_year = est_now.year
    st.session_state.cal_month = est_now.month

# Render small horizontal layout scroll arrow buttons inside the sidebar
c_prev, c_next = st.sidebar.columns(2)
with c_prev:
    if st.button("◀ Last Month", key="cal_scroll_prev", use_container_width=True):
        st.session_state.cal_month -= 1
        if st.session_state.cal_month == 0:
            st.session_state.cal_month = 12
            st.session_state.cal_year -= 1
with c_next:
    if st.button("Next Month ▶", key="cal_scroll_next", use_container_width=True):
        st.session_state.cal_month += 1
        if st.session_state.cal_month == 13:
            st.session_state.cal_month = 1
            st.session_state.cal_year += 1

# Calculate calendar dimensions using strict Monday-first formatting parameters (0 = Monday)
cal_obj = calendar.Calendar(firstweekday=0)
month_weeks = cal_obj.monthdayscalendar(st.session_state.cal_year, st.session_state.cal_month)
month_name = calendar.month_name[st.session_state.cal_month].upper()

# Generate the high-end custom visual grid table matrix on the fly
html_days_rows = ""
for week in month_weeks:
    html_days_rows += "<tr>"
    for day in week:
        if day == 0:
            html_days_rows += "<td style='padding: 4px; color: #334155;'>&nbsp;</td>"
        else:
            # Dynamically verify if this calendar box matches today's exact date
            is_today = (day == est_now.day and st.session_state.cal_month == est_now.month and st.session_state.cal_year == est_now.year)
            if is_today:
                html_days_rows += f"<td style='background-color: #22c55e; color: white; border-radius: 4px; font-weight: bold; padding: 4px;'>{day}</td>"
            else:
                html_days_rows += f"<td style='padding: 4px;'>{day}</td>"
    html_days_rows += "</tr>"

# Render the dynamic interface container directly inside the sidebar layout view
st.sidebar.markdown(f"""
<div style="background-color: #0f172a; padding: 10px; border-radius: 6px; border: 1px solid #334155; font-family: monospace;">
    <p style="color: #38bdf8; font-weight: bold; margin: 0 0 5px 0; text-align: center;">📅 {month_name} {st.session_state.cal_year}</p>
    <table style="width: 100%; text-align: center; color: #94a3b8; font-size: 0.8rem; border-collapse: collapse;">
        <tr style="color: #f1f5f9; font-weight: bold;">
            <td style="padding: 3px;">M</td><td style="padding: 3px;">T</td><td style="padding: 3px;">W</td><td style="padding: 3px;">T</td><td style="padding: 3px;">F</td><td style="color: #ef4444; padding: 3px;">S</td><td style="color: #ef4444; padding: 3px;">S</td>
        </tr>
        {html_days_rows}
    </table>
</div>
""", unsafe_allow_html=True)

# 💎 ROW 3: CORPORATE ACCESS HEADER BRIDGE
# 💎 PREMIUM ACCESS SIDEBAR LAYER POSITIONED ABOVE PAYPAL BUTTONS

# 🏢 CORPORATE INFORMATION FOOTPRINT BOUND TO SIDEBAR
st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    <div style="background-color: #0f172a; padding: 12px; border-radius: 6px; border: 1px solid #334155; color: #94a3b8; font-size: 0.8rem; line-height: 1.4;">
        <div style="font-weight: bold; color: #f1f5f9; font-size: 0.85rem; margin-bottom: 2px;">🖥️ Computer Systems & AI Management</div>
        <div style="color: #38bdf8; font-family: monospace; font-size: 0.75rem; margin-bottom: 1px;">📧 jcpython@outlook.com</div>
        <div style="color: #38bdf8; font-family: monospace; font-size: 0.75rem; margin-bottom: 6px;">📞 (864) 864-9954</div>
        <div style="margin-bottom: 2px;"><b>Version:</b> 4.2.0-SaaS (Production)</div>
        <div style="margin-bottom: 2px;"><b>Global Network Operations Center</b></div>
        <div style="margin-bottom: 2px; font-size: 0.7rem; color: #64748b;">All Rights Reserved © 2026</div>
    </div>
    """,
    unsafe_allow_html=True
)

# 💳 LEVEL 1: SILVER TIER BUTTON
with st.expander("🥈 Silver Node Access", expanded=False):
    st.markdown("**Cost:** $249 / month")
    st.markdown("""
    * 🔓 Access to Core System Utilities (Tabs 2, 7, 10)
    * ⚙️ Standard Engine Compute Performance
    * 📊 Basic File Operations Log & Workspace Ingestion
    """)
    st.link_button("Subscribe with PayPal", "https://www.paypal.com/ncp/payment/RQ5S9FDVX8RY2", use_container_width=True, type="secondary")

# 💳 LEVEL 2: GOLD TIER BUTTON
with st.expander("🥇 Gold Command Access", expanded=False):
    st.markdown("**Cost:** $359 / month")
    st.markdown("""
    * 🚀 Unlocks Advanced Predictive Suites (Tabs 1, 4, 8, 9)
    * 📈 Multi-Region Forecasting Models & Funnel Attribution Analytics
    * 🏎️ Fleet OBD Freeze Frame Telematics Diagnostics Generators
    """)
    st.link_button("Subscribe with PayPal", "https://www.paypal.com/ncp/payment/S38BCHZZRUWSE", use_container_width=True, type="secondary")

# 💳 LEVEL 3: PLATINUM TIER BUTTON
with st.expander("👑 Platinum Executive Suite", expanded=False):
    st.markdown("**Cost:** $499 / month")
    st.markdown("""
    * 👑 Complete Unrestricted Access Across All 115 Operational Diagnostics
    * 🔒 Full Integration of the 10-Tool Cybersecurity & Threat Arena (Tab 11)
    * 🤖 High-Performance AI-Ops Text Parsing & Sandbox Automation
    """)
    st.link_button("Subscribe with PayPal", "https://www.paypal.com/ncp/payment/FVYSK226TLYKA", use_container_width=True, type="secondary")

# 💳 LEVEL 4: DIAMOND ENTERPRISE TIER BUTTON
with st.expander("💎 Diamond Enterprise Node", expanded=False):
    st.markdown("**Cost:** $799 / month")
    st.markdown("""
    * 💎 Tailored Corporate White-Label Deployment Package
    * 🏢 Injection of Dedicated Company Branding, Names, & Asset Logos
    * ⚡ Priority Email Support & Custom Database Filter Configuration
    """)
    st.link_button("Subscribe with PayPal", "https://www.paypal.com/ncp/payment/GFQ2Y5KZMRM9E", use_container_width=True, type="secondary")

st.markdown("---")
    
# 💡 FEEDBACK & SUGGESTION BOX AREA
st.header("💡 Systems Suggestion Box")
with st.form(key="sidebar_suggestion_form", clear_on_submit=True):
    user_email = st.text_input("Subscriber Email Address:", placeholder="name@domain.com")
    suggestion_topic = st.selectbox("Target Node/Tool Component:", ["General Cockpit", "Analytics Streams", "Simulation Engine", "Audio Profiles", "Request New Tool"])
    suggestion_text = st.text_area("Provide System Feedback or Feature Requests:", max_chars=500, placeholder="Describe your requested feature or adjustment here...")

    # Define the form button first so Python recognizes the variable block!
    submit_suggestion = st.form_submit_button("Compile Feedback Logs")

    if submit_suggestion:
        if suggestion_text.strip():
            # 📝 Encode the text strings safely for browser link transit
            subject_encoded = urllib.parse.quote(f"🚀 Cockpit Feedback: {suggestion_topic}")
            body_encoded = urllib.parse.quote(f"Sender: {user_email}\n\nFeedback:\n{suggestion_text}")
            
            # Construct the native direct mail gateway link
            mailto_url = f"mailto:jcpps1@://outlook.com{subject_encoded}&body={body_encoded}"
            
            st.success("✅ Telemetry logs compiled! Click the routing link below to authorize final delivery:")
            st.markdown(f'<a href="{mailto_url}" target="_blank" style="display: inline-block; padding: 10px 20px; background-color: #22c55e; color: white; text-decoration: none; border-radius: 4px; font-weight: bold;">📧 Launch Mail Client Gateway</a>', unsafe_allow_html=True)
            
            # Ingestion logger settings
            target_corporate_node = "jcpps1@outlook.com"
        else:
            st.error("⚠️ System transmission error: Feedback message body content cannot be empty.")

        
    if submit_suggestion:
        if suggestion_text.strip():
            # 📡 STAGING DATA PAYLOAD ROUTING LOGS
            target_corporate_node = "jcpps1@outlook.com"

# 🎛️ COCKPIT MASTER NAVIGATION (Ungrouped Selection Panels)
active_panel = st.selectbox(
    "Select Workspace System Node To Deploy:",
    [
        "📊 Analytics (Tab 1)",
        "🛠 Utilities (Tab 2)",
        "💼 Workspace (Tab 3)",
        "✈ Simulation (Tab 4)",
        "📚 Library (Tab 5)",
        "💰 Commercial Control (Tab 6)",
        "📋 Project Management (Tab 7)",
        "📦 Supply Chain & Logistics (Tab 8)",
        "🏎️ Fleet & Automotive (Tab 9)",
        "🤖 AI-Ops Text Parsing (Tab 10)",
        "🔒 Cybersecurity & Intrusion (Tab 11)"
    ],
    key="cockpit_panel_navigation"
)
        
male_profile = "Male_Adam (Deep/Calm)"
female_profile = "Female_Emily (Smooth)"

if active_panel == "📚 Library (Tab 5)":
    st.sidebar.markdown("---")
    st.sidebar.header("🗣 Audio Profiles Configuration")
    male_profile = st.sidebar.selectbox("Male Actor Voice", ["Male_Adam (Deep/Calm)", "Male_Michael (Professional)", "Male_David"])
    female_profile = st.sidebar.selectbox("Female Actor Voice", ["Female_Emily (Smooth)", "Female_Serena (Narrator)", "Female_Rachel"])
    st.sidebar.markdown("---")
    st.sidebar.caption("Voice Profile Parameters Active on Library Canvas")
else:
    male_profile = "Male_Adam (Deep/Calm)"
    female_profile = "Female_Emily (Smooth)"


    # ==========================================================================
    # 📋 PERMANENT ACTIVE STREAM REGISTERS MAPPING
    # ==========================================================================
    st.markdown("---")
    st.markdown("### Real-Time Customer Purchase Logs & Delivery Staging Node")

# 📊 UNIFORM STRUCTURAL WRAPPERS FOR CORE TIMELINE ANALYTICS SUITES WITH STANDBY NOIDES
if 'wm' in locals() and active_panel == "📊 Analytics (Tab 1)":
    # Tool 1: KPI Pulse Grid
    with st.expander("📊 Core Corporate KPI Pulse Grid System", expanded=False):
        if hasattr(wm, 'render_kpi_pulse_grid'):
            wm.render_kpi_pulse_grid()
        else:
            st.warning("⚠️ System Standby Status: Core Ingestion Matrix Running Optimal.")

    # Tool 2: Funnel Attribution
    with st.expander("📈 Multi-Region Funnel Attribution Modeler", expanded=False):
        if hasattr(wm, 'render_funnel_attribution'):
            wm.render_funnel_attribution()
        else:
            st.warning("⚠️ System Standby Status: Analytical Alignment Parity Established.")

    # Tool 3: Pipeline Forecaster
    with st.expander("📉 Automated Predictive Sales Pipeline Forecaster", expanded=False):
        if hasattr(wm, 'render_pipeline_forecaster'):
            wm.render_pipeline_forecaster()
        else:
            st.warning("⚠️ System Standby Status: Predictive Model Horizon Fully Balanced.")

    # Tool 4: Conversion Velocity
    with st.expander("🔄 High-Velocity Conversion Drop-off Optimizer (V5)", expanded=False):
        if hasattr(wm, 'render_conversion_velocity_v5'):
            wm.render_conversion_velocity_v5()
        else:
            st.warning("⚠️ System Standby Status: Optimization Vectors Compressed Stable.")

    # Tool 5: Lead Velocity
    with st.expander("🏎️ Territorial Lead Generation Velocity Engine (V6)", expanded=False):
        if hasattr(wm, 'render_lead_velocity_v6'):
            wm.render_lead_velocity_v6()
        else:
            st.warning("⚠️ System Standby Status: Velocity Trajectory Monitored Active.")

# =========================================================================
# 📊 TAB 1: EXECUTIVE ANALYTICS COMPLIANCE EXPANSION (5 LIVE ACTIVE TOOLS)
# =========================================================================
if 'active_panel' in locals() and active_panel == "📊 Analytics (Tab 1)":
    st.markdown("---")
    st.markdown("### ⚡ Live Asset Optimization Core")
    
    # Tool 6: Pipeline Leakage Tracker
    with st.expander("📊 B2B Sales Funnel Pipeline Leakage Tracker", expanded=False):
        st.write("### 🔍 Live Funnel Analytics Data Flow")
        leakage_rate = st.slider("Simulate Pipeline Funnel Leakage Risk Rate (%):", 0, 100, 24, key="live_leakage_sl")
        if leakage_rate > 40:
            st.error(f"🚨 Critical Alert: Funnel leakage risk is elevated at {leakage_rate}%. Optimization required.")
        else:
            st.success(f"🟢 Optimal Operations: Pipeline leakage risk is highly stable at {leakage_rate}%.")

    # Tool 7: Conversion Funnel Drop-off Diagnostic Tool
    with st.expander("📈 B2B Operational Conversion Funnel Drop-off Diagnostic Tool", expanded=False):
        st.write("### 📈 Live Drop-off Volumetric Ingestion Vectors")
        drop_off = st.number_input("Enter Baseline Operational Drop-off Count:", min_value=0, value=150, key="live_drop_v")
        st.metric(label="📊 Computed Traffic Retention Index", value=f"{1000 - drop_off} Units")

    # Tool 8: Cross-Channel CAC Multiplier Calculator Matrix
    with st.expander("📉 Cross-Channel CAC Multiplier Calculator Matrix", expanded=False):
        st.write("### 📉 Live CAC Multiplier Asset Analysis Matrices")
        base_cac = st.number_input("Baseline Multi-Channel Acquisition Cost ($):", min_value=1.0, value=45.0, step=5.0, key="live_cac_mult")
        multiplier = st.slider("Cross-Channel Conversion Scale Factor:", 1.0, 5.0, 1.8, step=0.1, key="live_cac_sl")
        st.info(f"💰 True Enterprise Customer Acquisition Value: ${base_cac * multiplier:.2f}")

    # Tool 9: Regional Customer Acquisition Velocity Engine
    with st.expander("📊 Regional Customer Acquisition Velocity Engine", expanded=False):
        st.write("### 📊 Live Territorial Lead Velocity Tracking")
        lead_count = st.number_input("Enter New Ingested Monthly Leads:", min_value=0, value=250, key="live_lead_vel")
        days = st.slider("Select Horizon Observation Window (Days):", 1, 30, 7, key="live_days_vel")
        st.metric(label="🏎️ Computed Acquisition Rate", value=f"{lead_count / days:.1f} Leads / Day")

    # Tool 10: Multi-Channel Attribution Analytics Hub
    with st.expander("🎛️ Multi-Channel Attribution Analytics Hub", expanded=False):
        st.write("### 🎛️ Fractional Funnel Attribution Framework")
        paid_ads = st.slider("Paid Advertising Attribution Weight (%):", 0, 100, 40, key="live_attr_paid")
        organic = st.slider("Organic Search Traffic Weight (%):", 0, 100, 35, key="live_attr_org")
        referral = 100 - (paid_ads + organic)
        if paid_ads + organic > 100:
            st.error("⚠️ System calculation mismatch: Combined allocation weight cannot exceed 100%.")
        else:
            st.info(f"🔹 Remainder Channel Attribution Weight (Referrals/Direct): {referral}%")

# ---- PANEL 2: UTILITIES (Tab 2) ----
if active_panel == "🛠 Utilities (Tab 2)": # <--- MAKE SURE THIS IS 'elif' WITH NO INDENTATION SPACES
    if 'wm' in locals():
        if hasattr(wm, 'render_translator'): wm.render_translator()
        st.markdown("---")
        if hasattr(wm, 'render_renamer'): wm.render_renamer()
        if hasattr(wm, 'render_threat_analyzer'): wm.render_threat_analyzer()
        if hasattr(wm, 'render_ip_throttle_monitor'): wm.render_ip_throttle_monitor()
        if hasattr(wm, 'render_token_radar'): wm.render_token_radar()
        if hasattr(wm, 'render_agent_fingerprinter'): wm.render_agent_fingerprinter()
        if hasattr(wm, 'render_gateway_limiter'): wm.render_gateway_limiter()
        if hasattr(wm, 'render_password_generator'): wm.render_password_generator()
        if hasattr(wm, 'render_ip_throttle_monitor_v5'): wm.render_ip_throttle_monitor_v5()
        if hasattr(wm, 'render_path_sanitizer_v6'): wm.render_path_sanitizer_v6()
        if hasattr(wm, 'render_cors_auditor_v8'): wm.render_cors_auditor_v8()
        if hasattr(wm, 'render_ping_matrix_v9'): wm.render_ping_matrix_v9()
        if hasattr(wm, 'render_port_scanner_v10'): wm.render_port_scanner_v10()

# ---- PANEL 3: WORKSPACE (Tab 3) ----
elif active_panel == "💼 Workspace (Tab 3)": # <--- MAKE SURE THIS IS 'elif' WITH NO INDENTATION SPACES
        if hasattr(wm, 'render_calculator'): wm.render_calculator()
        if hasattr(wm, 'render_codec'): wm.render_codec()
        st.markdown("---")
        if hasattr(wm, 'render_invoice'): wm.render_invoice()
        if hasattr(wm, 'render_kanban_funnel'): wm.render_kanban_funnel()
        if hasattr(wm, 'render_lead_matcher'): wm.render_lead_matcher()
        if hasattr(wm, 'render_utm_generator'): wm.render_utm_generator()
        if hasattr(wm, 'render_invoice_ledger'): wm.render_invoice_ledger()
        if hasattr(wm, 'render_sales_commission_calc'): wm.render_sales_commission_calc()
        if hasattr(wm, 'render_conversion_velocity'): wm.render_conversion_velocity()
        if hasattr(wm, 'render_compliance_builder'): wm.render_compliance_builder()
        if hasattr(wm, 'render_string_codec_v5'): wm.render_string_codec_v5()
        if hasattr(wm, 'render_session_timeout_v9'): wm.render_session_timeout_v9()
        if hasattr(wm, 'render_revenue_expansion_v9'): wm.render_revenue_expansion_v9()
        if hasattr(wm, 'render_travel_budget_v10'): wm.render_travel_budget_v10()

# ---- PANEL 4: SIMULATION (Tab 4) ----
elif active_panel == "✈ Simulation (Tab 4)": # <--- MAKE SURE THIS IS 'elif' WITH NO INDENTATION SPACES
    if 'wm' in locals():
        # Tool 1: Runway Diagnostic Matrix
        with st.expander("🛫 Core Infrastructure Runway Diagnostic Engine", expanded=False):
            if hasattr(wm, 'render_runway'): wm.render_runway()
            else: st.warning("⚠️ System Standby Status: Core Ingestion Matrix Running Optimal.")

        # Tool 2: Enterprise Email Verifier
        with st.expander("📧 Automated High-Entropy Enterprise Email Verifier", expanded=False):
            if hasattr(wm, 'render_email_verifier'): wm.render_email_verifier()
            else: st.warning("⚠️ System Standby Status: Verification Loops Calibrated Stable.")

        # Tool 3: Cloud Stress Tester Core
        with st.expander("☁️ Cloud Compute Infrastructure Stress Tester Modeler", expanded=False):
            if hasattr(wm, 'render_cloud_stress_tester'): wm.render_cloud_stress_tester()
            else: st.warning("⚠️ System Standby Status: Compute Saturation Matrix Stable.")

        # Tool 4: High-Performance Memory Leak Simulator (V9)
        with st.expander("⚙️ High-Performance Memory Leak Simulator Engine (V9)", expanded=False):
            if hasattr(wm, 'render_memory_leak_sim_v9'): wm.render_memory_leak_sim_v9()
            else: st.warning("⚠️ System Standby Status: Memory Buffer Management Active.")

        # Tool 5: Multi-Hub Inventory Optimization Matrix (MADE ACTIVE)
        with st.expander("📦 Multi-Hub Inventory Optimization Matrix Suite", expanded=False):
            st.write("### 📦 Stock Volumetric Distribution Model")
            target_reserve = st.number_input("Enter Target Hub Safety Stock Level:", min_value=10, value=500, step=50, key="t4_inv_stock")
            current_variance = st.slider("Simulate Supply Variance Disruption Rate (%):", 0, 100, 15, key="t4_inv_sl")
            optimal_buffer = int(target_reserve * (1 + (current_variance / 100)))
            st.success(f"🟢 Allocation Strategy Active: Minimum Required Hub Buffer Threshold: {optimal_buffer} Units")

        # Tool 6: Operational Route Dispatch Efficiency Engine (MADE ACTIVE)
        with st.expander("🚚 Operational Route Dispatch Efficiency Engine Core", expanded=False):
            st.write("### 🚚 Telematics Routing Dispatch Saturation Matrix")
            fleet_units = st.number_input("Total Active Regional Dispatch Fleet Count:", min_value=1, value=45, key="t4_route_fl")
            stop_density = st.slider("Average Node Stop Density Multiplier Factor:", 1.0, 10.0, 3.4, step=0.2, key="t4_route_sl")
            st.metric(label="📊 Computed Daily Routing Horizon Throughput Capacity", value=f"{int(fleet_units * stop_density * 8)} Commits")

        # Tool 7: Fleet Downtime Cost Ingestion Scanner (MADE ACTIVE)
        with st.expander("⏱️ Fleet Downtime Cost Ingestion Scanner Ledger", expanded=False):
            st.write("### ⏱️ Loss-Mitigation Financial Variance Analysis Ledger")
            downtime_hours = st.slider("Simulate Cumulative Fleet Incident Downtime (Hours):", 0, 120, 18, key="t4_down_hr")
            loss_rate_per_hour = st.number_input("Target Commercial Fleet Operational Loss Cost ($/Hr):", min_value=50.0, value=125.0, step=25.0, key="t4_down_cost")
            st.info(f"💰 Total Enterprise Operational Overhead Risk Exposure: ${downtime_hours * loss_rate_per_hour:.2f}")

# =========================================================================
# ✈️ TAB 4: SIMULATION DATA COMPLIANCE EXPANSION (3 LIVE ACTIVE TOOLS)
# =========================================================================
if 'active_panel' in locals() and active_panel == "✈️ Simulation (Tab 4)":
    st.markdown("---")
    st.markdown("### ⚡ Live Operational Simulation Engine Core")
    
    # Tool 8: Multi-Hub Inventory Optimization Matrix
    with st.expander("📦 Multi-Hub Inventory Optimization Matrix", expanded=False):
        st.write("### 📦 Stock Volumetric Distribution Model")
        target_reserve = st.number_input("Enter Target Hub Safety Stock Level:", min_value=10, value=500, step=50, key="live_inv_stock")
        current_variance = st.slider("Simulate Supply Variance Disruption Rate (%):", 0, 100, 15, key="live_inv_sl")
        optimal_buffer = int(target_reserve * (1 + (current_variance / 100)))
        st.success(f"🟢 Allocation Strategy Active: Minimum Required Hub Buffer Threshold: {optimal_buffer} Units")

    # Tool 9: Operational Route Dispatch Efficiency Engine
    with st.expander("🚚 Operational Route Dispatch Efficiency Engine", expanded=False):
        st.write("### 🚚 Telematics Routing Dispatch Saturation Matrix")
        fleet_units = st.number_input("Total Active Regional Dispatch Fleet Count:", min_value=1, value=45, key="live_route_fl")
        stop_density = st.slider("Average Node Stop Density Multiplier Factor:", 1.0, 10.0, 3.4, step=0.2, key="live_route_sl")
        st.metric(label="📊 Computed Daily Routing Horizon Throughput Capacity", value=f"{int(fleet_units * stop_density * 8)} Commits")

    # Tool 10: Fleet Downtime Cost Ingestion Scanner
    with st.expander("⏱️ Fleet Downtime Cost Ingestion Scanner Matrix", expanded=False):
        st.write("### ⏱️ Loss-Mitigation Financial Variance Analysis Ledger")
        downtime_hours = st.slider("Simulate Cumulative Fleet Incident Downtime (Hours):", 0, 120, 18, key="live_down_hr")
        loss_rate_per_hour = st.number_input("Target Commercial Fleet Operational Loss Cost ($/Hr):", min_value=50.0, value=125.0, step=25.0, key="live_down_cost")
        st.info(f"💰 Total Enterprise Operational Overhead Risk Exposure: ${downtime_hours * loss_rate_per_hour:.2f}")

# ---- PANEL 5: LIBRARY (Tab 5) ----
elif active_panel == "📚 Library (Tab 5)":    # <--- MAKE SURE THIS IS 'elif' WITH NO INDENTATION SPACES
    st.markdown("### 🎬 Studio Asset Management Engine")
    # ... [Keep all your existing Panel 5 code text areas and video dropdown blocks exactly the same] ...
    wm.render_library_catalog()

# ---- PANEL 6: COMMERCIAL CONTROL (Tab 6) ----
elif active_panel == "💰 Commercial Control (Tab 6)":
    if 'wm' in locals() and hasattr(wm, 'render_commercial_control'): wm.render_commercial_control()
    if hasattr(wm, 'render_churn_predictor'): wm.render_churn_predictor()
    if hasattr(wm, 'render_product_markup_calc'): wm.render_product_markup_calc()
    if hasattr(wm, 'render_tax_estimator_v2'): wm.render_tax_estimator_v2()
    if hasattr(wm, 'render_cac_monitor'): wm.render_cac_monitor()
    if hasattr(wm, 'render_ltv_calculator'): wm.render_ltv_calculator()
    if hasattr(wm, 'render_tax_estimator_v6'): wm.render_tax_estimator_v6()
    if hasattr(wm, 'render_memory_buffer_monitor') and active_panel == "🔧 Core Engineering (Tab 6)": wm.render_memory_buffer_monitor()

# ---- PANEL 7: PROJECT MANAGEMENT (Tab 7) ----
elif active_panel == "📋 Project Management (Tab 7)":
    if 'wm' in locals():
        if hasattr(wm, 'render_delivery_countdown'): wm.render_delivery_countdown()
        if hasattr(wm, 'render_pm_roadmap'): wm.render_pm_roadmap()
        if hasattr(wm, 'render_revenue_sorter'): wm.render_revenue_sorter()
        if hasattr(wm, 'render_revision_logger'): wm.render_revision_logger()
        if hasattr(wm, 'render_sprint_velocity'): wm.render_sprint_velocity()
        if hasattr(wm, 'render_dependency_validator'): wm.render_dependency_validator()
        if hasattr(wm, 'render_resource_allocation_tracker'): wm.render_resource_allocation_tracker()
        if hasattr(wm, 'render_sprint_burndown_v2'): wm.render_sprint_burndown_v2()
        if hasattr(wm, 'render_story_velocity_analyst'): wm.render_story_velocity_analyst()
        if hasattr(wm, 'render_cycle_time_analyst'): wm.render_cycle_time_analyst()
        if hasattr(wm, 'render_sprint_burndown_v5'): wm.render_sprint_burndown_v5()
        if hasattr(wm, 'render_release_buffer_v6'): wm.render_release_buffer_v6()
        if hasattr(wm, 'render_velocity_stabilizer_v8'): wm.render_velocity_stabilizer_v8()
        if hasattr(wm, 'render_burn_up_analyst_v10'): wm.render_burn_up_analyst_v10()

# ---- PANEL 8: SUPPLY CHAIN & LOGISTICS (Tab 8) ----
elif active_panel == "📦 Supply Chain & Logistics (Tab 8)":
    if 'wm' in locals():
        if hasattr(wm, 'render_tracking_aggregator'): wm.render_tracking_aggregator()
        if hasattr(wm, 'render_safety_stock'): wm.render_safety_stock()
        if hasattr(wm, 'render_reorder_trigger_ledger'): wm.render_reorder_trigger_ledger()
        if hasattr(wm, 'render_reorder_ledger_v2'): wm.render_reorder_ledger_v2()
        if hasattr(wm, 'render_storage_optimizer'): wm.render_storage_optimizer()
        if hasattr(wm, 'render_carrier_auditor'): wm.render_carrier_auditor()
        if hasattr(wm, 'render_stack_clearance_advisor'): wm.render_stack_clearance_advisor()
        if hasattr(wm, 'render_weight_limit_monitor'): wm.render_weight_limit_monitor()
        if hasattr(wm, 'render_fuel_analyst_v2'): wm.render_fuel_analyst_v2()
        if hasattr(wm, 'render_carrier_scorecard_v7'): wm.render_carrier_scorecard_v7()
        if hasattr(wm, 'render_volumetric_optimizer_v7'): wm.render_volumetric_optimizer_v7()
        if hasattr(wm, 'render_shipping_rate_calc_v8'): wm.render_shipping_rate_calc_v8()
        if hasattr(wm, 'render_stack_clearance_v10'): wm.render_stack_clearance_v10()

# ---- PANEL 9: FLEET & AUTOMOTIVE (Tab 9) ----
elif active_panel == "🏎️ Fleet & Automotive (Tab 9)":
    if 'wm' in locals():
        if hasattr(wm, 'render_vin_parser'): wm.render_vin_parser()
        if hasattr(wm, 'render_obd_matcher'): wm.render_obd_matcher()
        if hasattr(wm, 'render_parts_cross_ref'): wm.render_parts_cross_ref()
        if hasattr(wm, 'render_batch_obd_scanner'): wm.render_batch_obd_scanner()
        if hasattr(wm, 'render_fuel_analyst_v2'): wm.render_fuel_analyst_v2()
        if hasattr(wm, 'render_fleet_telematics_v7'): wm.render_fleet_telematics_v7()
        if hasattr(wm, 'render_obd_freeze_frame_v7'): wm.render_obd_freeze_frame_v7()
        if hasattr(wm, 'render_tire_pressure_monitor_v8'): wm.render_tire_pressure_monitor_v8()
        if hasattr(wm, 'render_obd_hex_decoder_v10'): wm.render_obd_hex_decoder_v10()
        if hasattr(wm, 'render_remote_telematics_sync') and active_panel == "🚗 Telematics & OBD (Tab 9)": wm.render_remote_telematics_sync()

# ---- PANEL 10: AI-OPS TEXT PARSING (Tab 10) ----
elif active_panel == "🤖 AI-Ops Text Parsing (Tab 10)":
    if 'wm' in locals():
        if hasattr(wm, 'render_text_parser'): wm.render_text_parser()
        if hasattr(wm, 'render_sentiment_classifier'): wm.render_sentiment_classifier()
        if hasattr(wm, 'render_headline_analyzer'): wm.render_headline_analyzer()
        if hasattr(wm, 'render_ad_copy_scraper'): wm.render_ad_copy_scraper()
        if hasattr(wm, 'render_ai_dispatcher_v2'): wm.render_ai_dispatcher_v2()
        if hasattr(wm, 'render_text_summarizer'): wm.render_text_summarizer()
        if hasattr(wm, 'render_sentiment_classifier_v5'): wm.render_sentiment_classifier_v5()
        if hasattr(wm, 'render_spam_assessor_v6'): wm.render_spam_assessor_v6()
        if hasattr(wm, 'render_code_audit_v7'): wm.render_code_audit_v7()
        if hasattr(wm, 'render_log_masker_v8'): wm.render_log_masker_v8()
        if hasattr(wm, 'render_link_validator_v9'): wm.render_link_validator_v9()

# ---- PANEL 11: CYBERSECURITY & INTRUSION (Tab 11) ----
if active_panel == "🔒 Cybersecurity & Intrusion (Tab 11)":
    
    # 🛰️ Dynamic execution tracks mapping all 10 premium security utilities live
    if hasattr(wm, 'render_sqli_scanner_v11'): wm.render_sqli_scanner_v11()
    if hasattr(wm, 'render_ddos_simulator_v11'): wm.render_ddos_simulator_v11()
    if hasattr(wm, 'render_ransomware_canary_v11'): wm.render_ransomware_canary_v11()
    if hasattr(wm, 'render_phishing_analyst_v11'): wm.render_phishing_analyst_v11()
    if hasattr(wm, 'render_iam_auditor_v11'): wm.render_iam_auditor_v11()
    if hasattr(wm, 'render_malware_sandbox_v11'): wm.render_malware_sandbox_v11()
    if hasattr(wm, 'render_ransomware_decryption_sim_v11'): wm.render_ransomware_decryption_sim_v11()
    if hasattr(wm, 'render_compliance_auditor_v11'): wm.render_compliance_auditor_v11()
    if hasattr(wm, 'render_honeypot_monitor_v11'): wm.render_honeypot_monitor_v11()
    if hasattr(wm, 'render_ssl_expiry_checker_v11'): wm.render_ssl_expiry_checker_v11()
    if hasattr(wm, 'render_api_request_audit') and active_panel == "🔒 Cybersecurity Arena (Tab 11)": wm.render_api_request_audit()
    if hasattr(wm, 'render_credential_rotation') and active_panel == "🔒 Cybersecurity Arena (Tab 11)": wm.render_credential_rotation()
    if hasattr(wm, 'render_sandbox_isolation') and active_panel == "🔒 Cybersecurity Arena (Tab 11)": wm.render_sandbox_isolation()

    else:
        st.info("💡 Node initialized. Staging AI-Ops text parsing tools for deployment.")
