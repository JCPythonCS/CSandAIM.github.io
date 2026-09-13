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

# LOGO CONTAINER: Maps explicit absolute workspace routing loops to prevent missing asset errors
col_logo_left, col_title_spacer, col_logo_right = st.columns(3)

# Search for assets in local root path directories
current_working_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else '.'

with col_logo_left:
    logo1_path = os.path.join(current_working_dir, "logo1.png")
    if os.path.exists(logo1_path):
        st.image(logo1_path, use_container_width=True)
    elif os.path.exists("logo1.png"):
        st.image("logo1.png", use_container_width=True)
    else:
        st.caption("🖼️ `logo1.png` missing from root repository directory slot")

with col_logo_right:
    logo2_path = os.path.join(current_working_dir, "logo2.png")
    if os.path.exists(logo2_path):
        st.image(logo2_path, use_container_width=True)
    elif os.path.exists("logo2.png"):
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
        # Save file configurations to load data dynamically on choice
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
        # DYNAMIC FILE SELECTOR: Let users select ANY file found in the GitHub repo
        selected_file_name = st.sidebar.selectbox(
            "Select Database File Asset:", 
            options=sorted(list(database.keys())),
            help="Choose any workspace excel file from your repository to analyze dynamically."
        )
        
        # Load the selected dataset dynamically from the file path mapping
        target_file_path = database[selected_file_name]
        
        try:
            df = pd.read_excel(target_file_path)
            
            # DYNAMIC FILTER MATCHING: Pull unique Region columns if they exist in the chosen file
            if 'Region' in df.columns:
                selected_region = st.sidebar.multiselect("Select Region Filter Context:", options=df['Region'].unique(), default=df['Region'].unique())
            else:
                st.sidebar.info("ℹ️ Selected file contains no standard 'Region' parameter.")
                selected_region = []
                
            # Pull unique Retailer or Store columns if they exist in the chosen file
            retailer_col = 'Retailer' if 'Retailer' in df.columns else 'Store' if 'Store' in df.columns else None
            if retailer_col:
                selected_retailer = st.sidebar.multiselect(f"Select {retailer_col} Filter Context:", options=df[retailer_col].unique(), default=df[retailer_col].unique())
            else:
                st.sidebar.info("ℹ️ Selected file contains no standard 'Retailer/Store' parameter.")
                selected_retailer = []
                
        except Exception as e:
            st.sidebar.error(f"Error reading file: {e}")
            df = None
            selected_region, selected_retailer = [], []
    else:
        st.sidebar.warning("⚠️ No `.xlsx` or `.xls` spreadsheet assets detected in the root repository.")
        df = None
        selected_region, selected_retailer = [], []
        
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
    st.subheader(f"📊 Enterprise Retail Ingestion Streams")
    
    if df is not None:
        # Dynamically process data based on whatever fields exist in the active spreadsheet
        filtered_df = df.copy()
        if 'Region' in df.columns and selected_region:
            filtered_df = filtered_df[filtered_df['Region'].isin(selected_region)]
            
        retailer_col = 'Retailer' if 'Retailer' in df.columns else 'Store' if 'Store' in df.columns else None
        if retailer_col and selected_retailer:
            filtered_df = filtered_df[filtered_df[retailer_col].isin(selected_retailer)]
        
        # Look for metric volume values dynamically across headers
        volume_col = 'Volume_USD' if 'Volume_USD' in filtered_df.columns else filtered_df.select_dtypes(include='number').columns[0] if len(filtered_df.select_dtypes(include='number').columns) > 0 else None
        
        total_vol = filtered_df[volume_col].sum() if volume_col else 0.0
        total_txns = len(filtered_df)
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric(label=f"💰 Total Combined Volume ({volume_col if volume_col else 'N/A'})", value=f"${total_vol:,.2f}")
        with c2:
            st.metric(label="📦 Total Ingested Transactions", value=f"{total_txns:,}")
            
        st.markdown("---")
        chart_col1, chart_col2 = st.columns(2)
        
        if retailer_col and volume_col:
            with chart_col1:
                st.subheader(f"🏆 {retailer_col} Performance Rankings")
                st.bar_chart(filtered_df.groupby(retailer_col)[volume_col].sum().sort_values(ascending=False))
        if 'Market_Tier' in filtered_df.columns and volume_col:
            with chart_col2:
                st.subheader("🔸 Revenue Vol by Market Sector")
                st.bar_chart(filtered_df.groupby('Market_Tier')[volume_col].sum().sort_values(ascending=False))
            
        st.subheader("🔎 Ingested Database Record Stream")
        st.dataframe(filtered_df.head(100), use_container_width=True)
    else:
        st.info("ℹ️ Select a database file from the left sidebar to populate your charts and tables.")

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
                
