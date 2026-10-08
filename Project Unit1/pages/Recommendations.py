import streamlit as st
from classes import TripPrefrences


# Page Configuration

st.set_page_config(
    page_title="Tarhal - Recommendations",
    layout="wide"
)


# Load CSS from c.css (must be in the same folder as this file)

def load_css(file_name):
    with open(file_name, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css("c.css")


def norm(text):
    """lowercase + remove spaces so 'Cafés' == 'cafés'"""
    return str(text).lower().strip()


# Hero

with st.container(key="hero"):
    st.markdown(
        '<div class="eyebrow">Your journey, thoughtfully planned</div>'
        '<h1>Where will Saudi<br>take you next?</h1>'
        '<p class="sub">Tell us how you like to travel, and we’ll match you '
        'with places and experiences made for your moment.</p>',
        unsafe_allow_html=True
    )


# User choices

with st.container(key="choices"):

    city = st.radio(
        "Choose your city",
        ["Abha", "Riyadh", "Jeddah", "AlUla"],
        index=None,
        horizontal=True,
        key="city"
    )

    st.markdown("<hr>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 1.1, 1.6])

    with c1:
        budget = st.pills(
            "Your budget",
            ["Low", "Medium", "High"]
        )

    with c2:
        travel_type = st.pills(
            "Traveling with",
            ["Solo", "Friends", "Family"]
        )

    with c3:
        experience = st.pills(
            "Experience type",
            ["Tourism", "Entertainment", "Restaurants", "Cafés"]
        )

    with st.container(key="cta"):
        discover = st.button("Discover My Plan →")


# Wait until the user chooses everything and presses the button

if discover:
    st.session_state["show_results"] = True

if city is None or budget is None or travel_type is None:
    st.info("Choose your city, budget and travel type to see your recommendations.")
    st.stop()

if not st.session_state.get("show_results"):
    st.info("Press “Discover My Plan” to see your recommendations.")
    st.stop()


# Get Recommendations based on user choices

trip = TripPrefrences(
    city,
    budget,
    travel_type
)

recommendations = trip.check_choses()

# Filter by the chosen experience type (Tourism / Cafés / ...)
if experience and recommendations:
    wanted = norm(experience)
    filtered = {
        cat: places for cat, places in recommendations.items()
        if norm(cat) and (wanted in norm(cat) or norm(cat) in wanted)
    }
    if not filtered:
        st.warning(
            f"No '{experience}' category found for these choices. "
            f"Available categories: {', '.join(map(str, recommendations.keys()))}"
        )
        st.stop()
    recommendations = filtered


# Your Trip header and metrics

with st.container(key="trip"):

    st.markdown("<h2>Your Trip</h2>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Destination", city)

    with col2:
        st.metric("Budget", budget)

    with col3:
        st.metric("Travel Type", travel_type)

    with col4:
        st.metric("Experience", experience or "All")


# Images (keyed by city name; you can also add a specific place name)

images = {
    "Riyadh": "images/Riyadh.jpg",
    "Jeddah": "images/Jeddah.jpg",
    "Abha": "images/Abha.jpg",
    "AlUla": "images/AlUla.jpg",
}

# False = the city image shows once as a banner.
# True  = the city image also shows on every place card.
SHOW_CITY_IMAGE_ON_CARDS = False


def show_image(path):
    """Show the image only if the file really exists (no errors if missing)."""
    try:
        st.image(path, use_container_width=True)
    except Exception:
        pass


# City banner (one image for the chosen city)

if city in images:
    with st.container(key="banner"):
        show_image(images[city])



# Show Recommendations

if not recommendations:
    st.warning("No recommendations found for these choices.")

for category, places in recommendations.items():

    st.markdown(
        f'<div class="category-title">{category}</div>',
        unsafe_allow_html=True
    )

    columns = st.columns(3)

    for i, place in enumerate(places):

        # Skip empty names
        if not place:
            continue

        with columns[i % 3]:

            with st.container(key=f"place_{category}_{i}"):

                # A specific place image wins, otherwise the city image (optional)
                place_img = images.get(place) or (
                    images.get(city) if SHOW_CITY_IMAGE_ON_CARDS else None
                )
                if place_img:
                    show_image(place_img)

                st.subheader(place.strip())
                st.caption(f"{city} · {category}")


# Footer

st.markdown(
    '<div class="footer">Enjoy your journey with Tarhal </div>',
    unsafe_allow_html=True
)
