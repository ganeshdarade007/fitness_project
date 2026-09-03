import streamlit as st
import pandas as pd
import time

# =========================================================
# AI DIET & FITNESS PLANNER PRO (PREMIUM EDITION)
# =========================================================

st.set_page_config(
    page_title="AI Diet & Fitness Planner PRO",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------------- PREMIUM CSS ----------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.stApp {
    background: #090D16;
    color: #F3F4F6;
}

.block-container {
    max-width: 1300px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Glassmorphism Hero Section */
.hero {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.8) 100%);
    border: 1px solid rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(12px);
    border-radius: 24px;
    padding: 40px;
    margin-bottom: 30px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
    text-align: center;
}

.hero-badge {
    display: inline-block;
    background: linear-gradient(90deg, #6366F1, #8B5CF6);
    color: white;
    border-radius: 20px;
    padding: 6px 16px;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 16px;
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    background: linear-gradient(90deg, #FFFFFF, #94A3B8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
}

.hero-subtitle {
    color: #94A3B8;
    font-size: 16px;
    margin-top: 12px;
}

/* Premium Card */
.glass-card {
    background: rgba(17, 24, 39, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 28px;
    margin-bottom: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
}

/* Glass KPIs */
.kpi-card {
    background: linear-gradient(145deg, rgba(30, 41, 59, 0.6), rgba(15, 23, 42, 0.8));
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 18px;
    padding: 22px;
    text-align: center;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
}

.kpi-label {
    color: #64748B;
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}

.kpi-value {
    color: #F8FAFC;
    font-size: 32px;
    font-weight: 800;
    margin: 8px 0;
}

.kpi-note {
    color: #38BDF8;
    font-size: 13px;
    font-weight: 600;
}

/* Meal & Workout Cards */
.meal-card {
    background: rgba(30, 41, 59, 0.5);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 12px;
}

.meal-head {
    color: #38BDF8;
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.meal-food {
    color: #F8FAFC;
    font-size: 18px;
    font-weight: 700;
    margin-top: 4px;
}

.meal-meta {
    color: #94A3B8;
    font-size: 13px;
    margin-top: 6px;
}

.workout-card {
    background: rgba(30, 41, 59, 0.5);
    border-left: 4px solid #6366F1;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 12px;
}

.workout-head {
    color: #F8FAFC;
    font-size: 16px;
    font-weight: 700;
}

.workout-text {
    color: #94A3B8;
    font-size: 13px;
    margin-top: 4px;
}

/* Buttons */
.stButton > button, div[data-testid="stDownloadButton"] > button {
    background: linear-gradient(90deg, #6366F1, #8B5CF6) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    height: 52px !important;
    box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4) !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover, div[data-testid="stDownloadButton"] > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(99, 102, 241, 0.6) !important;
}

div[data-baseweb="input"] > div, div[data-baseweb="select"] > div {
    background-color: rgba(15, 23, 42, 0.8) !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 10px !important;
    color: white !important;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ------------------------- Dataset ------------------------

@st.cache_data
def load_data():
    try:
        data = pd.read_csv("diet_dataset.csv")
        required = ["Food_Item", "Calories", "Protein", "Category", "Goal"]
        if all(col in data.columns for col in required):
            return data
    except Exception:
        pass

    fallback = {
        "Food_Item": [
            "Eggs (3 whole)", "Oatmeal with Milk", "Poha (1 plate)", "Upma (1 plate)",
            "Chicken Breast (200g)", "Dal Tadka & Rice", "Paneer Bhurji & 2 Roti", "Mutton Curry & 2 Roti",
            "Mixed Green Salad", "Almonds & Walnuts", "Sprouted Moong Chaat", "Protein Shake",
            "Grilled Fish", "Khichdi & Ghee", "Paneer Tikka & Paratha", "Chicken Biryani"
        ],
        "Calories": [210, 250, 180, 220, 330, 450, 520, 600, 150, 200, 180, 300, 280, 400, 550, 650],
        "Protein": [18, 10, 5, 6, 60, 18, 30, 35, 4, 6, 12, 25, 35, 15, 20, 30],
        "Category": ["Breakfast", "Breakfast", "Breakfast", "Breakfast", "Lunch", "Lunch", "Lunch", "Lunch", "Snack", "Snack", "Snack", "Snack", "Dinner", "Dinner", "Dinner", "Dinner"],
        "Goal": ["Weight Gain", "Weight Loss", "Weight Loss", "Weight Loss", "Weight Loss", "Weight Loss", "Weight Gain", "Weight Gain", "Weight Loss", "Weight Gain", "Weight Loss", "Weight Gain", "Weight Loss", "Weight Loss", "Weight Gain", "Weight Gain"]
    }
    return pd.DataFrame(fallback)

df = load_data()

# Session State Initialization
if "step" not in st.session_state:
    st.session_state.step = "input"

# ------------------------- HEADER -------------------------

st.markdown("""
<div class="hero">
    <div class="hero-badge">AI Health Engine</div>
    <div class="hero-title">AI Diet & Fitness Planner PRO</div>
    <div class="hero-subtitle">
        Next-generation metabolic intelligence & customized nutrition planning.
    </div>
</div>
""", unsafe_allow_html=True)

# ------------------------- STEP 1: SHOW (DETAILS INPUT) -------------------------

if st.session_state.step == "input":
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 📋 Enter Your Profile Details")
    st.caption("Provide your metrics below to compute your personalized health protocol.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        user_name = st.text_input("Full Name", "Alex")
        age = st.number_input("Age (Years)", min_value=15, max_value=85, value=23, step=1)
        gender = st.selectbox("Gender", ["Male", "Female"])
        weight = st.number_input("Weight (kg)", min_value=35.0, max_value=180.0, value=68.5, step=0.5)

    with col2:
        height = st.number_input("Height (cm)", min_value=110.0, max_value=230.0, value=172.0, step=0.5)
        goal = st.selectbox("Fitness Goal", ["Weight Loss", "Weight Gain"])
        activity = st.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Moderately Active", "Highly Active"])

    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🚀 GENERATE PERSONALIZED PLAN", use_container_width=True):
        st.session_state.user_data = {
            "name": user_name, "age": age, "gender": gender,
            "weight": weight, "height": height, "goal": goal, "activity": activity
        }
        st.session_state.step = "process"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------- STEP 2: PROCESS (LOADING) -------------------------

elif st.session_state.step == "process":
    
    st.markdown('<div class="glass-card" style="text-align: center; padding: 60px;">', unsafe_allow_html=True)
    
    with st.spinner("⚡ Analyzing metabolic profile and building optimal plan..."):
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.015)
            progress_bar.progress(i + 1)
            
    st.session_state.step = "result"
    st.rerun()

# ------------------------- STEP 3: RESULT (DASHBOARD) -------------------------

elif st.session_state.step == "result":

    data = st.session_state.user_data

    # Calculations
    height_m = data["height"] / 100
    bmi = data["weight"] / (height_m ** 2)

    bmi_status = "Underweight" if bmi < 18.5 else ("Healthy range" if bmi < 25 else ("Overweight" if bmi < 30 else "High BMI"))

    if data["gender"] == "Male":
        bmr = (10 * data["weight"]) + (6.25 * data["height"]) - (5 * data["age"]) + 5
    else:
        bmr = (10 * data["weight"]) + (6.25 * data["height"]) - (5 * data["age"]) - 161

    factors = {"Sedentary": 1.20, "Lightly Active": 1.375, "Moderately Active": 1.55, "Highly Active": 1.725}
    tdee = bmr * factors[data["activity"]]

    target = tdee - 450 if data["goal"] == "Weight Loss" else tdee + 500
    target = max(target, 1200)

    # Top Action Bar
    top_col1, top_col2 = st.columns([0.8, 0.2])
    with top_col1:
        st.markdown(f"## Welcome back, {data['name']} 👋")
        st.caption("Here is your data-driven health and metabolic evaluation.")
    with top_col2:
        if st.button("🔄 Reset Plan", use_container_width=True):
            st.session_state.step = "input"
            st.rerun()

    # Metric Cards
    c1, c2, c3, c4 = st.columns(4)
    kpis = [
        ("BMI Status", f"{bmi:.1f}", bmi_status),
        ("BMR Rate", f"{int(bmr)}", "kcal / day"),
        ("TDEE Est.", f"{int(tdee)}", "maintenance"),
        ("Target Intake", f"{int(target)}", data["goal"])
    ]

    for col, (label, value, note) in zip([c1, c2, c3, c4], kpis):
        with col:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-label">{label}</div>
                <div class="kpi-value">{value}</div>
                <div class="kpi-note">{note}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Main Grid (Diet & Workout)
    left, right = st.columns([1.1, 0.9], gap="large")

    meal_html_cards = ""
    chart_rows = []

    with left:
        st.markdown("### 🥗 Tailored Nutrition Plan")
        filtered = df[df["Goal"].astype(str).str.strip() == data["goal"]]
        meal_slots = ["Breakfast", "Lunch", "Snack", "Dinner"]

        for meal in meal_slots:
            records = filtered[filtered["Category"].astype(str).str.strip() == meal]
            if not records.empty:
                item = records.sort_values("Protein", ascending=False).iloc[0]
                food, calories, protein = str(item["Food_Item"]), float(item["Calories"]), float(item["Protein"])
                chart_rows.append({"Meal": meal, "Calories": calories})

                card_content = f"""
                <div class="meal-card" style="background: rgba(30, 41, 59, 0.5); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 14px; padding: 18px; margin-bottom: 12px;">
                    <div style="color: #38BDF8; font-size: 12px; font-weight: 800; text-transform: uppercase;">{meal}</div>
                    <div style="color: #F8FAFC; font-size: 18px; font-weight: 700; margin-top: 4px;">{food}</div>
                    <div style="color: #94A3B8; font-size: 13px; margin-top: 6px;">🔥 {int(calories)} kcal &nbsp;•&nbsp; 💪 {int(protein)}g Protein</div>
                </div>
                """
                meal_html_cards += card_content
                st.markdown(card_content, unsafe_allow_html=True)

        if chart_rows:
            st.markdown("#### 📊 Calorie Distribution")
            chart_df = pd.DataFrame(chart_rows).set_index("Meal")
            st.bar_chart(chart_df["Calories"], height=200)

    workout_html_cards = ""
    with right:
        st.markdown("### 🏋️ Recommended Workout Routine")
        workouts = [
            ("CARDIO FOCUS", "25–30 mins of brisk walking or HIIT.") if data["goal"] == "Weight Loss" else ("STRENGTH FOCUS", "Focus on heavy compound movements."),
            ("RESISTANCE", "Full-body strength training 3x/week.") if data["goal"] == "Weight Loss" else ("HYPERTROPHY", "3-4 sets with 8-12 reps per exercise."),
            ("VOLUME", "3 sets of 10-15 controlled reps.") if data["goal"] == "Weight Loss" else ("PROGRESSIVE OVERLOAD", "Increase weight/reps progressively."),
            ("RECOVERY", "Ensure 7-8 hours of sound sleep and hydration.")
        ]

        for title, description in workouts:
            w_card = f"""
            <div style="background: rgba(30, 41, 59, 0.5); border-left: 4px solid #6366F1; border-radius: 12px; padding: 16px; margin-bottom: 12px;">
                <div style="color: #F8FAFC; font-size: 16px; font-weight: 700;">{title}</div>
                <div style="color: #94A3B8; font-size: 13px; margin-top: 4px;">{description}</div>
            </div>
            """
            workout_html_cards += w_card
            st.markdown(w_card, unsafe_allow_html=True)

    # ---------------- GENERATE DOWNLOADABLE PREMIUM HTML REPORT ----------------
    
    report_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <title>AI Fitness Report - {data['name']}</title>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    body {{
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #090D16;
        color: #F8FAFC;
        padding: 40px;
        max-width: 1000px;
        margin: auto;
    }}
    .hero {{
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.95));
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        margin-bottom: 25px;
    }}
    .kpi-grid {{
        display: flex;
        gap: 15px;
        margin-bottom: 30px;
    }}
    .kpi-card {{
        flex: 1;
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 14px;
        padding: 16px;
        text-align: center;
    }}
    .kpi-label {{ color: #64748B; font-size: 11px; font-weight: 700; text-transform: uppercase; }}
    .kpi-value {{ color: #F8FAFC; font-size: 24px; font-weight: 800; margin: 6px 0; }}
    .kpi-note {{ color: #38BDF8; font-size: 12px; font-weight: 600; }}
    .flex-grid {{ display: flex; gap: 30px; }}
    .col {{ flex: 1; }}
    h3 {{ border-left: 4px solid #6366F1; padding-left: 10px; color: #FFF; }}
    </style>
    </head>
    <body>

    <div class="hero">
        <div style="background: linear-gradient(90deg, #6366F1, #8B5CF6); color: white; display: inline-block; padding: 4px 14px; border-radius: 12px; font-size: 11px; font-weight: 800;">AI HEALTH ENGINE REPORT</div>
        <h1 style="margin: 10px 0 0 0; font-size: 32px;">AI Diet & Fitness Planner PRO</h1>
        <p style="color: #94A3B8; margin-top: 6px;">Personalized Client Report for <b>{data['name']}</b> ({data['age']} Yrs, {data['gender']})</p>
    </div>

    <div class="kpi-grid">
        <div class="kpi-card"><div class="kpi-label">BMI Status</div><div class="kpi-value">{bmi:.1f}</div><div class="kpi-note">{bmi_status}</div></div>
        <div class="kpi-card"><div class="kpi-label">BMR Rate</div><div class="kpi-value">{int(bmr)}</div><div class="kpi-note">kcal / day</div></div>
        <div class="kpi-card"><div class="kpi-label">TDEE Est.</div><div class="kpi-value">{int(tdee)}</div><div class="kpi-note">maintenance</div></div>
        <div class="kpi-card"><div class="kpi-label">Target Intake</div><div class="kpi-value">{int(target)}</div><div class="kpi-note">{data['goal']}</div></div>
    </div>

    <div class="flex-grid">
        <div class="col">
            <h3>🥗 Nutrition Plan</h3>
            {meal_html_cards}
        </div>
        <div class="col">
            <h3>🏋️ Training Protocol</h3>
            {workout_html_cards}
        </div>
    </div>

    <div style="text-align: center; margin-top: 40px; color: #64748B; font-size: 12px;">
        Generated by AI Diet & Fitness Planner PRO System
    </div>

    </body>
    </html>
    """

    st.markdown("<br>", unsafe_allow_html=True)
    st.download_button(
        "⬇️ DOWNLOAD PREMIUM UI REPORT (.HTML)",
        data=report_html,
        file_name=f"{data['name']}_AI_Fitness_Report.html",
        mime="text/html",
        use_container_width=True
    )

# ------------------------- FOOTER --------------------------

st.markdown("""
<div style="text-align: center; color: #64748B; font-size: 12px; margin-top: 50px;">
    AI Diet & Fitness Planner PRO • High Performance Health Analytics System
</div>
""", unsafe_allow_html=True)