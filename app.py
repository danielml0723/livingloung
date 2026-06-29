import streamlit as st

st.set_page_config(
    page_title="Living Lounge ERP",
    layout="wide"
)

st.sidebar.title("🏢 ERP Living Lounge")

page = st.sidebar.selectbox(
    "Menú",
    ["Dashboard", "RRHH", "Planillas"]
)

# DASHBOARD
if page == "Dashboard":
    st.title("📊 Dashboard")
    st.metric("Empleados", 12)
    st.metric("Planillas", 2)

# RRHH
elif page == "RRHH":
    st.title("👥 RRHH")
    st.write("Lista de empleados")

# PLANILLAS
elif page == "Planillas":
    st.title("💰 Planillas")
    st.write("Cálculo de nómina")
