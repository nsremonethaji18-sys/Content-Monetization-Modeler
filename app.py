import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))

st.title("YouTube Revenue Predictor")

views = st.number_input("Views")
likes = st.number_input("Likes")
comments = st.number_input("Comments")
watch_time = st.number_input("Watch Time")
video_length = st.number_input("Video Length")
subscribers = st.number_input("Subscribers")

if st.button("Predict"):
    engagement_rate = (likes + comments) / views if views != 0 else 0

    data = np.array([[views, likes, comments,
                      watch_time, video_length,
                      subscribers, 0, 0, 0,
                      engagement_rate]])

    result = model.predict(data)

    st.success(f"Revenue: ${result[0]:.2f}")
