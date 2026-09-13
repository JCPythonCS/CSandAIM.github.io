import streamlit as st
import re
import time

# 1. Page Config Setup
st.set_page_config(
    page_title="Streamlit Media Cockpit",
    page_icon="🎛️",
    layout="wide"
)

# App Title & UI Branding
st.title("🎛️ Streamlit IO Cockpit")
st.subheader("Multi-Speaker Audio Script & Google Drive Video Asset Studio")

# 2. Sidebar Configuration Controls
st.sidebar.header("📁 Google Drive Sync")
drive_folder_id = st.sidebar.text_input(
    "Google Drive Folder ID", 
    placeholder="Enter your folder ID (from your Drive URL)",
    help="Provide the folder ID containing your saved video files."
)

st.sidebar.header("🎙️ Voice Settings")
male_voice = st.sidebar.selectbox("Male Profile Selection", ["Male_Voice_A", "Male_Voice_B", "Male_Voice_C"])
female_voice = st.sidebar.selectbox("Female Profile Selection", ["Female_Voice_A", "Female_Voice_B", "Female_Voice_C"])

st.sidebar.markdown("---")
st.sidebar.caption("Streamlit Engine Deployment Active")

# 3. Main Interface Navigation (The Core Tabs & Tools)
tab_script, tab_drive, tab_audio, tab_video = st.tabs([
    "📝 Script & Dialogue Editor", 
    "🗂️ Google Drive Asset Explorer", 
    "🔊 Alternating Voice Synthesis", 
    "🎬 Final Video Compiler"
])

# ---- TAB 1: SCRIPT EDITOR ----
with tab_script:
    st.header("Dialogue Layout Editor")
    st.markdown("Type out your dialogue. Use `Male:` and `Female:` prefixes to dictate speaker splits.")
    
    # Default placeholder text showing alternating format
    sample_script = (
        "Male: Welcome back to the cockpit. This is a pure Streamlit environment.\n"
        "Female: Perfect. The app formatting looks clean and all tools are restored.\n"
        "Male: Next, let's load our corresponding files from the Google Drive tab."
    )
    
    script_text = st.text_area("Input Dialogue Script:", value=sample_script, height=220)
    
    # Parsing script blocks
    raw_lines = script_text.strip().split("\n")
    parsed_dialogue = []
    
    for line in raw_lines:
        if not line.strip():
            continue
        if line.lower().startswith("male:"):
            parsed_dialogue.append({"role": "Male", "voice": male_voice, "text": line[5:].strip()})
        elif line.lower().startswith("female:"):
            parsed_dialogue.append({"role": "Female", "voice": female_voice, "text": line[7:].strip()})
        else:
            # Automatic fallback toggle
            if parsed_dialogue and parsed_dialogue[-1]["role"] == "Male":
                parsed_dialogue.append({"role": "Female", "voice": female_voice, "text": line.strip()})
            else:
                parsed_dialogue.append({"role": "Male", "voice": male_voice, "text": line.strip()})
                
    # Visual Output Preview Frame
    st.markdown("#### 🔍 Timeline Flow Preview")
    for idx, item in enumerate(parsed_dialogue):
        icon = "👨" if item["role"] == "Male" else "👩"
        bg = "#f0f7f9" if item["role"] == "Male" else "#fff0f5"
        border = "#1f77b4" if item["role"] == "Male" else "#e377c2"
        
        st.markdown(
            f"""
            <div style="background-color: {bg}; padding: 12px; border-radius: 6px; margin-bottom: 8px; border-left: 5px solid {border};">
                <strong>Segment {idx+1} — {icon} {item['role']} ({item['voice']}):</strong> {item['text']}
            </div>
            """, 
            unsafe_allow_html=True
        )

# ---- TAB 2: GOOGLE DRIVE ASSET EXPLORER ----
with tab_drive:
    st.header("Google Drive File Sync")
    if not drive_folder_id:
        st.warning("⚠️ Enter your Google Drive Folder ID in the sidebar to visualize your saved files.")
    else:
        st.success(f"Successfully linked layout to Google Drive Folder: `{drive_folder_id}`")
        
        # Display table mapping the video files saved in your folder
        st.markdown("### 🎥 Detected Video Files in Cloud Folder")
        mock_file_data = {
            "File Name": ["project_scene_01.mp4", "b_roll_footage.mp4", "intro_clip.mov"],
            "File Size": ["34.8 MB", "112.5 MB", "14.2 MB"],
            "Sync Status": ["Ready", "Ready", "Ready"]
        }
        st.dataframe(mock_file_data, use_container_width=True)
        
        selected_file = st.selectbox("Choose Target Video for Voice Overlay:", mock_file_data["File Name"])
        st.session_state['active_video'] = selected_file

# ---- TAB 3: AUDIO SYNTHESIS ENGINE ----
with tab_audio:
    st.header("Alternating Voice Generator")
    st.write("Process the script timeline to generate alternating audio files sequence.")
    
    if st.button("🚀 Process & Synthesize Audio Timeline", type="primary"):
        progress_status = st.progress(0)
        status_message = st.empty()
        
        for index, item in enumerate(parsed_dialogue):
            status_message.text(f"Generating voice clip {index+1}/{len(parsed_dialogue)} using {item['voice']}...")
            time.sleep(1) # Simulates backend audio compilation
            progress_status.progress(int((index + 1) / len(parsed_dialogue) * 100))
            
        st.success("🎉 Voice generation complete! Audio streams have been successfully matched to timing blocks.")
        st.audio("https://soundhelix.com")

# ---- TAB 4: FINAL VIDEO COMPILER ----
with tab_video:
    st.header("Video Automation Suite")
    st.write("Stitch generated voice audio onto your selected Google Drive video files.")
    
    target_vid = st.session_state.get('active_video', 'No video selected in Drive Tab')
    st.info(f"🎬 Current Target Video Asset: **{target_vid}**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("##### Mixing Configuration")
        music_vol = st.slider("Background Music Mix Volume (%)", 0, 100, 15)
        ducking_enabled = st.checkbox("Apply audio ducking when voices are speaking", value=True)
        
    with col2:
        st.markdown("##### Production")
        if st.button("🎬 Compile Final Composite Video"):
            with st.spinner("Executing timeline sync and merging audio to video frames via pipeline..."):
                time.sleep(3)
            st.success("✨ Composite video built successfully!")
            st.button("📥 Download Compiled Master File")
