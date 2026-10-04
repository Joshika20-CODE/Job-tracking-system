import streamlit as st

st.set_page_config(
    page_title="Job & Internship Tracker",
    page_icon="💼",
    layout="wide"
)

# Store applications
if "applications" not in st.session_state:
    st.session_state.applications = []


st.title("💼 Job & Internship Tracker")
st.write("Track your job and internship applications easily.")


# ---------------- ADD APPLICATION ----------------

st.sidebar.header("➕ Add Application")

company = st.sidebar.text_input("Company Name")
role = st.sidebar.text_input("Job / Internship Role")

application_type = st.sidebar.selectbox(
    "Type",
    ["Job", "Internship"]
)

status = st.sidebar.selectbox(
    "Status",
    ["Applied", "Interview", "Selected", "Rejected"]
)

if st.sidebar.button("Add Application"):

    if company and role:

        application = {
            "Company": company,
            "Role": role,
            "Type": application_type,
            "Status": status
        }

        st.session_state.applications.append(application)

        st.sidebar.success("Application added!")

    else:
        st.sidebar.warning("Enter company name and role.")


# ---------------- DASHBOARD ----------------

st.subheader("📊 Dashboard")

applications = st.session_state.applications

total = len(applications)

applied = sum(
    1 for app in applications
    if app["Status"] == "Applied"
)

interview = sum(
    1 for app in applications
    if app["Status"] == "Interview"
)

selected = sum(
    1 for app in applications
    if app["Status"] == "Selected"
)

rejected = sum(
    1 for app in applications
    if app["Status"] == "Rejected"
)


col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("📋 Total", total)
col2.metric("📨 Applied", applied)
col3.metric("🎤 Interview", interview)
col4.metric("🎉 Selected", selected)
col5.metric("❌ Rejected", rejected)


# ---------------- SEARCH ----------------

st.subheader("🔍 Search")

search = st.text_input("Search company or role")

# ---------------- APPLICATIONS ----------------

st.subheader("📑 My Applications")

filtered_apps = applications

if search:

    filtered_apps = [
        app for app in applications
        if search.lower() in app["Company"].lower()
        or search.lower() in app["Role"].lower()
    ]


if filtered_apps:

    for index, app in enumerate(filtered_apps):

        with st.container(border=True):

            col1, col2, col3, col4 = st.columns(4)

            col1.write(f"🏢 **{app['Company']}**")
            col2.write(f"💼 {app['Role']}")
            col3.write(f"📌 {app['Type']}")
            col4.write(f"📊 {app['Status']}")

else:

    st.info("No applications found.")


st.divider()

