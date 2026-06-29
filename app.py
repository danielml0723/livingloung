import streamlit as st

from pages import dashboard, rrhh, payroll

st.set_page_config(
    page_title="Living Lounge ERP",
    layout="wide"
)

st.sidebar.title("🏢 Living Lounge ERP")

page = st.sidebar.selectbox(
    "Menú",
    ["Dashboard", "RRHH", "Planillas"]
)

if page == "Dashboard":
    dashboard.render()

elif page == "RRHH":
    rrhh.render()

elif page == "Planillas":
    payroll.render()