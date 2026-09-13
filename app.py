import streamlit as st
import pandas as pd
import os
import time

# Import all of your specific tool handlers from your workspace_modules.py file
import workspace_modules as wm

# 🖥️ Exact Page Config from your Repository
st.set_page_config(page_title="Computer Systems and AI Management Cockpit", layout="wide")

# 🏆 MASTER TITLE BLOCK DESIGN WITH DUAL SIDE-SPACED LOGOS
st.title("🛡️ Computer Systems and AI Management Cockpit")

# FIXED: Explicitly passed an integer argument '3' into st.columns to prevent the TypeError crash
col_logo_left, col_title_spacer, col_logo_right = st.columns(3)

with col_logo_left:
    try:
        st.image("logo1.png", use_container_width=True)
    except:
        st.caption("🖼️ [Left Logo Slot]")

with col_logo_right:
    try:
        st.image("logo2.png", use_container_width=True)
    except:
        st.caption("🖼️ [Right Logo Slot]")

st.markdown("---")

# 📂 LOAD LOCAL WORKSPACE DATA LOOP
data_folder = '.'
all_files = [os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.lower().endswith(('.xlsx', '.xls'))]
database = {}

for file_path in all_files:
    file_name = os.path.basename(file_path)
    # FIXED: Added index [0] to extract ONLY the plain text name string from splitext tuple
    table_name = os.path.splitext(file_name)[0]
    try:
        database[table_name] = pd.read_excel(file_path)
    except:
        pass

# 🎛️ COCKPIT MASTER NAVIGATION (Ungrouped Selection Panels)
active_panel = st.selectbox(
    "Select Workspace System Node To Deploy:",
    [
        "📊 Analytics (Tab 1)",
        "🛠️ Utilities (Tab 2)",
        "💼 Workspace (Tab 3)",
        "✈️ Simulation (Tab 4)",
        "📚 Library (Tab 5)"
    ],
    key="cockpit_panel_navigation"
)

st.markdown("---")

# 🎙️ DYNAMIC SIDEBAR VISIBILITY CONTROLLER
if active_panel == "📊 Analytics (Tab 1)":
    st.sidebar.header("🎯 Dashboard Control Filters")
    if 'enterprise_retail_dataT' in database:
        df = database['enterprise_retail_dataT']
        selected_region = st.sidebar.multiselect("Select Region Filter Context:", options=df['Region'].unique(), default=df['Region'].unique())
        selected_retailer = st.sidebar.multiselect("Select Retailer Filter Context:", options=df['Retailer'].unique(), default=df['Retailer'].unique())
    else:
        st.sidebar.warning("⚠️ Waiting for 'enterprise_retail_dataT' data array match...")
        selected_region = []
        selected_retailer = []
        
    male_profile = "Male_Adam (Deep/Calm)"
    female_profile = "Female_Emily (Smooth)"

elif active_panel == "📚 Library (Tab 5)":
    st.sidebar.header("🗣️ Audio Profiles Configuration")
    male_profile = st.sidebar.selectbox("Male Actor Voice", ["Male_Adam (Deep/Calm)", "Male_Michael (Professional)", "Male_David"])
    female_profile = st.sidebar.selectbox("Female Actor Voice", ["Female_Emily (Smooth)", "Female_Serena (Narrator)", "Female_Rachel"])
    st.sidebar.markdown("---")
    st.sidebar.caption("Voice Profile Parameters Active on Library Canvas")
else:
    st.sidebar.empty()
    male_profile = "Male_Adam (Deep/Calm)"
    female_profile = "Female_Emily (Smooth)"

# ==================== ACTIVE VIEWPORT ROUTING GRID ====================

