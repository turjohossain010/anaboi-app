import streamlit as st
import openai
import os

# Anaboi Branding & UI
st.set_page_config(page_title="Anaboi - AI Content Scout", page_icon="⚽", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #050a30; color: #ffffff; }
    .stHeader { color: #ffcc00; }
    .stButton>button { background-color: #e63946; color: white; border-radius: 10px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚽ ANABOI: The Ultimate AI Content Scout")
st.write("Professional Football Fan Persona Activated 🚀")

# API Setup
api_key = st.text_input("আপনার OpenAI API Key দিন (এটি ছাড়া AI কাজ করবে না):", type="password")

if api_key:
    openai.api_key = api_key

    # Layout: Two Columns
    col1, col2 = st.columns(2)

    with col1:
        st.header("📤 ড্র্যাগ এন্ড ড্রপ ভিডিও")
        uploaded_file = st.file_uploader("আপনার Shorts বা Reel আপলোড করুন", type=["mp4", "mov"])
        
        if uploaded_file:
            st.video(uploaded_file)
            if st.button("এনালাইসিস শুরু করো"):
                with st.spinner('Anaboi ফুটবল পিচে এনালাইসিস করছে...'):
                    # AI Analysis Logic
                    # (এখানে আমরা AI কে প্রম্পট দিচ্ছি আপনার দেওয়া সব শর্ত অনুযায়ী)
                    prompt = f"You are a professional football fan and social media analyst. Analyze the provided video content. Give me subtitles, suggestions for hooks to keep viewers engaged, 3 SEO titles for YouTube, 3 for Instagram, and 6 trending hashtags for each. Use football terminology and be high-energy!"
                    
                    # Simulated output for preview (Integration with OpenAI starts here)
                    st.success("এনালাইসিস রিপোর্ট তৈরি!")
                    st.markdown("""
                    ### 🏟️ Anaboi's Scouting Report:
                    - **ভিডিওর বিষয়:** [AI এনালাইসিস অনুযায়ী এখানে তথ্য আসবে]
                    - **সাবটাইটেল টিপস:** টেক্সট ওভারলে আরও বোল্ড হতে হবে।
                    - **হুক আইডিয়া:** ভিডিওর প্রথম ২ সেকেন্ডে একটি বিতর্কিত ফুটবল প্রশ্ন যোগ করুন।
                    - **YouTube SEO:** 
                        - টাইটেল: সেরা ফুটবল স্কিল ২০২৪! ⚽
                        - হ্যাশট্যাগ: #FootballShorts #AnaboiAnalysis
                    - **Instagram SEO:**
                        - টাইটেল: এই গোলটি কি সেরা? 🔥
                        - হ্যাশট্যাগ: #ReelsIndia #FootballStrategy
                    """)

    with col2:
        st.header("📊 চ্যানেল ও কম্পিটিটর এনালাইসিস")
        channel_input = st.text_input("ইউটিউব বা ইনস্টাগ্রাম চ্যানেলের নাম/লিঙ্ক দিন")
        
        if st.button("চ্যানেল এনালাইসিস করো"):
            st.info(f"{channel_input} চ্যানেলের ডাটা স্ক্র্যাপ করা হচ্ছে...")
            st.write("✅ **সেরা সময়:** এই চ্যানেল সাধারণত রাত ৮টার সময় বেশি রিচ পায়।")
            st.write("✅ **ট্রিকস:** এরা ব্যাকগ্রাউন্ডে ট্রেন্ডিং অডিও এবং ফাস্ট কাটিং এডিট ব্যবহার করে।")
            st.write("✅ **হুক:** এরা ভিডিও শুরু করে সরাসরি একটি বড় শট দিয়ে যা অডিয়েন্সকে ধরে রাখে।")

else:
    st.warning("সফটওয়্যারটি চালু করতে আপনার একটি OpenAI API Key প্রয়োজন।")