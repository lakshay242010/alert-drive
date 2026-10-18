import random
import time
import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AlertDrive: Edge Fatigue Monitor", page_icon="🚗", layout="wide"
)

st.title("🚗 AlertDrive: Real-Time Driver Fatigue & Distraction Monitor")
st.write(
    "Edge-optimized telemetry dashboard tracking Eye Aspect Ratio (EAR),"
    " Mouth Aspect Ratio (MAR), and PERCLOS metrics."
)

# --- SIDEBAR: Calibration & Edge Settings ---
st.sidebar.header("⚙️ Edge Sensor & Thresholds")
camera_mode = st.sidebar.selectbox(
    "Camera Source",
    ["USB Webcam (1080p)", "IR Night-Vision Module", "Simulation Mode"],
)
ear_threshold = st.sidebar.slider(
    "EAR Alert Threshold (Eye Closure)", 0.15, 0.30, 0.20, 0.01
)
mar_threshold = st.sidebar.slider(
    "MAR Alert Threshold (Yawning)", 0.40, 0.70, 0.55, 0.01
)
perclos_window = st.sidebar.slider(
    "PERCLOS Rolling Window (Seconds)", 30, 120, 60
)

# --- MAIN DASHBOARD: Live Metrics & Simulation ---
col1, col2, col3 = st.columns(3)

with col1:
  st.metric(
      label="👁️ Current EAR (Eye Aspect Ratio)",
      value="0.22",
      delta="-0.03 (Normal)",
      delta_color="normal",
  )

with col2:
  st.metric(
      label="🥱 Current MAR (Mouth Aspect Ratio)",
      value="0.35",
      delta="+0.05",
      delta_color="off",
  )

with col3:
  st.metric(
      label="📊 PERCLOS Score (60s Window)",
      value="12.4%",
      delta="Safe (<15%)",
      delta_color="inverse",
  )

st.markdown("---")

# --- SIMULATED REAL-TIME TELEMETRY LOG ---
st.subheader("📋 Temporal Safety Event Log & Sliding-Window Metrics")

# Mock telemetry history dataframe
telemetry_data = [
    {
        "Timestamp": "14:45:02",
        "Event Type": "Normal Blink",
        "EAR": "0.28",
        "MAR": "0.25",
        "Status": "✅ Safe",
    },
    {
        "Timestamp": "14:45:18",
        "Event Type": "Prolonged Closure (>1.5s)",
        "EAR": "0.17",
        "MAR": "0.22",
        "Status": "⚠️ Microsleep Warning",
    },
    {
        "Timestamp": "14:45:45",
        "Event Type": "Yawn Detected (MAR > 0.55)",
        "EAR": "0.26",
        "MAR": "0.61",
        "Status": "⚠️ Fatigue Sign",
    },
    {
        "Timestamp": "14:46:12",
        "Event Type": "Head Pose Yaw Shift (Gaze)",
        "EAR": "0.25",
        "MAR": "0.24",
        "Status": "⚠️ Distraction Alert",
    },
]

df_logs = pd.DataFrame(telemetry_data)
st.dataframe(df_logs, use_container_width=True)

# --- ANALYTICS & INTERVENTIONS ---
st.markdown("---")
col_left, col_right = st.columns(2)

with col_left:
  st.subheader("📈 Sliding-Window Stability & Pose Tracking")
  st.progress(
      0.88, text="Blinks Per Minute Regularity: 88% (Optimal Range)"
  )
  st.progress(
      0.35, text="Head Pitch/Yaw Deviation Risk: 35% (Minimal Distraction)"
  )
  st.write(
      "*"
      f"Computed continuously across {perclos_window}-second rolling frames"
      " using local CPU optimization.*"
  )

with col_right:
  st.subheader("🚨 Active Intervention & Buzzer Controls")
  st.success("🟢 **In-Cabin Status:** Driver alert and focused.")

  if st.button("🔴 Simulate Emergency Fatigue Alarm"):
    st.error(
        "🚨 **BUZZER TRIGGERED:** Persistent eye closure detected! Local"
        " Arduino/LED buzzer activated."
    )

# --- FOOTER DISCLAIMER ---
st.markdown("---")
st.caption(
    "⚠️ **Automotive Safety Disclaimer:** AlertDrive is an edge-AI prototype"
    " designed for educational demonstration and safety research."
)
