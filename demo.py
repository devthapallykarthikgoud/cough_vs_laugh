import streamlit as st
import pandas as pd

st.title("A Tiny Sound, A Big Insight")
st.write("This app shows how a smartwatch can use features to differentiate between cough and laugh.")

features = {
    "Input Audio": "array",
    "Frequency": "float",
    "Intensity": "float",
    "Heart rate": "integer",
    "Blood pressure": "integer",
    "Oxygen": "float",
    "Time": "datetime"
}
df = pd.DataFrame(features, index=["Datatype"]).T
st.dataframe(df)

st.subheader("Adjust Feature Values")
st.write("Demo only: if any attribute value 50% then chances increase for cough.")
freq = st.slider("Frequency (Hz)", 100, 1000, 400)
intensity = st.slider("Intensity (dB)", 30, 100, 65)
heart_rate = st.slider("Heart Rate (BPM)", 50, 140, 80)
bp = st.slider("Blood Pressure (mmHg, systolic)", 90, 180, 120)
oxygen = st.slider("Oxygen Saturation (%)", 85, 100, 97)
env_noise = st.slider("Environment Noise (dB)", 20, 100, 50)

cough_score = 0
laugh_score = 0

if intensity > 75: cough_score += 1
if freq < 500: cough_score += 1
if oxygen < 95: cough_score += 1
if heart_rate > 100: cough_score += 1

if 300 < freq < 700: laugh_score += 1
if 50 < intensity < 75: laugh_score += 1
if 70 < heart_rate < 110: laugh_score += 1
if oxygen >= 96: laugh_score += 1

total = cough_score + laugh_score + 0.0001
cough_prob = cough_score / total
laugh_prob = laugh_score / total

st.subheader("Prediction Result")
if cough_prob > laugh_prob:
    st.write(f"Likely a Cough ({cough_prob:.2f} confidence)")
else:
    st.write(f"Likely a Laugh ({laugh_prob:.2f} confidence)")

st.write(f"Cough Likelihood: {cough_prob:.2f}")
st.write(f"Laugh Likelihood: {laugh_prob:.2f}")
