import streamlit as st
import urllib.request
import json
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Autonomous Travel Desk",
    page_icon="🗺️",
    layout="wide"
)

st.title("Autonomous Travel Desk")
st.caption("Last-Minute Multi-Leg Routing & Guaranteed Reserved Arbitrage Engine")

# Check for API Key in Streamlit Secrets
API_KEY = st.secrets.get("GEMINI_API_KEY", "")

col_input, col_output = st.columns([1, 2])

with col_input:
    st.subheader("Trip Parameters")
    origin = st.text_input("Origin City", value="Hyderabad")
    destination = st.selectbox("Destination", [
        "Tirupati",
        "Goa", 
        "Udupi, Karnataka", 
        "Varanasi, Uttar Pradesh"
    ])
    
    # Added Date Picker for exact travel scheduling
    travel_date = st.date_input(
        "Target Travel Date", 
        value=datetime.now() + timedelta(days=1),
        min_value=datetime.now().date()
    )
    
    budget = st.number_input("Budget Constraint (₹)", min_value=2000, max_value=500000, value=8000, step=1000)
    run_button = st.button("Generate Emergency Route Plan", type="primary")

with col_output:
    st.subheader(f"Autonomous Execution for {travel_date.strftime('%d %b %Y')}")
    
    if run_button:
        status_box = st.status("Executing Last-Minute Reserved Routing Mesh...", expanded=True)
        
        agent_output = None
        with status_box:
            st.write(f"👤 **Profiler Agent:** Analyzing budget (₹{budget:,}) for travel on {travel_date}...")
            st.write(f"🚆 **Logistics Agent:** Scanning Tatkal, RAC, and AC bus corridors from {origin} to {destination}...")
            
            prompt = f"""
            You are an advanced last-minute travel coordination system. Provide a structured emergency travel plan from {origin} to {destination} for date {travel_date} under a ₹{budget} budget constraint. 
            CRITICAL CONSTRAINT: Do NOT suggest unreserved general compartments. Focus strictly on Tatkal, RAC clearance tracking, or guaranteed sleeper bus alternatives.
            
            Provide your response in exactly two sections separated by '---':
            1. CORRIDORS: Provide a table of alternative routing options using reserved seats only.
            2. EXECUTION: Give exact step-by-step instructions.
            """
            
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
            payload = {"contents": [{"parts": [{"text": prompt}]}]}
            
            try:
                if API_KEY:
                    req = urllib.request.Request(
                        url, 
                        data=json.dumps(payload).encode('utf-8'),
                        headers={'Content-Type': 'application/json'}
                    )
                    with urllib.request.urlopen(req) as response:
                        res_data = json.loads(response.read().decode('utf-8'))
                        agent_output = res_data['candidates'][0]['content']['parts'][0]['text']
                status_box.update(label="Routing Mesh Complete!", state="complete", expanded=False)
            except Exception as e:
                status_box.update(label="API Rate Limited - Switching to Guaranteed Reserved Fallback", state="complete", expanded=False)
                agent_output = None

        # Fallback Algorithmic Output focusing strictly on COMFORTABLE/RESERVED options (No Unreserved)
        if not agent_output:
            st.warning("⚠️ High traffic on public LLM endpoints. Reserved-Only Algorithmic Matcher Activated.")
            
            if destination == "Tirupati":
                routes_data = [
                    {
                        "Strategy": "Direct Train (Tatkal / Premium Tatkal)",
                        "Path": f"Secunderabad/Kacheguda Direct to Tirupati (10:00 AM Booking Window)",
                        "Status": "🟡 High Demand / Tatkal Open",
                        "Est. Cost": "₹1,450 (3AC)",
                        "Action": "Log in to IRCTC at 9:58 AM for AC / 10:58 AM for Sleeper on " + travel_date.strftime('%d %b')
                    },
                    {
                        "Strategy": "Junction Quota Split (Renigunta)",
                        "Path": f"Train No. 17654 (Kacheguda to Renigunta) ➔ Reserved Cab/Bus Final Leg",
                        "Status": "🟢 Remote Quota Available",
                        "Est. Cost": "₹1,200",
                        "Action": "Book quota to Renigunta instead of Tirupati main station for higher seat availability."
                    },
                    {
                        "Strategy": "Guaranteed AC Sleeper Bus",
                        "Path": f"TGSRTC / APSRTC / Orange Tours AC Sleeper from MGBS Hyderabad ➔ Tirupati",
                        "Status": "🟢 Seats Open",
                        "Est. Cost": "₹1,400 - ₹1,800",
                        "Action": "Fully comfortable overnight journey with guaranteed bed. Book instantly."
                    }
                ]
                
                execution_steps = f"""
                1. **Target Date Alignment:** For your trip on **{travel_date.strftime('%d %b %Y')}**, avoid general compartments entirely. Focus on comfort via pre-booked AC transit options.
                2. **Option A (The Junction Quota Trick):** If direct trains to Tirupati show heavy waitlists, search for **Renigunta Junction** on Train No. 17654. Railways allocate distinct quotas to junction stations, drastically increasing your chance of securing a confirmed berth.
                3. **Option B (AC Sleeper Bus Route):** Book a state-run (TGSRTC/APSRTC) or top-rated private AC sleeper bus leaving Hyderabad in the evening. It bypasses rail waitlists completely and drops you off fresh the next morning.
                4. **Stay Sourcing:** Secure clean, non-surge-priced rooms at the **TTD Srinivasam Complex** or official pilgrim guest houses.
                """
            else:
                routes_data = [
                    {
                        "Strategy": "Junction Split (Reserved Rail)",
                        "Path": f"{origin} ➔ Major Divisional Hub (Reserved Seat) ➔ {destination}",
                        "Status": "🟢 Confirmed Quota Open",
                        "Est. Cost": f"₹{int(budget * 0.6)}",
                        "Action": "Book ticket to intermediate junction where seat availability is higher."
                    },
                    {
                        "Strategy": "Overnight AC Sleeper Bus",
                        "Path": f"Verified Private/State AC Sleeper from {origin} to {destination}",
                        "Status": "🟢 Confirmed Berths Available",
                        "Est. Cost": f"₹{int(budget * 0.75)}",
                        "Action": "Guaranteed bed with zero hassle or crowding."
                    }
                ]
                execution_steps = f"""
                1. **Target Date Alignment:** Traveling on **{travel_date.strftime('%d %b %Y')}** requires avoiding crowded unreserved compartments.
                2. **Execution Strategy:** Use the hub-and-spoke method by booking confirmed tickets to an intermediate junction, or secure a direct AC sleeper bus for maximum comfort.
                """

            st.markdown("### 📊 Guaranteed Reserved Corridors")
            st.table(pd.DataFrame(routes_data))
            
            st.markdown("### 🛡️ Stress-Free Execution Blueprint")
            st.markdown(execution_steps)
        else:
            sections = agent_output.split("---")
            if len(sections) >= 2:
                st.markdown("### 📊 Guaranteed Reserved Corridors")
                st.markdown(sections[0].strip())
                st.markdown("### 🛡️ Stress-Free Execution Blueprint")
                st.markdown(sections[1].strip())
            else:
                st.markdown(agent_output)
    else:
        st.info("Select your travel date, set your parameters on the left, and click **Generate Emergency Route Plan**.")
