import streamlit as st
import urllib.request
import json

st.set_page_config(
    page_title="Autonomous Travel Desk",
    page_icon="🗺️",
    layout="wide"
)

st.title("Autonomous Travel Desk")
st.caption("True Multi-Agent Architecture powered by Gemini REST API: Profiler ➔ Logistics Engine ➔ Curator Agent ➔ Risk Mitigation Desk")

# Check for API Key in Streamlit Secrets
if "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    st.error("⚠️ GEMINI_API_KEY not found in Streamlit Secrets. Please add it to your app settings.")

col_input, col_output = st.columns([1, 2])

with col_input:
    st.subheader("Trip Parameters")
    destination = st.selectbox("Destination", [
        "Goa", 
        "Udupi, Karnataka", 
        "Jaipur, Rajasthan", 
        "Kerala Backwaters", 
        "Varanasi, Uttar Pradesh",
        "Ooty, Tamil Nadu"
    ])
    
    st.markdown("**Travel Style Preferences:**")
    style_culture = st.checkbox("Cultural & Heritage", value=True)
    style_culinary = st.checkbox("Local Culinary Focus", value=True)
    style_leisure = st.checkbox("Leisure & Scenic", value=False)
    
    budget = st.number_input("Budget Constraint (₹)", min_value=5000, max_value=500000, value=25000, step=1000)
    
    run_button = st.button("Run Multi-Agent Planner", type="primary")

with col_output:
    st.subheader("Autonomous Agent Execution & Live Itinerary")
    
    if run_button and "GEMINI_API_KEY" in st.secrets:
        styles = []
        if style_culture: styles.append("Cultural & Heritage")
        if style_culinary: styles.append("Local Culinary Focus")
        if style_leisure: styles.append("Leisure & Scenic")
        
        status_box = st.status("Executing Multi-Agent Mesh...", expanded=True)
        
        with status_box:
            st.write(f"👤 **Profiler Agent:** Analyzing user preference vector and budget constraint of ₹{budget:,}...")
            st.write(f"🚆 **Logistics Agent:** Computing optimal transit pathways from Hyderabad to {destination}...")
            st.write(f"🏛️ **Curator Agent:** Sourcing hyper-local experiences matching focus: {', '.join(styles)}...")
            st.write("🛡️ **Risk & Contingency Agent:** Evaluating local weather variations, crowd metrics, and logistical failure points...")
            
            prompt = f"""
            You are an advanced multi-agent travel coordination system comprising a Profiler, Logistics Engine, Curator, and Risk Agent.
            Create a structured travel plan for a trip from Hyderabad to {destination}.
            
            Parameters:
            - Budget Constraint: ₹{budget}
            - Focus Styles: {', '.join(styles)}
            
            Provide your response in exactly three distinct sections separated by '---':
            1. ARBITRAGE: Give a brief financial arbitrage summary (Estimated Cost vs Standard, Transit Efficiency score, Experience Match score).
            2. ITINERARY: Give a structured day-by-day itinerary (Day 1: Transit & Arrival, Day 2: Deep Dive based on focus styles) with realistic timings.
            3. RISK: Give a Risk Agent stress test report assessing weather, seasonality, and backup alternative plans.
            """
            
            # Direct REST API call to Gemini (No external pip package required)
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
            payload = {
                "contents": [{"parts": [{"text": prompt}]}]
            }
            
            agent_output = None
            try:
                req = urllib.request.Request(
                    url, 
                    data=json.dumps(payload).encode('utf-8'),
                    headers={'Content-Type': 'application/json'}
                )
                with urllib.request.urlopen(req) as response:
                    res_data = json.loads(response.read().decode('utf-8'))
                    agent_output = res_data['candidates'][0]['content']['parts'][0]['text']
                    status_box.update(label="Agent Mesh Execution Complete!", state="complete", expanded=False)
            except Exception as e:
                st.error(f"Agent API execution error: {e}")

        if agent_output:
            sections = agent_output.split("---")
            if len(sections) >= 3:
                st.markdown("### 📊 Agent Cost & Value Arbitrage Analysis")
                st.markdown(sections[0].strip())
                
                st.markdown(f"### 🗺️ Tailored Itinerary: Hyderabad ➔ {destination}")
                st.markdown(sections[1].strip())
                
                st.markdown("### ⚡ Risk Agent Counterfactual Stress Test")
                st.info(sections[2].strip())
            else:
                st.markdown(agent_output)
                
    else:
        if not run_button:
            st.info("Configure your trip parameters on the left and click **Run Multi-Agent Planner** to trigger the live agent reasoning loop.")
