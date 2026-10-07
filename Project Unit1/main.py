import streamlit as st
#Import classes from another fils
#from classes import TripPrefrences
from Log_In import Authentication

auth = Authentication()

st.set_page_config(
    page_title="TARHAL",
    layout="wide"
)
# Load CSS
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
#
city_chose = input("Where do you want to go? ")
budget_chose = input("What is your budget? ")
travelType_chose = input("Who are you going with? ")

#trip = TripPrefrences(city_chose, budget_chose, travelType_chose)

#trip.check_choses(city_chose, budget_chose, travelType_chose)
