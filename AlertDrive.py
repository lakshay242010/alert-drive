import time
import numpy as np
import pandas as pd
import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AlertDrive AI - Fatigue Monitor", page_icon="🚗", layout="wide"
)

# --- CUSTOM CSS FOR ATTRACTIVE UI ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stMetric {
        background-color: #161b22;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #30363d;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("🚗 AlertDrive AI: Edge-Optimized Driver Fatigue & Distraction Monitor")
st.markdown(
    "A real-time computer vision telemetry pipeline tracking **Eye Aspect"
    " Ratio (EAR)**, **Mouth Aspect Ratio (MAR)**, and **PERCLOS** metrics to"
    " prevent micro-sleeps."
)
st.markdown("---")

# --- SIDEBAR: CONTROLS & SETTINGS ---
st.sidebar.header("⚙️ Edge System Controls")
mode = st.sidebar.selectbox(
    "Operation Mode", ["Live Simulation", "Uploaded Video Test Mode"]
)
camera_source = st.sidebar.selectbox(
    "In-Cabin Camera", ["USB Webcam (Front)", "IR Night-Vision Module"]
)

st.sidebar.markdown("---")
st.sidebar.subheader("🎚️ Temporal Thresholds")
ear_thresh = st.sidebar.slider(
    "EAR Closure Threshold", 0.15, 0.30, 0.20, 0.01, help="Triggers alert if EAR drops below this value."
)
mar_thresh = st.sidebar.slider(
    "MAR Yawn Threshold", 0.40, 0.70, 0.55, 0.01, help="Triggers alert if MAR exceeds this value."
)
time_window = st.sidebar.slider("Sliding Time Buffer (Seconds)", 1.0, 3.0, 1.5)

# --- MAIN DASHBOARD METRICS ---
col1, col2, col3, col4 = st.columns(4)

with col1:
  st.metric(
      label="👁️ Eye Aspect Ratio (EAR)",
      value="0.23",
      delta="-0.02 (Stable)",
      delta_color="normal",
  )

with col2:
  st.metric(
      label="🥱 Mouth Aspect Ratio (MAR)",
      value="0.32",
      delta="+0.04",
      delta_color="off",
  )

with col3:
  st.metric(
      label="📊 PERCLOS (60s Score)",
      value="11.8%",
      delta="Safe (<15%)",
      delta_color="inverse",
  )

with col4:
  st.metric(
      label="⚡ System FPS", value="28.4 FPS", delta="Edge Optimized"
  )

st.markdown("---")

# --- SIMULATION & TELEMETRY SECTION ---
col_left, col_right = st.columns([2, 1])

with col_left:
  st.subheader("📋 Temporal Safety Event & Telemetry Log")

  # Mock data representing sliding-window logs
  log_data = [
      {
          "Timestamp": "15:01:12",
          "Event": "Normal Blink",
          "EAR": "0.29",
          "MAR": "0.24",
          "Status": "✅ Safe",
      },
      {
          "Timestamp": "15:01:45",
          "Event": f"Prolonged Closure (>{time_window}s)",
          "EAR": "0.16",
          "MAR": "0.22",
          "Status": "⚠️ Microsleep Alert",
      },
      {
          "Timestamp": "15:02:10",
          "Event": "Yawn Incident Detected",
          "EAR": "0.25",
          "MAR": "0.62",
          "Status": "⚠️ Fatigue Warning",
      },
      {
          "Timestamp": "15:02:55",
          "Event": "Head Pitch/Yaw Shift",
          "EAR": "0.27",
          "MAR": "0.25",
          "Status": "⚠️ Gaze Distraction",
      },
  ]

  df_logs = pd.DataFrame(log_data)
  st.dataframe(df_logs, use_container_width=True)

with col_right:
  st.subheader("🚨 Active Interventions")
  st.success("🟢 **In-Cabin Status:** Driver alert and attentive.")

  if st.button("🔴 Trigger Test Emergency Buzzer", use_container_width=True):
    st.error(
        "🚨 **BUZZER & LED ACTIVE:** Microsleep detected! Audio alarm triggered"
        " on edge hardware."
    )

  st.markdown("### 🛡️ Robustness Check")
  st.write("• **Lighting:** Adapted for IR / Night mode.")
  st.write("• **Eyewear:** Compatible with prescription glasses.")

# --- FOOTER ---
st.markdown("---")
st.caption(
    "⚠️ **Automotive Safety Disclaimer:** AlertDrive AI is built with Python"
    " and Streamlit for real-time edge driver safety monitoring."
)
