import streamlit as st
from weather_api import get_weather
import pandas  as pd
from datetime import datetime

# UI
st.title("CalmCast 🌤️🧠")
st.subheader("Track how weather affects your mood")

name = st.text_input("Your name (optional)")
mood = st.slider("How do you feel today?", 1, 5)
journal = st.text_area("Write a short journal entry (optional)")
city = st.text_input("Enter your city")

if st.button("Submit Entry"):
    weather = get_weather(city)
    today = datetime.now().strftime("%Y-%m-%d")
    
    entry = {
        "Date": today,
        "Name": name,
        "City": city,
        "Mood": mood,
        "Journal": journal,
        "Temp": weather['temp'],
        "Humidity": weather['humidity'],
        "Pressure": weather['pressure']
    }
    
    df = pd.DataFrame([entry])
    try:
        existing = pd.read_csv("data.csv")
        df = pd.concat([existing, df])
    except FileNotFoundError:
        pass
    df.to_csv("data.csv", index=False)
    st.success("Entry saved!")

# Plot
if st.button("Show Trends"):
    df = pd.read_csv("data.csv")
    st.line_chart(df[['Mood', 'Temp', 'Humidity']])
