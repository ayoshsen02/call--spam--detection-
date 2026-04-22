import streamlit as st
import pickle
import numpy as np

# Load model and vectorizer
# Ensure these are in the same directory as this app.py
try:
    model = pickle.load(open('model.pkl', 'rb'))
    vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
except Exception as e:
    st.error("Model files not found! Ensure model.pkl and vectorizer.pkl are in the folder.")
    st.stop()

# --- MODERN DARK THEME & CSS ---
st.markdown("""
    <style>
    /* Global Background */
    .stApp { 
        background-color: #0e1117; 
        color: white; 
    }
    /* Centering and Animation */
    .centered { display: flex; justify-content: center; flex-direction: column; align-items: center; text-align: center; }
    @keyframes fadeIn { from {opacity: 0;} to {opacity:1;} }
    .fade-in { animation: fadeIn 1.2s; }
    
    /* Input Fields Style */
    input, textarea { 
        background-color: #262730 !important; 
        color: white !important; 
        border: 1px solid #444 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation logic
if 'page' not in st.session_state: st.session_state.page = 'home'

# --- PAGE 1: HOMEPAGE ---
if st.session_state.page == 'home':
    st.markdown('<div class="centered fade-in">', unsafe_allow_html=True)
    st.title("📞 Scam Call Detection AI")
    st.image("https://images.unsplash.com/photo-1563986768609-322da13575f3?w=800")
    st.write("### Advanced NLP protection against malicious fraud.")
    if st.button("Click to Login 🚀"):
        st.session_state.page = 'login'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 2: LOGIN ---
elif st.session_state.page == 'login':
    st.markdown('<div class="centered fade-in">', unsafe_allow_html=True)
    st.title("🔒 Secure Access")
    phone = st.text_input("Enter your Phone Number to continue:")
    if st.button("Authenticate"):
        if len(phone) >= 10:
            st.session_state.page = 'main'
            st.rerun()
        else: st.error("Please enter a valid 10-digit number.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 3: MAIN ANALYSIS ---
elif st.session_state.page == 'main':
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("🛡️ Call Analysis Lab")
    
    user_input = st.text_area("Paste call transcript here:")
    
    if st.button("Analyze Pattern"):
        # NLP Logic
        data = vectorizer.transform([user_input])
        prediction = model.predict(data)
        
        if prediction[0] == 1:
            st.error("🚨 DANGER: Scam pattern detected!")
        else:
            st.success("✅ SAFE: Conversation appears genuine.")
            
    if st.button("Logout"):
        st.session_state.page = 'home'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)