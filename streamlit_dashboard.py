from supabase import create_client
import pandas as pd 
import streamlit as st 
import plotly.express as px
import pydeck as pdk

API_URL = 'your_supabase_url'
API_KEY = 'your_supabase_api_key'
supabase = create_client(API_URL, API_KEY)

supabaseList = supabase.table('maintable').select('*').execute().data

df = pd.DataFrame()
for row in supabaseList:
    row["created_at"] = row["created_at"].split(".")[0]
    row["time"] = row["created_at"].split("T")[1]
    row["date"] = row["created_at"].split("T")[0]
    row["DateTime"] = row["created_at"]
    df = df.append(row, ignore_index=True)

st.set_page_config(page_title="ITUS Dashboard", layout='wide', initial_sidebar_state='collapsed')

st.title("ITUS Dashboard")
st.markdown("### Integrated Technology for Urban Sustainability")

time_filter = st.selectbox("Filter by", ["15 Minutes", "Hour", "Day", "Week", "Month"])

if time_filter == "15 Minutes":
    df_filtered = df
elif time_filter == "Hour":
    df_filtered = df.resample('H', on='DateTime').mean().reset_index().tail(5)  # Last 5 hours of data
elif time_filter == "Day":
    df_filtered = df.resample('H', on='DateTime').mean().reset_index().tail(24)  # Last 24 hours of data
elif time_filter == "Week":
    df_filtered = df.resample('D', on='DateTime').mean().reset_index().tail(7)  # Last 7 days of data
elif time_filter == "Month":
    df_filtered = df.resample('W', on='DateTime').mean().reset_index().tail(4)  # Last 4 weeks of data

col1, col2 = st.columns(2)

with col1:
    st.markdown('#### PM1 Levels')
    fig = px.line(df_filtered, x="DateTime", y="pm1", title='PM1 Levels Over Time', markers=True)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('#### PM2.5 Levels')
    fig = px.line(df_filtered, x="DateTime", y="pm2_5", title='PM2.5 Levels Over Time', markers=True)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('#### PM10 Levels')
    fig = px.line(df_filtered, x="DateTime", y="pm10", title='PM10 Levels Over Time', markers=True)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown('#### VOC Levels')
    fig = px.bar(df_filtered, x="DateTime", y="voc", title='VOC Levels Over Time')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('#### Humidity')
    fig = px.bar(df_filtered, x="DateTime", y="humidity", title='Humidity Over Time')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('#### Temperature')
    fig = px.bar(df_filtered, x="DateTime", y="temperature", title='Temperature Over Time')
    st.plotly_chart(fig, use_container_width=True)

st.markdown("### Device Location")

initial_view_state = pdk.ViewState(
    latitude=df["latitude"].mean(),
    longitude=df["longitude"].mean(),
    zoom=12,
    pitch=0,
)

device_name = "ITUS Device"

layer = pdk.Layer(
    "ScatterplotLayer",
    data=pd.DataFrame({
        'latitude': [df["latitude"].mean()],
        'longitude': [df["longitude"].mean()],
        'device_name': [device_name]
    }),
    get_position=["longitude", "latitude"],
    get_color=[135, 206, 235],
    get_radius=100,
    pickable=True,
)

tool_tip = {
    "html": "Device Name: <b>{device_name}</b><br/>Device Location:<br/> <b>Latitude:</b> {latitude} <br/> <b>Longitude:</b> {longitude}",
    "style": {"backgroundColor": "steelblue", "color": "white"},
}

map = pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v10",
    initial_view_state=initial_view_state,
    layers=[layer],
    tooltip=tool_tip,
)

st.pydeck_chart(map)
