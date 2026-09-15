import streamlit as st
import pandas as pd
import os
import time
import datetime

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


# ⏱️ FIXED: REAL-TIME ISOLATED COUNTDOWN ENGINE
# Using st.fragment ensures ONLY this block reloads, stopping the entire page from breaking
@st.fragment(run_every=1.0)
def render_live_countdown():
    st.sidebar.markdown("### ⏳ Target Countdown")
    
    # Force the engine to establish the exact target: Saturday, Sept 19, 2026 at 11:00 AM EST
    # Streamlit Cloud runs on UTC, which is exactly 4 hours ahead of Eastern Daylight Time (EDT)
    # Therefore, 11:00 AM EST is exactly 15:00 (3:00 PM) UTC server-time!
    
    now_utc = datetime.datetime.utcnow()
    target_saturday_utc = datetime.datetime(2026, 9, 19, 15, 0, 0)
    
    time_remaining = target_saturday_utc - now_utc
    
    if time_remaining.total_seconds() > 0:
        days = time_remaining.days
        hours, remainder = divmod(time_remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        st.markdown(
            f"""
            <div style="background-color: #1e293b; padding: 12px; border-radius: 6px; border-left: 5px solid #ef4444; color: #f8fafc; font-family: monospace; text-align: center;">
                <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; color: #94a3b8; margin-bottom: 5px;">Time remaining to SaaS Briefing</div>
                <div style="font-size: 1.2rem; font-weight: bold;">{days}d : {hours:02d}h : {minutes:02d}m : {seconds:02d}s</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.success("🚀 Operational Window Active! SaaS Paywall Deploying.")

# Run the isolated countdown module in the sidebar safely
with st.sidebar:
    render_live_countdown()

    # 🏙️ 1. Dynamic Region Selection Filter
    if 'Region' in df.columns:
        region_opts = sorted(df['Region'].dropna().unique())
        selected_region = st.selectbox("Select Operational Region:", ["All Regions"] + list(region_opts), key="sb_region_opt_v4")
        if selected_region != "All Regions":
            df = df[df['Region'] == selected_region]

    # 🏢 2. Dynamic Agency Selection Filter
    if 'Agency' in df.columns:
        agency_opts = sorted(df['Agency'].dropna().unique())
        selected_agency = st.selectbox("Select Core Reporting Agency:", ["All Agencies"] + list(agency_opts), key="sb_agency_opt_v4")
        if selected_agency != "All Agencies":
            df = df[df['Agency'] == selected_agency]

    # 🎖️ 3. Dynamic Command Level Selection Filter
    if 'Command' in df.columns:
        command_opts = sorted(df['Command'].dropna().unique())
        selected_command = st.selectbox("Select Strategic Command:", ["All Commands"] + list(command_opts), key="sb_command_opt_v4")
        if selected_command != "All Commands":
            df = df[df['Command'] == selected_command]

    # 📊 4. Dynamic Performance Tier Selection Filter
    if 'Tier' in df.columns:
        tier_opts = sorted(df['Tier'].dropna().unique())
        selected_tier = st.selectbox("Select Operational Performance Tier:", ["All Tiers"] + list(tier_opts), key="sb_tier_opt_v4")
        if selected_tier != "All Tiers":
            df = df[df['Tier'] == selected_tier]
                
    # Assign the master filtered data slice down to your Tab 1 layout views
    filtered_df = df

# 📂 MASTER FILE INGESTION ENGINE: Dynamically reads ALL files in the repository
current_working_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else '.'
data_folder = current_working_dir
all_files = [f for f in os.listdir(data_folder) if f.lower().endswith(('.xlsx', '.xls'))]
database = {}

for file_name in all_files:
    file_path = os.path.join(data_folder, file_name)
    display_name = os.path.splitext(file_name)[0]
    try:
        database[display_name] = file_path
    except:
        pass

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
        "🤖 AI-Ops Text Parsing (Tab 10)"
    ],
    key="cockpit_panel_navigation"
)

st.markdown("---")

# 🎙️ FIXED SIDEBAR VISIBILITY CONTROLLER
# Appends data options or audio profile settings underneath the isolated live timer box
if active_panel == "📊 Analytics (Tab 1)":
    st.sidebar.markdown("---")
    st.sidebar.header("🎯 Dashboard Control Filters")
    
    if database:
        selected_file_name = st.sidebar.selectbox(
            "Select Database File Asset:", 
            options=sorted(list(database.keys())),
            help="Choose any workspace excel file from your repository to analyze dynamically."
        )
        
        target_file_path = database[selected_file_name]
        
        try:
            df = pd.read_excel(target_file_path)
            
            if 'Active Combat Unit Name' in df.columns:
                selected_units = st.sidebar.multiselect("Active Combat Unit Name:", options=df['Active Combat Unit Name'].unique(), default=df['Active Combat Unit Name'].unique())
            else:
                selected_units = []

            if 'Strategic Command Sector' in df.columns:
                selected_sectors = st.sidebar.multiselect("Strategic Command Sector:", options=df['Strategic Command Sector'].unique(), default=df['Strategic Command Sector'].unique())
            else:
                selected_sectors = []

            if 'Agency Command Tier' in df.columns:
                selected_tiers = st.sidebar.multiselect("Agency Command Tier:", options=df['Agency Command Tier'].unique(), default=df['Agency Command Tier'].unique())
            else:
                selected_tiers = []
                
        except Exception as e:
            st.sidebar.error(f"Error reading file elements: {e}")
            df = None
            selected_units, selected_sectors, selected_tiers = [], [], []
    else:
        st.sidebar.warning("⚠️ No `.xlsx` or `.xls` spreadsheet assets detected in the root repository.")
        df = None
        selected_units, selected_sectors, selected_tiers = [], [], []
        
    male_profile = "Male_Adam (Deep/Calm)"
    female_profile = "Female_Emily (Smooth)"

elif active_panel == "📚 Library (Tab 5)":
    st.sidebar.markdown("---")
    st.sidebar.header("🗣️ Audio Profiles Configuration")
    male_profile = st.sidebar.selectbox("Male Actor Voice", ["Male_Adam (Deep/Calm)", "Male_Michael (Professional)", "Male_David"])
    female_profile = st.sidebar.selectbox("Female Actor Voice", ["Female_Emily (Smooth)", "Female_Serena (Narrator)", "Female_Rachel"])
    st.sidebar.markdown("---")
    st.sidebar.caption("Voice Profile Parameters Active on Library Canvas")
else:
    male_profile = "Male_Adam (Deep/Calm)"
    female_profile = "Female_Emily (Smooth)"

# ==========================================================================
# 🚀 LIVE WORKSPACE ROUTING NODE LOOP EXECUTION
# ==========================================================================

# ---- PANEL 1: ANALYTICS (Tab 1) ----
if active_panel == "📊 Analytics (Tab 1)":
    st.subheader(f"📊 Tactical Systems & Analytics Stream")
    
    if df is not None:
        filtered_df = df.copy()
        # ... [Keep all your existing Panel 1 internal code and filters exactly the same] ...
        st.dataframe(filtered_df.head(100), use_container_width=True)
    else:
        st.info("ℹ️ Select an operational file from the left sidebar to populate your tactical dashboard data lines.")

    # ==========================================================================
    # 📋 PERMANENT ACTIVE STREAM REGISTERS MAPPING
    # ==========================================================================
    st.markdown("---")
    st.markdown("## 📋 Active Stream Registers")
    st.markdown("### Real-Time Customer Purchase Logs & Delivery Staging Node")
    
    if 'wm' in locals() and hasattr(wm, 'fetch_active_stream_registers'):
        with st.spinner("🛰️ Pinging autonomous database container registries..."):
            customer_store_df = wm.fetch_active_stream_registers()
        if not customer_store_df.empty:
            st.dataframe(customer_store_df, use_container_width=True)
        else:
            st.warning("📡 Standby: Scanning for live client transactions... Active storage block is empty.")
            
        if hasattr(wm, 'render_kpi_pulse_grid'): wm.render_kpi_pulse_grid()
        if hasattr(wm, 'render_funnel_attribution'): wm.render_funnel_attribution()

# ---- PANEL 2: UTILITIES (Tab 2) ----
elif active_panel == "🛠 Utilities (Tab 2)": # <--- MAKE SURE THIS IS 'elif' WITH NO INDENTATION SPACES
    if 'wm' in locals():
        if hasattr(wm, 'render_translator'): wm.render_translator()
        st.markdown("---")
        if hasattr(wm, 'render_renamer'): wm.render_renamer()
        if hasattr(wm, 'render_threat_analyzer'): wm.render_threat_analyzer()
        if hasattr(wm, 'render_ip_throttle_monitor'): wm.render_ip_throttle_monitor()
        if hasattr(wm, 'render_token_radar'): wm.render_token_radar()
        if hasattr(wm, 'render_agent_fingerprinter'): wm.render_agent_fingerprinter()


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

# ---- PANEL 4: SIMULATION (Tab 4) ----
elif active_panel == "✈ Simulation (Tab 4)": # <--- MAKE SURE THIS IS 'elif' WITH NO INDENTATION SPACES
    if 'wm' in locals():
        if hasattr(wm, 'render_runway'): wm.render_runway()
        st.markdown("---")
        if hasattr(wm, 'render_email_verifier'): wm.render_email_verifier()
        if hasattr(wm, 'render_cloud_stress_tester'): wm.render_cloud_stress_tester()

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

# ---- PANEL 8: SUPPLY CHAIN & LOGISTICS (Tab 8) ----
elif active_panel == "📦 Supply Chain & Logistics (Tab 8)":
    st.subheader("📦 Supply Chain & Logistics Control")
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

# ---- PANEL 9: FLEET & AUTOMOTIVE (Tab 9) ----
elif active_panel == "🏎️ Fleet & Automotive (Tab 9)":
    st.subheader("🏎️ Fleet & Automotive Operations")
    if 'wm' in locals():
        if hasattr(wm, 'render_vin_parser'): wm.render_vin_parser()
        if hasattr(wm, 'render_obd_matcher'): wm.render_obd_matcher()
        if hasattr(wm, 'render_parts_cross_ref'): wm.render_parts_cross_ref()
        if hasattr(wm, 'render_batch_obd_scanner'): wm.render_batch_obd_scanner()
        if hasattr(wm, 'render_fuel_analyst_v2'): wm.render_fuel_analyst_v2()

# ---- PANEL 10: AI-OPS TEXT PARSING (Tab 10) ----
elif active_panel == "🤖 AI-Ops Text Parsing (Tab 10)":
    if 'wm' in locals():
        if hasattr(wm, 'render_text_parser'): wm.render_text_parser()
        if hasattr(wm, 'render_sentiment_classifier'): wm.render_sentiment_classifier()
        if hasattr(wm, 'render_headline_analyzer'): wm.render_headline_analyzer()
        if hasattr(wm, 'render_ad_copy_scraper'): wm.render_ad_copy_scraper()
        if hasattr(wm, 'render_ai_dispatcher_v2'): wm.render_ai_dispatcher_v2()

    else:
        st.info("💡 Node initialized. Staging AI-Ops text parsing tools for deployment.")
