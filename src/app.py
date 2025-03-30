```python
import streamlit as st
from utils import get_travel_recommendations, get_travel_tips

def main():
    st.set_page_config(page_title="🌍 AI Travel Planner", layout="wide")
    
    # Custom CSS for styling
    st.markdown("""
        <style>
            .title { font-size: 2.5rem; font-weight: bold; color: #1abc9c; text-align: center; }
            .subtitle { font-size: 1.3rem; text-align: center; color: #3498db; }
            .stButton>button { background-color: #e74c3c !important; color: white !important; font-size: 1.2rem; }
        </style>
    """, unsafe_allow_html=True)
    
    # Display Title and Subtitle
    st.markdown("<div class='title'>✈️ AI-Powered Travel Planner</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Plan smarter. Travel better. Get personalized routes and tips powered by AI.</div>", unsafe_allow_html=True)
    
    # User input form for travel planning
    with st.form("travel_form"):
        col1, col2 = st.columns(2)
        with col1:
            source = st.text_input("🌍 **Enter Source Location**")
        with col2:
            destination = st.text_input("📍 **Enter Destination Location**")
        submitted = st.form_submit_button("🔍 Get Travel Recommendations")
    
    # Handle form submission
    if submitted:
        if source and destination:
            with st.spinner("✨ Fetching smart travel suggestions..."):
                travel_info = get_travel_recommendations(source, destination)
                travel_tips = get_travel_tips(destination)
            
                # Display AI-generated travel recommendations
                st.markdown("### 🗺️ Recommended Travel Options")
                st.success(travel_info)
            
                # Display AI-generated travel tips
                st.markdown("### 💡 Travel Tips")
                st.warning(travel_tips)
        else:
            st.error("🚨 Please enter both source and destination to continue.")

# Run the Streamlit application
if __name__ == "__main__":
    main()
```
