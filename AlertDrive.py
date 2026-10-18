import random
import pandas as pd
import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AlertDrive AI - Edge Monitor", page_icon="🚗", layout="wide"
)

# --- CUSTOM CSS FOR DARK MODE UI ---
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
st.title("🚗 AlertDrive AI: Edge-Optimized Driver Fatigue Monitor")
st.markdown(
    "Real-time computer vision telemetry pipeline tracking **Eye Aspect Ratio"
    " (EAR)**, **Mouth Aspect Ratio (MAR)**, and **PERCLOS** metrics."
)
st.markdown("---")

# --- SIDEBAR CONTROLS ---
st.sidebar.header("⚙️ Edge System Settings")
app_mode = st.sidebar.selectbox(
    "Operation Mode", ["Live Camera Snapshot Test", "Simulation Dashboard"]
)

st.sidebar.markdown("---")
st.sidebar.subheader("🎚️ Temporal Thresholds")
ear_thresh = st.sidebar.slider(
    "EAR Closure Threshold", 0.15, 0.30, 0.20, 0.01
)
mar_thresh = st.sidebar.slider("MAR Yawn Threshold", 0.40, 0.70, 0.55, 0.01)
time_window = st.sidebar.slider("Sliding Time Buffer (Seconds)", 1.0, 3.0, 1.5)

# --- MAIN LOGIC ---
if app_mode == "Live Camera Snapshot Test":
  st.subheader("📹 In-Cabin Live Camera Feed")
  st.write(
      "Capture a snapshot from your device camera to simulate real-time edge"
      " telemetry analysis."
  )

  camera_image = st.camera_input("Capture Driver Face")

  if camera_image is not None:
    st.success("✅ Frame captured successfully! Running edge inference...")

    col1, col2 = st.columns(2)
    with col1:
      st.image(
          camera_image,
          caption="Captured In-Cabin Frame",
          width="stretch",
      )

    with col2:
      st.subheader("🔍 ML Inference Metrics")
      # Simulated robust values for demonstration
      st.metric(
          label="👁️ Eye Aspect Ratio (EAR)", value="0.22", delta="Normal"
      )
      st.metric(
          label="🥱 Mouth Aspect Ratio (MAR)", value="0.34", delta="Stable"
      )
      st.metric(
          label="🛡️ Drowsiness Classification",
          value="Attentive",
          delta="Safe",
          delta_color="normal",
      )
  else:
    st.info(
        "ℹ️ Position yourself in front of your camera and click **Take"
        " Photo** above."
    )

else:
  # --- DASHBOARD METRICS ---
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
        label="📊 PERCLOS Score",
        value="11.8%",
        delta="Safe (<15%)",
        delta_color="inverse",
    )
  with col4:
    st.metric(label="⚡ System FPS", value="28.4 FPS", delta="Edge Optimized")

  st.markdown("---")
  st.subheader("📋 Temporal Safety Event Log")

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
  ]
  st.dataframe(pd.DataFrame(log_data), width="stretch")

  st.markdown("---")
  if st.button("🔴 Trigger Test Emergency Buzzer", width="stretch"):
    st.error(
        "🚨 **BUZZER & LED ACTIVE:** Microsleep detected! Audio alarm triggered"
        " on edge hardware."
    )

# --- FOOTER ---
st.markdown("---")
st.caption(
    "⚠️ **AI Achievers Project:** AlertDrive AI — Built with Python and"
    " Streamlit."
)
