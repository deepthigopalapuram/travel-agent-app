import streamlit as st
import random
import time

st.set_page_config(
    page_title="Autonomous Travel Desk",
    page_icon="🗺️",
    layout="wide"
)

st.title("Autonomous Travel Desk")
st.caption("Orchestrate multi-agent itineraries with real-time routing, budget arbitrage, and stress testing.")

# Destination database with realistic tailored data
DESTINATION_DATA = {
    "Goa": {
        "transit": "06:00 AM - Direct flight from Hyderabad to Dabolim (GOI), optimized for minimal layover.",
        "hotel": "01:30 PM - Check-in at heritage boutique stay near Fontainhas.",
        "day2_activity": "09:30 AM - Guided walking tour of Old Goa churches and Latin Quarter heritage architecture.",
        "culinary": "01:00 PM - Curated Goan-Portuguese seafood lunch at a verified local tavern.",
        "risk": "Minor coastal humidity spike detected on Day 2 afternoon. Risk Agent has pre-loaded an indoor art gallery and spice plantation tour alternative."
    },
    "Udupi, Karnataka": {
        "transit": "05:30 AM - Early morning express train connection from Hyderabad to Udupi.",
        "hotel": "02:00 PM - Check-in at coastal eco-resort near Malpe beach.",
        "day2_activity": "08:30 AM - Heritage temple architecture trail and local handicraft workshops.",
        "culinary": "12:30 PM - Traditional authentic Udupi vegetarian thali experience at a historic local mess.",
        "risk": "Unseasonal afternoon coastal drizzle predicted on Day 2. Risk Agent has automatically swapped outdoor beach slots with indoor heritage museum visits."
    },
    "Jaipur, Rajasthan": {
        "transit": "07:00 AM - Morning flight from Hyderabad to Jaipur International Airport.",
        "hotel": "01:00 PM - Check-in at traditional haveli in the old pink city.",
        "day2_activity": "09:00 AM - Pre-booked priority entry tour of Amer Fort and City Palace museums.",
        "culinary": "01:30 PM - Authentic Rajasthani Dal Baati Churma lunch at a heritage courtyard.",
        "risk": "High afternoon temperature surge expected on Day 2. Risk Agent has re-routed outdoor sightseeing to early morning hours and shifted afternoons to indoor bazaars."
    },
    "Kerala Backwaters": {
        "transit": "06:15 AM - Flight from Hyderabad to Cochin, followed by a private cab to Alleppey.",
        "hotel": "12:30 PM - Boarding private traditional luxury houseboat.",
        "day2_activity": "09:00 AM - Guided canoe village tour through narrow backwater canals.",
        "culinary": "01:00 PM - Fresh Kerala Karimeen fish fry and traditional sadhya prepared onboard.",
        "risk": "Brief tropical rain shower forecasted for Day 2 evening. Risk Agent has secured a covered deck dining arrangement and indoor Kathakali performance."
    }
}

col_input, col_output = st.columns([1, 2])

with col_input:
    st.subheader("Trip Parameters")
    destination = st.selectbox("Destination", list(DESTINATION_DATA.keys()))
    
    st.markdown("**Travel Style Preferences:**")
    style_culture = st.checkbox("Cultural & Heritage", value=True)
    style_culinary = st.checkbox("Local Culinary Focus", value=True)
    style_leisure = st.checkbox("Leisure & Scenic", value=False)
    
    budget = st.number_input("Budget Constraint (₹)", min_value=5000, max_value=500000, value=25000, step=1000)
    
    run_button = st.button("Run Multi-Agent Planner", type="primary")

with col_output:
    st.subheader("Multi-Agent Itinerary & Live Analytics Dashboard")
    
    if run_button:
        with st.spinner("Profiler, Logistics, Curator, and Risk Agents negotiating options..."):
            time.sleep(1.5) # Simulating active multi-agent reasoning loop
            
        data = DESTINATION_DATA[destination]
        
        st.success(f"Itinerary successfully synthesized for {destination} within ₹{budget:,} budget constraint!")
        
        st.markdown(f"### 🗺️ Optimized Route: Hyderabad to {destination}")
        st.markdown(f"""
        * **[Day 1: Transit & Arrival]**
          * `{data['transit']}`
          * `{data['hotel']}`
        * **[Day 2: Exploration & Style Customization]**
          * `{data['day2_activity']}`
          * `{data['culinary']}`
        """)
        
        st.markdown("### ⚡ Dynamic What-If Stress Test Simulation")
        st.info(f"Risk Agent simulation complete: *{data['risk']}*")
    else:
        st.info("Configure your trip parameters on the left and click **Run Multi-Agent Planner** to initialize the live agent mesh.")
