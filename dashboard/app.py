import streamlit as st
import pandas as pd
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="OLA Ride Insights Dashboard",
    layout="wide"
)

st.title("🚕 OLA Ride Insights Dashboard")

# ---------------- LOAD EXCEL DATA ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "OLA_DataSet.xlsx")

st.write("📂 Loading file:", DATA_PATH)

# Read Excel (simple, single call – the one that worked)
df = pd.read_excel(DATA_PATH)

# ---------------- BASIC CLEANING ----------------
df.columns = df.columns.str.strip()

for col in ["Payment_Method", "Booking_Status", "Vehicle_Type"]:
    if col in df.columns:
        df[col] = df[col].fillna("Unknown").astype(str).str.strip()

df["Booking_Value"] = pd.to_numeric(df["Booking_Value"], errors="coerce").fillna(0)
df["Customer_Rating"] = pd.to_numeric(df["Customer_Rating"], errors="coerce")
df["Driver_Ratings"] = pd.to_numeric(df["Driver_Ratings"], errors="coerce")

st.success(f"✅ Loaded {len(df)} rows")

# ---------------- SIDEBAR NAV ----------------
st.sidebar.markdown("## 🟡 OLA")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["Overall", "Vehicle Type", "Revenue", "Cancellation", "Ratings"]
)

# ---------------- OVERALL ----------------
if page == "Overall":
    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Bookings", len(df))
    c2.metric("Total Revenue", f"₹ {df['Booking_Value'].sum():,.0f}")
    c3.metric(
        "Cancelled Rides",
        int(df["is_cancelled"].sum()) if "is_cancelled" in df.columns else 0
    )
    c4.metric(
        "Avg Customer Rating",
        round(df["Customer_Rating"].mean(), 2)
    )

    st.divider()

    col1, col2 = st.columns(2)

    if "hour" in df.columns:
        col1.subheader("Bookings by Hour")
        col1.bar_chart(df.groupby("hour")["Booking_ID"].count())

    if "day" in df.columns:
        col2.subheader("Bookings by Day")
        col2.bar_chart(df.groupby("day")["Booking_ID"].count())

# ---------------- VEHICLE TYPE ----------------
elif page == "Vehicle Type":
    st.subheader("🚗 Vehicle Type Analysis")

    vehicle_summary = (
        df.groupby("Vehicle_Type")
        .agg(
            Total_Booking_Value=("Booking_Value", "sum"),
            Avg_Booking_Value=("Booking_Value", "mean"),
            Avg_Distance=("Ride_Distance", "mean"),
            Total_Distance=("Ride_Distance", "sum")
        )
        .reset_index()
    )

    st.dataframe(vehicle_summary, use_container_width=True)

# ---------------- REVENUE ----------------
elif page == "Revenue":
    st.subheader("💰 Revenue Analysis")

    col1, col2 = st.columns(2)

    col1.subheader("Revenue by Payment Method")
    col1.bar_chart(df.groupby("Payment_Method")["Booking_Value"].sum())

    col2.subheader("Revenue by Vehicle Type")
    col2.bar_chart(df.groupby("Vehicle_Type")["Booking_Value"].sum())

# ---------------- CANCELLATION ----------------
elif page == "Cancellation":
    st.subheader("❌ Cancellation Analysis")

    col1, col2 = st.columns(2)

    if "Canceled_Rides_by_Customer" in df.columns:
        col1.subheader("Cancelled by Customer")
        col1.bar_chart(df["Canceled_Rides_by_Customer"].value_counts())

    if "Canceled_Rides_by_Driver" in df.columns:
        col2.subheader("Cancelled by Driver")
        col2.bar_chart(df["Canceled_Rides_by_Driver"].value_counts())

# ---------------- RATINGS ----------------
elif page == "Ratings":
    st.subheader("⭐ Ratings Analysis")

    col1, col2 = st.columns(2)

    col1.subheader("Customer Ratings")
    col1.bar_chart(df["Customer_Rating"].value_counts().sort_index())

    col2.subheader("Driver Ratings")
    col2.bar_chart(df["Driver_Ratings"].value_counts().sort_index())

# ---------------- RAW DATA ----------------
with st.expander("📄 View Raw Data"):
    st.dataframe(df)
