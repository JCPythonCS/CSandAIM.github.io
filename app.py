import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import datetime
import plotly.express as px

# ==========================================================================
# 🛑 MANDATORY CONFIGURATION: MUST REMAIN AT THE ABSOLUTE TOP OF FILE
# ==========================================================================
st.set_page_config(
    page_title="JCPSS Enterprise Cockpit",
    page_icon="🚀",
    layout="wide"
)

# ==========================================================================
# ⏱️ COCKPIT SATURDAY DEADLINE TIMER - PERFECTLY CENTERED AT THE TOP
# ==========================================================================
left_gap, center_core, right_gap = st.columns([1, 2, 1])

with center_core:
    countdown_html_code = """
    <div style="background: linear-gradient(135deg, #151522 0%, #0a0a0f 100%); color: #ffffff; font-family: 'Segoe UI', -apple-system, Arial, sans-serif; padding: 20px; border-radius: 12px; border: 2px solid #ff4757; text-align: center; max-width: 100%; margin: 0 auto; box-shadow: 0 8px 16px rgba(0,0,0,0.5);">
        <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 2px; color: #ff4757; margin-bottom: 15px; font-weight: bold;">⏱️ SATURDAY COCKPIT SYSTEM TARGET DEADLINE</div>
        <div style="display: flex; justify-content: center; gap: 10px;">
            <div style="background: #040407; padding: 8px; border-radius: 6px; min-width: 65px;"><div id="days" style="font-size: 26px; font-family: monospace; font-weight: bold; color: #00d2d3;">00</div><div style="font-size: 9px; color: #888;">Days</div></div>
            <div style="background: #040407; padding: 8px; border-radius: 6px; min-width: 65px;"><div id="hours" style="font-size: 26px; font-family: monospace; font-weight: bold; color: #00d2d3;">00</div><div style="font-size: 9px; color: #888;">Hours</div></div>
            <div style="background: #040407; padding: 8px; border-radius: 6px; min-width: 65px;"><div id="minutes" style="font-size: 26px; font-family: monospace; font-weight: bold; color: #00d2d3;">00</div><div style="font-size: 9px; color: #888;">Minutes</div></div>
            <div style="background: #040407; padding: 8px; border-radius: 6px; min-width: 65px;"><div id="seconds" style="font-size: 26px; font-family: monospace; font-weight: bold; color: #00d2d3;">00</div><div style="font-size: 9px; color: #888;">Seconds</div></div>
        </div>
    </div>

    <script>
        const targetDeadline = new Date("Sep 19, 2026 11:00:00").getTime();
        const timerInterval = setInterval(function() {
            const now = new Date().getTime();
            const diff = targetDeadline - now;
            let d = Math.floor(diff / (1000 * 60 * 60 * 24));
            let h = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            let m = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
            let s = Math.floor((diff % (1000 * 60)) / 1000);
            
            if (diff >= 0) {
                document.getElementById("days").textContent = d < 10 ? "0" + d : d;
                document.getElementById("hours").textContent = h < 10 ? "0" + h : h;
                document.getElementById("minutes").textContent = m < 10 ? "0" + m : m;
                document.getElementById("seconds").textContent = s < 10 ? "0" + s : s;
            } else {
                clearInterval(timerInterval);
                document.getElementById("days").textContent = "00";
                document.getElementById("hours").textContent = "00";
                document.getElementById("minutes").textContent = "00";
                document.getElementById("seconds").textContent = "00";
            }
        }, 1000);
    </script>
    """
    components.html(countdown_html_code, height=160)

# ==========================================================================
# 🛰️ ORIGINAL APP LAYOUT BRANDING HEADER
# ==========================================================================
col1, col2 = st.columns([1, 4])
with col1:
    try:
        st.image("logo.png", width=120)
    except:
        pass
with col2:
    st.markdown("# JCPSS Lakehouse Cockpit")
    st.markdown("### Integrated Control Hub & Telemetry Stream Engine")

# Try to pull in your original background worker module safely
try:
    import workspace_module as wm
except ImportError:
    st.sidebar.error("⚠️ Warning: workspace_module.py connector script not found.")

# ==========================================================================
# 📊 DATA LOADERS & DATA DICTIONARY RECOVERY
# ==========================================================================
@st.cache_data
def load_excel_telemetry():
    try:
        return pd.read_excel("Combined_Data.xlsx")
    except:
        # Fallback to keep dataframes functional if file path updates
        return pd.DataFrame(columns=["Region", "Metric_Value", "Status", "Date"])

df = load_excel_telemetry()

# ==========================================================================
# 🎛️ SIDEBAR INTERACTIVE PARAMETERS CONTROL
# ==========================================================================
st.sidebar.markdown("## ⚙️ Navigation Control")

if not df.empty and "Region" in df.columns:
    unique_regions = df["Region"].unique()
    selected_regions = st.sidebar.multiselect("Select Target Regions", unique_regions, default=unique_regions)
    filtered_df = df[df["Region"].isin(selected_regions)]
else:
    st.sidebar.info("Data layers offline. System running in baseline mode.")
    filtered_df = pd.DataFrame(columns=["Region", "Metric_Value", "Status", "Date"])

# ==========================================================================
# 📑 NAVIGATION TABS INFRASTRUCTURE - RESTORING FULL COCKPIT CORE
# ==========================================================================
tab_analytics, tab_utilities, tab_workspace, tab_simulation, tab_library = st.tabs([
    "📊 Real-Time Analytics", 
    "🔧 System Utilities", 
    "📂 Core Workspace", 
    "🧪 Model Simulations",
    "📚 Document Library"
])

with tab_analytics:
    st.markdown("### 📈 Live Telemetry Distributions")
    if not filtered_df.empty:
        fig = px.line(filtered_df, x="Date", y="Metric_Value", color="Region", title="Regional Stream Scaling Performance")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("💡 Standby. Waiting for live telemetry feeds from your 998 Oracle instance arrays.")

with tab_utilities:
    st.markdown("### 🛠️ Shell Management Tools")
    st.write("Controls for executing batch transaction migrations and file tracking pipelines.")

with tab_workspace:
    st.markdown("### 📁 Target Directory Mapping")
    st.write("Displays structural tables, catalog linkages, and data definitions active within the workspace.")

with tab_simulation:
    st.markdown("### 🥽 Quantum Logic & Swarm Profiles")
    st.write("Sandboxed model testing workspace for simulating matrix asset distributions.")

with tab_library:
    st.markdown("### 📑 Storefront Resource Center")
    st.write("Pickup terminal for tracking paid CSV data sheets, PDF schematics, and automation files.")
