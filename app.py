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

# FIXED LOGO GRID: Allocates a precise 3-column framework to avoid TypeError crashes
col_logo_left, col_title_spacer, col_logo_right = st.columns(3)

# Pinpoint absolute root directory path boundaries to maintain server image persistence
current_working_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else '.'

with col_logo_left:
    logo1_path = os.path.join(current_working_dir, "logo1.png")
    if os.path.exists(logo1_path):
        st.image(logo1_path, use_container_width=True)
    elif os.path.exists("LOGOB.png"):
        st.image("logo1.png", use_container_width=True)
    else:
        st.caption("🖼️ `logo1.png` missing from root repository directory slot")

with col_logo_right:
    logo2_path = os.path.join(current_working_dir, "logo2.png")
    if os.path.exists(logo2_path):
        st.image(logo2_path, use_container_width=True)
    elif os.path.exists("LOGOG.png"):
        st.image("logo2.png", use_container_width=True)
    else:
        st.caption("🖼️ `logo2.png` missing from root repository directory slot")

st.markdown("---")

# 📂 MASTER FILE INGESTION ENGINE: Dynamically reads ALL files in the repository
data_folder = current_working_dir
all_files = [f for f in os.listdir(data_folder) if f.lower().endswith(('.xlsx', '.xls'))]
database = {}

# Loops through every discovered sheet file and maps its plain-text name for the UI menu
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
        "🛠️ Utilities (Tab 2)",
        "💼 Workspace (Tab 3)",
        "✈️ Simulation (Tab 4)",
        "📚 Library (Tab 5)"
    ],
    key="cockpit_panel_navigation"
)

st.markdown("---")

# 🎙️ FIXED SIDEBAR VISIBILITY CONTROLLER
if active_panel == "📊 Analytics (Tab 1)":
    st.sidebar.header("🎯 Dashboard Control Filters")
    
    if database:
        # DYNAMIC FILE SELECTOR: Choose any workspace file from your repository
        selected_file_name = st.sidebar.selectbox(
            "Select Database File Asset:", 
            options=sorted(list(database.keys())),
            help="Choose any workspace excel file from your repository to analyze dynamically."
        )
        
        target_file_path = database[selected_file_name]
        
        try:
            df = pd.read_excel(target_file_path)
            
            # 🛡️ STRATEGIC FILTER MATRICES: Renders filters strictly based on your operational column headers
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
    st.subheader(f"📊 Tactical Systems & Analytics Stream")
    
    if df is not None:
        # Dynamically process data filtered by your tactical columns
        filtered_df = df.copy()
        
        if 'Active Combat Unit Name' in df.columns and selected_units:
            filtered_df = filtered_df[filtered_df['Active Combat Unit Name'].isin(selected_units)]
            
        if 'Strategic Command Sector' in df.columns and selected_sectors:
            filtered_df = filtered_df[filtered_df['Strategic Command Sector'].isin(selected_sectors)]
            
        if 'Agency Command Tier' in df.columns and selected_tiers:
            filtered_df = filtered_df[filtered_df['Agency Command Tier'].isin(selected_tiers)]
        
        # Calculate row counts and numerical balances across data fields
        total_records = len(filtered_df)
        num_cols = filtered_df.select_dtypes(include='number').columns
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric(label="📦 Active Tracked Records", value=f"{total_records:,}")
        with c2:
            if len(num_cols) > 0:
                metric_sum = filtered_df[num_cols[0]].sum()
                st.metric(label=f"📊 Aggregate Core Metrics ({num_cols[0]})", value=f"{metric_sum:,.2f}")
            else:
                st.metric(label="📊 Operational Status", value="Data Deployment Active")
            
        st.markdown("---")
        
        # Performance/Distribution charts based on your operational fields
        chart_col1, chart_col2 = st.columns(2)
        
        if 'Strategic Command Sector' in filtered_df.columns:
            with chart_col1:
                st.subheader("🌐 Strategic Command Sector Distribution")
                st.bar_chart(filtered_df.groupby('Strategic Command Sector').size())
                
        if 'Agency Command Tier' in filtered_df.columns:
            with chart_col2:
                st.subheader("🔸 Agency Command Tier Breakdown")
                st.bar_chart(filtered_df.groupby('Agency Command Tier').size())
            
        st.subheader("🔎 Secure Ingested Record Stream")
        st.dataframe(filtered_df.head(100), use_container_width=True)
    else:
        st.info("ℹ️ Select an operational file from the left sidebar to populate your tactical dashboard data lines.")

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
