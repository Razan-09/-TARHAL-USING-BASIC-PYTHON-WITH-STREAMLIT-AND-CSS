import streamlit as st

st.set_page_config(page_title="Tarhal - Explore", layout="wide")

# Load CSS
with open("Style_1.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Headers of page
with st.container(key="hero"):
    st.markdown("""
    <div class="main-title">TARHAL</div>
    <div class="subtitle">Explore. Plan. Travel.</div>
    """, unsafe_allow_html=True)

    st.title("Explore Saudi Arabia")

    st.subheader(
        "Discover beautiful cities and famous attractions "
        "before planning your trip."
    )

# The information of cities
cities = [
    {
        "name": "Riyadh",
        "image": "Images/riyadh.jpg",
        "subtitle": "The Vibrant Heart of Heritage and Modernity",
        "text": "The capital city of Riyadh thrives with life, brilliantly blending deep-rooted history with futuristic innovation. As a tourism destination, Riyadh takes you on a complete journey starting from the historic alleys of the Masmak Fortress, which tells the story of the Kingdom's foundation, through traditional heritage markets like Al-Dirah, and up to modern architectural icons such as the Kingdom Centre and Riyadh Front. Famous for its massive seasonal events, global entertainment festivals, and luxury dining scene, Riyadh is a dynamic destination that buzzes with energy all year round.",
        "places": ["Boulevard City", "KAFD", "Diriyah", "Al Masmak Palace"]
    },
    {
        "name": "Abha",
        "image": "Images/abha.jpg",
        "subtitle": "The Bride of the Clouds and Mountain Paradise",
        "text": "Perched high above the Asir mountains, Abha touches the clouds to offer visitors enchanting weather and breathtaking natural landscapes unlike anywhere else. Abha is the ultimate sanctuary for nature and crisp-air lovers, featuring lush green highlands, stunning parks like Al-Soudah, and unique traditional architecture such as the region's historic stone towers and the cultural hub of Al-Muftaha Village. If you are looking for mist, panoramic views, mountain adventures, and cable cars soaring between sky and earth, Abha is your premier destination.",
        "places": ["Green Mountain", "Al-Soudah Mountain", "Fog Walkway", "Abha Dam"]
    },
    {
        "name": "Jeddah",
        "image": "Images/jeddah.webp",
        "subtitle": "The Bride of the Red Sea and Window to History",
        "text": "Jeddah effortlessly merges ancient heritage with the mesmerizing charm of the Red Sea. The city invites you on a magical stroll through Al-Balad (Historic Jeddah)—a UNESCO World Heritage site featuring coral-stone architecture and intricate wooden Rawashin (bay windows) that whisper tales of pilgrims and merchants through the centuries. In striking contrast, Jeddah’s modern Waterfront Corniche delivers a vibrant contemporary experience complete with world-class restaurants, pristine beaches, and the world's tallest fountain, making it the ideal blend of cultural discovery and seaside relaxation.",
        "places": ["Jeddah Corniche", "Al-Balad", "Red Sea", "King Fahd Fountain"]
    },
    {
        "name": "AlUla",
        "image": "Images/alula.jpg",
        "subtitle": "An Open-Air Museum and Desert Masterpiece",
        "text": "AlUla stands as one of the world's most magnificent archaeological and natural wonders, looking like a masterpiece sculpted by time itself. It is home to Hegra (Madain Saleh), the Kingdom's first UNESCO World Heritage site, featuring monumental Nabataean tombs masterfully carved into towering sandstone cliffs. AlUla's allure extends far beyond ancient history into a stunning landscape of lush palm oases, dramatic desert canyons, and modern architectural marvels like Maraya, the world's largest mirrored building, offering visitors an ultra-luxurious and unforgettable travel experience.",
        "places": ["Hegra", "Elephant Rock", "AlUla Old Town", "Maraya"]
    },
]

#Displaying cities (right then left image alternately)
for i, city in enumerate(cities):

    with st.container(key="city_" + str(i)):

        # Even cities pictured are on the left, odd cities are on the right
        if i % 2 == 0:
            image_col, text_col = st.columns([1, 1.1], gap="large", vertical_alignment="center")
        else:
            text_col, image_col = st.columns([1.1, 1], gap="large", vertical_alignment="center")

        with image_col:
            st.image(city["image"], use_container_width=True)

        with text_col:
            st.header(city["name"])
            st.subheader(city["subtitle"])
            st.write(city["text"])

            with st.expander("Famous places in " + city["name"]):
                for place in city["places"]:
                    st.write("- " + place)



# Button
if st.button(" Start Planning Your Trip", key="plan"):

    st.session_state.can_plan = True
#switch to next page
    st.switch_page("pages/Recommendations.py")


if st.button("Logout", key="logout"):

    st.session_state.logged_in = False
    st.session_state.can_explore = False
    st.session_state.can_plan = False
    st.session_state.can_recommend = False
#return to log in page
    st.switch_page("pages/app.py")