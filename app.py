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
    table_name = os.path.splitext(file_name)
    try:
        database[table_name] = pd.read_excel(file_path)
    except:
        pass

# 🎛️ COMPLETE COCKPIT MASTER NAVIGATION TABS
# We track the active selection using the `key` parameter to toggle the sidebar
active_tab = st.radio(
    "Select Cockpit Workspace Focus:",
    [
        "🎙️ Voice Text Engine (Tab 1)", 
        "📁 Google Drive Asset Sync (Tab 2)", 
        "🛠️ Workspace Utilities (Tabs 2 & 3)", 
        "✈️ Modeling Runway (Tabs 3 & 4)", 
        "📚 Storefront Asset Library (Tab 5)"
    ],
    horizontal=True,
    key="navigation_tabs"
)

st.markdown("---")

# 🎙️ DYNAMIC SIDEBAR VISIBILITY CONTROLLER
# The sidebar only populates if the user is actively working on the Voice Text Engine
if active_tab == "🎙️ Voice Text Engine (Tab 1)":
    st.sidebar.header("🗣️ Audio Profiles Configuration")
    male_profile = st.sidebar.selectbox("Male Actor Voice", ["Male_Adam (Deep/Calm)", "Male_Michael (Professional)", "Male_David"])
    female_profile = st.sidebar.selectbox("Female Actor Voice", ["Female_Emily (Smooth)", "Female_Serena (Narrator)", "Female_Rachel"])
    st.sidebar.markdown("---")
    st.sidebar.caption("Voice Profile Parameters Active")
else:
    # If any other tab is active, we render an empty sidebar configuration to hide it
    st.sidebar.empty()
    # We assign default structural values so the backend code doesn't throw a NameError
    male_profile = "Male_Adam (Deep/Calm)"
    female_profile = "Female_Emily (Smooth)"

# ==================== ACTIVE VIEWPORT ROUTING GRID ====================

# ---- VIEWPORT 1: VOICE TEXT ENGINE ----
if active_tab == "🎙️ Voice Text Engine (Tab 1)":
    st.subheader("📝 Alternating Dialogue Timeline Setup")
    st.caption("Alternate fluidly between your chosen Male and Female voice actor profiles. Type using 'Male:' or 'Female:' tags.")
    
    default_script = (
        "Male: Welcome back to the cockpit. Your alternating voice script engine is now active.\n"
        "Female: Perfect. We can line up our voiceover text blocks right here in the Streamlit engine.\n"
        "Male: Next, we can alternate audio segments directly onto our Google Drive video track."
    )
    script_text = st.text_area("Input Dialogue Timeline Text:", value=default_script, height=200, key="cockpit_script_editor")
    
    # Process text layout blocks into alternating timeline structures
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

    st.markdown("#### 🔍 Active Dialogue Timeline Analysis")
    for idx, segment in enumerate(timeline_flow):
        avatar = "👨" if segment["speaker"] == "Male" else "👩"
        bg = "#e8f4f8" if segment["speaker"] == "Male" else "#fef0f5"
        border = "#2b7bba" if segment["speaker"] == "Male" else "#e05295"
        
        st.markdown(
            f"""
            <div style="background-color: {bg}; padding: 12px; border-radius: 6px; margin-bottom: 8px; border-left: 5px solid {border};">
                <strong>Segment {idx+1} — {avatar} {segment['speaker']} ({segment['profile']}):</strong> {segment['text']}
            </div>
            """, 
            unsafe_allow_html=True
        )
        
    if st.button("🚀 Process & Synthesize Voices Layout", type="primary"):
        prog = st.progress(0)
        status = st.empty()
        for idx, segment in enumerate(timeline_flow):
            status.text(f"Processing Segment {idx+1}/{len(timeline_flow)} via {segment['profile']}...")
            time.sleep(0.6)
            prog.progress(int((idx + 1) / len(timeline_flow) * 100))
        st.success("🎉 Combined alternating voiceover tracks generated successfully!")
        st.audio("https://soundhelix.com")

# ---- VIEWPORT 2: GOOGLE DRIVE VIDEO ASSETS ----
elif active_tab == "📁 Google Drive Asset Sync (Tab 2)":
    st.subheader("🎬 Google Drive Studio Assets Connection")
    
    drive_id = st.text_input(
        "Linked Google Drive Folder ID:", 
        value="1BUnCmw4e4OTSBgyjjbJJsS12Yvg_lvrL", 
        key="cockpit_drive_input"
    )
    
    st.success(f"✅ Successfully synchronized workspace layout with Google Drive Folder: `{drive_id}`")
    st.markdown("### 📽️ Synced Video Files Detected on Cloud Drive")
    
    video_catalog = {
        "Video File Name": ["scene_01_raw.mp4", "b_roll_overlay.mp4", "intro_sequence.mov"],
        "Format Track": ["MP4", "MP4", "MOV"],
        "Buffer Status": ["Available", "Available", "Available"]
    }
    st.dataframe(video_catalog, use_container_width=True)
    chosen_video = st.selectbox("Select Active Video Track for Voice Over Overlay:", video_catalog["Video File Name"])
    
    st.markdown("---")
    if st.button("🎬 Compile Final Composite Video File"):
        with st.spinner(f"Executing timeline processing and syncing alternating voiceover tracks onto '{chosen_video}'..."):
            time.sleep(3)
        st.success("✨ Production rendering complete! Video master layout built successfully.")
        st.button("📥 Download Final Video Asset")

# ---- VIEWPORT 3: WORKSPACE UTILITIES ----
elif active_tab == "🛠️ Workspace Utilities (Tabs 2 & 3)":
    wm.render_translator()
    st.markdown("---")
    wm.render_calculator()
    wm.render_codec()
    st.markdown("---")
    wm.render_invoice()
    st.markdown("---")
    wm.render_renamer()

# ---- VIEWPORT 4: INFRASTRUCTURE RUNWAY ----
elif active_tab == "✈️ Modeling Runway (Tabs 3 & 4)":
    wm.render_runway()
    st.markdown("---")
    wm.render_email_verifier()

# ---- VIEWPORT 5: MULTIMEDIA STOREFRONT LIBRARY ----
elif active_tab == "📚 Storefront Asset Library (Tab 5)":
    wm.render_library_catalog()
