This is the working link 
https://ola-dashboard-ojas.streamlit.app/

---

```md
# 🚕 OLA Ride Insights Dashboard  

> 📊 **An interactive analytics dashboard built with Streamlit to explore, analyze, and visualize OLA ride data in real time.**  
> Designed with a **Power BI–style UI** and built using **Python & Pandas**.

---

## 🌟 Project Overview

The **OLA Ride Insights Dashboard** provides deep insights into ride bookings, revenue, cancellations, vehicle usage, and customer/driver ratings.  
It uses a cleaned Excel dataset and presents the analysis through an intuitive, dark-themed, interactive dashboard.

✨ **Key Highlights**
- Power BI–style left navigation
- KPI cards for quick insights
- Interactive charts & tables
- Automatic Excel sheet detection
- Robust handling of missing data

---

## 🧰 Tech Stack

| Tool | Purpose |
|----|----|
| 🐍 **Python** | Core programming language |
| 📊 **Streamlit** | Interactive dashboard UI |
| 🐼 **Pandas** | Data processing & analysis |
| 📄 **Excel (.xlsx)** | Data source |
| 📦 **openpyxl** | Excel file reader |

---

## 📁 Project Structure

```

logistics-management-system/
│
├── dashboard/
│   └── app.py          # Streamlit dashboard code
│
├── data/
│   └── OLA_Dataset.xlsx  # Cleaned dataset (Excel)
│
├── requirements.txt
└── README.md

````

---

## 📄 Dataset Information

- **File Name:** `OLA_Dataset.xlsx`
- **Format:** Excel (.xlsx)
- **Special Handling:**
  - Automatically detects and loads the sheet that contains data
  - Handles missing values safely
  - Normalizes column names

### 🔑 Key Columns Used
- `Booking_ID`
- `Booking_Status`
- `Vehicle_Type`
- `Payment_Method`
- `Booking_Value`
- `Ride_Distance`
- `Customer_Rating`
- `Driver_Ratings`
- `hour`, `day`
- `is_cancelled`

---

## 🧭 Dashboard Sections

### 📊 Overall
- Total Bookings
- Total Revenue (₹)
- Cancelled Rides
- Average Customer Rating
- Bookings by Hour & Day

### 🚗 Vehicle Type
- Total Booking Value
- Average Booking Value
- Average Distance
- Total Distance by vehicle type

### 💰 Revenue
- Revenue by Payment Method
- Revenue by Vehicle Type

### ❌ Cancellation
- Cancellations by Customer
- Cancellations by Driver

### ⭐ Ratings
- Customer Ratings Distribution
- Driver Ratings Distribution

---

## ▶️ How to Run the Project

### 1️⃣ Clone / Download the Project
```bash
git clone <your-repo-url>
cd logistics-management-system
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App

```bash
python -m streamlit run dashboard/app.py
```

The dashboard will open automatically in your browser 🌐

---

## 🛡️ Data Handling & Safety Features

* ✅ No empty dashboards
* ✅ Safe handling of NaN values
* ✅ Filters are optional (no selection = all data)
* ✅ Auto-fallback if filters remove all rows
* ✅ Clean numeric conversions

---

## 🎓 Academic / Viva Explanation (One-Liner)

> “This project analyzes OLA ride data using Python and Pandas, and presents insights through an interactive Streamlit dashboard with Power BI–style navigation.”

---

## 🚀 Future Enhancements

* 🔄 Convert Excel → SQLite / PostgreSQL
* 🎨 Enhanced branding & animations
* 🌍 City-wise / geo-map visualizations
* ☁️ Cloud deployment (Streamlit Cloud / AWS)

---

## 👤 Author

**👨‍💻 Ojas Sharma**
📘 Data Analytics | Python | Visualization
🚀 Built as part of an academic data analytics project

---

## ⭐ Final Note

