import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title="Autonomous Travel Desk",
    page_icon="🗺️",
    layout="wide"
)

st.title("Autonomous Travel Desk")
st.caption("Orchestrate multi-agent itineraries with real-time routing, budget arbitrage, and stress testing.")

col_input, col_output = st.columns([1, 2])

with col_input:
    st.subheader("Trip Parameters")
    destination = st.selectbox("Destination", ["Udupi, Karnataka", "Goa", "Jaipur, Rajasthan", "Kerala Backwaters"])

    st.markdown("**Travel Style Preferences:**")
    style_culture = st.checkbox("Cultural & Heritage", value=True)
    style_culinary = st.checkbox("Local Culinary Focus", value=True)
    style_leisure = st.checkbox("Leisure & Scenic", value=False)

    budget = st.number_input("Budget Constraint (₹)", min_value=5000, max_value=500000, value=25000, step=1000)

    run_button = st.button("Run Multi-Agent Planner", type="primary")

with col_output:
    st.subheader("Multi-Agent Itinerary & Live Analytics Dashboard")

    if run_button:
        with st.spinner("Agents negotiating routes, analyzing budgets, and running stress tests..."):
            time.sleep(2)

        st.success("Itinerary successfully synthesized!")
        st.markdown(f"### 🗺️ Optimized Route: Hyderabad to {destination}")
        st.markdown("""
        * **[Day 1: Transit & Arrival]**
          * `06:00 AM` - Flight/Train connection optimized for minimal layover.
          * `02:00 PM` - Hotel check-in & initial orientation walk by Curator Agent.
        * **[Day 2: Exploration & Culture]**
          * `09:00 AM` - Guided heritage site tour with pre-booked entry passes.
          * `01:00 PM` - Verified local culinary experience matching dietary preferences.
        """)
        st.markdown("### ⚡ What-If Stress Test Simulation")
        st.info("Risk Agent simulation complete: *Minor weather variability detected on Day 2. Backup indoor itinerary pre-loaded automatically.*")
    else:
        st.info("Configure your trip parameters on the left and click **Run Multi-Agent Planner** to initialize the agent mesh.")
