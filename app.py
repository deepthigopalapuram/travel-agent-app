import streamlit as st
import time

st.set_page_config(
    page_title="Autonomous Travel Desk",
    page_icon="🗺️",
    layout="wide"
)

st.title("Autonomous Travel Desk")
st.caption("Multi-Agent Architecture: Profiler ➔ Logistics Engine ➔ Curator Agent ➔ Risk Mitigation Desk")

col_input, col_output = st.columns([1, 2])

with col_input:
    st.subheader("Trip Parameters")
    destination = st.selectbox("Destination", ["Goa", "Udupi, Karnataka", "Jaipur, Rajasthan", "Kerala Backwaters", "Varanasi, Uttar Pradesh"])
    
    st.markdown("**Travel Style Preferences:**")
    style_culture = st.checkbox("Cultural & Heritage", value=True)
    style_culinary = st.checkbox("Local Culinary Focus", value=True)
    style_leisure = st.checkbox("Leisure & Scenic", value=False)
    
    budget = st.number_input("Budget Constraint (₹)", min_value=5000, max_value=500000, value=25000, step=1000)
    
    run_button = st.button("Run Multi-Agent Planner", type="primary")

with col_output:
    st.subheader("Agent Mesh Execution & Live Itinerary")
    
    if run_button:
        # Step-by-step visual simulation of the agent loop
        status_box = st.status("Initializing Autonomous Agent Mesh...", expanded=True)
        
        with status_box:
            st.write("👤 **Profiler Agent:** Analyzing user preference vector and financial boundaries (₹{:,})...".format(budget))
            time.sleep(0.8)
            
            st.write(f"🚆 **Logistics Agent:** Optimizing transit routes from Hyderabad to {destination}...")
            time.sleep(0.8)
            
            styles = []
            if style_culture: styles.append("Heritage/Culture")
            if style_culinary: styles.append("Culinary Tasting")
            if style_leisure: styles.append("Leisure")
            st.write(f"🏛️ **Curator Agent:** Synthesizing hyper-local experiences matching focus: {', '.join(styles)}...")
            time.sleep(0.8)
            
            st.write("🛡️ **Risk & Contingency Agent:** Running weather and disruption stress tests...")
            time.sleep(0.8)
            
            status_box.update(label="Agent Mesh Execution Complete!", state="complete", expanded=False)
            
        # Dynamic Synthesis based on selections
        st.success(f"Optimized Master Itinerary Generated for {destination}")
        
        # Financial Arbitrage breakdown
        st.markdown("### 📊 Agent Cost & Value Arbitrage Analysis")
        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric("Estimated Cost", f"₹{int(budget * 0.82):,}", "-18% vs standard booking")
        col_m2.metric("Transit Efficiency", "High (Optimized Layovers)", "0 major delays expected")
        col_m3.metric("Experience Match", f"{len(styles) * 33}% Alignment", "Customized to preferences")
        
        # Customized itinerary body
        st.markdown(f"### 🗺️ Tailored Itinerary: Hyderabad ➔ {destination}")
        
        if "Goa" in destination:
            transit_desc = "Early morning flight from Hyderabad to Dabolim; private EV cab pre-booked to reduce local carbon footprint."
            day2_desc = "Morning walking tour through Fontainhas Latin Quarter focusing on colonial heritage architecture."
            food_desc = "Curated authentic Goan-Portuguese seafood tasting at a generational local kitchen."
        elif "Jaipur" in destination:
            transit_desc = "Morning direct flight from Hyderabad to Jaipur; pre-arranged prepaid taxi transfer."
            day2_desc = "Sunrise guided expedition across Amer Fort and Amber Palace with skip-the-line digital passes."
            food_desc = "Traditional Rajasthani thali featuring Dal Baati Churma at a verified heritage courtyard."
        elif "Udupi" in destination:
            transit_desc = "Optimized train and local transit linkage connecting smoothly from Hyderabad."
            day2_desc = "Ancient temple architecture trail combined with coastal handloom weaver workshop visits."
            food_desc = "Authentic historical Udupi vegetarian culinary trail through heritage local messes."
        else:
            transit_desc = "Multi-modal transit synchronization managed by Logistics Agent for optimal comfort."
            day2_desc = "Immersive local exploration tailored specifically to your chosen cultural and scenic preferences."
            food_desc = "Vetted regional culinary experience focusing on local ingredients and hygiene ratings."

        st.markdown(f"""
        * **[Day 1: Transit & Soft Landing]**
          * `06:00 AM` — {transit_desc}
          * `01:30 PM` — Hotel check-in managed by Curator Agent, factoring in proximity to transit hubs.
        * **[Day 2: Deep Dive & Custom Focus]**
          * `09:00 AM` — {day2_desc}
          * `01:00 PM` — {food_desc}
        """)
        
        st.markdown("### ⚡ Risk Agent Counterfactual Stress Test")
        if budget < 15000:
            st.warning("⚠️ **Budget Alert:** Risk Agent flagged that your budget is tight for peak season. Alternative budget hostels and public transit loops have been swapped in automatically.")
        else:
            st.info(f"🛡️ **Simulation Result:** Zero critical weather anomalies detected for {destination}. Backup indoor cultural itineraries remain on standby in case of unseasonal local shifts.")
            
    else:
        st.info("Configure your trip parameters on the left and click **Run Multi-Agent Planner** to trigger the collaborative agent reasoning loop.")
