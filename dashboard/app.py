#streamlit run dashboard/app.py
import streamlit as st
import requests

# ----------------------------------
# Page Configuration
# ----------------------------------

st.set_page_config(
    page_title="Job Aggregator",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Job Aggregator")
st.write("Search jobs collected from We Work Remotely")

# ----------------------------------
# Load Locations
# ----------------------------------

try:

    location_response = requests.get(
        "http://127.0.0.1:8000/locations"
    )

    locations = ["All"] + location_response.json()

except Exception:

    st.error(
        "Could not load locations.\n"
        "Make sure FastAPI is running."
    )

    st.stop()

# ----------------------------------
# Load Companies
# ----------------------------------

try:

    company_response = requests.get(
        "http://127.0.0.1:8000/companies"
    )

    companies = ["All"] + company_response.json()

except Exception:

    st.error(
        "Could not load companies.\n"
        "Make sure FastAPI is running."
    )

    st.stop()

# ----------------------------------
# Search Form
# ----------------------------------

with st.form("search_form"):

    keyword = st.text_input(
        "Keyword",
        placeholder="Python, Manager, Data Engineer..."
    )

    selected_location = st.selectbox(
        "Location",
        locations
    )

    selected_company = st.selectbox(
        "Company",
        companies
    )

    page = st.number_input(
        "Page Number",
        min_value=1,
        value=1,
        step=1
    )

    search_clicked = st.form_submit_button(
        "🔍 Search"
    )

# ----------------------------------
# Search Logic
# ----------------------------------

if search_clicked:

    try:

        url = (
            "http://127.0.0.1:8000/search"
            f"?keyword={keyword}"
            f"&location={selected_location}"
            f"&company={selected_company}"
            f"&page={page}"
        )

        response = requests.get(url)

        data = response.json()

        if data:

            st.success(
                f"Found {len(data)} Jobs"
            )

            for job in data:

                st.divider()

                st.subheader(
                    job["title"]
                )

                st.write(
                    f"🏢 Company: {job['company']}"
                )

                st.write(
                    f"📍 Location: {job['location']}"
                )

                st.write(
                    f"🌐 Source: {job['source']}"
                )

                st.markdown(
                    f"🔗 [Apply Here]({job['job_url']})"
                )

        else:

            st.warning(
                "No jobs found."
            )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )