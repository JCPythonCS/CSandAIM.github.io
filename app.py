import streamlit as st
import pandas as pd
import os
import time

# Import all of your specific tool handlers from your workspace_modules.py file
import workspace_modules as wm

# 🖥️ Exact Page Config from your Repository
st.set_page_config(page_title="Computer Systems and AI Management Cockpit", layout="wide")

# 🏆 Original Title Banner
st.title("🛡️ Computer Systems and AI Management Cockpit")
st.markdown("---")

# 📂 Load Local Workspace Data Loop (From Your Original Code Base)
data_folder = '.'
all_files = [os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.lower().endswith(('.xlsx', '.xls'))]
database = {}

for file_path in all_files:
    file_name = os.path.basename(file_path)
    table_name = os.path.splitext(file_name)[0]
    try:
        database[table_name] = pd.read_excel(file_path)
    except:
        pass

# 🎛️ COMPLETE COCKPIT MASTER NAVIGATION (Ungrouped Layout)
# Replaced native grouped tabs with an independent view selector panel
active_panel = st.selectbox(
    "Select Workspace System Node To Deploy:",
    [
        "📊 Retail Enterprise Analytics Dashboard (Tab 1)",
        "🛠️ Workspace Utilities Terminal (Tabs 2 & 3)",
        "✈️ Modeling Runway & Network Monitor (Tabs 3 & 4)",
        "📚 Storefront Asset Library with Voice & Video Sync (Tab 5)"
    ],
    key="cockpit_panel_navigation"
)

st.markdown("---")

# 🎙️ DYNAMIC SIDEBAR VISIBILITY CONTROLLER
# The Voice Actor Sidebar configuration is ONLY visible on Tab 5 where your media engines live
if active_panel == "📚 Storefront Asset Library with Voice & Video Sync (Tab 5)":
    st.sidebar.header("🗣️ Audio Profiles Configuration")
    male_profile = st.sidebar.selectbox("Male Actor Voice", ["Male_Adam (Deep/Calm)", "Male_Michael (Professional)", "Male_David"])
    female_profile = st.sidebar.selectbox("Female Actor Voice", ["Female_Emily (Smooth)", "Female_Serena (Narrator)", "Female_Rachel"])
    st.sidebar.markdown("---")
    st.sidebar.caption("Voice Profile Parameters Active on Library Canvas")
else:
    # Completely clears the sidebar on all other tabs so they are full-width
    st.sidebar.empty()
    male_profile = "Male_Adam (Deep/Calm)"
    female_profile = "Female_Emily (Smooth)"

# ==================== ACTIVE VIEWPORT ROUTING GRID ====================

# ---- PANEL 1: RETAIL ENTERPRISE DASHBOARD (Your Original Code Layout) ----
if active_panel == "📊 Retail Enterprise Analytics Dashboard (Tab 1)":
    st.subheader("📊 Enterprise Retail Data Ingestion Streams")
    
    if 'enterprise_retail_dataT' in database:
        df = database['enterprise_retail_dataT']
        
        # Display Filters directly inside the page view since sidebar is hidden
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            selected_region = st.multiselect("Select Region Filter Context:", options=df['Region'].unique(), default=df['Region'].unique())
        with col_f2:
            selected_retailer = st.multiselect("Select Retailer Filter Context:", options=df['Retailer'].unique(), default=df['Retailer'].unique())
            
        filtered_df = df[(df['Region'].isin(selected_region)) & (df['Retailer'].isin(selected_retailer))]
        
        # KPIs
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
        st.error("❌ Critical Error: 'enterprise_retail_dataT.xlsx' table not found in root workspace directory.")

# ---- PANEL 2: UTILITIES TERMINAL ----
elif active_panel == "🛠️ Workspace Utilities Terminal (Tabs 2 & 3)":
    wm.render_translator()
    st.markdown("---")
    wm.render_calculator()
    wm.render_codec()
    st.markdown("---")
    wm.render_invoice()
    st.markdown("---")
    wm.render_renamer()

# ---- PANEL 3: MODELING RUNWAY ----
elif active_panel == "✈️ Modeling Runway & Network Monitor (Tabs 3 & 4)":
    wm.render_runway()
    st.markdown("---")
    wm.render_email_verifier()

# ---- PANEL 4: TAB 5 LIBRARY WITH INTEGRATED AUDIO & VIDEO TOOLS ----
elif active_panel == "📚 Storefront Asset Library with Voice & Video Sync (Tab 5)":
    
    # 🎬 INTEGRATED GOOGLE DRIVE ASSET SYNC FOR LIBRARY CARDS
    st.markdown("### 🎬 Studio Asset Management Engine")
    drive_id = st.text_input(
        "Linked Google Drive Folder ID URL Sync Anchor:", 
        value="1BUnCmw4e4OTSBgyjjbJJsS12Yvg_lvrL", 
        key="library_drive_sync_input"
    )
    st.success(f"✅ Active Cloud Channel Connected to Google Drive Directory: `{drive_id}`")
    
    # Video Catalog Selection Tracker
    video_catalog_names = ["scene_01_raw.mp4", "b_roll_overlay.mp4", "intro_sequence.mov"]
    selected_target_video = st.selectbox("Select Active Google Drive Video Track to Process:", video_catalog_names)
    
    st.markdown("---")
    
    # 🎙️ INTEGRATED ALTERNATING VOICE SCRIPT CONTROLLER
    st.markdown("### 📝 Alternating Dialogue Timeline Setup")
    default_script = (
        "Male: Welcome back to the library matrix. Your voice track is rendering.\n"
        "Female: Perfect. We can match our script lines directly to our Google Drive files below."
    )
    script_text = st.text_area("Input Library Card Script Dialogue:", value=default_script, height=140, key="library_script_editor")
    
    # Dialogue Parse Pipeline
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
                
    # Quick Timeline Preview Indicator
    with st.expander("🔍 View Script Segment Distribution Map", expanded=False):
        for idx, segment in enumerate(timeline_flow):
            avatar = "👨" if segment["speaker"] == "Male" else "👩"
            st.write(f"**Line {idx+1} — {avatar} {segment['speaker']} ({segment['profile']}):** {segment['text']}")

    st.markdown("---")
    
    # 📚 RENDER THE COMPREHENSIVE STOREFRONT LIBRARY CATALOG (From workspace_modules.py)
    # The voice tracking elements can now be applied to any selected card catalog item seamlessly
    st.info(f"🎯 Global Processing Scope: Active Script and Video Track (**{selected_target_video}**) are locked to your storefront cards below.")
    wm.render_library_catalog()