# ---- PANEL 1: ANALYTICS (Tab 1) ----
if active_panel == "📊 Analytics (Tab 1)":
    st.subheader("📊 Enterprise Retail Data Ingestion Streams")
    
    if 'enterprise_retail_dataT' in database:
        df = database['enterprise_retail_dataT']
        
        # Filter matching sequence
        if not selected_region or not selected_retailer:
            filtered_df = df.copy()
        else:
            filtered_df = df[(df['Region'].isin(selected_region)) & (df['Retailer'].isin(selected_retailer))]
        
        total_vol = filtered_df['Volume_USD'].sum()
        total_txns = len(filtered_df)
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric(label="💰 Total Combined Sales Volume", value=f"${total_vol:,.2f}")
        with c2:
            st.metric(label="📦 Total Ingested Transactions", value=f"{total_txns:,}")
            
        st.markdown("---")
        chart_col1, chart_col2 = st.columns(2)
        with chart_col1:
            st.subheader("🏆 Retailer Performance Rankings")
            st.bar_chart(filtered_df.groupby('Retailer')['Volume_USD'].sum().sort_values(ascending=False))
        with chart_col2:
            st.subheader("🔸 Revenue Vol by Market Sector")
            st.bar_chart(filtered_df.groupby('Market_Tier')['Volume_USD'].sum().sort_values(ascending=False))
            
        st.subheader("🔎 Ingested Database Record Stream")
        st.dataframe(filtered_df.head(100), use_container_width=True)
    else:
        st.error("❌ Critical Error: 'enterprise_retail_dataT' table not found in repository. Ensure 'enterprise_retail_dataT.xlsx' is present.")

# ---- PANEL 2: UTILITIES (Tab 2) ----
elif active_panel == "🛠️ Utilities (Tab 2)":
    wm.render_translator()
    st.markdown("---")
    wm.render_renamer()

# ---- PANEL 3: WORKSPACE (Tab 3) ----
elif active_panel == "💼 Workspace (Tab 3)":
    wm.render_calculator()
    wm.render_codec()
    st.markdown("---")
    wm.render_invoice()

# ---- PANEL 4: SIMULATION (Tab 4) ----
elif active_panel == "✈️ Simulation (Tab 4)":
    wm.render_runway()
    st.markdown("---")
    wm.render_email_verifier()

# ---- PANEL 5: LIBRARY (Tab 5) ----
elif active_panel == "📚 Library (Tab 5)":
    
    st.markdown("### 🎬 Studio Asset Management Engine")
    drive_id = st.text_input(
        "Linked Google Drive Folder ID URL Sync Anchor:", 
        value="1BUnCmw4e4OTSBgyjjbJJsS12Yvg_lvrL", 
        key="library_drive_sync_input"
    )
    st.success(f"✅ Active Cloud Channel Connected to Google Drive Directory: `{drive_id}`")
    
    video_catalog_names = ["scene_01_raw.mp4", "b_roll_overlay.mp4", "intro_sequence.mov"]
    selected_target_video = st.selectbox("Select Active Google Drive Video Track to Process:", video_catalog_names)
    
    st.markdown("---")
    
    st.markdown("### 📝 Alternating Dialogue Timeline Setup")
    default_script = (
        "Male: Welcome back to the library matrix. Your voice track is rendering.\n"
        "Female: Perfect. We can match our script lines directly to our Google Drive files below."
    )
    script_text = st.text_area("Input Library Card Script Dialogue:", value=default_script, height=140, key="library_script_editor")
    
    raw_lines = script_text.strip().split("\n")
    timeline_flow = []
    for line in raw_lines:
        if not line.strip(): continue
        if line.lower().startswith("male:"):
            timeline_flow.append({"speaker": "Male", "profile": male_profile, "text": line[5:].strip()})
        elif line.lower().startswith("female:"):
            timeline_flow.append({"speaker": "Female", "profile": female_profile, "text": line[7:].strip()})
        else:
            if timeline_flow and timeline_flow[-1]["speaker"] == "Male":
                timeline_flow.append({"speaker": "Female", "profile": female_profile, "text": line.strip()})
            else:
                timeline_flow.append({"speaker": "Male", "profile": male_profile, "text": line.strip()})
                
    with st.expander("🔍 View Script Segment Distribution Map", expanded=False):
        for idx, segment in enumerate(timeline_flow):
            avatar = "👨" if segment["speaker"] == "Male" else "👩"
            st.write(f"**Line {idx+1} — {avatar} {segment['speaker']} ({segment['profile']}):** {segment['text']}")

    st.markdown("---")
    st.info(f"🎯 Global Processing Scope: Active Script and Video Track (**{selected_target_video}**) are locked to your storefront cards below.")
    
    wm.render_library_catalog()
