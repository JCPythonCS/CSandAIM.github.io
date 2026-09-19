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

# 🗓️ ROW 2: MONDAY-FIRST STATIC CORPORATE CALENDAR MATRIX NATIVELY SEALED
st.sidebar.markdown("#### 🗓️ Master Operations Calendar")
st.sidebar.markdown("""
<div style="background-color: #0f172a; padding: 10px; border-radius: 6px; border: 1px solid #334155; font-family: monospace;">
    <p style="color: #38bdf8; font-weight: bold; margin: 0 0 5px 0; text-align: center;">📅 SEPTEMBER 2026</p>
    <table style="width: 100%; text-align: center; color: #94a3b8; font-size: 0.8rem; border-collapse: collapse;">
        <tr style="color: #f1f5f9; font-weight: bold;">
            <td style="padding: 3px;">M</td><td style="padding: 3px;">T</td><td style="padding: 3px;">W</td><td style="padding: 3px;">T</td><td style="padding: 3px;">F</td><td style="color: #ef4444; padding: 3px;">S</td><td style="color: #ef4444; padding: 3px;">S</td>
        </tr>
        <tr>
            <td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td>
        </tr>
        <tr>
            <td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td>
        </tr>
        <tr>
            <td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td style="background-color: #22c55e; color: white; border-radius: 4px; font-weight: bold; padding: 2px;">19</td><td>20</td>
        </tr>
        <tr>
            <td>21</td><td>22</td><td>23</td><td>24</td><td>25</td><td>26</td><td>27</td>
        </tr>
        <tr>
            <td>28</td><td>29</td><td>30</td><td></td><td></td><td></td><td></td>
        </tr>
    </table>
</div>
""", unsafe_allow_html=True)

# 💎 ROW 3: CORPORATE ACCESS HEADER BRIDGE
st.sidebar.markdown("---")
st.sidebar.markdown("### 💎 Premium SaaS Access")
st.sidebar.caption("Select your operational tier to unlock full cockpit capabilities.")

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
    
    # 🏢 CORPORATE INFORMATION FOOTPRINT
    st.markdown(
        """
        <div style="background-color: #0f172a; padding: 15px; border-radius: 6px; border: 1px solid #334155; color: #94a3b8; font-size: 0.85rem;">
            <div style="font-weight: bold; color: #f1f5f9; font-size: 0.95rem; margin-bottom: 2px;">🏢 Computer Systems & AI Management</div>
            <div style="color: #38bdf8; font-family: monospace; font-size: 0.85rem; margin-bottom: 2px; padding-top: 4px;">📧 jcpython@outlook.com</div>
            <div style="color: #38bdf8; font-family: monospace; font-size: 0.85rem; margin-bottom: 8px;">📞 (864) 864-9954</div>
            <div style="margin-bottom: 3px; padding-top: 4px;"><b>Version:</b> 4.2.0-SaaS (Production)</div>
            <div style="margin-bottom: 3px;"><b>Global Network Operations Center</b></div>
            <div style="margin-bottom: 10px; font-size: 0.75rem; color: #64748b;">All Rights Reserved © 2026</div>
            <div style="border-top: 1px solid #1e293b; padding-top: 8px; font-size: 0.8rem;">
                🔗 <a href="https://paypal.com" target="_blank" style="color: #38bdf8; text-decoration: none;">Subscriber Portal</a><br>
                🛡️ <a href="#" style="color: #38bdf8; text-decoration: none;">Security Protocols</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

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

if 'wm' in locals() and hasattr(wm, 'fetch_active_stream_registers') and active_panel == "📊 Analytics (Tab 1)":
        with st.spinner("🛰️ Pinging autonomous database container registries..."):
            customer_store_df = wm.fetch_active_stream_registers()
        if not customer_store_df.empty:
            st.dataframe(customer_store_df, use_container_width=True)
        else:
            st.warning("📡 Standby: Scanning for live client transactions... Active storage block is empty.")
        if hasattr(wm, 'render_kpi_pulse_grid') and active_panel == "📊 Analytics (Tab 1)": wm.render_kpi_pulse_grid()
        if hasattr(wm, 'render_funnel_attribution') and active_panel == "📊 Analytics (Tab 1)": wm.render_funnel_attribution()
        if hasattr(wm, 'render_pipeline_forecaster') and active_panel == "📊 Analytics (Tab 1)": wm.render_pipeline_forecaster()
        if hasattr(wm, 'render_conversion_velocity_v5') and active_panel == "📊 Analytics (Tab 1)": wm.render_conversion_velocity_v5()
        if hasattr(wm, 'render_lead_velocity_v6') and active_panel == "📊 Analytics (Tab 1)": wm.render_lead_velocity_v6()
        if hasattr(wm, 'render_volume_saturation') and active_panel == "📊 Analytics (Tab 1)": wm.render_volume_saturation()
        if hasattr(wm, 'render_cac_multiplier') and active_panel == "📊 Analytics (Tab 1)": wm.render_cac_multiplier()

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
        if hasattr(wm, 'render_runway'): wm.render_runway()
        st.markdown("---")
        if hasattr(wm, 'render_email_verifier'): wm.render_email_verifier()
        if hasattr(wm, 'render_cloud_stress_tester'): wm.render_cloud_stress_tester()
        if hasattr(wm, 'render_memory_leak_sim_v9'): wm.render_memory_leak_sim_v9()
        if hasattr(wm, 'render_inventory_optimization') and active_panel == "🚀 Fleet & Ops (Tab 4)": wm.render_inventory_optimization()
        if hasattr(wm, 'render_route_dispatch') and active_panel == "🚀 Fleet & Ops (Tab 4)": wm.render_route_dispatch()
        if hasattr(wm, 'render_downtime_cost') and active_panel == "🚀 Fleet & Ops (Tab 4)": wm.render_downtime_cost()

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
