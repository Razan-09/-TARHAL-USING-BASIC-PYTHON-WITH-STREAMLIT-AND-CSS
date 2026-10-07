import streamlit as st
from classes import TripPrefrences



# Page Configuration

st.set_page_config(
    page_title="Tarhal - Recommendations",
    layout="wide"
)


#css desgin
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&display=swap');

html, body, p, span, div, label, button, li {
    font-family: 'Manrope', sans-serif;
}

/* Background */
.stApp {
    background-color: #F3F1EA;
}

.stMainBlockContainer {
    max-width: 1200px;
    padding-top: 30px;
}

/* Hero */
.st-key-hero {
    background: linear-gradient(135deg, #194B3A, #1A5A43);
    border-radius: 36px;
    padding: 50px 40px;
    text-align: center;
    margin-bottom: 40px;
}

.st-key-hero h1 {
    color: white;
    font-size: 52px;
    font-weight: 800;
    padding: 0;
}

.st-key-hero p {
    color: #D9E3DC;
    font-size: 17px;
}


/* Trip Information */
.st-key-trip {
    background-color: white;
    border-radius: 28px;
    padding: 28px;
    margin-bottom: 40px;
    box-shadow: 0 15px 40px rgba(23, 56, 45, 0.08);
}

.st-key-trip h2 {
    color: #17382D;
    font-size: 28px;
    font-weight: 800;
}


/* Metrics */
[data-testid="stMetric"] {
    background-color: #FAF9F5;
    border: 1px solid #E4E2DA;
    border-radius: 18px;
    padding: 20px;
}

[data-testid="stMetricLabel"] {
    color: #1A5A43;
    font-weight: 700;
}

[data-testid="stMetricValue"] {
    color: #17382D;
    font-weight: 800;
}


/* Category */
.st-key-category {
    color: #17382D;
}


/* Place Cards */
[class*="st-key-place_"] {
    background-color: white;
    border-radius: 28px;
    padding: 18px;
    margin-bottom: 30px;
    box-shadow: 0 15px 40px rgba(23, 56, 45, 0.08);
}

[class*="st-key-place_"] h3 {
    color: #17382D;
    font-size: 21px;
    font-weight: 800;
    padding-top: 8px;
}


/* Images */
[data-testid="stImage"] img {
    width: 100%;
    height: 230px;
    object-fit: cover;
    border-radius: 20px;
}


/* Category title */
.category-title {
    color: #17382D;
    font-size: 34px;
    font-weight: 800;
    margin-top: 35px;
    margin-bottom: 20px;
}


/* Footer */
.footer {
    text-align: center;
    color: #1A5A43;
    font-size: 17px;
    font-weight: 600;
    padding: 30px;
}


/* Phone */
@media (max-width: 800px) {

    .st-key-hero h1 {
        font-size: 34px;
    }

    [data-testid="stImage"] img {
        height: 200px;
    }

}

</style>
""", unsafe_allow_html=True)



# Get user preferences from session state


city = st.session_state.city
budget = st.session_state.budget
travel_type = st.session_state.travel_type



# Get Recommendations based on user preferences


trip = TripPrefrences(
    city,
    budget,
    travel_type
)

recommendations = trip.check_choses()


#using containers to organize the layout of the page


with st.container(key="hero"):

    st.markdown(
        "<h1>Tarhal</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p>Places selected specially for your journey</p>",
        unsafe_allow_html=True
    )



# Your Trip header and metrics


with st.container(key="trip"):

    st.markdown(
        "<h2>Your Trip</h2>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Destination", city)

    with col2:
        st.metric("Budget", budget)

    with col3:
        st.metric("Travel Type", travel_type)


# Images


images = {

    # Riyadh
    "KAFD": "Recommendations.image/KADF.png",
    "Via Riyadh": "via.riyadh.png",
    "Diryah": "Diryah.png",
    "Six Flags": "sixflags.png",
    "Wonder graden": "wondergardn.png",
    "BLVD city": "blvd.png",
    "COOL ARENA": "coolarena.png",

    # Abha
    "Green Mountain": "greenmountain.png",
    "Al-Soudah Mountain": "soudah.png",
    "Fog Walkway": "fogwalk.png",
    "Abha Dam Lake": "abhadam.png",

    # Jeddah
    "Albalad": "albald.png",
    "Jeddah Corniche": "jeddahcou.png",
    "Fakieh Aquarium": "sea.png",

    # AlUla
    "Hegra": "alu.png",
    "Elephant rock": "ele.png",
    "AlUla oasis": "oa.png",
}


# Recommendations 


for category, places in recommendations.items():

    st.markdown(
        f'<div class="category-title">{category}</div>',
        unsafe_allow_html=True
    )

    columns = st.columns(3)

    for i, place in enumerate(places):

        if not place:
            continue

        with columns[i % 3]:

            with st.container(key=f"place_{category}_{i}"):

                # If the place has an image
                if place in images:

                    st.image(
                        images[place],
                        use_container_width=True
                    )

                    st.subheader(place)

                # If the place does not have an image
                else:

                    st.subheader(place)



# Footer


st.markdown(
    '<div class="footer">Enjoy your journey with Tarhal ✈️</div>',
    unsafe_allow_html=True
)
