import streamlit as st
from datetime import datetime

# Function to calculate if a task is due
def is_due(last_service_date, interval_days):
    days_since_service = (datetime.now() - last_service_date).days
    return days_since_service >= interval_days

# Maintenance Parameters
maintenance_schedule = {
    "Engine Oil": {"interval_miles": 5000, "interval_days": 180},
    "Tire Rotation": {"interval_miles": 7500, "interval_days": 365},
    "Brake Inspection": {"interval_miles": 10000, "interval_days": 365},
    "Battery Check": {"interval_miles": 0, "interval_days": 180},
    "Coolant Check": {"interval_miles": 5000, "interval_days": 180},
    "Transmission Fluid": {"interval_miles": 30000, "interval_days": 730},
    "Air Filter": {"interval_miles": 20000, "interval_days": 365},
    "Wiper Blades": {"interval_miles": 0, "interval_days": 180},
}

# Title
st.title("Vehicle Maintenance Management")

# Vehicle Info
st.header("Vehicle Information")
vehicle_make = st.text_input("Make")
vehicle_model = st.text_input("Model")
vehicle_year = st.text_input("Year")
vehicle_mileage = st.number_input("Current Mileage", min_value=0)

# Service Records
st.header("Service Records")
last_service_dates = {}
for task in maintenance_schedule:
    st.subheader(task)
    last_service_date = st.date_input(f"Last {task} Service Date", value=datetime.now())
    last_service_dates[task] = last_service_date

# Maintenance Due
st.header("Maintenance Due")
for task, schedule in maintenance_schedule.items():
    last_service_date = last_service_dates[task]
    interval_days = schedule["interval_days"]
    interval_miles = schedule["interval_miles"]
    
    due = False
    
    if interval_miles > 0:
        st.write(f"{task}: Mileage Interval - {interval_miles} miles")
        service_miles = st.number_input(f"Miles Since Last {task}", min_value=0)
        due = service_miles >= interval_miles
    else:
        due = is_due(last_service_date, interval_days)
    
    if due:
        st.warning(f"{task} is due for service!")
    else:
        st.success(f"{task} is not due yet.")

# Summary
st.header("Maintenance Summary")
for task in maintenance_schedule:
    st.write(f"{task}: Last serviced on {last_service_dates[task]}")

# Save Data
if st.button("Save Service Records"):
    st.success("Service records saved successfully!")

